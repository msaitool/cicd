from pydantic import BaseModel, Field
import uuid 
from typing import Optional

class UserSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(..., unique_items= None)
    password: str = Field(...)


    class Config:
        schema_extra= {
            "example": {
                "_id": "123",
                "name": "thuha",
                "email": "a@",
                "password": "123"
            }
        }


class UpdateUserSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra= {
            "example": {
                "name": "thuha",
                "email": "a@",
                "password": "123"
            }
        }