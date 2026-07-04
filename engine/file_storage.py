import json
from models.user import User


class FileStorage ():
    __storage = {}
    __filepath = "topzero.json"
    mapper = {
        "User": User
    }
    
    @classmethod
    def new(cls, obj):
        cls.__storage[f"{obj.__class__.__name__}.{str(obj.id)}"] = obj
        return obj.id
    
    @classmethod
    def save(cls):
        with open(cls.__filepath, "w+", encoding="utf-8") as f:
            sterilized_storage = {}
            for k, v in cls.__storage.items():
                sterilized_storage.update({str(k): v.to_dict()})
            f.write(json.dumps(sterilized_storage))
            
        return
    
    @classmethod
    def reload(cls):
        with open(cls.__filepath, "r") as f:
            d = json.loads(f.read())
            for k, v in d.items():
                new_obj = cls.mapper[k.split(".", 1)[0]](**v)
                cls.new(new_obj)
                
        return
    
    @classmethod
    def find(cls, obj_name):
        res = []
        for v in cls.__storage.values():
            if (v.__class__.__name__ == obj_name):
                res.append(v)
        return res