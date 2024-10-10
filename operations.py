from database import db
from datetime import datetime,timedelta
from fastapi import FastAPI
from models import ItemCreate

app=FastAPI()


def create_item(item_data):
    item_data['insert_date'] = datetime.now() 
    result = db.items.insert_one(item_data)      
    return str(result.inserted_id)  


# FastAPI route to create a new item
@app.post("/items", response_model=ItemCreate)
async def add_item(item: ItemCreate):
    item_id = create_item(item.model_dump())           
    return {"id": item_id} 