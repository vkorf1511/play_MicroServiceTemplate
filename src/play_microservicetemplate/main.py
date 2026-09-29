from fastapi import FastAPI
from .page_landing import landing_page
from .page_root import hello_world  
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
app.mount(
    "/static/css",
    StaticFiles(directory=Path(__file__).parent / "static/css"),
    name="static/css",
)

app.mount(
    "/static/js",
    StaticFiles(directory=Path(__file__).parent / "static/js"),
    name="static/jss",
)


@app.get("/")
def read_root():
    return hello_world()

@app.get("/FE")
def read_FE():
    return landing_page()