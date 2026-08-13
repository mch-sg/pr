"""
Computes pagerank via the power iteration method.
"""
from pagerank.utils import *

def rank_update(web, pageranks, page, d):
    ''''
    Updates the value of the pagerank for page based on the formula
        PR(p)= (1-d)/N + d*sum_j (PR(q)/OB(q))
    where the sum is over all pages q that link to page, PR(q) is the current
    pagerank of page q (from "pageranks") and OB(q) is the number of pages 
    outbound from page q.  Sinks are treated as linking to all pages in web.
     '''
    increment = 0
    # Pagerank of initial page 
    PR_old = pageranks[page]
    inbound_p = set()
    N = len(web.keys())

    # add elements to inbound_p 
    # the set of all pages that link in to p, i.e. loop through and check if each links to p
    for key, val in web.items():
        # if the page is in the links of key, add it to inbound
        if page in val:
            inbound_p.add(key)

        # sink, if page does not link to any pages, then add them all to inbound_p
        elif not web[key]:
            inbound_p.add(key)

    # split the equation up between first and second part
    del1 = (1 - d) * (1 / N)
    del2 = 0

    # loop through each inbound and sum them up 
    for q in inbound_p:
        # pagerank and outbound of q
        PR_q = pageranks[q]
        OB_q = len(web[q])

        # sink for sinks q, outbound is N
        if OB_q < 1:
            OB_q = N

        del2 += (PR_q) / (OB_q)
    
    # modify the existing pageranks dictionary
    pageranks[page] = del1 + (d * del2)    
    increment = abs(PR_old - (del1 + (d * del2)))

    return increment
    
   

def recursive_pagerank(web, stopvalue, max_iterations=200, d=0.85):
    """
    Implements the recursive version of the PageRank algorithm by first creating a
    pagerank of 1/N to all pages (where N is the total number of pages)
    then applying "rank_update" repeteadly until either of two stopping conditions is
    reached.
    """
    pageranks = dict()
    iteration = 0
    N = len(web.keys())

    for key, val in web.items():
        pageranks[key] = 1 / N
    
    # Loop through until max iterations
    for _ in range(max_iterations):
        max_change = 0

        # Go through each page and update the rank
        for page in web.keys():
            change = rank_update(web, pageranks, page, d)
            if change > max_change:
                max_change = change
        
        # Break out if it reaches below stopvalue
        if(max_change < stopvalue):
            break
        
        iteration += 1

    return pageranks, iteration
