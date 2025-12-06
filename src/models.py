from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorit_people: Mapped[List["FavoritPeople"]
                           ] = relationship(back_populates="user")
    favorit_planeta: Mapped[List["FavoritPlaneta"]
                           ] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    height: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorit_people: Mapped[List["FavoritPeople"]
                           ] = relationship(back_populates="persona")
    name: Mapped[str] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "age": self.age,
            "height": self.height,
            "name": self.name,
        }


class FavoritPeople(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(
        db.ForeignKey("user.id"), primary_key=True)
    id_people: Mapped[int] = mapped_column(
        db.ForeignKey("people.id"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="favorit_people")
    persona: Mapped[List["People"]] = relationship(
        back_populates="favorit_people")

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.user,
            "id_people": self.people,
        }


class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    diametro: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    gravedad: Mapped[str] = mapped_column(nullable=False)
    clima: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    name: Mapped[str] = mapped_column(
        String(120), unique=False, nullable=False)
    favorit_planeta: Mapped[List["FavoritPlaneta"]] = relationship(back_populates="planeta")

    def serialize(self):
        return {
            "id": self.id,
            "diametro": self.diametro,
            "name": self.name,
            "clima": self.clima,
            "gravedad": self.gravedad,
        }


class FavoritPlaneta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(
        db.ForeignKey("user.id"), primary_key=True)
    id_planeta: Mapped[int] = mapped_column(
        db.ForeignKey("planeta.id"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="favorit_planeta")
    planeta: Mapped["Planeta"] = relationship(back_populates="favorit_planeta")

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.user,
            "id_planeta": self.planeta,
        }
