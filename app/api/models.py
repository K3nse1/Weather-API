from pydantic import BaseModel, Field

class Weather(BaseModel):
    city: str
    temperature: str
    description: str | None = None

class CityCreate(BaseModel):
    city: str = Field(..., min_length=1, max_length=50)
    temperature: int = Field(..., ge=-40, le=50)
    description:str | None = Field(None, min_length=2, max_length=50)

class CityDelete(BaseModel):
    city:str = Field(..., min_length=1, max_length=50)

class MessageResponse(BaseModel):
    detail:str = Field(..., min_length=5, max_length=50)