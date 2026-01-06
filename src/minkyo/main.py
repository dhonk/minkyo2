from minkyo.models import users
from minkyo.pathmaking import path_opt
import minkyo.pathmaking.gmap_integration

if __name__ == '__main__':
    temp = []
    t = users.rider(id = '0')
    print(t.id, t.name, t.address, t.gmaps_place_id)
    temp.append(t)
    t = users.driver(id = '1', capacity=4)
    print(t.id, t.capacity)
    temp.append(t)


