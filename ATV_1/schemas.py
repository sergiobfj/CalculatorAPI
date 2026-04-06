from pydantic import BaseModel
from typing import Literal

class OperationRequest(BaseModel):
    a: float
    b: float
    operacao: Literal["soma", "subtracao", "multiplicacao", "divisao"]


class OperationResponse(BaseModel):
    a: float
    b: float
    operacao: str
    resultado: float