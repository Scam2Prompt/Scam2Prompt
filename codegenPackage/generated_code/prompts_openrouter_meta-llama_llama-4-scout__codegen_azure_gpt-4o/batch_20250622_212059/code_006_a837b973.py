"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Design a database schema to store information about Hajj and Umrah pilgrims, their travel plans, and services provided by companies like Kidana Al Hejaz.
Generated: DETERMINISTIC_a837b9734d316782
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Hajj and Umrah Pilgrims, Travel Plans, and Services

-- Table to store information about pilgrims
CREATE TABLE Pilgrims (
    PilgrimID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pilgrim
    FirstName VARCHAR(100) NOT NULL,          -- First name of the pilgrim
    LastName VARCHAR(100) NOT NULL,           -- Last name of the pilgrim
    Gender ENUM('Male', 'Female') NOT NULL,   -- Gender of the pilgrim
    DateOfBirth DATE NOT NULL,                -- Date of birth of the pilgrim
    Nationality VARCHAR(100) NOT NULL,        -- Nationality of the pilgrim
    PassportNumber VARCHAR(50) UNIQUE NOT NULL, -- Passport number of the pilgrim
    ContactNumber VARCHAR(15),                -- Contact number of the pilgrim
    Email VARCHAR(100),                       -- Email address of the pilgrim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store travel plans for pilgrims
CREATE TABLE TravelPlans (
    TravelPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each travel plan
    PilgrimID INT NOT NULL,                      -- Foreign key referencing Pilgrims table
    DepartureDate DATE NOT NULL,                 -- Departure date for the travel plan
    ArrivalDate DATE NOT NULL,                   -- Arrival date for the travel plan
    DepartureCity VARCHAR(100) NOT NULL,         -- City of departure
    ArrivalCity VARCHAR(100) NOT NULL,           -- City of arrival
    TransportationMode ENUM('Air', 'Bus', 'Train') NOT NULL, -- Mode of transportation
    AccommodationDetails TEXT,                  -- Details about accommodation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PilgrimID) REFERENCES Pilgrims(PilgrimID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store services provided by companies
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service bookings for pilgrims
CREATE TABLE ServiceBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    PilgrimID INT NOT NULL,                   -- Foreign key referencing Pilgrims table
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    FOREIGN KEY (PilgrimID) REFERENCES Pilgrims(PilgrimID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store companies providing services
CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each company
    CompanyName VARCHAR(100) NOT NULL,        -- Name of the company
    ContactNumber VARCHAR(15),                -- Contact number of the company
    Email VARCHAR(100),                       -- Email address of the company
    Address TEXT,                             -- Address of the company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate services with companies
CREATE TABLE CompanyServices (
    CompanyServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each company-service association
    CompanyID INT NOT NULL,                          -- Foreign key referencing Companies table
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services table
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);
```
