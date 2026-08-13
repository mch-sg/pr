"""
Computes pagerank via the monte carlo method.
"""
from pagerank.utils import *

def surf_step(web, page, d=0.85):
    """
    Return a probability distribution over which page to visit next,
    given a current page.
    """
    distribution = dict()
    N = len(web.keys())

    # Every key in web needs a place in distribution 
    for key, val in web.items():
        distribution[key] = 0

    # If page does not link to any page, then choose any page in web at random
    if len(web[page]) < 1:
        for key, val in web.items():
            distribution[key] += 1 / N

    if len(web[page]) > 0:
        # With probability `d`, choose a page at random linked to by `page`,  
        for link in web[page]:
            distribution[link] += d / (len(web[page]))
        # With probability `1 - d`, choose  a page at random  from all pages in the web.
        for key, val in web.items():
            distribution[key] += (1-d) / N

    return distribution


def random_surf(web, n, d=0.85):
    """
    Return pagerank values for each page by sampling `n` pages
    according to surf_step. 
    """
    ranking = dict() # the ranking for each page
    all_pages = list(web.keys())

    # initialize that every key in web needs a place in distribution 
    for key, val in web.items():
        ranking[key] = 0
 
    p = np.random.choice(all_pages) 
    for _ in range(n):
        # Add 1 each time we visit a site
        ranking[p] += 1
        # Get our probability distribution of the page p
        probdist = surf_step(web, p, d)
        # Make a list of the probabilities of visiting the next site, given we're at page p
        probs = []
        for key, val in probdist.items():
            probs.append(val)
        # Choose a new page based on that probability
        p = np.random.choice(all_pages, p=probs) 
    
    # Divide by n to get the pagerank
    for key, val in ranking.items():
        ranking[key] /= n

    return ranking