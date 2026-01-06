from pydantic import BaseModel
import typing

'''
for creating ride assignments
'''

type id = str

class user(BaseModel):
    id: id
    name: str = 'No name'
    address: str = 'No address'
    gmaps_place_id: str = 'No pid'

class rider(user):
    pass

class driver(user):
    capacity: int # number of PASSENGERS driver can carry
