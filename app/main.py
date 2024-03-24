from fastapi import FastAPI
from starlette.status import HTTP_200_OK

app = FastAPI(description="FastAPI backend for registration in ali")


@app.get("/")
def check_health():
    return {"status": HTTP_200_OK}
