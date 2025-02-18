from datetime import date
from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: int
    name: str
    birthday_date: date

    @field_validator('name', mode='before')
    def validate_name(cls, v):
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValueError("Имя должно быть строкой или числом")


dima = User(
    id="3",
    name=123,
    birthday_date="1990-11-22"
)

to_dict = dima.model_dump()
to_json = dima.model_dump_json()

print(to_dict, type(to_dict))
print(to_json, type(to_json))
