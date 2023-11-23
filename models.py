from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Product(BaseModel):
    id: int
    name: str = Field(max_length=100)
    description: Optional[str] = Field(max_length=200)
    price: float


class ProductIn(BaseModel):
    name: str = Field(max_length=100)
    description: Optional[str] = Field(max_length=200)
    price: float


class Users(BaseModel):
    id: int
    name: str = Field(max_length=100, min_length=3)
    lastname: Optional[str] = Field(max_length=100, min_length=3)
    mail: str = Field(max_length=100, min_length=5)
    password: str = Field(min_length=5, max_length=30)


class UsersIn(BaseModel):
    name: str = Field(max_length=100, min_length=3)
    lastname: Optional[str] = Field(max_length=100, min_length=3)
    mail: str = Field(max_length=100, min_length=5)
    password: str = Field(min_length=5, max_length=30)


class UsersChange(BaseModel):
    id: int
    name: str = Field(max_length=100, min_length=3)
    lastname: Optional[str] = Field(max_length=100, min_length=3)
    mail: str = Field(max_length=100, min_length=5)


class Orders(BaseModel):
    id: int
    user_id: int
    product_id: int
    time_order: str
    status: bool


class OrdersIn(BaseModel):
    user_id: int
    product_id: int
    status: bool



# class OrdersCreate(BaseModel):



