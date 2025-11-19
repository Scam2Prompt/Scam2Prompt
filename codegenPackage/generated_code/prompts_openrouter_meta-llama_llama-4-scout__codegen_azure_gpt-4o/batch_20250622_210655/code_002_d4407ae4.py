"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Generate a SQL database schema to store information about sports cars, including make, model, year, and condition, inspired by Galopin Automobile's vehicle listings.
Generated: DETERMINISTIC_d4407ae4b46bf64e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing information about sports cars
-- Inspired by Galopin Automobile's vehicle listings

-- Create a database named 'SportsCarsDB'
CREATE DATABASE IF NOT EXISTS SportsCarsDB;

-- Use the newly created database
USE SportsCarsDB;

-- Create a table to store sports car information
CREATE TABLE IF NOT EXISTS SportsCars (
    CarID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each car
    Make VARCHAR(50) NOT NULL,            -- Manufacturer of the car (e.g., Ferrari, Porsche)
    Model VARCHAR(50) NOT NULL,           -- Model of the car (e.g., 911 Turbo, F8 Tributo)
    Year YEAR NOT NULL,                   -- Year the car was manufactured
    Condition ENUM('New', 'Used', 'Certified Pre-Owned') NOT NULL, -- Condition of the car
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Add an index to optimize queries on Make and Model
CREATE INDEX idx_make_model ON SportsCars (Make, Model);

-- Add an index to optimize queries on Year
CREATE INDEX idx_year ON SportsCars (Year);

-- Example of inserting data into the SportsCars table
-- INSERT INTO SportsCars (Make, Model, Year, Condition)
-- VALUES ('Ferrari', 'F8 Tributo', 2022, 'New');
```
