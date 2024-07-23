from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.car import CreateCar, ShowCar, UpdateCar
from db.repository.car import create_new_car, retrieve_car, update_car, cars_with_brand, remove_car_by_name

router = APIRouter()

@router.post("/addCar", response_model=ShowCar, status_code=status.HTTP_201_CREATED)
async def create_car(car: CreateCar, db: Session = Depends(get_db)):
    car = create_new_car(car=car, db=db)
    return car

@router.get("/getCars/name/{name}", response_model=ShowCar, status_code=status.HTTP_200_OK)
async def get_car_by_name(name: str, db: Session = Depends(get_db)):
    car = retrieve_car(name=name, db=db)
    if not car:
        raise HTTPException(detail=f"car with name {name} is not found", status_code=status.HTTP_404_NOT_FOUND)
    return car

@router.get("/getCars/brand/{brand}", response_model=List[ShowCar], status_code=status.HTTP_200_OK)
async def get_cars_by_brand(brand: str, db: Session = Depends(get_db)):
    cars = cars_with_brand(brand=brand, db=db)
    if not cars:
        raise HTTPException(detail=f"no car found with brand ${brand}", status_code=status.HTTP_404_NOT_FOUND)
    return cars

@router.put("/updateCar/power/{power}", response_model=ShowCar, status_code=status.HTTP_200_OK)
async def update_car_by_power(power: str, car: UpdateCar, db: Session = Depends(get_db)):
    car = update_car(power=power, car=car, db=db)
    if not car:
        raise HTTPException(detail=f"car with power {power} cannot be updated", status_code=status.HTTP_403_FORBIDDEN)
    return car

@router.delete("/deleteCar/name/{name}", status_code=status.HTTP_200_OK)
async def delete_car_by_name(name: str, db: Session = Depends(get_db)):
    message = remove_car_by_name(name=name, db=db)
    if message.get("error"):
        raise HTTPException(detail=f"car with name {name} is not found", status_code=status.HTTP_400_BAD_REQUEST)
    return {"message": message.get("message")}