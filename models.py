from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date