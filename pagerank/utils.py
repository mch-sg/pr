import numpy as np
import time

def make_web(n, k, kmin=0):
    assert(k < n)
    keys = np.array(range(n))
    web = dict()
    
    for j in keys:
        numlinks = np.random.choice(range(kmin,k+1))
        web[j] = set(np.random.choice(keys[keys!=j], numlinks, replace=False))

    return web

def print_rank(ranking, k=4, title=""):
    keys = ranking.keys()

    if len(title) > 0:
        print(title, end=": ")

    for p in keys:
        print(str(p)+":  "+str(round(ranking[p],k)), end=",  ")

    print("\n")
    return