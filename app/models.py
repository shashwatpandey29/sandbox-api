from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    value: str
    description: Optional[str] = None
