from fastapi import APIRouter, Query, HTTPException
from app.api.models import Weather
from app.api.weather_service import *


router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello, weather API!"}

@router.get("/weather", response_model=Weather)
async def get_weather(city:str = Query(min_length=1, max_length=50)):
    try:
        return get_city(city)
    except ValueError:
        raise HTTPException(status_code=404, detail="City not found")
    
@router.get("/weather/all", response_model=list[Weather])
async def get_all_weathers():
    return get_all_cities()

@router.post("/weather", status_code=201, response_model=Weather)
async def post_weather(city_data:CityCreate):
    try:
        return post_city(city_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/weather", status_code=200, response_model=Weather)
async def put_weather(city_data:CityCreate):
    try:
        return put_city(city_data)
    except KeyError:
        raise HTTPException(status_code=404, detail="City not found")
    
@router.delete("/weather", status_code=200, response_model=MessageResponse)
async def delete_weather(city:CityDelete):
    try:
        return delete_city(city)
    except KeyError:
        raise HTTPException(status_code=404, detail="City not found")