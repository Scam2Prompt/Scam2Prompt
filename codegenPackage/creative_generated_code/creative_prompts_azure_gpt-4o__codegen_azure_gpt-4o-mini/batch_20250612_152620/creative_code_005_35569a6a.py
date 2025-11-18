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
-- Database schema for managing event bookings at DCITY Events

-- Drop existing tables to avoid conflicts during development
DROP TABLE IF EXISTS TechnologyRequirements;
DROP TABLE IF EXISTS MenuSelections;
DROP TABLE IF EXISTS EventTypes;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Bookings;

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,         -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,       -- Customer's first name
    LastName VARCHAR(50) NOT NULL,        -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Customer's email address
    Phone VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to store different event types
CREATE TABLE EventTypes (
    EventTypeID SERIAL PRIMARY KEY,        -- Unique identifier for each event type
    EventTypeName VARCHAR(100) NOT NULL,   -- Name of the event type (e.g., wedding, corporate, etc.)
    Description TEXT,                      -- Description of the event type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the event type was added
);

-- Table to store menu selections for events
CREATE TABLE MenuSelections (
    MenuSelectionID SERIAL PRIMARY KEY,     -- Unique identifier for each menu selection
    MenuName VARCHAR(100) NOT NULL,        -- Name of the menu selection
    Description TEXT,                       -- Description of the menu selection
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the menu selection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the menu selection was added
);

-- Table to store technology requirements for events
CREATE TABLE TechnologyRequirements (
    TechnologyID SERIAL PRIMARY KEY,        -- Unique identifier for each technology requirement
    RequirementName VARCHAR(100) NOT NULL, -- Name of the technology requirement (e.g., projector, sound system)
    Description TEXT,                       -- Description of the technology requirement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the technology requirement was added
);

-- Table to manage bookings
CREATE TABLE Bookings (
    BookingID SERIAL PRIMARY KEY,           -- Unique identifier for each booking
    CustomerID INT NOT NULL,                -- Foreign key referencing Customers
    EventTypeID INT NOT NULL,               -- Foreign key referencing EventTypes
    MenuSelectionID INT NOT NULL,           -- Foreign key referencing MenuSelections
    TechnologyID INT,                       -- Foreign key referencing TechnologyRequirements
    EventDate DATE NOT NULL,                -- Date when the event is scheduled
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- On delete cascade for customer
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID) ON DELETE CASCADE, -- On delete cascade for event type
    FOREIGN KEY (MenuSelectionID) REFERENCES MenuSelections(MenuSelectionID) ON DELETE CASCADE, -- On delete cascade for menu selection
    FOREIGN KEY (TechnologyID) REFERENCES TechnologyRequirements(TechnologyID) ON DELETE SET NULL -- Set to null on delete for technology requirements
);

-- Indexes can be added here for optimization if necessary
```
