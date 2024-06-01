from pydantic import BaseModel

class Speech(BaseModel):
    id: str
    firstname: str
    lastname: str
    speaker: str | None = None
    distance: str | None = None
    content: str | None = None