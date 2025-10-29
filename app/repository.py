from sqlalchemy.orm import Session
from . import models, schemas


class VeterinarioRepository:
    """Repositorio simple para Veterinario.

    Responsable de acceder y modificar la BBDD. Mantiene la lógica de acceso a datos
    separada de la API (Single Responsibility, Dependency Inversion via inyección de Session).
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, vet: schemas.VeterinarioCreate) -> models.Veterinario:
        db_vet = models.Veterinario(**vet.dict())
        self.db.add(db_vet)
        self.db.commit()
        self.db.refresh(db_vet)
        return db_vet

    def update(self, vet: schemas.VeterinarioUpdate) -> models.Veterinario | None:
        db_vet = self.db.query(models.Veterinario).filter(models.Veterinario.id == vet.id).first()
        if not db_vet:
            return None
        for key, value in vet.dict(exclude={"id"}).items():
            setattr(db_vet, key, value)
        self.db.commit()
        self.db.refresh(db_vet)
        return db_vet

    def get_all(self) -> list[models.Veterinario]:
        return self.db.query(models.Veterinario).all()

    def get_by_id(self, v_id: int) -> models.Veterinario | None:
        return self.db.query(models.Veterinario).filter(models.Veterinario.id == v_id).first()
