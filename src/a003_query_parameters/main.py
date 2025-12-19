# --- Query Parameters ---
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# --- Optional Query Parameters ---
@app.get("/items_optional/{item_id}")
async def read_optional(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# --- bool Query Parameters ---
# short: bool in {1, 0, true, false, True, False, yes, no, Yes, No}
@app.get("/items_bool/{item_id}")
async def read_bool(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# -- Required Query Parameters ---
@app.get("/items_required/{item_id}")
async def read_required(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


# --- Enum Query Parameters ---
from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    leet = "leet"


@app.get("/models/{item_id}")
async def get_model(item_id: int, model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "leet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}