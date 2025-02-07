from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

#  включим параметр pattern в функцию Query(), чтобы ограничить значение first_name либо начинаться
#  с J, либо заканчиваться на s (как например John, Tomas).
@app.get("/user/{username}")
async def login(
        username: Annotated[
            str, Path(min_length=3, max_length=15, description='Enter your username', example='permin0ff')],
        first_name: Annotated[
            str | None, Query(max_length=10, pattern="^J|s$")] = None) -> dict:
    return {"user": username, "Name": first_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)