from app.api.mock_data import cities
from app.api.models import *

def get_city(city:str) -> Weather:
    city = city.strip().lower()
    for place in cities:
        if place["city"].lower() == city:
            return Weather(**place)
    raise ValueError("City not found")

def get_all_cities() -> list[Weather]:
    return [Weather(**place) for place in cities]

def post_city(city_data: CityCreate) -> Weather:
    new_city = {
        "city": city_data.city,
        "temperature": f"{city_data.temperature}ºC",
        "description": city_data.description
    }
    cities.append(new_city)
    return Weather(**new_city)

def put_city(city_data:CityCreate) -> Weather:
    
    city = city_data.city.strip().lower()
    for place in cities:
        if place["city"].lower() == city:
            place["temperature"] = f"{city_data.temperature}ºC"
            place["description"] = city_data.description
            return Weather(**place)
    raise KeyError("The city provided does not exist")

def delete_city(city_name:CityDelete) -> MessageResponse:
    city = city_name.city.strip().lower()
    for idx, place in enumerate(cities):
        if place["city"].lower() == city:
            cities.pop(idx)
            return MessageResponse(detail=f"{city_name.city} has been removed successfully.")
    raise KeyError ("The city provided does not exist.")