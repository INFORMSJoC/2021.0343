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

The code in this repo implements an effective Radial Basis Function (RBF) surrogate-assisted algorithm named **RECAS** for computationally expensive multi- and many-objective optimization problem where each objective is assumed to be black-box and expensive-to-evaluate.



## Installation

The Python version of RECAS is implemented upon a surrogate optimization toolbox, pySOT, which provides various types of surrogate models, experimental desings, acquisition functions, and test problems. To find out more about pySOT, please visit its [toolbox documentation](http://pysot.readthedocs.io/) or refer to the corresponding paper [David Eriksson, David Bindel, Christine A. Shoemaker. pySOT and POAP: An event-driven asynchronous framework for surrogate optimization. arXiv preprint arXiv:1908.00420, 2019](https://doi.org/10.48550/arXiv.1908.00420).

In a virtual environment with Python 3.4 or newer, pySOT can be easily installed via

```
pip install pySOT
```



## Repository Structure

* scripts folder

* src folder

* results folder



## Examples for Replicating

### Test Problem Setup
```python
# Create a DTLZ2 test problem with 2 objectives and 10 decision variables
from multiobjective_problems import DTLZ2

opt_prob = DTLZ2(dim=10, nobj=2)
```

### Surrogate and Algorithm Setup
```python
from RECAS import RECAS
from pySOT.surrogate import RBFInterpolant, CubicKernel, LinearTail

# Create an RBF model with cubic kernel and linear tail
surrogate = RBFInterpolant(
    dim=opt_prob.dim,
    lb=opt_prob.lb,
    ub=opt_prob.ub,
    kernel=CubicKernel(),
    tail=LinearTail(opt_prob.dim),
)

# Initialize an RECAS strategy
strategy = RECAS(
    max_evals=MAX_EVALS, # Maximum number of evaluations
    opt_prob=opt_prob, # Optimization problem
    exp_design=exp_design, # Experimental design method
    surrogate=surrogate, # Surrogate model
    batch_size=BATCH_SIZE, # Size of each batch
    asynchronous=False,
)
```

### Run Experiment
```python
from poap.controller import ThreadController

controller = ThreadController()
controller.strategy = strategy

# Launch the threads and give them access to the objective function
for _ in range(BATCH_SIZE):
    worker = BasicWorkerThread(controller, opt_prob.eval)
    controller.launch_worker(worker)

# Run the optimization strategy
def merit(r):
    return r.value[0]
controller.run(merit=merit)
```



## Ongoing Development

This code is being developed on an on-going basis at the author's [Github site](https://github.com/tkralphs/JoCTemplate).



## Support

For support in using this software, submit an [issue](https://github.com/tkralphs/JoCTemplate/issues/new).
