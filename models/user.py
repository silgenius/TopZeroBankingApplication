from .base_model import BaseModel
import random
from hashlib import md5


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        self.account_number = random.randint(111111, 999999)
        super().__init__(*args, **kwargs)
        
    def __setattr__(self, name, value):
        if (name == "account_pin" and len(value) != 32):
            value = md5(value.encode()).hexdigest()
        return super().__setattr__(name, value)
    
    @classmethod
    def find_account(cls, account_pin, account_number):
        from . import storage
        res = storage.find(cls.__name__)
        for v in res:
            if v["account_number"] == account_number and v["account_pin"] == account_pin:
                return v
        return None