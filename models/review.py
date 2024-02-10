#!/usr/bin/python3
"""
Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Child of BaseModel
    Public class attributes:
        place_id:   (str)
        user_id:    (str)
        text:       (str)
    """
    place_id = ""
    user_id = ""
    text = ""
