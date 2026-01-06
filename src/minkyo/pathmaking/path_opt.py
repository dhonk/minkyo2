import typing

from minkyo.models import users

'''
for creating ride assignments

goal is to create a distance matrix that stores 
'''

class ride_assignment():
    def __init__(self, users: list[users.user]):
        self.users = users
    
    