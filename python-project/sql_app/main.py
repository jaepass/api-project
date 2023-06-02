import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import Location as ModelLocation
from schema import Location as SchemaLocation

# Instantiate a FastAPI Python class instance
app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

#
# Crud operations start
#

@app.post("/location/", response_model=SchemaLocation)
def create_location(location: SchemaLocation):
    db_location = ModelLocation(
        city=location.city, country=location.country, description=location.description, image_url=location.image_url
    )
    db.session.add(db_location)
    db.session.commit()
    return location


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

