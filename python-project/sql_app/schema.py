from pydantic import BaseModel


class Location(BaseModel):
    city = str
    country = str
    description = str
    image_url = str

    class Config:
        orm_mode = True