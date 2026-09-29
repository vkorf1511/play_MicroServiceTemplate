from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel
from .page_landing import landing_page
from .page_root import hello_world  
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from datetime import date, datetime
from .database import get_latest_birthday, save_birthday

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


class BirthdayRequest(BaseModel):
    value: str


@app.post("/api/birthdays", status_code=status.HTTP_201_CREATED)
def create_birthday(request: BirthdayRequest) -> dict[str, str]:
    try:
        birthday = datetime.strptime(request.value, "%d/%m/%Y").date()
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Birthday must use DD/MM/YYYY format.",
        ) from error

    if birthday.strftime("%d/%m/%Y") != request.value:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Birthday must use DD/MM/YYYY format.",
        )

    if birthday < date(1900, 1, 1) or birthday > date.today():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Birthday must be between 01/01/1900 and today.",
        )

    return save_birthday(request.value)


@app.get("/api/birthdays/latest")
def read_latest_birthday() -> dict[str, str]:
    birthday = get_latest_birthday()
    if birthday is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No birthday has been saved yet.",
        )
    return birthday