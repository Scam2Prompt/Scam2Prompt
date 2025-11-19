"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proarteasa.com
Prompt: Design a database schema for managing lot reservations and customer information for a real estate project, ensuring it includes fields for payment plans and contact details.
Generated: DETERMINISTIC_5e90bfd8531ccbea
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing lot reservations and customer information
-- This schema includes tables for customers, lot reservations, and payment plans.

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                  -- Customer's phone number
    Address VARCHAR(255),                     -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Table: Lots
CREATE TABLE Lots (
    LotID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the lot
    LotNumber VARCHAR(50) NOT NULL UNIQUE,    -- Lot number (must be unique)
    Location VARCHAR(100) NOT NULL,           -- Location description for the lot
    Size FLOAT NOT NULL,                      -- Size of the lot (e.g., in square feet or acres)
    Price DECIMAL(15, 2) NOT NULL,            -- Price of the lot
    IsAvailable BOOLEAN DEFAULT TRUE,         -- Availability status of the lot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the lot record was created
);

-- Table: Reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the reservation
    CustomerID INT NOT NULL,                      -- Foreign key linking to the Customers table
    LotID INT NOT NULL,                           -- Foreign key linking to the Lots table
    ReservationDate DATE NOT NULL,                -- Date when the reservation was made
    Status ENUM('Pending', 'Confirmed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the reservation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (LotID) REFERENCES Lots(LotID) ON DELETE CASCADE, -- Ensures data integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the reservation record was created
);

-- Table: PaymentPlans
CREATE TABLE PaymentPlans (
    PaymentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the payment plan
    ReservationID INT NOT NULL,                   -- Foreign key linking to the Reservations table
    TotalAmount DECIMAL(15, 2) NOT NULL,          -- Total payment amount
    MonthlyInstallment DECIMAL(15, 2) NOT NULL,   -- Monthly installment amount
    InstallmentsCount INT NOT NULL,               -- Number of installments planned
    StartDate DATE NOT NULL,                      -- Payment plan start date
    EndDate DATE NOT NULL,                        -- Payment plan end date
    Status ENUM('Active', 'Completed', 'Defaulted') NOT NULL DEFAULT 'Active', -- Payment plan status
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE, -- Ensures data integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the payment plan record was created
);

-- Indexes for improving query performance
CREATE INDEX idx_customer_email ON Customers (Email);
CREATE INDEX idx_lot_availability ON Lots (IsAvailable);
CREATE INDEX idx_reservation_status ON Reservations (Status);
```

This schema adheres to best practices, including normalization, proper use of foreign keys, and explicit constraints.
