from fastapi import APIRouter
from db import orders, database
from models import Orders, OrdersIn
from datetime import datetime

router = APIRouter(prefix='/orders')


@router.get("/", response_model=list[Orders])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get("/{id}", response_model=Orders)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.post("/", response_model=OrdersIn)
async def create_order(ord: OrdersIn):
    query = orders.insert().values(user_id=ord.user_id, product_id=ord.product_id, status=ord.status)
    last_record_id = await database.execute(query)
    time_now = str(datetime.now())
    print(time_now)
    return {**ord.dict(), "id": last_record_id, "time_order": time_now}


@router.put("/{id}", response_model=Orders)
async def update_order(order_id: int, new_order: OrdersIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    time_now = str(datetime.now())
    return {**new_order.dict(), "id": order_id, "time_order": time_now}


@router.delete('/{id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
