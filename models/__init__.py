#!/usr/bin/python3
"""instance for your application"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage

list_class = {"BaseModel": BaseModel, "State": State, "Amenity": Amenity,
              "Place": Place, "Review": Review, "User": User, "City": City}
storage = FileStorage()
storage.reload()
