#!/usr/bin/python3
"""
User class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''Child of BaseModel class'''

    email = ""
    first_name = ""
    last_name = ""
    password = ""
