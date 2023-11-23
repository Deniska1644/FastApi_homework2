from fastapi import APIRouter
from db import product, database
from models import ProductIn, Product

router = APIRouter(prefix='/product')


@router.get("/", response_model=list[Product])
async def read_products():
    query = product.select()
    return await database.fetch_all(query)


@router.get("/{id}", response_model=ProductIn)
async def read_product(product_id: int):
    query = product.select().where(product.c.id == product_id)
    return await database.fetch_one(query)


@router.post("/", response_model=Product)
async def create_product(prod: ProductIn):
    query = product.insert().values(name=prod.name, description=prod.description, price=prod.price)
    last_record_id = await database.execute(query)
    return {**prod.dict(), "id": last_record_id}


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = product.update().where(product.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete('/{product_id}')
async def delete_product(product_id: int):
    query = product.delete().where(product.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
