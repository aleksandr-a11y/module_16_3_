from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_users(username: Annotated[str, Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$")],
                     age: Annotated[int, Path(ge=18, le=100, description="Age from 18 to 100")]) -> str:
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def put_users(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='75')],
                    username: Annotated[str, Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$")],
                    age: Annotated[int, Path(ge=18, le=100, description="Age from 18 to 100")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_users(user_id: str) -> str:
    del users[user_id]
    return f"User {user_id} has been deleted"
