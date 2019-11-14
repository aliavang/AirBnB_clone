#!/usr/bin/python3
"""Defines a FileStorage class."""
import json
from pathlib import Path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """A class for object serialization using a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gets the __objects class attribute."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        my_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file (__file_path) to __objects."""
        config = Path(FileStorage.__file_path)
        if config.is_file():
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {
                    k: classes[v["__class__"]](**v)
                    for k, v in json.load(f).items()
                }
