# FastAPI Veterinarios

Pequeña API para manejar entidades `Veterinario` con SQLite.

Endpoints:

- POST /veterinarios/create -> Crear veterinario
- POST /veterinarios/update -> Actualizar veterinario
- GET  /veterinarios/all -> Obtener todos
- GET  /veterinarios/v_id={id} -> Obtener por id

Instalación y ejecución rápida (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

El proyecto usa SQLAlchemy y un patrón repositorio simple para respetar principios SOLID.
