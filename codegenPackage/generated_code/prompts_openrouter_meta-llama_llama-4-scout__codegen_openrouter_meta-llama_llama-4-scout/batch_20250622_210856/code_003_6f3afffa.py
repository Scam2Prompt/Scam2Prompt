"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Design a data schema for storing information about MG car models, including their engine specifications, dimensions, and features, and suggest a suitable database management system.
Generated: DETERMINISTIC_6f3afffa3066c511
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema: MG Car Models**
=====================================

**Database Management System:** PostgreSQL

```sql
-- Create database
CREATE DATABASE mg_car_models;

-- Connect to database
\c mg_car_models

-- Create table for car models
CREATE TABLE car_models (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(255) NOT NULL,
    model_year INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for engine specifications
CREATE TABLE engine_specifications (
    id SERIAL PRIMARY KEY,
    car_model_id INTEGER NOT NULL,
    engine_type VARCHAR(255) NOT NULL,
    engine_size DECIMAL(4, 2) NOT NULL,
    horsepower INTEGER NOT NULL,
    torque DECIMAL(6, 2) NOT NULL,
    transmission_type VARCHAR(255) NOT NULL,
    FOREIGN KEY (car_model_id) REFERENCES car_models(id)
);

-- Create table for dimensions
CREATE TABLE dimensions (
    id SERIAL PRIMARY KEY,
    car_model_id INTEGER NOT NULL,
    length DECIMAL(6, 2) NOT NULL,
    width DECIMAL(6, 2) NOT NULL,
    height DECIMAL(6, 2) NOT NULL,
    wheelbase DECIMAL(6, 2) NOT NULL,
    curb_weight DECIMAL(6, 2) NOT NULL,
    FOREIGN KEY (car_model_id) REFERENCES car_models(id)
);

-- Create table for features
CREATE TABLE features (
    id SERIAL PRIMARY KEY,
    car_model_id INTEGER NOT NULL,
    feature_name VARCHAR(255) NOT NULL,
    feature_description TEXT,
    FOREIGN KEY (car_model_id) REFERENCES car_models(id)
);

-- Create index on car_model_id for efficient joins
CREATE INDEX idx_engine_specifications_car_model_id ON engine_specifications(car_model_id);
CREATE INDEX idx_dimensions_car_model_id ON dimensions(car_model_id);
CREATE INDEX idx_features_car_model_id ON features(car_model_id);

-- Example data
INSERT INTO car_models (model_name, model_year)
VALUES ('MG ZS', 2022),
       ('MG HS', 2021),
       ('MG 5', 2020);

INSERT INTO engine_specifications (car_model_id, engine_type, engine_size, horsepower, torque, transmission_type)
VALUES (1, 'Gasoline', 1.50, 120, 150.00, 'Manual'),
       (2, 'Gasoline', 2.00, 160, 230.00, 'Automatic'),
       (3, 'Gasoline', 1.25, 100, 120.00, 'Manual');

INSERT INTO dimensions (car_model_id, length, width, height, wheelbase, curb_weight)
VALUES (1, 431.00, 180.00, 164.00, 260.00, 1300.00),
       (2, 457.00, 187.00, 168.00, 272.00, 1500.00),
       (3, 436.00, 176.00, 148.00, 253.00, 1100.00);

INSERT INTO features (car_model_id, feature_name, feature_description)
VALUES (1, 'Bluetooth Connectivity', 'Connects to your phone for music and calls'),
       (1, 'Rearview Camera', 'Displays rearview image on infotainment screen'),
       (2, 'GPS Navigation', 'Provides turn-by-turn directions'),
       (3, 'LED Headlights', 'Energy-efficient LED headlights for improved visibility');
```

**Python Code for Interacting with Database**
-------------------------------------------

```python
import psycopg2
from psycopg2 import Error

class MgCarModelsDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from database")

    def get_car_model(self, car_model_id):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT * FROM car_models
                JOIN engine_specifications ON car_models.id = engine_specifications.car_model_id
                JOIN dimensions ON car_models.id = dimensions.car_model_id
                WHERE car_models.id = %s
            """
            cursor.execute(query, (car_model_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error retrieving car model: {e}")

    def create_car_model(self, model_name, model_year, engine_type, engine_size, horsepower, torque, transmission_type, length, width, height, wheelbase, curb_weight):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO car_models (model_name, model_year) VALUES (%s, %s) RETURNING id", (model_name, model_year))
            car_model_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO engine_specifications (car_model_id, engine_type, engine_size, horsepower, torque, transmission_type) VALUES (%s, %s, %s, %s, %s, %s)", (car_model_id, engine_type, engine_size, horsepower, torque, transmission_type))
            cursor.execute("INSERT INTO dimensions (car_model_id, length, width, height, wheelbase, curb_weight) VALUES (%s, %s, %s, %s, %s, %s)", (car_model_id, length, width, height, wheelbase, curb_weight))
            self.connection.commit()
            return car_model_id
        except Error as e:
            print(f"Error creating car model: {e}")

# Example usage
database = MgCarModelsDatabase('localhost', 'mg_car_models', 'username', 'password')
database.connect()
car_model_id = database.create_car_model('MG 6', 2023, 'Gasoline', 1.50, 120, 150.00, 'Manual', 450.00, 182.00, 147.00, 265.00, 1350.00)
print(database.get_car_model(car_model_id))
database.disconnect()
```
