from app.account.models import User
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(session: AsyncSession, name: str, email: str):
   new_user = User(name=name, email=email)
   session.add(new_user)
   await session.commit()
   await session.refresh(new_user)
   return new_user