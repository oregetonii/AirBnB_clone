#!/usr/bin/python3
'''Storing files'''
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                  "Place": Place, "Review": Review, "State": State,
                  "User": User}

    def all(self):
        '''Returns dict of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Adds new obj to existing dict of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''Saves obj dicts to json file'''
        my_dict = {}
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w+') as f:
            json.dump(my_dict, f)

    def reload(self):
        '''If json file exists, convert obj dicts back to instances'''
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
