from pydantic import BaseModel
from typing import Dict, Any
import json # change to ijson or different stream, for now load everything into memory

from minkyo.models import users
import minkyo.pathmaking.gmap_integration as gmap

'''
for creating ride assignments

ride_assignment object for each instance of creating rides
created with a list of users (should be handled by caller)

create tree, with each node being a state
check only terminal nodes (where all passengers are picked up)
'''

class distance_node(BaseModel):
    
    children: list[distance_node]

    def compute_distance(self):
        

# each instance of ride assignment
class ride_assignment():
    def __init__(self, users: list[users.user]) -> None:
        self.users: list[users.user] = users
        self.dists: Dict[str, Dict[str, float]]
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