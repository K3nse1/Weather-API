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

def put_city(city:str, temperature:int, description:str):
    if temperature < -40 or temperature > 50:
        raise ValueError("The temperature provided makes no sense")
    
    city = city.strip().lower()
    for place in cities:
        if place["city"].lower() == city:
            place["temperature"] = f"{temperature}ºC"
            place["description"] = description
            return {"detail": f"{place["city"]} has been updated successfully."}
    raise KeyError("The city provided does not exist")

def delete_city(city:str):
    city = city.strip().lower()
    for idx, place in enumerate(cities):
        if place["city"].lower() == city:
            cities.pop(idx)
            return {"detail": f'{place["city"]} removed successfully.'}
    raise KeyError ("The city provided does not exist.")