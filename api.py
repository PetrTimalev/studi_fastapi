from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome():
    return "Hello World"


@app.get("/hello/{first_name}/{last_name}")
async def welcome_user(first_name: str, last_name: str) -> dict:
    return {"user": f'Hello, {first_name.title()} {last_name.title()}'}


@app.get("/order/{order_id}")
async def order(order_id: int) -> dict:
    return {"id": order_id}


@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}


@app.get("/user")
async def login(username: str, age: int=30) -> dict:
    return {"user": username, "age": age}


@app.get('/users')
async def users(name: str = 'Undefined', age: int = 18) -> dict:
    return {'user_name': name, 'user_age': age}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", reload=True)



