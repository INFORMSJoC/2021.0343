[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Reference Vector Assisted Candidate Search with Aggregated Surrogate for Computationally Expensive Many Objective Optimization Problems

This archive is distributed in association with the [INFORMS Journal on Computing](https://pubsonline.informs.org/journal/ijoc) under
the [MIT License](LICENSE).

To cite this material, please cite this repository, using the following DOI.

[![DOI](https://zenodo.org/badge/554791093.svg)](https://zenodo.org/badge/latestdoi/554791093)

Below is the BibTex for citing this version of the code.

```
@article{RefVecCSASManyObjective2022,
  author =        {Wang, Wenyu and Shoemaker, Christine},
  publisher =     {INFORMS Journal on Computing},
  title =         {Reference Vector Assisted Candidate Search with Aggregated Surrogate for Computationally Expensive Many Objective
                   Optimization Problems},
  year =          {2022},
  doi =           { 10.5281/zenodo.7243971},
  url =           {https://github.com/INFORMSJoC/2021.0343},
}  
```


## Introduction

Multi-objective Optimization Problems (MOPs), which aim to find optimal trade-off solutions regarding to multiple conflicting and equally important
objectives, commonly exist in real-world applications. Without loss of generality, an MOP is mathematically defined by

$$ \min_{\mathbf{x} \in \mathcal{D}} \mathbf{f}(\mathbf{x}) = \[f_1(\mathbf{x}), \dots, f_k(\mathbf{x})\]^T $$

where $\mathbf{x}$ denotes a vector composed of $d$ decision variables. The search space $\mathcal{D}$ denotes a hypercube in $\mathbb{R}^d$ and it is
bounded by a lower bound $\mathbf{l}$ and a upper bound $\mathbf{u} \in \mathbb{R}^d$. $\mathbf{f}$ is composed of $k$ objective functions with $f_i$ representing the $i$-th objective to be optimized, $i = 1, \dots, k$. In the literature, MOPs with more than
three objectives are also known as Many-objective Optimization Problems (MaOPs).

The codes in this repo implement an effective Radial Basis Function (RBF) surrogate-assisted algorithm named **RECAS** for computationally expensive
multi- and many-objective optimization problem where each objective is assumed to be black-box and expensive-to-evaluate.

## Installation

The Python version of RECAS is implemented upon a surrogate optimization toolbox, pySOT, which provides various types of surrogate models,
experimental desings, acquisition functions, and test problems. To find out more about pySOT, please visit
its [toolbox documentation](http://pysot.readthedocs.io/) or refer to the corresponding
paper [David Eriksson, David Bindel, Christine A. Shoemaker. pySOT and POAP: An event-driven asynchronous framework for surrogate optimization. arXiv preprint arXiv:1908.00420, 2019](https://doi.org/10.48550/arXiv.1908.00420)
.

In a virtual environment with Python 3.4 or newer, RECASOpt package can be installed by
```
pip install git+https://github.com/WY-Wang/RECASOpt.git
```

## Using RECAS

The example below shows how to run RECAS on a multi-objective optimization problem with predefined experiment setups. Please also refer to
the [script](https://github.com/INFORMSJoC/2021.0343/blob/master/scripts/experiment.py) for this example.

### Test Problem Setup

The following codes create an instance for DTLZ2 test problem with 2 objectives and 10 decision variables.

```python
from RECASOpt.problems.multiobjective_problems import DTLZ2

OPT_PROB = DTLZ2(nobj=2, dim=10)
```

*Note: The RECASOpt package have already implemented some problems for testing. You can also easily design your own test problem classes by inheriting
from the OptimizationProblem class defined in pySOT.*

### Run Experiment

The following codes run the RECAS for 10 independent trials on the DTLZ2 test problem instantiated above. Each trial starts with $11d-1$ (where 
$d$ denotes the number of decison variables) sample points and ends after 300 objective evaluations. 

```python
from RECASOpt.optimize.optimization import RECASoptimize

# Experiment Setup
N_TRIALS = 10
INIT_EVALS = 11 * OPT_PROB.dim - 1
MAX_EVALS = 300
BATCH_SIZE = 5

# Run multiple independent trials for RECAS
for trial in range(1, N_TRIALS + 1):
    RECASoptimize(
        trial_number=trial,     # int: Current trial number
        opt_prob=OPT_PROB,      # pySOT.OptimizationProblem: multi-objective test problem
        exp_design=None,        # pySOT.ExperimentalDesign: Default method is Latin Hypercube Sampling
        surrogate=None,         # pySOT.Surrogate: Default model is RBF with cubic kernel and linear tail
        init_evals=INIT_EVALS,  # int: Initial number of evaluations for experimental design
        max_evals=MAX_EVALS,    # int: Maximum number of evaluations
        batch_size=BATCH_SIZE,  # int: The size of each batch
    )
```

*Note: Other experimental design methods (exp_design) and surrogate models (surrogate) are available in pySOT. Like the customization for test
problem (opt_prob), you can also program and use your own exp_design and surrogate classes in RECAS, but they must inherit from the parent classes,
pySOT.ExperimentalDesign and pySOT.Surrogate, respectively.*

### Experiment Result

While executing the above experiment, you can monitor the algorith progress in real time:
```text
Trial Number: 1
Number of evaluations completed = 109
Number of evaluations completed = 114
Number of evaluations completed = 119
Number of evaluations completed = 124
Number of evaluations completed = 129
Number of evaluations completed = 134
......
```

Once a trial on DTLZ2(nobj=2, dim=10) is completed, the algorithm will automatically generate a separate result file (.txt), each row of which is composed of a point (the first 10 columns) and its corresponding objective vector (the last 2 columns). Here are the first 10 rows in a result file:
```text
1.855699321102256272e-01 8.424419023429166042e-01 6.217761832726059756e-01 9.715319886143165551e-01 2.727913608860354500e-01 3.420138389999665129e-01 4.131355367929151479e-01 9.555960537820530343e-01 3.126903495436407221e-01 3.030895852559572501e-01 1.647437322477533606e+00 4.942954356867825250e-01
3.642461134171878223e-01 7.486242170770491811e-01 1.891040567340959710e-01 2.932352853580730834e-01 3.794598906465902477e-01 4.431765525725954724e-01 7.323291443703634496e-01 7.175164010598548137e-01 9.503106953571850424e-01 8.628671473340784326e-01 1.391184300842630783e+00 8.959438146411728976e-01
9.506741504113179475e-02 5.088006332155829980e-01 9.230839900616722993e-01 1.740956543208035667e-01 4.634739386295273073e-02 2.939938192420180757e-02 7.958373799891709233e-01 4.630803211080338766e-01 3.115946171176599555e-01 1.254091441551329345e-01 1.955249140117332640e+00 2.941702924062253310e-01
4.353844660906761588e-01 5.977470922908388884e-01 5.180326138874716824e-01 5.181631460558120406e-01 1.907143519597005454e-01 9.691934315695300839e-01 2.661643024566033300e-01 8.701087308585928604e-01 9.654225339039117504e-01 8.430779563962417233e-01 1.435503872136607129e+00 1.170126129455426378e+00
6.320356123313336516e-01 8.124821303174933895e-01 9.680998817986001814e-01 4.073836545189319369e-01 7.794324909779218324e-02 2.509234268137779389e-01 5.762880772184199030e-01 6.523011424586782070e-01 1.051543774472713383e-01 2.224822478708869677e-02 1.081045080969014416e+00 1.657257729503796018e+00
5.583517541795081085e-01 3.103652970818247536e-01 9.939222598608863368e-01 8.687852542608885953e-01 7.743905954450871487e-01 9.015903799188746959e-01 3.453091096519863429e-02 6.890953282245021461e-01 8.353519956497881260e-01 4.744953582108867307e-01 1.290354571511755477e+00 1.551574054550507453e+00
4.935433640746357820e-01 5.224740572910804293e-01 7.831413773478310691e-01 4.389924250609056333e-01 6.347971967630697820e-01 3.306725043920795137e-01 8.641609705285324683e-01 5.941356036808639191e-02 8.066712804826726979e-02 7.630799280206358448e-01 1.216367275604530063e+00 1.191941228762028793e+00
5.289322186891435296e-01 9.895294358136180746e-01 7.606552887718162070e-01 3.507442273051026294e-01 6.232762599519355851e-01 6.683850742158081726e-01 7.168639649695451865e-01 1.541049670472060401e-02 6.034979920253500385e-01 4.213977151014007827e-01 1.127454212410932799e+00 1.234888694618530014e+00
6.823346896439577147e-01 4.843628274298237835e-01 8.008004173853683350e-01 3.980478604148112165e-01 8.522050342086793240e-01 4.858411733263879873e-01 1.743000504046768595e-01 4.562497373348803897e-01 9.573310172924671679e-01 7.369757963631328179e-01 7.650234066739882710e-01 1.403742183222207007e+00
4.582836630096273067e-01 2.062569500266957581e-02 9.903188996510402520e-01 4.444843097783555685e-01 9.751113248720674198e-01 7.877729534128323774e-01 8.061605843319720188e-01 9.413178739085397151e-01 2.420150030615750639e-02 1.744924466624346304e-01 1.806549202110252272e+00 1.584051792727361629e+00
......
```

## Repository Structure

### results folder

[parameter_analysis/batch_size.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/parameter_analysis/batch_size.pdf) (i.e., Figure 2 in the supplementary
material) shows the average IGD progress curves (against the number of iterations) for RECAS with batch size being 2, 5, 10, 15, ane 20 on DTLZ2 test
problems with 2 to 10 objectives.

[parameter_analysis/initial_size.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/parameter_analysis/initial_size.pdf) (i.e., Figure 1 in the supplementary
material) shows the average IGD progress curves (against the number of evaluations) for RCAS with $2d-1$, $5d-1$, $11d-1$, and $15d-1$ initial points
on DTLZ2 test problems with 2 to 10 objectives.

[results_on_tbrook/tbrook_box_plots.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/results_on_tbrook/tbrook_box_plots.pdf) (i.e., Figure 3 in the supplementary
material) shows the box plots of IGD, Hypervolume (HV), and the number of non-dominated solutions (NS) obtained by four algorithms after 600
evaluations on TBrook1 and TBrook2 problems.

[results_on_test_suites/dtlz6_fronts.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/results_on_test_suites/dtlz6_fronts.pdf) (i.e., Figure 4 in the main paper) shows the best and
worst non-dominated fronts obtained by seven algorithms among 20 indepedent trials on bi-objective DTLZ6.

[results_on_test_suites/dtlz_data_profile.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/results_on_test_suites/dtlz_data_profile.pdf) (i.e., Figure 5 in the main paper) shows the average
data profiles with error bars for seven algorithms on DTLZ problem sets with 10 and 20 decision variables.

[results_on_test_suites/dtlz_10d_table.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/results_on_test_suites/dtlz_10d_table.pdf) (i.e., Table 2 in the main paper) collects the numerical
results of seven algorithms over DTLZ1 to DTLZ7 where the number of decision variales is 10 and the number of objectives varies from 2 to 10. The IGD
indicator values obtained by each algorithm after 300 evaluations are averaged over 20 independent trials and are statistically compared to those
obtained by RECAS.

[results_on_test_suites/dtlz_20d_table.pdf](https://github.com/INFORMSJoC/2021.0343/blob/master/results/results_on_test_suites/dtlz_20d_table.pdf) (i.e., Table 3 in the main paper) collects the numerical
results of seven algorithms over DTLZ1 to DTLZ7 where the number of decision variales is 20 and the number of objectives varies from 2 to 10. The IGD
indicator values obtained by each algorithm after 600 evaluations are averaged over 20 independent trials and are statistically compared to those
obtained by RECAS.

[supplementary_material.pfd](https://github.com/INFORMSJoC/2021.0343/blob/master/results/supplementary_material.pdf) is the online supplementary material for the RECAS paper.

### scripts folder

[experiment.py](https://github.com/INFORMSJoC/2021.0343/blob/master/scripts/experiment.py) shows an example for setting up test problem and RECAS
algorithm for numerical experiments.

### src folder

[algorithm/multiobjective_strategies.py](https://github.com/INFORMSJoC/2021.0343/blob/master/src/RECASOpt/algorithm/multiobjective_strategies.py)
implements the RECAS strategy class that starts with sample_init() method (i.e., initilization phase) and then automatically executes the
generate_evals(num_pts) method by iterations (i.e., iteration phase). Inheriting from SurrogateBaseStrategy in pySOT, the RECA strategy supports
running in serial and batch synchronous parallel.

[algorithm/multiobjective_sampling.py](https://github.com/INFORMSJoC/2021.0343/blob/master/src/RECASOpt/utils/multiobjective_sampling.py) implements the method
to generate a group of candidates given a center point and the surrogate-assisted method to select one promising candidate for expensive evaluation

[optimize/optimization.py](https://github.com/INFORMSJoC/2021.0343/blob/master/src/RECASOpt/optimize/optimization.py) provides the method to set up the
user-defined experiemtal parameters, test problem, experimental design method and surrogate model for RECAS and initiate a single algorithm run.

[problems/multiobjective_problems.py](https://github.com/INFORMSJoC/2021.0343/blob/master/src/RECASOpt/problems/multiobjective_problems.py) implements
several multi-objective test problem classes based on the OptimizationProblem class in pySOT.

[utils/multiobjective_archives.py](https://github.com/INFORMSJoC/2021.0343/blob/master/src/RECASOpt/utils/multiobjective_archives.py) implements the class
for recording the evaluation information related to a point and the class for archiving the non-dominated set and front of all previoiusly evaluated
points.

[utils/multiobjective_utilities.py](https://github.com/INFORMSJoC/2021.0343/blob/master/src/RECASOpt/utils/multiobjective_utilities.py) implements other
auxiliary tools used in RECAS.

## Ongoing Development

This code is being developed on an on-going basis at the author's [Github site](https://github.com/WY-Wang/RECASOpt).

## Support

For support in using this software, submit an [issue](https://github.com/WY-Wang/RECASOpt/issues/new).
