"""
Generated Code Metadata:
========================
Original URL: https://bienbonvoyage.com
Prompt: Design a basic database schema for a travel agency specializing in luxury adventures.
Generated: DETERMINISTIC_e2702cc6f564ff37
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a travel agency specializing in luxury adventures

-- Create a table for storing information about destinations
CREATE TABLE Destinations (
    DestinationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each destination
    Name VARCHAR(100) NOT NULL,                     -- Name of the destination
    Description TEXT,                               -- Description of the destination
    Country VARCHAR(100) NOT NULL,                  -- Country where the destination is located
    Region VARCHAR(100),                             -- Region within the country
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Create a table for storing information about luxury adventures
CREATE TABLE Adventures (
    AdventureID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each adventure
    Name VARCHAR(100) NOT NULL,                     -- Name of the adventure
    Description TEXT,                               -- Description of the adventure
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the adventure
    Duration INT NOT NULL,                           -- Duration of the adventure in days
    DestinationID INT,                              -- Foreign key referencing Destinations
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for last update
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,                 -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                   -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,              -- Customer's email address (must be unique)
    Phone VARCHAR(15),                               -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Create a table for storing bookings made by customers
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each booking
    CustomerID INT,                                  -- Foreign key referencing Customers
    AdventureID INT,                                 -- Foreign key referencing Adventures
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the booking was made
    NumberOfGuests INT NOT NULL,                     -- Number of guests for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,             -- Total price for the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (AdventureID) REFERENCES Adventures(AdventureID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for storing customer reviews for adventures
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each review
    CustomerID INT,                                  -- Foreign key referencing Customers
    AdventureID INT,                                 -- Foreign key referencing Adventures
    Rating INT CHECK (Rating BETWEEN 1 AND 5),       -- Rating given by the customer (1 to 5)
    Comment TEXT,                                    -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (AdventureID) REFERENCES Adventures(AdventureID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
