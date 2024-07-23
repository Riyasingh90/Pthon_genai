from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from schemas.car import CreateCar, UpdateCar
from db.models.car_model import Car

def create_new_car(car: CreateCar, db: Session):
    try:
        new_car = Car(**car.model_dump())
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        return new_car
    except SQLAlchemyError as e:
        raise HTTPException(detail="Database error", status_code=500)

def retrieve_car(name: str, db: Session):
    car = db.query(Car).filter(Car.name==name).first()
    return car

def cars_with_brand(brand: str, db: Session):
    try:
        cars_in_db = db.query(Car).filter(Car.brand==brand).all()
        if not cars_in_db:
            raise HTTPException(status_code=404, detail=f"No cars with brand {brand} found.")
        return cars_in_db
    except SQLAlchemyError as e:
        raise HTTPException(detail="Database error", status_code=500)

def update_car(power: str, car: UpdateCar, db: Session):
    try:
        car_in_db = db.query(Car).filter(Car.power == power).first()
        if not car_in_db:
            raise HTTPException(status_code=404, detail="Car not found")

        car_in_db.brand = car.brand
        car_in_db.color = car.color
        car_in_db.name = car.name
        car_in_db.safety_ratings = car.safety_ratings
        db.add(car_in_db)
        db.commit()
        db.refresh(car_in_db)
        return car_in_db
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

def remove_car_by_name(name: str, db: Session):
    try:
        car_in_db = db.query(Car).filter(Car.name == name)
        if not car_in_db.first():
            return {"error": f"Car with name {name} not found"}
        car_in_db.delete()
        db.commit()
        return {"message": f"Delete car with name {name}"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")