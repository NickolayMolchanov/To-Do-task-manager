from datetime import date, datetime
from typing import List

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(auto_now_add=True)

    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        back_populates="project",
    )