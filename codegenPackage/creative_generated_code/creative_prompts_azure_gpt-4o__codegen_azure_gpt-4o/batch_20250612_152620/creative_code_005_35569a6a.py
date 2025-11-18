"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Create a database schema for managing event bookings at DCITY Events, including tables for customer details, event types, menu selections, and technology requirements.
Generated: DETERMINISTIC_35569a6a79c4fd66
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- DCITY Events Database Schema for Managing Event Bookings

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique ID for each customer
    FirstName VARCHAR(50) NOT NULL,            -- First name of the customer
    LastName VARCHAR(50) NOT NULL,             -- Last name of the customer
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address (must be unique)
    Phone VARCHAR(15) NOT NULL,                -- Contact number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table: EventTypes
CREATE TABLE EventTypes (
    EventTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique ID for each event type
    Name VARCHAR(100) NOT NULL,                 -- Name of the event type (e.g., Wedding, Corporate Meeting)
    Description TEXT,                           -- Description of the event type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table: MenuSelections
CREATE TABLE MenuSelections (
    MenuID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique ID for each menu option
    Name VARCHAR(100) NOT NULL,                 -- Name of the menu option (e.g., Vegan, Buffet)
    Description TEXT,                           -- Description of the menu option
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the menu option
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table: TechnologyRequirements
CREATE TABLE TechnologyRequirements (
    TechID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique ID for each technology requirement
    Name VARCHAR(100) NOT NULL,                 -- Name of the technology requirement (e.g., Projector, WiFi)
    Description TEXT,                           -- Description of the technology requirement
    Price DECIMAL(10, 2) NOT NULL,              -- Price for using this technology
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table: Bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique ID for each booking
    CustomerID INT NOT NULL,                    -- Foreign key: ID of the customer
    EventTypeID INT NOT NULL,                   -- Foreign key: ID of the event type
    MenuID INT,                                 -- Foreign key: ID of the menu selection
    TechID INT,                                 -- Foreign key: ID of the technology requirement
    EventDate DATE NOT NULL,                    -- Date of the event
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the booking
    Notes TEXT,                                 -- Additional notes for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID),
    FOREIGN KEY (MenuID) REFERENCES MenuSelections(MenuID),
    FOREIGN KEY (TechID) REFERENCES TechnologyRequirements(TechID)
);

-- Indexes for optimized query performance
CREATE INDEX idx_eventDate ON Bookings(EventDate); -- Index for event date in bookings
```
