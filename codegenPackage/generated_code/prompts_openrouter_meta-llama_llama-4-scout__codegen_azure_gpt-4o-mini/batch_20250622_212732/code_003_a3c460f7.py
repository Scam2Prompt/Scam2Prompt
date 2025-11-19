"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Design a database schema to store information about boat charters, including trip schedules, customer details, and fleet information for a company operating in the U.S. Virgin Islands."
Generated: DETERMINISTIC_a3c460f7b5a72afc
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a boat charter company in the U.S. Virgin Islands

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL, -- Customer's first name
    LastName VARCHAR(50) NOT NULL, -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL, -- Customer's email address
    Phone VARCHAR(15), -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store fleet information
CREATE TABLE Boats (
    BoatID SERIAL PRIMARY KEY, -- Unique identifier for each boat
    Name VARCHAR(100) NOT NULL, -- Name of the boat
    Type VARCHAR(50) NOT NULL, -- Type of the boat (e.g., sailboat, motorboat)
    Capacity INT NOT NULL, -- Maximum number of passengers
    Status VARCHAR(20) DEFAULT 'Available', -- Current status of the boat (e.g., Available, In Maintenance)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store trip schedules
CREATE TABLE Trips (
    TripID SERIAL PRIMARY KEY, -- Unique identifier for each trip
    BoatID INT NOT NULL, -- Foreign key referencing the Boats table
    CustomerID INT NOT NULL, -- Foreign key referencing the Customers table
    TripDate DATE NOT NULL, -- Date of the trip
    StartTime TIME NOT NULL, -- Start time of the trip
    EndTime TIME NOT NULL, -- End time of the trip
    Destination VARCHAR(100) NOT NULL, -- Destination of the trip
    Price DECIMAL(10, 2) NOT NULL, -- Price of the trip
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (BoatID) REFERENCES Boats(BoatID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store payment information
CREATE TABLE Payments (
    PaymentID SERIAL PRIMARY KEY, -- Unique identifier for each payment
    TripID INT NOT NULL, -- Foreign key referencing the Trips table
    Amount DECIMAL(10, 2) NOT NULL, -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of payment
    PaymentMethod VARCHAR(50) NOT NULL, -- Method of payment (e.g., Credit Card, PayPal)
    FOREIGN KEY (TripID) REFERENCES Trips(TripID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_boat_name ON Boats(Name);
CREATE INDEX idx_trip_date ON Trips(TripDate);
```
