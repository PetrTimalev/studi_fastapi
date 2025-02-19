from pydantic import BaseModel


class Message(BaseModel):
    id: int | None = None
    text: str

    model_config = {
        "json_schema_extra": {"examples": [{"text": "Simple message", }]}
    }
