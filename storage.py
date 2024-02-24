import json
from models.base_model import BaseModel  # Adjust the import based on your actual model classes

class Storage:
    """Class to handle data storage"""

    __file_path = "file.json"  # Adjust the file path as needed
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to a JSON file"""
        serialized = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)  # Use eval with caution, make sure it's safe in your context
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass  # File doesn't exist yet, ignore

    def close(self):
        """Method to close the storage"""
        self.reload()  # You might need to adjust this based on your needs

# Create a single instance of the Storage class for reuse
storage = Storage()
