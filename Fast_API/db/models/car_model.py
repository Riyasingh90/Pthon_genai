from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime
from db.base_class import Base

class Car(Base):
    brand = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    power = Column(String, nullable=False)
    safety_ratings = Column(String)