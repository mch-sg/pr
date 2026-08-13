from pagerank.power_iteration import recursive_pagerank
from pagerank.monte_carlo import random_surf
from pagerank.eigendecomposition import matrix_pagerank, eigenvector_pagerank
from pagerank.utils import *

""" 
Below is a couple of different "web" versions. Each is a dictionary consisting of keys (page) and values (links). 
The make_web function makes random links given (pages, links).
"""
#web = {0: {4}, 1: {0, 4, 7}, 2: {0, 9, 5}, 3: set(), 4: {2}, 5: {1, 2, 3, 7}, \
# 6: {2, 5}, 7: {8, 5, 6}, 8: {9, 5, 1}, 9: {8, 1, 0}}

#web = {0: {4}, 1: {0, 4}, 2: {0, 5}, 3: set(), 4: {2}, 5: {1, 2, 3}}

#update_web_dict = {0: {4}, 1: {0, 8, 4}, 2: set(), 3: set(), 4: {1}, 5: {0, 9, 2}, \
#        6: set(), 7: set(), 8: {6}, 10: {0, 1, 4}}

web = make_web(6,5)

ranking1 = random_surf(web, 100000)
ranking2, iterations = recursive_pagerank(web,0.0000001)
ranking3 = eigenvector_pagerank(web)
ranking4 = matrix_pagerank(web,20)

print("\n===PROBABILITIES===\n")
print("Shown below is a comparison of the four methods. \nEach key 0-5 is a web page, and the value is the probability of landing on the given page.\nThe eigendecomposition version is considered the base value here.\n")

print("Monte carlo :")
print_rank(ranking1)
print("Power iteration :")
print_rank(ranking2)
print("Eigendecomposition :")
print_rank(ranking3)
print("Matrix :")
print_rank(ranking4)