from fastapi import APIRouter
from apis import route_car

api_router = APIRouter()

api_router.include_router(route_car.router, prefix="/cars", tags=["cars"])