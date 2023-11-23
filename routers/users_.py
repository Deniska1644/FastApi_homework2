from fastapi import APIRouter
from db import users, database
from models import Users, UsersIn, UsersChange

router = APIRouter(prefix='/users')


@router.get("/", response_model=list[UsersIn])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/{id}", response_model=UsersIn)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.post("/", response_model=Users)
async def create_user(user: UsersIn):
    query = users.insert().values(name=user.name, lastname=user.lastname, mail=user.mail,password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.put("/{id}", response_model=UsersChange)
async def update_user(user_id: int, new_user: UsersIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@router.delete('/{id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
