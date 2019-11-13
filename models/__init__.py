#!/usr/bin/python3
"""Creates a FileStorage instance."""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


storage = FileStorage()
storage.reload()
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}
