from pydantic import BaseModel

class Weather(BaseModel):
    city: str
    temperature: str
    description: str | None = None