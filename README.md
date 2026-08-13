# Pagerank and convergence analysis

This project implements the pagerank algorithm via Power iteration, Monte carlo and eigenvalues/matrix. We also check and analyze its convergence using Markov chains.

The goal is to verify convergence across all three methods and compare their computational tradeoffs.

## Methods
- **Power Iteration** — iterative approximation
- **Monte Carlo** — random walk simulation
- **Eigenvalue/Matrix decomposition** — direct solve


## Installation
Clone the repository and install in editable mode:

```bash
git clone https://github.com/mch-sg/pr.git
cd pr
pip install -e .
```

This installs the `pagerank` package along with its dependencies.


## Usage

```python
from pagerank.power_iteration import recursive_pagerank
from pagerank.monte_carlo import random_surf
from pagerank.eigendecomposition import matrix_pagerank, eigenvector_pagerank
from pagerank.utils import make_web

# Generate a random web with 6 pages and 0-5 links per page
web = make_web(6, 5)

# Compute pagerank via eigendecomposition
ranks = eigenvector_pagerank(web)
print_rank(ranks)
```


## Results

A visualization of a sample network can be seen in the image below.

![Network visualization plot of the pageranks.](/data/network_visualization.png)

We found that the eigendecomposition method proved to work most accurately in our tested cases, however, the power iteration method had the lowest runtime and fastest convergence over a web of 20000 pages with 0-4000 links each. 

See the [report](/paper.pdf) for further details on the analysis.


## Project Structure
```
pr/
├── README.md
├── pagerank/
│   ├── __init__.py
│   ├── utils.py
│   ├── power_iteration.py
│   ├── monte_carlo.py
│   ├── eigendecomposition.py
│   └── update_web.py
├── tests/
│   └── test_pagerank.py
├── notebooks/
│   └── plot.ipynb
├── data/
│   └── network_visualization.png
└── requirements.txt
```

## References

We drew theory from the following textbooks (mostly excerpts).

- "Discrete mathematics and its Applications" - Kenneth Rosen
- "Linear Algebra Done Wrong" - Sergei Treil
- "Elementary Linear Algebra" - Howard Anton, Chris Rorres


## License

[MIT](https://choosealicense.com/licenses/mit/)