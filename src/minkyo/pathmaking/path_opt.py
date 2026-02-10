from pydantic import BaseModel
from typing import Any
import json # change to ijson or different stream, for now load everything into memory
import itertools

from minkyo.models import users
import minkyo.pathmaking.gmap_integration as gmap

from math import inf
'''
for creating ride assignments

ride_assignment object for each instance of creating rides
created with a list of users (should be handled by caller)

create tree, with each node being a state
check only terminal nodes (where all passengers are picked up)

time complexity on this is kinda cooked atm tho
- Tree generation: O(b^m) -> b = avg branch factor, m = depth of tree
- let n be total number of people
- avg depth is ... n...
- unless assign multiple at once? 
'''

def get_gmap_dist(a: users.user, 
                  b: users.user) -> float:
    return gmap.get_distance(a.gmaps_place_id, b.gmaps_place_id)

def get_dist_from_store(distmatrix: dict[str, dict[str, float]],
                        a: users.user,
                        b: users.user) -> float | None:
    a_map = distmatrix.get(a.id)
    if a_map:
        distance = a_map.get(b.id)
        return distance
    
def get_dist(distmatrix: dict[str, dict[str, float]],
             a: users.user,
             b: users.user) -> float:
    distance = get_dist_from_store(distmatrix, a, b)
    if not distance:
        distance = get_gmap_dist(a, b)
    
    if not distance:
        raise Exception('None type distance returned')
    
    return distance

def list_min_dist(dmatrix: dict[str, dict[str, float]],
                  inlist: list[users.user]) -> tuple[list[users.user], float]:
    perm_iter = itertools.permutations(inlist)
    min_dist: float = inf
    min_perm: list[users.user] = []
    for perm in perm_iter:
        dist = 0
        for i, val in enumerate(perm[:-1]):
            dist += get_dist(dmatrix, val, perm[i+1])
        if dist < min_dist:
            min_dist = dist
            min_perm = list(perm)
    return min_perm, min_dist

class distance_node(BaseModel):
    terminal: bool = False
    children: list[distance_node]
        
# each instance of ride assignment
class ride_assignment():
    def __init__(self, users: list[users.user]) -> None:
        self.users: list[users.user] = users
        self.dists: dict[str, dict[str, float]]
        self.state_tree: distance_node

    ''' 
    initialize weight matrix, structure of the weight matrix is as follows:
    {src pId : {dst pId : distance}}
    '''
    def init_dists(self) -> None:
        for src in self.users:
            for dst in self.users:
                if src.gmaps_place_id in self.dists and dst.gmaps_place_id in self.dists[src.gmaps_place_id]:
                    continue
                self.dists[src.gmaps_place_id][dst.gmaps_place_id] = gmap.get_distance(src.gmaps_place_id, dst.gmaps_place_id)
        
    '''
    construct 
    '''