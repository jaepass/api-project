from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    country = Column(String)
    description = Column(String)
    image_url = Column(String)


# from sqlalchemy import String, ForeignKey, Column, Integer
# from .database import Base


# class Program(Base):
#     __tablename__ = "programs"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     category_id = Column(String, index=True)
#     country = Column(String, index=True)
#     city = Column()

# class Program(Base):
#   __tablename__ = "programs"

#   id = Column(Integer, primary_key=True, index=True)
#   name = Column(String, index=True)
