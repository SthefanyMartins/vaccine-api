from fastapi import FastAPI
from app.routers.health_check import health_check_router


app = FastAPI()

app.include_router(health_check_router)
