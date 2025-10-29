from sqlalchemy import Column, Integer, String
from .database import Base


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    especialidad = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    email = Column(String, nullable=True)
