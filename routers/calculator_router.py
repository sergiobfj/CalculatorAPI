from fastapi import APIRouter, HTTPException
from schemas import OperationRequest, OperationResponse
import operations

router = APIRouter(prefix="/calculator", tags=["Calculator"])


operation_map = {
    "soma": operations.sum,
    "subtracao": operations.subtract,
    "multiplicacao": operations.multiply,
    "divisao": operations.divide,
}


@router.post("/", response_model=OperationResponse)
def calcular(payload: OperationRequest):
    try:
        func = operation_map.get(payload.operacao)

        if not func:
            raise ValueError("Operação inválida")

        resultado = func(payload.a, payload.b)

        return {
            "a": payload.a,
            "b": payload.b,
            "operacao": payload.operacao,
            "resultado": resultado
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))