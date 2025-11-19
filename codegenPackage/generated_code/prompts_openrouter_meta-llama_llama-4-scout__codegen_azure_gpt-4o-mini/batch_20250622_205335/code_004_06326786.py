"""
Generated Code Metadata:
========================
Original URL: https://graylinegeneva.com
Prompt: Create a sample database schema for storing information about Gray Line Geneva's tours, including details such as tour name, location, duration, and price.
Generated: DETERMINISTIC_06326786a8574502
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Gray Line Geneva's tours

-- Create a table to store tour information
CREATE TABLE Tours (
    TourID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour
    TourName VARCHAR(255) NOT NULL,         -- Name of the tour
    Location VARCHAR(255) NOT NULL,         -- Location where the tour takes place
    Duration INT NOT NULL,                   -- Duration of the tour in minutes
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the tour in the local currency
    Description TEXT,                        -- Optional description of the tour
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the tour was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create an index on the TourName for faster search queries
CREATE INDEX idx_tour_name ON Tours (TourName);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,            -- Customer's first name
    LastName VARCHAR(100) NOT NULL,             -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Customer's email address
    Phone VARCHAR(20),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the customer was created
);

-- Create a table to store bookings for tours
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each booking
    TourID INT NOT NULL,                        -- Foreign key referencing Tours
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the booking
    NumberOfParticipants INT NOT NULL,         -- Number of participants in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    FOREIGN KEY (TourID) REFERENCES Tours(TourID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the BookingDate for faster queries
CREATE INDEX idx_booking_date ON Bookings (BookingDate);
```
