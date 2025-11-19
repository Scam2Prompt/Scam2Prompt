"""
Generated Code Metadata:
========================
Original URL: https://merdeka-tower.com
Prompt: Create a SQL database schema to store information about the different components of Merdeka 118 Tower, such as the hotel, offices, mall, and observation decks.
Generated: DETERMINISTIC_9a44baf722441925
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for Merdeka 118 Tower components

-- Create the database
CREATE DATABASE Merdeka118;

-- Use the created database
USE Merdeka118;

-- Table to store information about the hotel
CREATE TABLE Hotel (
    hotel_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each hotel
    name VARCHAR(255) NOT NULL,                -- Name of the hotel
    number_of_rooms INT NOT NULL,              -- Total number of rooms in the hotel
    rating DECIMAL(2, 1) CHECK (rating BETWEEN 1.0 AND 5.0),  -- Hotel rating (1.0 to 5.0)
    amenities TEXT,                             -- Description of amenities offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about office spaces
CREATE TABLE Office (
    office_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each office space
    name VARCHAR(255) NOT NULL,                -- Name of the office space
    floor_number INT NOT NULL,                  -- Floor number where the office is located
    square_footage INT NOT NULL,                -- Size of the office in square feet
    amenities TEXT,                             -- Description of amenities offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about the mall
CREATE TABLE Mall (
    mall_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each mall
    name VARCHAR(255) NOT NULL,                 -- Name of the mall
    number_of_stores INT NOT NULL,              -- Total number of stores in the mall
    amenities TEXT,                             -- Description of amenities offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about observation decks
CREATE TABLE ObservationDeck (
    deck_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each observation deck
    name VARCHAR(255) NOT NULL,                 -- Name of the observation deck
    floor_number INT NOT NULL,                  -- Floor number where the deck is located
    capacity INT NOT NULL,                       -- Maximum capacity of the observation deck
    amenities TEXT,                             -- Description of amenities offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about the tower itself
CREATE TABLE Tower (
    tower_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the tower
    name VARCHAR(255) NOT NULL,                  -- Name of the tower
    height DECIMAL(10, 2) NOT NULL,              -- Height of the tower in meters
    total_floors INT NOT NULL,                   -- Total number of floors in the tower
    year_completed INT NOT NULL,                 -- Year the tower was completed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Optional: Add foreign key relationships if needed in the future
-- For example, if you want to link offices to the tower, you can add a tower_id column in the Office table.
```
