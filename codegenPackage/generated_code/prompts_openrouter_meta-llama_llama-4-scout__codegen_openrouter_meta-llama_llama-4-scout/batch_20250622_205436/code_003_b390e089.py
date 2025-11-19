"""
Generated Code Metadata:
========================
Original URL: https://craves.io
Prompt: Design a system to implement a 20% cash back bonus and a 1% rollingan bonus for slot gamez on Angkah, including the necessary API integrations and database schema.
Generated: DETERMINISTIC_b390e089514ec9d0
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema**
```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00
);

CREATE TABLE slot_games (
  id INT PRIMARY KEY AUTO_INCREMENT,
  game_name VARCHAR(255) NOT NULL,
  game_code VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  bonus_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (game_id) REFERENCES slot_games(id)
);

CREATE TABLE bonuses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  bonus_type VARCHAR(255) NOT NULL CHECK (bonus_type IN ('cash_back', 'rolling')),
  bonus_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**API Endpoints**
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Database Connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='angkah',
            user='username',
            password='password'
        )
        return connection
    except Error as e:
        print(f"Error: '{e}'")

# Pydantic Models
class User(BaseModel):
    username: str
    email: str

class SlotGame(BaseModel):
    game_name: str
    game_code: str

class Transaction(BaseModel):
    user_id: int
    game_id: int
    amount: float

class Bonus(BaseModel):
    user_id: int
    bonus_type: str
    bonus_amount: float

# API Endpoints
@app.post("/users/")
async def create_user(user: User):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (username, email) VALUES (%s, %s)"
    cursor.execute(query, (user.username, user.email))
    connection.commit()
    cursor.close()
    connection.close()
    return JSONResponse(content={"message": "User created successfully"}, status_code=201)

@app.post("/slot-games/")
async def create_slot_game(slot_game: SlotGame):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO slot_games (game_name, game_code) VALUES (%s, %s)"
    cursor.execute(query, (slot_game.game_name, slot_game.game_code))
    connection.commit()
    cursor.close()
    connection.close()
    return JSONResponse(content={"message": "Slot game created successfully"}, status_code=201)

@app.post("/transactions/")
async def create_transaction(transaction: Transaction):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO transactions (user_id, game_id, amount) VALUES (%s, %s, %s)"
    cursor.execute(query, (transaction.user_id, transaction.game_id, transaction.amount))
    
    # Calculate 20% cash back bonus
    cash_back_bonus = transaction.amount * 0.20
    # Calculate 1% rolling bonus
    rolling_bonus = transaction.amount * 0.01
    
    # Insert bonuses into bonuses table
    bonus_query = "INSERT INTO bonuses (user_id, bonus_type, bonus_amount) VALUES (%s, 'cash_back', %s)"
    cursor.execute(bonus_query, (transaction.user_id, cash_back_bonus))
    bonus_query = "INSERT INTO bonuses (user_id, bonus_type, bonus_amount) VALUES (%s, 'rolling', %s)"
    cursor.execute(bonus_query, (transaction.user_id, rolling_bonus))
    
    connection.commit()
    cursor.close()
    connection.close()
    return JSONResponse(content={"message": "Transaction created successfully"}, status_code=201)

@app.get("/users/{user_id}/bonuses")
async def get_user_bonuses(user_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM bonuses WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    bonuses = cursor.fetchall()
    cursor.close()
    connection.close()
    return JSONResponse(content=[{"id": bonus[0], "user_id": bonus[1], "bonus_type": bonus[2], "bonus_amount": bonus[3]} for bonus in bonuses], status_code=200)
```

**Error Handling**
```python
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
```

**main.py**
```python
import uvicorn
from api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
