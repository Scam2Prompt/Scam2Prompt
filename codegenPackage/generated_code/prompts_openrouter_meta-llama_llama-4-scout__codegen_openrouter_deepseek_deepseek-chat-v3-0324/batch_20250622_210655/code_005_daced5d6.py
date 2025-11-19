"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Design an API for integrating agricultural data from various sources, including mobile apps and web platforms, for analytics and reporting, like Azagros.
Generated: DETERMINISTIC_daced5d6dc712740
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agricultural_data_api.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Agricultural Data Integration API",
    description="API for integrating agricultural data from various sources",
    version="1.0.0"
)

# Security configurations
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# MongoDB configurations
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "agri_data_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Field(BaseModel):
    name: str
    location: str
    area: float
    crop_type: str
    soil_type: Optional[str] = None

class SensorData(BaseModel):
    field_id: str
    sensor_type: str
    value: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    unit: str

class WeatherData(BaseModel):
    field_id: str
    temperature: float
    humidity: float
    precipitation: float
    wind_speed: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class CropYield(BaseModel):
    field_id: str
    crop_type: str
    yield_amount: float
    unit: str
    harvest_date: datetime

class ReportRequest(BaseModel):
    start_date: datetime
    end_date: datetime
    field_ids: List[str]
    report_type: str

# Utility functions
async def get_user(username: str):
    user = await db.users.find_one({"username": username})
    if user:
        return UserInDB(**user)

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
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
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/fields/", response_model=Field)
async def create_field(field: Field, current_user: User = Depends(get_current_active_user)):
    try:
        field_dict = field.dict()
        result = await db.fields.insert_one(field_dict)
        field_dict["_id"] = str(result.inserted_id)
        return field_dict
    except Exception as e:
        logger.error(f"Error creating field: {e}")
        raise HTTPException(status_code=500, detail="Error creating field")

@app.get("/fields/", response_model=List[Field])
async def get_fields(current_user: User = Depends(get_current_active_user)):
    try:
        fields = []
        async for field in db.fields.find():
            field["_id"] = str(field["_id"])
            fields.append(field)
        return fields
    except Exception as e:
        logger.error(f"Error fetching fields: {e}")
        raise HTTPException(status_code=500, detail="Error fetching fields")

@app.post("/sensor-data/", response_model=SensorData)
async def add_sensor_data(data: SensorData, current_user: User = Depends(get_current_active_user)):
    try:
        data_dict = data.dict()
        result = await db.sensor_data.insert_one(data_dict)
        data_dict["_id"] = str(result.inserted_id)
        return data_dict
    except Exception as e:
        logger.error(f"Error adding sensor data: {e}")
        raise HTTPException(status_code=500, detail="Error adding sensor data")

@app.get("/sensor-data/{field_id}", response_model=List[SensorData])
async def get_sensor_data(field_id: str, current_user: User = Depends(get_current_active_user)):
    try:
        sensor_data = []
        async for data in db.sensor_data.find({"field_id": field_id}):
            data["_id"] = str(data["_id"])
            sensor_data.append(data)
        return sensor_data
    except Exception as e:
        logger.error(f"Error fetching sensor data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching sensor data")

@app.post("/weather-data/", response_model=WeatherData)
async def add_weather_data(data: WeatherData, current_user: User = Depends(get_current_active_user)):
    try:
        data_dict = data.dict()
        result = await db.weather_data.insert_one(data_dict)
        data_dict["_id"] = str(result.inserted_id)
        return data_dict
    except Exception as e:
        logger.error(f"Error adding weather data: {e}")
        raise HTTPException(status_code=500, detail="Error adding weather data")

@app.post("/crop-yields/", response_model=CropYield)
async def add_crop_yield(yield_data: CropYield, current_user: User = Depends(get_current_active_user)):
    try:
        yield_dict = yield_data.dict()
        result = await db.crop_yields.insert_one(yield_dict)
        yield_dict["_id"] = str(result.inserted_id)
        return yield_dict
    except Exception as e:
        logger.error(f"Error adding crop yield: {e}")
        raise HTTPException(status_code=500, detail="Error adding crop yield")

@app.post("/generate-report/")
async def generate_report(report_request: ReportRequest, current_user: User = Depends(get_current_active_user)):
    try:
        # Placeholder for report generation logic
        # In production, this would query the database and generate reports
        return {
            "status": "success",
            "message": "Report generation initiated",
            "report_id": str(ObjectId())
        }
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        raise HTTPException(status_code=500, detail="Error generating report")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Event handlers
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = client
    app.mongodb = db

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
```
