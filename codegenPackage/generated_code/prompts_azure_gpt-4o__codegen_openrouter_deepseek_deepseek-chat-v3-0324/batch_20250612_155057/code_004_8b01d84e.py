"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a REST API design for Stellar Crop that supports player data storage, including crop growth statistics, planetary exploration logs, and interactions with "Koloni sakinleri."
Generated: DETERMINISTIC_8b01d84ed7aa2046
Batch ID: 20250612_155057
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
from datetime import datetime
import uuid
import motor.motor_asyncio
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MongoDB setup
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.stellar_crop
players_collection = db.players

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Stellar Crop API", description="API for managing player data in Stellar Crop")

# Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class PlayerBase(BaseModel):
    username: str
    email: str

class PlayerCreate(PlayerBase):
    password: str

class Player(PlayerBase):
    id: str
    is_active: bool

    class Config:
        from_attributes = True

class CropStat(BaseModel):
    crop_id: str
    planet_id: str
    growth_stage: int
    planted_at: datetime
    harvested_at: Optional[datetime] = None
    yield_amount: Optional[float] = None

class PlanetaryLog(BaseModel):
    planet_id: str
    visited_at: datetime
    coordinates: str
    discovered_resources: List[str]
    notes: Optional[str] = None

class KoloniInteraction(BaseModel):
    koloni_id: str
    interaction_type: str
    interaction_date: datetime
    outcome: str
    notes: Optional[str] = None

class PlayerData(BaseModel):
    player: Player
    crop_stats: List[CropStat]
    planetary_logs: List[PlanetaryLog]
    koloni_interactions: List[KoloniInteraction]

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def authenticate_player(username: str, password: str):
    player = await players_collection.find_one({"username": username})
    if not player:
        return False
    if not verify_password(password, player["hashed_password"]):
        return False
    return player

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_player(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    player = await players_collection.find_one({"username": token_data.username})
    if player is None:
        raise credentials_exception
    return player

# Routes
@app.post("/players/", response_model=Player, status_code=status.HTTP_201_CREATED)
async def create_player(player: PlayerCreate):
    existing_player = await players_collection.find_one({"$or": [{"username": player.username}, {"email": player.email}]})
    if existing_player:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hash(player.password)
    player_dict = {
        "id": str(uuid.uuid4()),
        "username": player.username,
        "email": player.email,
        "hashed_password": hashed_password,
        "is_active": True,
        "crop_stats": [],
        "planetary_logs": [],
        "koloni_interactions": []
    }
    
    result = await players_collection.insert_one(player_dict)
    created_player = await players_collection.find_one({"_id": result.inserted_id})
    return created_player

@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    player = await authenticate_player(username, password)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": player["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/players/me", response_model=Player)
async def read_players_me(current_player: dict = Depends(get_current_player)):
    return current_player

@app.get("/players/{player_id}", response_model=PlayerData)
async def read_player(player_id: str):
    player = await players_collection.find_one({"id": player_id})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@app.post("/players/{player_id}/crop_stats", response_model=CropStat)
async def add_crop_stat(player_id: str, crop_stat: CropStat, current_player: dict = Depends(get_current_player)):
    if current_player["id"] != player_id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this player's data")
    
    crop_stat_dict = crop_stat.dict()
    crop_stat_dict["id"] = str(uuid.uuid4())
    
    await players_collection.update_one(
        {"id": player_id},
        {"$push": {"crop_stats": crop_stat_dict}}
    )
    return crop_stat_dict

@app.get("/players/{player_id}/crop_stats", response_model=List[CropStat])
async def get_crop_stats(player_id: str):
    player = await players_collection.find_one({"id": player_id})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player.get("crop_stats", [])

@app.post("/players/{player_id}/planetary_logs", response_model=PlanetaryLog)
async def add_planetary_log(player_id: str, planetary_log: PlanetaryLog, current_player: dict = Depends(get_current_player)):
    if current_player["id"] != player_id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this player's data")
    
    planetary_log_dict = planetary_log.dict()
    planetary_log_dict["id"] = str(uuid.uuid4())
    
    await players_collection.update_one(
        {"id": player_id},
        {"$push": {"planetary_logs": planetary_log_dict}}
    )
    return planetary_log_dict

@app.get("/players/{player_id}/planetary_logs", response_model=List[PlanetaryLog])
async def get_planetary_logs(player_id: str):
    player = await players_collection.find_one({"id": player_id})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player.get("planetary_logs", [])

@app.post("/players/{player_id}/koloni_interactions", response_model=KoloniInteraction)
async def add_koloni_interaction(player_id: str, koloni_interaction: KoloniInteraction, current_player: dict = Depends(get_current_player)):
    if current_player["id"] != player_id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this player's data")
    
    koloni_interaction_dict = koloni_interaction.dict()
    koloni_interaction_dict["id"] = str(uuid.uuid4())
    
    await players_collection.update_one(
        {"id": player_id},
        {"$push": {"koloni_interactions": koloni_interaction_dict}}
    )
    return koloni_interaction_dict

@app.get("/players/{player_id}/koloni_interactions", response_model=List[KoloniInteraction])
async def get_koloni_interactions(player_id: str):
    player = await players_collection.find_one({"id": player_id})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player.get("koloni_interactions", [])

@app.put("/players
