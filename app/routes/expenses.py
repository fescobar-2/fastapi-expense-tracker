from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_expenses():
    return {"message": "Expenses route placeholder"}
