from typing import Optional
from pydantic import BaseModel

class CreateCar(BaseModel):
    brand: str
    name: str
    color: str
    power: str
    safety_ratings: str
    
class UpdateCar(CreateCar):
    brand: str
    name: str
    color: str
    power: str
    safety_ratings: str

class ShowCar(BaseModel):
    brand: str
    name: str
    color: str
    power: str
    safety_ratings: str
    
    class Config():
        orm_mode = True #TODO: Need to understand this line