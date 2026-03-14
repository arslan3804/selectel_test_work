from pydantic import BaseModel
from http import HTTPStatus


class ErrorResponse(BaseModel):
    detail: str


NOT_FOUND_RESPONSE = {
    HTTPStatus.NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Resource not found",
    }
}

ALREADY_EXISTS_RESPONSE = {
    HTTPStatus.OK: {
        "model": ErrorResponse,
        "description": "Resource already exists",
    }
}
