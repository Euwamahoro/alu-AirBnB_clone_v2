#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import os

class FileStorage:
    """Storage class for handling JSON serialization/deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                loaded_objs = json.load(f)

            for key, value in loaded_objs.items():
                class_name, obj_id = key.split('.')
                module = __import__('models.' + class_name, fromlist=[class_name])
                class_ = getattr(module, class_name)
                obj = class_(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    def close(self):
        """Calls reload method for deserializing the JSON file to objects"""
        self.reload()


