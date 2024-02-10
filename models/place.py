#!/usr/bin/python3
"""
Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Child of BaseModel
    Public attributes:
        city_id:            (str)
        user_id:            (str)
        name:               (str)
        description:        (str)
        number_rooms:       (int)
        number_bathrooms:   (int)
        max_guests:         (int)
        price_by_night:     (int)
        latitude:           (float)
        longitude:          (float)
        amenity_ids:        (list)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    numer_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
