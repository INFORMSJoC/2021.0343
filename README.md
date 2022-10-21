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
pip install git+https://github.com/WY-Wang/RECASOpt.git
```



## Repository Structure

* results folder

* scripts folder

* src folder



## Replicating

The following example shows how to run RECAS on a multi-objective optimization problem with predefined experiment setups. Please also refer to the [script](https://github.com/WY-Wang/RECASOpt/blob/main/Examples/experiment.py) for this example.

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
