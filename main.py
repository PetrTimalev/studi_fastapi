from fastapi import FastAPI, Path

app = FastAPI()

# Добавив проверку на минимальную и максимальную длину имени -username.
# Также мы добавили описание поля и добавили в поле пример имени, username

# установили границы числа для поля age от 0 до 100 и добавили описание поля, age
@app.get("/user/{username}/{age}")
async def login(username: str = Path(min_length=3, max_length=15, description='Enter your username', example='Ilya'),
                age: int = Path(ge=0, le=100, description="Enter your age")) -> dict:
    return {"user": username, "age": age}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)