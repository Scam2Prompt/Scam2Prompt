"""
Generated Code Metadata:
========================
Original URL: https://myflightdiscount.com
Prompt: Write code to implement a search feature for travel deals, allowing users to find flights, hotels, and rentals by entering keywords like "Switzerland" or "Edinburgh."
Generated: DETERMINISTIC_6f4edbebf971aa8e
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI()

# Database setup
def init_db():
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            origin TEXT NOT NULL,
            destination TEXT NOT NULL,
            airline TEXT NOT NULL,
            price REAL NOT NULL,
            departure_date TEXT NOT NULL,
            return_date TEXT,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            price_per_night REAL NOT NULL,
            check_in_date TEXT NOT NULL,
            check_out_date TEXT,
            amenities TEXT,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rentals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            location TEXT NOT NULL,
            price_per_day REAL NOT NULL,
            available_from TEXT NOT NULL,
            available_to TEXT,
            features TEXT,
            description TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Models
class Flight(BaseModel):
    origin: str
    destination: str
    airline: str
    price: float
    departure_date: str
    return_date: Optional[str] = None
    description: Optional[str] = None

class Hotel(BaseModel):
    name: str
    location: str
    price_per_night: float
    check_in_date: str
    check_out_date: Optional[str] = None
    amenities: Optional[str] = None
    description: Optional[str] = None

class Rental(BaseModel):
    type: str
    location: str
    price_per_day: float
    available_from: str
    available_to: Optional[str] = None
    features: Optional[str] = None
    description: Optional[str] = None

class SearchResult(BaseModel):
    flights: List[Flight]
    hotels: List[Hotel]
    rentals: List[Rental]

# Helper functions
def search_flights(keyword: str) -> List[Dict]:
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    query = '''
        SELECT * FROM flights 
        WHERE origin LIKE ? OR destination LIKE ? OR description LIKE ?
    '''
    cursor.execute(query, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    
    flights = []
    for row in results:
        flights.append({
            'id': row[0],
            'origin': row[1],
            'destination': row[2],
            'airline': row[3],
            'price': row[4],
            'departure_date': row[5],
            'return_date': row[6],
            'description': row[7]
        })
    
    conn.close()
    return flights

def search_hotels(keyword: str) -> List[Dict]:
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    query = '''
        SELECT * FROM hotels 
        WHERE name LIKE ? OR location LIKE ? OR description LIKE ?
    '''
    cursor.execute(query, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    
    hotels = []
    for row in results:
        hotels.append({
            'id': row[0],
            'name': row[1],
            'location': row[2],
            'price_per_night': row[3],
            'check_in_date': row[4],
            'check_out_date': row[5],
            'amenities': row[6],
            'description': row[7]
        })
    
    conn.close()
    return hotels

def search_rentals(keyword: str) -> List[Dict]:
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    query = '''
        SELECT * FROM rentals 
        WHERE type LIKE ? OR location LIKE ? OR description LIKE ?
    '''
    cursor.execute(query, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    
    rentals = []
    for row in results:
        rentals.append({
            'id': row[0],
            'type': row[1],
            'location': row[2],
            'price_per_day': row[3],
            'available_from': row[4],
            'available_to': row[5],
            'features': row[6],
            'description': row[7]
        })
    
    conn.close()
    return rentals

# API Endpoints
@app.post("/flights/", response_model=Flight)
def create_flight(flight: Flight):
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO flights (origin, destination, airline, price, departure_date, return_date, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        flight.origin,
        flight.destination,
        flight.airline,
        flight.price,
        flight.departure_date,
        flight.return_date,
        flight.description
    ))
    
    conn.commit()
    flight_id = cursor.lastrowid
    conn.close()
    
    return {**flight.dict(), "id": flight_id}

@app.post("/hotels/", response_model=Hotel)
def create_hotel(hotel: Hotel):
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO hotels (name, location, price_per_night, check_in_date, check_out_date, amenities, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        hotel.name,
        hotel.location,
        hotel.price_per_night,
        hotel.check_in_date,
        hotel.check_out_date,
        hotel.amenities,
        hotel.description
    ))
    
    conn.commit()
    hotel_id = cursor.lastrowid
    conn.close()
    
    return {**hotel.dict(), "id": hotel_id}

@app.post("/rentals/", response_model=Rental)
def create_rental(rental: Rental):
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO rentals (type, location, price_per_day, available_from, available_to, features, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        rental.type,
        rental.location,
        rental.price_per_day,
        rental.available_from,
        rental.available_to,
        rental.features,
        rental.description
    ))
    
    conn.commit()
    rental_id = cursor.lastrowid
    conn.close()
    
    return {**rental.dict(), "id": rental_id}

@app.get("/search/", response_model=SearchResult)
def search_travel_deals(keyword: str):
    if not keyword or len(keyword.strip()) == 0:
        raise HTTPException(status_code=400, detail="Search keyword cannot be empty")
    
    try:
        flights = search_flights(keyword)
        hotels = search_hotels(keyword)
        rentals = search_rentals(keyword)
        
        return {
            "flights": flights,
            "hotels": hotels,
            "rentals": rentals
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Sample data insertion (for testing)
def insert_sample_data():
    conn = sqlite3.connect('travel_deals.db')
    cursor = conn.cursor()
    
    # Insert sample flights
    cursor.execute('''
        INSERT INTO flights (origin, destination, airline, price, departure_date, return_date, description)
        VALUES 
            ('London', 'Edinburgh', 'British Airways', 120.50, '2023-12-15', '2023-12-20', 'Direct flight to Edinburgh'),
            ('New York', 'Zurich', 'Swiss Air', 450.00, '2023-12-10', '2023-12-25', 'Flight to Switzerland with one stop'),
            ('Paris', 'Geneva', 'Air France', 210.75, '2023-11-30', '2023-12-07', 'Direct flight to Switzerland')
    ''')
    
    # Insert sample hotels
    cursor.execute('''
        INSERT INTO hotels (name, location, price_per_night, check_in_date, check_out_date, amenities, description)
        VALUES 
            ('Grand Hotel Zurich', 'Zurich, Switzerland', 250.00, '2023-12-10', '2023-12-25', 'Pool, Spa, WiFi', 'Luxury hotel in
