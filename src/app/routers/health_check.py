from fastapi import APIRouter
from http import HTTPStatus

health_check_router = APIRouter(
    prefix="/health",
    tags=["health"]
)

@health_check_router.get("/", status_code=HTTPStatus.OK)
def health_check_verify():
    return {
        "status": "healthy",
        "message": "Application working perfectly."
    }
