"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: Design a database schema for managing lot reservations and customer information for a real estate project, ensuring it includes fields for payment plans and contact details.
Generated: DETERMINISTIC_5e90bfd8531ccbea
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing lot reservations and customer information
-- This schema includes tables for customers, lots, reservations, and payment plans.

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store lot information
CREATE TABLE Lots (
    LotID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each lot
    LotNumber VARCHAR(20) NOT NULL UNIQUE,     -- Unique lot number
    Size DECIMAL(10, 2) NOT NULL,              -- Size of the lot (e.g., in square meters)
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the lot
    Status ENUM('Available', 'Reserved', 'Sold') DEFAULT 'Available', -- Current status of the lot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store reservation information
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    LotID INT NOT NULL,                           -- Foreign key referencing Lots table
    ReservationDate DATE NOT NULL,                -- Date of reservation
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Reservation status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (LotID) REFERENCES Lots(LotID) ON DELETE CASCADE
);

-- Table to store payment plan information
CREATE TABLE PaymentPlans (
    PaymentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment plan
    ReservationID INT NOT NULL,                   -- Foreign key referencing Reservations table
    TotalAmount DECIMAL(15, 2) NOT NULL,          -- Total amount to be paid
    Installments INT NOT NULL,                    -- Number of installments
    InstallmentAmount DECIMAL(15, 2) NOT NULL,    -- Amount per installment
    DueDate DATE NOT NULL,                        -- Due date for the next installment
    Status ENUM('Active', 'Completed', 'Defaulted') DEFAULT 'Active', -- Payment plan status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_lot_status ON Lots(Status);         -- Index for filtering lots by status
CREATE INDEX idx_reservation_status ON Reservations(Status); -- Index for filtering reservations by status
CREATE INDEX idx_paymentplan_status ON PaymentPlans(Status); -- Index for filtering payment plans by status
```
