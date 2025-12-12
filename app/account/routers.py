from fastapi import APIRouter, Depends, HTTPException
from app.account.services import create_user
from app.db.config import SessionDep


router = APIRouter(prefix="/account", tags=["Account"])

@router.post("/register")
async def register_user(session: SessionDep, name: str, email: str):
    try:
        user = await create_user(session, name, email)
        return {"id": user.id, "name": user.name, "email": user.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

