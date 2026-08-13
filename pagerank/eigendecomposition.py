"""
Computes pagerank via the eigendecomposition  method.
"""
from pagerank.utils import *

def modified_link_matrix(web, pagelist, d=0.85):
    """ 
    Create a modified link matrix from web.
    """
    N = len(web.keys())
    E = np.ones([N,N])
    # Init A as zero matrix
    A = np.zeros([N,N])

    # Modifying our adjacency matrix
    for j in range(N):          
        for i in range(N):     
            # if p_j links to p_i
            if pagelist[i] in web[pagelist[j]]:
               N_j = len(web[pagelist[j]])
               A[j,i] = 1 / N_j

            # if p_j is a sink
            if len(web[pagelist[j]]) < 1:
               A[j, i] = 1 / N

    return d * A.T + (1 - d) * (E / N)

def eigenvector_pagerank(web, d=0.85):
    """
    Returns the pagerank of web as the eigenvector of the modified link matrix
    """
    start = time.time()
    ranking = dict()   

    for key, val in web.items():
        ranking[key] = 0

    pages = list(web.keys())
    M = modified_link_matrix(web,pages, d)

    # Use np eigenvector function to find our eigenvals and vects
    lamda, V = np.linalg.eig(M)
    # Choose the first vector
    V1 = V[:,0:1]   
    # normalize the eigenvector
    V1 = np.real(V1)
    ranking3 = V1 / (np.sum(V1))  # ranking from eigenvector 1

    # Loop through the vector and input them into the ranking dict.
    for k in range(len(pages)):
        ranking[k] = float(ranking3[k])

    end = time.time()
    print(f"Total runtime of the eigenvector is {end - start} seconds")

    return ranking

def matrix_pagerank(web, power, d=0.85):
    """
    Returns the pagerank as the first column of the power'th power of the modified link matrix
    """
    start = time.time()
    ranking = dict() 

    for key, val in web.items():
        ranking[key] = 0

    # Create pages and M adjacency matrix
    pages = list(web.keys())
    M = modified_link_matrix(web,pages, d)

    # Use method (b) by computing powerth power of M
    K = np.linalg.matrix_power(M,power)
    # Choose the first col
    new_rank = K[:,0] 

    # Loop through the vector and input it into the ranking dict.
    for k in range(len(pages)):
        ranking[k] = float(new_rank[k])

    end = time.time()
    print(f"Total runtime of the matrix is {end - start} seconds")

    return ranking