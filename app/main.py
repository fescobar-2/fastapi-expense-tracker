from fastapi import FastAPI
from app.routes import users, expenses

app = FastAPI(title="Expense Tracker API")

# Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
