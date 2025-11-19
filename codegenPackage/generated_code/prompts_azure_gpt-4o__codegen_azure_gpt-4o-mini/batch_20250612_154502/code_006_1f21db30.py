"""
Generated Code Metadata:
========================
Original URL: https://www.traveloagency.com
Prompt: Create a database schema for storing flight routes, airlines, and travel dates, similar to the popular routes listed on Traveloagency.
Generated: DETERMINISTIC_1f21db30badf919e
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing flight routes, airlines, and travel dates

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS FlightRoutes;
DROP TABLE IF EXISTS Airlines;
DROP TABLE IF EXISTS TravelDates;

-- Table to store airline information
CREATE TABLE Airlines (
    airline_id SERIAL PRIMARY KEY, -- Unique identifier for each airline
    name VARCHAR(100) NOT NULL, -- Name of the airline
    code VARCHAR(10) UNIQUE NOT NULL, -- IATA code for the airline
    country VARCHAR(100) NOT NULL, -- Country where the airline is based
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store flight routes
CREATE TABLE FlightRoutes (
    route_id SERIAL PRIMARY KEY, -- Unique identifier for each flight route
    airline_id INT NOT NULL, -- Foreign key referencing Airlines table
    origin VARCHAR(100) NOT NULL, -- Departure airport code
    destination VARCHAR(100) NOT NULL, -- Arrival airport code
    distance INT NOT NULL, -- Distance of the flight in kilometers
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (airline_id) REFERENCES Airlines(airline_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store travel dates for each flight route
CREATE TABLE TravelDates (
    travel_date_id SERIAL PRIMARY KEY, -- Unique identifier for each travel date
    route_id INT NOT NULL, -- Foreign key referencing FlightRoutes table
    travel_date DATE NOT NULL, -- Date of travel
    available_seats INT NOT NULL, -- Number of available seats on the flight
    price DECIMAL(10, 2) NOT NULL, -- Price of the flight
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (route_id) REFERENCES FlightRoutes(route_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_airline_code ON Airlines(code);
CREATE INDEX idx_route_origin_destination ON FlightRoutes(origin, destination);
CREATE INDEX idx_travel_date_route ON TravelDates(route_id);
```
