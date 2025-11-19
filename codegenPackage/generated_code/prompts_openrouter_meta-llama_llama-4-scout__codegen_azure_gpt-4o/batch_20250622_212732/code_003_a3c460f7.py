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
-- Database schema for a boat charter company operating in the U.S. Virgin Islands

-- Table to store information about the fleet of boats
CREATE TABLE Fleet (
    BoatID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each boat
    BoatName VARCHAR(100) NOT NULL,        -- Name of the boat
    Capacity INT NOT NULL,                 -- Maximum number of passengers the boat can carry
    MakeModel VARCHAR(100),                -- Make and model of the boat
    YearBuilt YEAR,                        -- Year the boat was built
    Status ENUM('Available', 'Maintenance', 'Out of Service') DEFAULT 'Available', -- Current status of the boat
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store trip schedules
CREATE TABLE Trips (
    TripID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each trip
    BoatID INT NOT NULL,                       -- Foreign key referencing the Fleet table
    TripDate DATE NOT NULL,                    -- Date of the trip
    DepartureTime TIME NOT NULL,               -- Departure time of the trip
    ReturnTime TIME NOT NULL,                  -- Return time of the trip
    DepartureLocation VARCHAR(100) NOT NULL,   -- Departure location
    Destination VARCHAR(100) NOT NULL,         -- Destination of the trip
    Price DECIMAL(10, 2) NOT NULL,             -- Price per passenger for the trip
    MaxPassengers INT NOT NULL,                -- Maximum number of passengers for the trip
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Current status of the trip
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (BoatID) REFERENCES Fleet(BoatID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store bookings made by customers
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    TripID INT NOT NULL,                       -- Foreign key referencing the Trips table
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    NumberOfPassengers INT NOT NULL,           -- Number of passengers in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the booking
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was made
    Status ENUM('Confirmed', 'Cancelled') DEFAULT 'Confirmed', -- Current status of the booking
    FOREIGN KEY (TripID) REFERENCES Trips(TripID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_trip_date ON Trips (TripDate);
CREATE INDEX idx_customer_email ON Customers (Email);
CREATE INDEX idx_booking_trip_customer ON Bookings (TripID, CustomerID);
```
