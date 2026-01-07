import sqlite3
import typing

import minkyo.pathmaking.gmap_integration as gmap
import minkyo.models.users as models

# return google maps distance
def gmaps_dist(a: models.user, b: models.user) -> int:
    # check storage

    return 0