"""
Generated Code Metadata:
========================
Original URL: https://purworejokab.go.id
Prompt: Design a RESTful API for managing and retrieving information on fasilitas kesehatan and fasilitas transportasi in Purworejo Regency.
Generated: DETERMINISTIC_ff22571b286a4790
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import databases
import sqlalchemy
from datetime import datetime

# Database configuration
DATABASE_URL = "sqlite:///./purworejo.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Enums
class FasilitasType(str, Enum):
    kesehatan = "kesehatan"
    transportasi = "transportasi"

class FasilitasKesehatanType(str, Enum):
    rumah_sakit = "rumah_sakit"
    puskesmas = "puskesmas"
    klinik = "klinik"
    apotek = "apotek"

class FasilitasTransportasiType(str, Enum):
    terminal = "terminal"
    stasiun = "stasiun"
    halte = "halte"
    pelabuhan = "pelabuhan"

# Models
fasilitas = sqlalchemy.Table(
    "fasilitas",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nama", sqlalchemy.String(100)),
    sqlalchemy.Column("alamat", sqlalchemy.String(200)),
    sqlalchemy.Column("latitude", sqlalchemy.Float),
    sqlalchemy.Column("longitude", sqlalchemy.Float),
    sqlalchemy.Column("tipe", sqlalchemy.Enum(FasilitasType)),
    sqlalchemy.Column("subtipe", sqlalchemy.String(50)),
    sqlalchemy.Column("deskripsi", sqlalchemy.Text),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
)

# Pydantic models
class FasilitasBase(BaseModel):
    nama: str
    alamat: str
    latitude: float
    longitude: float
    tipe: FasilitasType
    subtipe: str
    deskripsi: Optional[str] = None

class FasilitasCreate(FasilitasBase):
    pass

class Fasilitas(FasilitasBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class FasilitasKesehatanCreate(BaseModel):
    nama: str
    alamat: str
    latitude: float
    longitude: float
    tipe: FasilitasKesehatanType
    deskripsi: Optional[str] = None

class FasilitasTransportasiCreate(BaseModel):
    nama: str
    alamat: str
    latitude: float
    longitude: float
    tipe: FasilitasTransportasiType
    deskripsi: Optional[str] = None

# App setup
app = FastAPI(title="Purworejo Facilities API", 
              description="API for managing health and transportation facilities in Purworejo Regency")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Routes
@app.post("/fasilitas/", response_model=Fasilitas, status_code=status.HTTP_201_CREATED)
async def create_fasilitas(fasilitas_data: FasilitasCreate):
    query = fasilitas.insert().values(**fasilitas_data.dict())
    last_record_id = await database.execute(query)
    return {**fasilitas_data.dict(), "id": last_record_id}

@app.post("/fasilitas/kesehatan/", response_model=Fasilitas, status_code=status.HTTP_201_CREATED)
async def create_fasilitas_kesehatan(fasilitas_data: FasilitasKesehatanCreate):
    fasilitas_dict = fasilitas_data.dict()
    fasilitas_dict["tipe"] = FasilitasType.kesehatan
    fasilitas_dict["subtipe"] = fasilitas_dict.pop("tipe")
    
    query = fasilitas.insert().values(**fasilitas_dict)
    last_record_id = await database.execute(query)
    return {**fasilitas_dict, "id": last_record_id}

@app.post("/fasilitas/transportasi/", response_model=Fasilitas, status_code=status.HTTP_201_CREATED)
async def create_fasilitas_transportasi(fasilitas_data: FasilitasTransportasiCreate):
    fasilitas_dict = fasilitas_data.dict()
    fasilitas_dict["tipe"] = FasilitasType.transportasi
    fasilitas_dict["subtipe"] = fasilitas_dict.pop("tipe")
    
    query = fasilitas.insert().values(**fasilitas_dict)
    last_record_id = await database.execute(query)
    return {**fasilitas_dict, "id": last_record_id}

@app.get("/fasilitas/", response_model=List[Fasilitas])
async def get_all_fasilitas():
    query = fasilitas.select()
    return await database.fetch_all(query)

@app.get("/fasilitas/{fasilitas_id}", response_model=Fasilitas)
async def get_fasilitas(fasilitas_id: int):
    query = fasilitas.select().where(fasilitas.c.id == fasilitas_id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail="Fasilitas not found")
    return result

@app.get("/fasilitas/kesehatan/", response_model=List[Fasilitas])
async def get_fasilitas_kesehatan():
    query = fasilitas.select().where(fasilitas.c.tipe == FasilitasType.kesehatan)
    return await database.fetch_all(query)

@app.get("/fasilitas/kesehatan/{subtype}", response_model=List[Fasilitas])
async def get_fasilitas_kesehatan_by_type(subtype: FasilitasKesehatanType):
    query = fasilitas.select().where(
        (fasilitas.c.tipe == FasilitasType.kesehatan) & 
        (fasilitas.c.subtipe == subtype.value)
    )
    return await database.fetch_all(query)

@app.get("/fasilitas/transportasi/", response_model=List[Fasilitas])
async def get_fasilitas_transportasi():
    query = fasilitas.select().where(fasilitas.c.tipe == FasilitasType.transportasi)
    return await database.fetch_all(query)

@app.get("/fasilitas/transportasi/{subtype}", response_model=List[Fasilitas])
async def get_fasilitas_transportasi_by_type(subtype: FasilitasTransportasiType):
    query = fasilitas.select().where(
        (fasilitas.c.tipe == FasilitasType.transportasi) & 
        (fasilitas.c.subtipe == subtype.value)
    )
    return await database.fetch_all(query)

@app.put("/fasilitas/{fasilitas_id}", response_model=Fasilitas)
async def update_fasilitas(fasilitas_id: int, fasilitas_data: FasilitasCreate):
    query = (
        fasilitas.update()
        .where(fasilitas.c.id == fasilitas_id)
        .values(**fasilitas_data.dict())
    )
    await database.execute(query)
    return await get_fasilitas(fasilitas_id)

@app.delete("/fasilitas/{fasilitas_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fasilitas(fasilitas_id: int):
    query = fasilitas.delete().where(fasilitas.c.id == fasilitas_id)
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Fasilitas not found")

# Create tables (for development)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
```
