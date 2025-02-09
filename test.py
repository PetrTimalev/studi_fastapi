
from fastapi import FastAPI, Query

app = FastAPI()
profiles_dict = {
    'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'}
}


@app.get("/users")
async def retrieve_user_profile(username: str = Query(min_length=2, max_length=50, description='Имя пользователя')):
    if username in profiles_dict:
        return profiles_dict[username]
    return {'message': f'Пользователь {username} не найден.'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("test:app", reload=True)
