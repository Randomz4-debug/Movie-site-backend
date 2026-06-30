from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import logging


app = FastAPI(title="Chat App", version="0.1.0")
# templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/movies")
async def get_movies(name: str = "popular", type: str = "shows"):
    url = f"https://api.tvmaze.com/search/{type}?q={name}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8000)
