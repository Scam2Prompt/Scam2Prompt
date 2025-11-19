"""
Generated Code Metadata:
========================
Original URL: https://tetherfi.us
Prompt: Develop a simple and secure login system for remote agents using biometrics and Edge-AI vision models, as described in Tetherfi's Secure Work From Home solution.
Generated: DETERMINISTIC_e2fedd449a28c36f
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import json
import time
from typing import Optional, Dict, Any
import cv2
import numpy as np
import onnxruntime
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Biometric model paths
FACE_MODEL_PATH = "models/face_recognition.onnx"
LIVENESS_MODEL_PATH = "models/liveness_detection.onnx"

# Initialize FastAPI
app = FastAPI(title="Tetherfi Secure WFH Login System")

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    biometric_hash: Optional[str] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class BiometricLoginRequest(BaseModel):
    image_data: str  # Base64 encoded image
    username: str

# Mock database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("secret"),
        "biometric_hash": hashlib.sha256(b"john_face_embeddings").hexdigest(),
        "disabled": False,
    }
}

# Load ONNX models
def load_onnx_model(model_path: str):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return onnxruntime.InferenceSession(model_path)

face_model = load_onnx_model(FACE_MODEL_PATH)
liveness_model = load_onnx_model(LIVENESS_MODEL_PATH)

# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str) -> Optional[UserInDB]:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str) -> Optional[UserInDB]:
    user = get_user(fake_db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def preprocess_image(image_data: str) -> np.ndarray:
    # Decode base64 image
    nparr = np.frombuffer(image_data.encode(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Preprocess for face recognition
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (112, 112))
    img = img.transpose(2, 0, 1)
    img = np.expand_dims(img, axis=0).astype(np.float32)
    img /= 255.0
    return img

def extract_face_embeddings(image: np.ndarray) -> np.ndarray:
    input_name = face_model.get_inputs()[0].name
    output_name = face_model.get_outputs()[0].name
    embeddings = face_model.run([output_name], {input_name: image})[0]
    return embeddings

def check_liveness(image: np.ndarray) -> bool:
    input_name = liveness_model.get_inputs()[0].name
    output_name = liveness_model.get_outputs()[0].name
    pred = liveness_model.run([output_name], {input_name: image})[0]
    return pred[0][0] > 0.5  # Assuming binary classification

def verify_biometric(username: str, image_data: str) -> bool:
    try:
        # Preprocess image
        img = preprocess_image(image_data)
        
        # Check liveness
        if not check_liveness(img):
            return False
        
        # Extract embeddings
        embeddings = extract_face_embeddings(img)
        current_hash = hashlib.sha256(embeddings.tobytes()).hexdigest()
        
        # Compare with stored hash
        user = get_user(fake_users_db, username)
        if not user:
            return False
            
        return current_hash == user.biometric_hash
    except Exception as e:
        print(f"Biometric verification error: {e}")
        return False

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
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

@app.post("/biometric-login", response_model=Token)
async def biometric_login(request: BiometricLoginRequest):
    if not verify_biometric(request.username, request.image_data):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Biometric verification failed",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = get_user(fake_users_db, request.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
