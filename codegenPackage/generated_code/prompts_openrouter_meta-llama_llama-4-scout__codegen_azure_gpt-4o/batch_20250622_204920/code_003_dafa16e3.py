"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Create a SQL database schema to store information about armourer services, uniform hire, and prop rentals for a film production company in NSW.
Generated: DETERMINISTIC_dafa16e33226c500
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing information about armourer services, uniform hire, and prop rentals
-- This schema is designed for a film production company in NSW

-- Create a table to store information about armourer services
CREATE TABLE ArmourerServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Availability BOOLEAN DEFAULT TRUE,        -- Whether the service is currently available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about uniform hire
CREATE TABLE UniformHire (
    UniformID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each uniform
    UniformName VARCHAR(255) NOT NULL,        -- Name of the uniform
    Size VARCHAR(50),                         -- Size of the uniform
    QuantityAvailable INT NOT NULL,           -- Number of uniforms available for hire
    DailyRate DECIMAL(10, 2) NOT NULL,        -- Daily hire rate for the uniform
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about prop rentals
CREATE TABLE PropRentals (
    PropID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each prop
    PropName VARCHAR(255) NOT NULL,           -- Name of the prop
    Description TEXT,                         -- Detailed description of the prop
    QuantityAvailable INT NOT NULL,           -- Number of props available for rental
    DailyRate DECIMAL(10, 2) NOT NULL,        -- Daily rental rate for the prop
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- First name of the customer
    LastName VARCHAR(255) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the customer
    PhoneNumber VARCHAR(20),                   -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store bookings for armourer services
CREATE TABLE ArmourerBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    CustomerID INT NOT NULL,                  -- Reference to the customer making the booking
    ServiceID INT NOT NULL,                   -- Reference to the armourer service being booked
    BookingDate DATE NOT NULL,                -- Date of the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES ArmourerServices(ServiceID) ON DELETE CASCADE
);

-- Create a table to store uniform hire transactions
CREATE TABLE UniformHireTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    CustomerID INT NOT NULL,                      -- Reference to the customer making the hire
    UniformID INT NOT NULL,                       -- Reference to the uniform being hired
    HireStartDate DATE NOT NULL,                  -- Start date of the hire
    HireEndDate DATE NOT NULL,                    -- End date of the hire
    TotalPrice DECIMAL(10, 2) NOT NULL,           -- Total price for the hire
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (UniformID) REFERENCES UniformHire(UniformID) ON DELETE CASCADE
);

-- Create a table to store prop rental transactions
CREATE TABLE PropRentalTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    CustomerID INT NOT NULL,                      -- Reference to the customer making the rental
    PropID INT NOT NULL,                          -- Reference to the prop being rented
    RentalStartDate DATE NOT NULL,                -- Start date of the rental
    RentalEndDate DATE NOT NULL,                  -- End date of the rental
    TotalPrice DECIMAL(10, 2) NOT NULL,           -- Total price for the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PropID) REFERENCES PropRentals(PropID) ON DELETE CASCADE
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_armourer_service_name ON ArmourerServices(ServiceName);
CREATE INDEX idx_uniform_name ON UniformHire(UniformName);
CREATE INDEX idx_prop_name ON PropRentals(PropName);
```
