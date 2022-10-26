from pydantic import BaseModel
from typing import List


class Link(BaseModel):
    name: str
    link: str
    type: str
    tags: List[str]
