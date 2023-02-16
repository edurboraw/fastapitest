from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q":q}

def start():
    uvicorn.run("fast_api_demo.main:app", host = "0.0.0.0", port=8000, reload=True)
