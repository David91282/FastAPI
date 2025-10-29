from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, repository
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Veterinarios API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/veterinarios/create", response_model=schemas.VeterinarioOut)
def create_veterinario(veterinario: schemas.VeterinarioCreate, db: Session = Depends(get_db)):
    repo = repository.VeterinarioRepository(db)
    return repo.create(veterinario)


@app.post("/veterinarios/update", response_model=schemas.VeterinarioOut)
def update_veterinario(veterinario: schemas.VeterinarioUpdate, db: Session = Depends(get_db)):
    repo = repository.VeterinarioRepository(db)
    updated = repo.update(veterinario)
    if not updated:
        raise HTTPException(status_code=404, detail="Veterinario not found")
    return updated


@app.get("/veterinarios/all", response_model=list[schemas.VeterinarioOut])
def get_veterinarios(db: Session = Depends(get_db)):
    repo = repository.VeterinarioRepository(db)
    return repo.get_all()


@app.get("/veterinarios/v_id={v_id}", response_model=schemas.VeterinarioOut)
def get_veterinario_by_id(v_id: int, db: Session = Depends(get_db)):
    repo = repository.VeterinarioRepository(db)
    vet = repo.get_by_id(v_id)
    if not vet:
        raise HTTPException(status_code=404, detail="Veterinario not found")
    return vet
