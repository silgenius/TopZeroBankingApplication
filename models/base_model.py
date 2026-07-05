from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            
            if kwargs.get("id") is None:
                setattr(self, "id", str(uuid.uuid4()))
                
            if kwargs.get("created_at") and type(kwargs["created_at"]) is str:
                setattr(self, "created_at", datetime.fromisoformat(kwargs["created_at"]))
            else:
                setattr(self, "created_at", datetime.now())
                
            if kwargs.get("updated_at") and type(kwargs["updated_at"]) is str:
                setattr(self, "updated_at", datetime.fromisoformat(kwargs["updated_at"]))
            else:
                setattr(self, "updated_at", datetime.now())
    
    def to_dict(self):
        obj_dict = {**self.__dict__}
        obj_dict["id"] = str(obj_dict["id"])
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
    
    def save(self):
        from . import storage
        storage.new(self)
        storage.save()
        
    
    def __str__(self):
        for k, v in self.__dict__.items():
            if k is not "password" or k is not "__class__":
                print()
                