"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Suggest a set of features and functionalities for a mobile app aimed at customers of boat charter services like Salty Daze Charters, including booking, payment, and real-time updates."
Generated: DETERMINISTIC_b9dba449328d8950
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mobile App Backend for Boat Charter Services
Features:
- User authentication and profiles
- Boat listing and search
- Booking system
- Payment processing
- Real-time updates
- Reviews and ratings
- Push notifications
"""

from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator
from fastapi import FastAPI, HTTPException, status, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import stripe
import pytz

app = FastAPI(
    title="Salty Daze Charters API",
    description="Backend for boat charter mobile app",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stripe configuration
stripe.api_key = "your_stripe_secret_key"

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models
class User(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    phone: Optional[str] = None
    hashed_password: str
    disabled: bool = False

class BoatType(str, Enum):
    sailboat = "sailboat"
    motorboat = "motorboat"
    yacht = "yacht"
    catamaran = "catamaran"

class Boat(BaseModel):
    id: str
    name: str
    type: BoatType
    capacity: int
    price_per_hour: float
    description: Optional[str] = None
    image_urls: List[str] = []
    is_available: bool = True

class BookingStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"

class Booking(BaseModel):
    id: str
    user_id: str
    boat_id: str
    start_time: datetime
    end_time: datetime
    status: BookingStatus = BookingStatus.pending
    total_price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    payment_intent_id: Optional[str] = None

    @validator('end_time')
    def validate_end_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError("End time must be after start time")
        return v

class PaymentIntent(BaseModel):
    id: str
    amount: int  # in cents
    currency: str = "usd"
    status: str
    client_secret: Optional[str] = None

class Review(BaseModel):
    id: str
    user_id: str
    boat_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

# In-memory database (replace with real DB in production)
fake_users_db = {}
fake_boats_db = {}
fake_bookings_db = {}
fake_reviews_db = {}

# Helper functions
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_users_db.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_boat(boat_id: str):
    boat = fake_boats_db.get(boat_id)
    if not boat:
        raise HTTPException(status_code=404, detail="Boat not found")
    return boat

async def get_booking(booking_id: str, user: User):
    booking = fake_bookings_db.get(booking_id)
    if not booking or booking.user_id != user.id:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

# API endpoints
@app.post("/users/", response_model=User)
async def create_user(user: User):
    if user.email in [u.email for u in fake_users_db.values()]:
        raise HTTPException(status_code=400, detail="Email already registered")
    fake_users_db[user.id] = user
    return user

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/boats/", response_model=List[Boat])
async def list_boats(
    type: Optional[BoatType] = None,
    min_capacity: Optional[int] = None,
    max_price: Optional[float] = None
):
    boats = list(fake_boats_db.values())
    if type:
        boats = [b for b in boats if b.type == type]
    if min_capacity:
        boats = [b for b in boats if b.capacity >= min_capacity]
    if max_price:
        boats = [b for b in boats if b.price_per_hour <= max_price]
    return boats

@app.get("/boats/{boat_id}", response_model=Boat)
async def get_boat_details(boat_id: str):
    return await get_boat(boat_id)

@app.post("/bookings/", response_model=Booking)
async def create_booking(
    boat_id: str,
    start_time: datetime,
    end_time: datetime,
    current_user: User = Depends(get_current_user)
):
    boat = await get_boat(boat_id)
    
    # Check availability
    for booking in fake_bookings_db.values():
        if booking.boat_id == boat_id and booking.status != BookingStatus.cancelled:
            if (start_time < booking.end_time) and (end_time > booking.start_time):
                raise HTTPException(
                    status_code=400,
                    detail="Boat is already booked for this time period"
                )
    
    # Calculate price
    duration_hours = (end_time - start_time).total_seconds() / 3600
    total_price = round(duration_hours * boat.price_per_hour, 2)
    
    # Create booking
    booking = Booking(
        id=f"book_{len(fake_bookings_db)+1}",
        user_id=current_user.id,
        boat_id=boat_id,
        start_time=start_time,
        end_time=end_time,
        total_price=total_price
    )
    
    fake_bookings_db[booking.id] = booking
    return booking

@app.post("/bookings/{booking_id}/pay", response_model=PaymentIntent)
async def create_payment_intent(
    booking_id: str,
    current_user: User = Depends(get_current_user)
):
    booking = await get_booking(booking_id, current_user)
    
    if booking.status != BookingStatus.pending:
        raise HTTPException(
            status_code=400,
            detail="Booking is not in pending state"
        )
    
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(booking.total_price * 100),  # convert to cents
            currency="usd",
            metadata={"booking_id": booking_id}
        )
        
        # Update booking with payment intent ID
        booking.payment_intent_id = payment_intent.id
        fake_bookings_db[booking.id] = booking
        
        return PaymentIntent(
            id=payment_intent.id,
            amount=payment_intent.amount,
            currency=payment_intent.currency,
            status=payment_intent.status,
            client_secret=payment_intent.client_secret
        )
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/bookings/{booking_id}/confirm")
async def confirm_booking(
    booking_id: str,
    current_user: User = Depends(get_current_user)
):
    booking = await get_booking(booking_id, current_user)
    
    if booking.payment_intent_id is None:
        raise HTTPException(
            status_code=400,
            detail="Payment not completed"
        )
    
    # Verify payment with Stripe
    try:
        payment_intent = stripe.PaymentIntent.retrieve(booking.payment_intent_id)
        if payment_intent.status != "succeeded":
            raise HTTPException(
                status_code=400,
                detail="Payment not succeeded"
            )
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Update booking status
    booking.status = BookingStatus.confirmed
    fake_bookings_db[booking.id] = booking
    
    return {"message": "Booking confirmed successfully"}

@app.get("/bookings/", response_model=List[Booking])
async def list_user_bookings(current_user: User = Depends(get_current_user)):
    return [b for b in fake_bookings_db.values() if b.user_id == current_user.id]

@app.post("/reviews/", response_model=Review)
async def create_review
