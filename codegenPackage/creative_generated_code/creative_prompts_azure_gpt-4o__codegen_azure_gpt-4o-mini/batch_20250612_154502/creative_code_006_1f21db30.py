"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.traveloagency.com
Prompt: Create a database schema for storing flight routes, airlines, and travel dates, similar to the popular routes listed on Traveloagency.
Generated: DETERMINISTIC_1f21db30badf919e
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing flight routes, airlines, and travel dates
CREATE DATABASE IF NOT EXISTS TravelAgencyDB;

USE TravelAgencyDB;

-- Table to store airline information
CREATE TABLE IF NOT EXISTS Airlines (
    airline_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each airline
    name VARCHAR(100) NOT NULL,                -- Name of the airline
    code VARCHAR(10) NOT NULL UNIQUE,          -- IATA code of the airline
    country VARCHAR(100) NOT NULL,             -- Country where the airline is based
    established_year YEAR NOT NULL,            -- Year the airline was established
    contact_number VARCHAR(15)                  -- Contact number for the airline
);

-- Table to store flight routes
CREATE TABLE IF NOT EXISTS FlightRoutes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each flight route
    airline_id INT NOT NULL,                    -- Foreign key referencing Airlines
    departure_city VARCHAR(100) NOT NULL,      -- City of departure
    arrival_city VARCHAR(100) NOT NULL,        -- City of arrival
    distance_km INT NOT NULL,                   -- Distance between the two cities in kilometers
    duration_hours INT NOT NULL,                 -- Duration of the flight in hours
    FOREIGN KEY (airline_id) REFERENCES Airlines(airline_id) ON DELETE CASCADE  -- Cascade deletes for related routes
);

-- Table to store travel dates
CREATE TABLE IF NOT EXISTS TravelDates (
    travel_date_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each travel date
    route_id INT NOT NULL,                          -- Foreign key referencing FlightRoutes
    travel_date DATE NOT NULL,                      -- Date of travel
    available_seats INT NOT NULL,                   -- Number of available seats on the flight
    price DECIMAL(10, 2) NOT NULL,                  -- Price of the flight
    FOREIGN KEY (route_id) REFERENCES FlightRoutes(route_id) ON DELETE CASCADE  -- Cascade deletes for related travel dates
);

-- Sample data insertion for Airlines
INSERT INTO Airlines (name, code, country, established_year, contact_number) VALUES
('Airline A', 'AA', 'USA', 1980, '123-456-7890'),
('Airline B', 'AB', 'UK', 1990, '098-765-4321');

-- Sample data insertion for FlightRoutes
INSERT INTO FlightRoutes (airline_id, departure_city, arrival_city, distance_km, duration_hours) VALUES
(1, 'New York', 'Los Angeles', 3940, 6),
(2, 'London', 'Tokyo', 9560, 12);

-- Sample data insertion for TravelDates
INSERT INTO TravelDates (route_id, travel_date, available_seats, price) VALUES
(1, '2024-05-01', 150, 500.00),
(2, '2024-06-01', 50, 1200.00);
```
