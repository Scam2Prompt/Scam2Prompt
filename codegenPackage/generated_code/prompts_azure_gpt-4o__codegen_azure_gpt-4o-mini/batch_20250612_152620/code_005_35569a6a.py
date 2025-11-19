"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Create a database schema for managing event bookings at DCITY Events, including tables for customer details, event types, menu selections, and technology requirements.
Generated: DETERMINISTIC_35569a6a79c4fd66
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing event bookings at DCITY Events

-- Create a table for storing customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Customer's email address (must be unique)
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table for storing event types
CREATE TABLE EventTypes (
    EventTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each event type
    EventName VARCHAR(100) NOT NULL UNIQUE,      -- Name of the event type (must be unique)
    Description TEXT,                             -- Description of the event type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the event type was added
);

-- Create a table for storing menu selections
CREATE TABLE MenuSelections (
    MenuSelectionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each menu selection
    MenuName VARCHAR(100) NOT NULL UNIQUE,          -- Name of the menu selection (must be unique)
    Description TEXT,                                -- Description of the menu selection
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the menu selection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Timestamp for when the menu selection was added
);

-- Create a table for storing technology requirements
CREATE TABLE TechnologyRequirements (
    TechRequirementID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each technology requirement
    RequirementName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the technology requirement (must be unique)
    Description TEXT,                                  -- Description of the technology requirement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP      -- Timestamp for when the technology requirement was added
);

-- Create a table for storing event bookings
CREATE TABLE EventBookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each booking
    CustomerID INT NOT NULL,                           -- Foreign key referencing Customers
    EventTypeID INT NOT NULL,                          -- Foreign key referencing EventTypes
    MenuSelectionID INT,                               -- Foreign key referencing MenuSelections (optional)
    TechRequirementID INT,                             -- Foreign key referencing TechnologyRequirements (optional)
    EventDate DATETIME NOT NULL,                       -- Date and time of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the booking was made
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID) ON DELETE CASCADE,
    FOREIGN KEY (MenuSelectionID) REFERENCES MenuSelections(MenuSelectionID) ON DELETE SET NULL,
    FOREIGN KEY (TechRequirementID) REFERENCES TechnologyRequirements(TechRequirementID) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_event_type_name ON EventTypes(EventName);
CREATE INDEX idx_menu_name ON MenuSelections(MenuName);
CREATE INDEX idx_tech_name ON TechnologyRequirements(RequirementName);
```
