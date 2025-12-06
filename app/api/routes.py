from fastapi import APIRouter, Query, HTTPException
from app.api.models import Weather, CityCreate, CityDelete, MessageResponse
from app.api.weather_service import *

router = APIRouter()

@router.get(
    "/",
    tags=["Root"],
    summary="API health check",
    description="Simple endpoint to verify that the API is running correctly."
)
def root():
    return {"message": "Hello, weather API!"}

@router.get(
    "/weather",
    response_model=Weather,
    tags=["Weather"],
    summary="Get weather by city",
    description="Retrieves the weather information for the specified city."
)
async def get_weather(city: str = Query(min_length=1, max_length=50)):
    try:
        return get_city(city)
    except ValueError:
        raise HTTPException(status_code=404, detail="City not found")

@router.get(
    "/weather/all",
    response_model=list[Weather],
    tags=["Weather"],
    summary="Get all cities and weather data",
    description="Returns a list with the weather information of all registered cities."
)
async def get_all_weathers():
    return get_all_cities()

@router.post(
    "/weather",
    status_code=201,
    response_model=Weather,
    tags=["Weather"],
    summary="Register a new city",
    description="Creates a new city weather entry if it does not already exist."
)
async def post_weather(city_data: CityCreate):
    try:
        return post_city(city_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put(
    "/weather",
    status_code=200,
    response_model=Weather,
    tags=["Weather"],
    summary="Update a city's weather",
    description="Updates the weather information for an existing city."
)
async def put_weather(city_data: CityCreate):
    try:
        return put_city(city_data)
    except KeyError:
        raise HTTPException(status_code=404, detail="City not found")

@router.delete(
    "/weather",
    status_code=200,
    response_model=MessageResponse,
    tags=["Weather"],
    summary="Delete a city",
    description="Removes a city from the database by its name."
)
async def delete_weather(city: CityDelete):
    try:
        return delete_city(city)
    except KeyError:
        raise HTTPException(status_code=404, detail="City not found")