#!/usr/bin/python3
"""
City class
"""
from models.base_model import BaseModel


class city(BaseModel):
    """
    Child of BaseModel
    Public attributes:
        state_id: (str)
        name: (str)
    """
    state_id = ""
    name = ""
