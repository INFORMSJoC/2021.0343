[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Reference Vector Assisted Candidate Search with Aggregated Surrogate for Computationally Expensive Many Objective Optimization Problems

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper [This is a Template](https://doi.org/10.1287/ijoc.2019.0934) by T. Ralphs. The snapshot is based on [this SHA](https://github.com/tkralphs/JoCTemplate/commit/f7f30c63adbcb0811e5a133e1def696b74f3ba15) in the development repository. 

**Important: This code is being developed on an on-going basis at https://github.com/tkralphs/JoCTemplate. Please go there if you would like to get a more recent version or would like support**



## Cite

To cite this software, please cite the [paper](https://doi.org/10.1287/ijoc.2019.0934) using its DOI and the software itself, using the following DOI.

[![DOI](https://zenodo.org/badge/285853815.svg)](https://zenodo.org/badge/latestdoi/285853815)

Below is the BibTex for citing this version of the code.

```
@article{CacheTest,
  author =        {T. Ralphs},
  publisher =     {INFORMS Journal on Computing},
  title =         {{CacheTest} Version v1.0},
  year =          {2020},
  doi =           {10.5281/zenodo.3977566},
  url =           {https://github.com/INFORMSJoC/JoCTemplate},
}  
```



## Introduction

Multi-objective Optimization Problems (MOPs), which aim to find optimal trade-off solutions regarding to multiple conflicting and equally important objectives, commonly exist in real-world applications. Without loss of generality, an MOP is mathematically defined by

$$
\min_{\mathbf{x} \in \mathcal{D}} \mathbf{f}(\mathbf{x}) = \[f_1(\mathbf{x}), \dots, f_k(\mathbf{x})\]^T
$$

where $\mathbf{x}$ denotes a vector composed of $d$ decision variables. The search space $\mathcal{D}$ denotes a hypercube in $\mathbb{R}^d$ and it is bounded by a lower bound $\mathbf{l}$ and a upper bound $\mathbf{u} \in \mathbb{R}^d$. $\mathbf{f}$ is composed of $k$ objective functions with $f_i : \mathbb{R}^d \rightarrow \mathbb{R}$ representing the $i$-th objective to be optimized, $i = 1, \dots, k$. In the literature, MOPs with more than three objectives are also known as Many-objective Optimization Problems (MaOPs).

The codes in this repo implement an effective Radial Basis Function (RBF) surrogate-assisted algorithm named **RECAS** for computationally expensive multi- and many-objective optimization problem where each objective is assumed to be black-box and expensive-to-evaluate.



## Installation

The Python version of RECAS is implemented upon a surrogate optimization toolbox, pySOT, which provides various types of surrogate models, experimental desings, acquisition functions, and test problems. To find out more about pySOT, please visit its [toolbox documentation](http://pysot.readthedocs.io/) or refer to the corresponding paper [David Eriksson, David Bindel, Christine A. Shoemaker. pySOT and POAP: An event-driven asynchronous framework for surrogate optimization. arXiv preprint arXiv:1908.00420, 2019](https://doi.org/10.48550/arXiv.1908.00420).

1. In a virtual environment with Python 3.4 or newer, pySOT can be installed via

```
pip install pySOT
```

2. Install RECASOpt package to your local environment

```
pip install git+https://github.com/WY-Wang/2021.0343.git
```



## Repository Structure

### results folder

[main/Figure_4.png](https://github.com/WY-Wang/2021.0343/blob/master/results/main/Figure_4.png) (i.e., Figure 4 in the main paper) shows the best and worst non-dominated fronts obtained by seven algorithms among 20 indepedent trials on bi-objective DTLZ6.

[main/Figure_5.png](https://github.com/WY-Wang/2021.0343/blob/master/results/main/Figure_5.png) (i.e., Figure 5 in the main paper) shows the average data profiles with error bars for seven algorithms on DTLZ problem sets with 10 and 20 decision variables.

[main/Table_2.png](https://github.com/WY-Wang/2021.0343/blob/master/results/main/Table_2.png) (i.e., Table 2 in the main paper) collects the numerical results of seven algorithms over DTLZ1 to DTLZ7 where the number of decision variales is 10 and the number of objectives varies from 2 to 10. The IGD indicator values obtained by each algorithm after 300 evaluations are averaged over 20 independent trials and are statistically compared to those obtained by RECAS.

[main/Table_3.png](https://github.com/WY-Wang/2021.0343/blob/master/results/main/Table_3.png) (i.e., Table 3 in the main paper) collects the numerical results of seven algorithms over DTLZ1 to DTLZ7 where the number of decision variales is 20 and the number of objectives varies from 2 to 10. The IGD indicator values obtained by each algorithm after 600 evaluations are averaged over 20 independent trials and are statistically compared to those obtained by RECAS.

[supplemental/Figure_1.png](https://github.com/WY-Wang/2021.0343/blob/master/results/supplemental/Figure_1.png) (i.e., Figure 1 in the supplementary material) shows the average IGD progress curves (against the number of evaluations) for RCAS with $2d-1$, $5d-1$, $11d-1$, and $15d-1$ initial points on DTLZ2 test problems with 2 to 10 objectives.

[supplemental/Figure_2.png](https://github.com/WY-Wang/2021.0343/blob/master/results/supplemental/Figure_2.png) (i.e., Figure 2 in the supplementary material) shows the average IGD progress curves (against the number of iterations) for RECAS with batch size being 2, 5, 10, 15, ane 20 on DTLZ2 test problems with 2 to 10 objectives. 

[supplemental/Figure_3.png](https://github.com/WY-Wang/2021.0343/blob/master/results/supplemental/Figure_3.png) (i.e., Figure 3 in the supplementary material) shows the box plots of IGD, Hypervolume (HV), and the number of non-dominated solutions (NS) obtained by four algorithms after 600 evaluations on TBrook1 and TBrook2 problems.

### scripts folder
[experiment.py](https://github.com/WY-Wang/2021.0343/blob/master/scripts/experiment.py) shows an example for setting up test problem and RECAS algorithm for numerical experiments.

### src folder
All the codes for the RECAS algorithm are collected in the RECASOpt subfolder:

[algorithm/multiobjective_strategies.py](https://github.com/WY-Wang/2021.0343/blob/master/src/RECASOpt/algorithm/multiobjective_strategies.py) implements the RECAS strategy class that starts with sample_init() method (i.e., initilization phase) and then automatically executes the generate_evals(num_pts) method by iterations (i.e., iteration phase). Inheriting from SurrogateBaseStrategy in pySOT, the RECA strategy supports running in serial and batch synchronous parallel.

[optimize/optimization.py](https://github.com/WY-Wang/2021.0343/blob/master/src/RECASOpt/optimize/optimization.py) provides the method to set up the user-defined experiemtal parameters, test problem, experimental design method and surrogate model for RECAS and initiate a single algorithm run.

[problems/multiobjective_problems.py](https://github.com/WY-Wang/2021.0343/blob/master/src/RECASOpt/problems/multiobjective_problems.py) implements several multi-objective test problem classes based on the OptimizationProblem class in pySOT.

[utils/multiobjective_archives](https://github.com/WY-Wang/2021.0343/blob/master/src/RECASOpt/utils/multiobjective_archives.py) implements the class for recording the evaluation information related to a point and the class for archiving the non-dominated set and front of all previoiusly evaluated points.

[utils/multiobjective_sampling](https://github.com/WY-Wang/2021.0343/blob/master/src/RECASOpt/utils/multiobjective_sampling.py) implements the method to generate a group of candidates given a center point and the surrogate-assisted method to select one promising candidate for expensive evaluation

[utils/multiobjective_utilities](https://github.com/WY-Wang/2021.0343/blob/master/src/RECASOpt/utils/multiobjective_utilities.py) implements other auxiliary tools used in RECAS.



## Replicating

The following example shows how to run RECAS on a multi-objective optimization problem with predefined experiment setups. Please also refer to the [script](https://github.com/INFORMSJoC/2021.0343/blob/master/scripts/experiment.py) for this example.

### Test Problem Setup
```python
# Create a DTLZ2 test problem with 2 objectives and 10 decision variables
from RECASOpt.problems.multiobjective_problems import DTLZ2
OPT_PROB = DTLZ2(nobj=2, dim=10)
```
*Note: The RECASOpt package have already implemented some problems for testing. You can also easily design your own test problem classes by inheriting the OptimizationProblem class defined in pySOT.*

### Run Experiment
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
        trial_number=trial,         # int: Current trial number
        opt_prob=OPT_PROB,          # pySOT.OptimizationProblem: multi-objective test problem
        exp_design=None,            # pySOT.ExperimentalDesign: Default method is Latin Hypercube Sampling
        surrogate=None,             # pySOT.Surrogate: Default model is RBF with cubic kernel and linear tail
        init_evals=INIT_EVALS,      # int: Initial number of evaluations for experimental design
        max_evals=MAX_EVALS,        # int: Maximum number of evaluations
        batch_size=BATCH_SIZE,      # int: The size of each batch
    )
```
*Note: Like the customization for test problem (opt_prob), you can customize both experimental design (exp_design) and surrogate mode (surrogate) if and only if you inherite their parent classes, pySOT.ExperimentalDesign and pySOT.Surrogate, respectively.*



## Ongoing Development

This code is being developed on an on-going basis at the author's [Github site](https://github.com/WY-Wang/RECASOpt).



## Support

For support in using this software, submit an [issue](https://github.com/tkralphs/JoCTemplate/issues/new).
