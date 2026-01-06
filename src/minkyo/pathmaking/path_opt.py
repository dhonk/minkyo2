from minkyo.models import users
import minkyo.pathmaking.gmap_integration as gmap
from typing import Dict, Any

import json # change to ijson or different stream, for now load everything into memory

'''
for creating ride assignments

goal is to create a distance matrix that stores 
'''

# each instance of ride assignment
class ride_assignment():
    def __init__(self, users: list[users.user]) -> ride_assignment:
        self.users: list[users.user] = users
        self.dists: Dict[id, Dict[id, float]]

    def init_dists(self) -> None:
        for i in self.users:
            for j in self.users:
                self.dists[]