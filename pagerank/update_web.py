"""
A function updating the web dictionary.
"""

from pagerank.utils import *
from pagerank.eigendecomposition import matrix_pagerank
from pagerank.power_iteration import rank_update

def update_web(web, webadd={}, removelinks={}, removepages=[], d=0.85):
    '''
    web: Current web
    webadd: The web dictionary we wish to add to current web
    removelinks: Dictionary of all links we want to remove
    removepages: List of all pages we want to remove
    d: Damping factor
    '''
    pageranks = matrix_pagerank(web,20)
    N = len(web.keys())

    print(f"web:{web}")
    print(f"pagerank:{pageranks}")

    # Go through webadd dict, and, if not in web, then initialize and give it an initial pagerank
    # Then add all the links to the set
    if len(webadd) > 0:
        for key, val in webadd.items():
            if key not in web:
                web[key] = set()
                pageranks[key] = 1 / (N + 1)
            
            for num in val:
                web[key].add(num)

    # Go through removelinks dict and remove the links associated with the key
    if len(removelinks) > 0:
        for key, val in removelinks.items():
            for num in val:
                web[key].remove(num)

    # Go through removepages list and remove each page and all its inbound and outbound links
    if len(removepages) > 0:
        for page in removepages:
            # Remove page from web and pageranks
            if page in web:
                del web[page]
            if page in pageranks:
                del pageranks[page]

            # Go through every single link in the web and remove page
            for key, val in web.items():
                if page in val:
                    web[key].remove(page)

    # Now we loop through (from recursive model)
    # and update rank based on previous rankings
    for _ in range(200):
        # Log the change diffs to break out if it reaches below stopvalue
        max_change = 0
        # Remember to save the ranks whilst going through each page
        new_ranks = pageranks.copy()
        # Go through each page and update the rank
        for page in web.keys():
            change = rank_update(web, new_ranks, page, d)
            if (change > max_change):
                max_change = change
        
        pageranks = new_ranks
        # Break out if it reaches below stopvaluepyp
        if(max_change < 0.0000001):
            break

    print(f"web updated:{web}")
    print(f"pagerank updated:{pageranks}")