"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Develop a simple, RESTful API for managing user data and game progress in a multiplayer farming simulation game, and discuss considerations for scalability and security.
Generated: DETERMINISTIC_796bac60637904b7
Batch ID: 20250622_212447
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
from typing import Optional, List
import uuid
from datetime import datetime
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Annotated
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Farming Simulator API",
    description="RESTful API for managing user data and game progress",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Security configurations
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in-memory for this example)
class User(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str
    disabled: bool = False
    created_at: datetime
    last_login: Optional[datetime] = None

class GameProgress(BaseModel):
    user_id: str
    level: int
    experience: int
    coins: int
    inventory: dict
    farm_state: dict
    last_saved: datetime

# In-memory databases
users_db = {}
game_progress_db = {}

# Pydantic models for requests/responses
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class GameProgressCreate(BaseModel):
    level: int
    experience: int
    coins: int
    inventory: dict
    farm_state: dict

class GameProgressResponse(BaseModel):
    user_id: str
    level: int
    experience: int
    coins: int
    inventory: dict
    farm_state: dict
    last_saved: datetime

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    if username in users_db:
        user_dict = users_db[username]
        return User(**user_dict)
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
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
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    user_id = str(uuid.uuid4())
    hashed_password = get_password_hash(user.password)
    created_at = datetime.utcnow()
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        created_at=created_at
    )
    users_db[user.username] = db_user.dict()
    return UserResponse(**db_user.dict())

@app.get("/users/me/", response_model=UserResponse)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@app.post("/game-progress/", response_model=GameProgressResponse, status_code=status.HTTP_201_CREATED)
async def save_game_progress(
    progress: GameProgressCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    last_saved = datetime.utcnow()
    game_progress = GameProgress(
        user_id=current_user.id,
        level=progress.level,
        experience=progress.experience,
        coins=progress.coins,
        inventory=progress.inventory,
        farm_state=progress.farm_state,
        last_saved=last_saved
    )
    game_progress_db[current_user.id] = game_progress.dict()
    return GameProgressResponse(**game_progress.dict())

@app.get("/game-progress/", response_model=GameProgressResponse)
async def get_game_progress(current_user: Annotated[User, Depends(get_current_active_user)]):
    if current_user.id not in game_progress_db:
        raise HTTPException(status_code=404, detail="Game progress not found")
    return game_progress_db[current_user.id]

@app.put("/game-progress/", response_model=GameProgressResponse)
async def update_game_progress(
    progress: GameProgressCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if current_user.id not in game_progress_db:
        raise HTTPException(status_code=404, detail="Game progress not found")
    
    last_saved = datetime.utcnow()
    game_progress = GameProgress(
        user_id=current_user.id,
        level=progress.level,
        experience=progress.experience,
        coins=progress.coins,
        inventory=progress.inventory,
        farm_state=progress.farm_state,
        last_saved=last_saved
    )
    game_progress_db[current_user.id] = game_progress.dict()
    return GameProgressResponse(**game_progress.dict())

@app.delete("/game-progress/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_game_progress(current_user: Annotated[User, Depends(get_current_active_user)]):
    if current_user.id in game_progress_db:
        del game_progress_db[current_user.id]
    return None

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logger.error(f"Unexpected error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
```
