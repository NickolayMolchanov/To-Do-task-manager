from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(default="in progress")
    deadline: Mapped[date | None] = mapped_column(Date, nullable=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))

    project: Mapped["Project"] = relationship(
        "Project",
        back_populates="tasks",
    )