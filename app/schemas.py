from pydantic import BaseModel
from typing import Optional


class VeterinarioBase(BaseModel):
    nombre: str
    apellidos: str
    especialidad: Optional[str] = None


class VeterinarioCreate(VeterinarioBase):
    pass


class VeterinarioUpdate(VeterinarioBase):
    id: int


class VeterinarioOut(VeterinarioBase):
    id: int

    class Config:
        orm_mode = True
