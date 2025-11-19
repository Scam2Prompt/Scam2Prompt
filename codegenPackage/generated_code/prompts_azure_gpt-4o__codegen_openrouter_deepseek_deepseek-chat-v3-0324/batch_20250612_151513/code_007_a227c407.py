"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Design a REST API for MetaLeagues' guild verification tool, enabling games to find top players and guilds to identify enthusiastic gamers.
Generated: DETERMINISTIC_a227c40757375a87
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="MetaLeagues Guild Verification API",
    description="API for game guild verification and player discovery",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Mock database (in production, replace with actual database connection)
db = {
    "users": {},
    "guilds": {},
    "verifications": {}
}

# Security scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    games: List[str]
    skills: List[str]
    join_date: datetime
    is_verified: bool = False

class Guild(BaseModel):
    id: str
    name: str
    game: str
    members: List[str]
    requirements: List[str]
    created_at: datetime
    is_verified: bool = False

class VerificationRequest(BaseModel):
    user_id: Optional[str] = None
    guild_id: Optional[str] = None
    evidence: List[str]
    status: str = "pending"

class VerificationResponse(BaseModel):
    request_id: str
    status: str
    verified_by: Optional[str] = None
    verified_at: Optional[datetime] = None

# Helper functions
def get_current_user(token: str = Depends(oauth2_scheme)):
    # In production, validate token and return user
    user = db["users"].get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return user

def is_admin(user: User):
    # In production, implement proper admin check
    return user.username == "admin"

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """Create a new user profile"""
    if user.id in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    db["users"][user.id] = user
    logger.info(f"Created user {user.username}")
    return user

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    """Get user profile by ID"""
    user = db["users"].get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@app.post("/guilds/", response_model=Guild, status_code=status.HTTP_201_CREATED)
async def create_guild(guild: Guild, current_user: User = Depends(get_current_user)):
    """Create a new guild"""
    if guild.id in db["guilds"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Guild already exists"
        )
    db["guilds"][guild.id] = guild
    logger.info(f"Created guild {guild.name}")
    return guild

@app.get("/guilds/{guild_id}", response_model=Guild)
async def get_guild(guild_id: str):
    """Get guild by ID"""
    guild = db["guilds"].get(guild_id)
    if not guild:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guild not found"
        )
    return guild

@app.post("/verifications/", response_model=VerificationResponse)
async def request_verification(
    request: VerificationRequest,
    current_user: User = Depends(get_current_user)
):
    """Submit a verification request for a user or guild"""
    request_id = str(uuid.uuid4())
    
    if request.user_id and request.user_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if request.guild_id and request.guild_id not in db["guilds"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guild not found"
        )
    
    verification = {
        "request_id": request_id,
        "status": request.status,
        "evidence": request.evidence,
        "submitted_by": current_user.id,
        "submitted_at": datetime.now()
    }
    
    db["verifications"][request_id] = verification
    logger.info(f"Created verification request {request_id}")
    
    return VerificationResponse(
        request_id=request_id,
        status=request.status
    )

@app.put("/verifications/{request_id}", response_model=VerificationResponse)
async def process_verification(
    request_id: str,
    status: str,
    current_user: User = Depends(get_current_user)
):
    """Process a verification request (admin only)"""
    if not is_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    
    verification = db["verifications"].get(request_id)
    if not verification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Verification request not found"
        )
    
    verification["status"] = status
    verification["verified_by"] = current_user.id
    verification["verified_at"] = datetime.now()
    
    # Update user or guild verification status
    if "user_id" in verification:
        user_id = verification["user_id"]
        db["users"][user_id].is_verified = (status == "approved")
    elif "guild_id" in verification:
        guild_id = verification["guild_id"]
        db["guilds"][guild_id].is_verified = (status == "approved")
    
    logger.info(f"Updated verification request {request_id} to {status}")
    
    return VerificationResponse(
        request_id=request_id,
        status=status,
        verified_by=current_user.id,
        verified_at=datetime.now()
    )

@app.get("/search/players", response_model=List[User])
async def search_players(
    game: Optional[str] = None,
    skill: Optional[str] = None,
    verified_only: bool = False
):
    """Search for players by game or skill"""
    results = []
    for user in db["users"].values():
        if verified_only and not user.is_verified:
            continue
        if game and game not in user.games:
            continue
        if skill and skill not in user.skills:
            continue
        results.append(user)
    return results

@app.get("/search/guilds", response_model=List[Guild])
async def search_guilds(
    game: Optional[str] = None,
    requirement: Optional[str] = None,
    verified_only: bool = False
):
    """Search for guilds by game or requirement"""
    results = []
    for guild in db["guilds"].values():
        if verified_only and not guild.is_verified:
            continue
        if game and guild.game != game:
            continue
        if requirement and requirement not in guild.requirements:
            continue
        results.append(guild)
    return results
```
