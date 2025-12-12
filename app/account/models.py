from app.db.config import Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
  __tablename__ = "users"
  
  id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
  name : Mapped[str] = mapped_column(String(50), nullable=False)
  email : Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
  