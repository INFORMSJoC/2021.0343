from poap.controller import BasicWorkerThread, ThreadController
from pySOT.surrogate import RBFInterpolant, CubicKernel, LinearTail
from pySOT.experimental_design import LatinHypercube
from ..algorithm.multiobjective_strategies import RECAS


def RECASoptimize(
    trial_number,
    opt_prob,
    exp_design = None,
    surrogate = None,
    init_evals = None,
    max_evals = 300,
    batch_size = 5,
):
    """Method to set up a single RECAS trial.

    While executing this method, the algorithm progress can be monitored, e.g.,
        Trial Number: 1
        Number of evaluations completed = 109
        Number of evaluations completed = 114
        Number of evaluations completed = 119
        Number of evaluations completed = 124
        Number of evaluations completed = 129
        Number of evaluations completed = 134
        ......
    Once the trial is completed, this method will automatically generate a result
    file (.txt), each row of which is composed of a point (the first opt_prob.dim
    columns) and its corresponding objective vector (the last opt_prob.nobj columns).

    Args:
        trial_number: int
            Number of the current trial
        opt_prob: pySOT.OptimizationProblem
            Instance of an optimization problem
        exp_design: pySOT.ExperimentalDesign
            Instance of an experimental design method (Default is Latin Hypercube Sampling)
        surrogate: pySOT.Surrogate
            Instance of a surrogate model (Default is RBF with cubic kernel and linear tail)
        init_evals: int
            Initial number of evaluations (Default is 11 * opt_prob.dim - 1)
        max_evals: int
            Maximum number of evaluations (Default is 300)
        batch_size: int
            Size of batch in each iteration (Default is 5)
    """
    print(f"Trial Number: {trial_number}")

    if init_evals is None:
        init_evals = 11 * opt_prob.dim - 1
    if exp_design is None:
        exp_design = LatinHypercube(dim=opt_prob.dim, num_pts=init_evals)
    if surrogate is None:
        surrogate = RBFInterpolant(
            dim=opt_prob.dim,
            lb=opt_prob.lb,
            ub=opt_prob.ub,
            kernel=CubicKernel(),
            tail=LinearTail(opt_prob.dim),
        )

    # Create a controller and set its strategy as RECAS
    controller = ThreadController()
    controller.strategy = RECAS(
        max_evals=max_evals,
        opt_prob=opt_prob,
        exp_design=exp_design,
        surrogate=surrogate,
        batch_size=batch_size,
        asynchronous=False,
    )

    # Launch the threads and give them access to the objective function
    for _ in range(batch_size):
        worker = BasicWorkerThread(controller, opt_prob.eval)
        controller.launch_worker(worker)

    # Run the optimization strategy
    def merit(r):
        return r.value[0]
    controller.run(merit=merit)

    fpath = "_".join(['RECAS', opt_prob.name, str(opt_prob.nobj), str(opt_prob.dim), str(trial_number)]) + ".txt"
    controller.strategy.save_to_file(fpath)


if __name__ == '__main__':
    pass
