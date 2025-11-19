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
CREATE DATABASE RealEstateProject;

USE RealEstateProject;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store lot information
CREATE TABLE Lots (
    LotID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each lot
    LotNumber VARCHAR(20) NOT NULL UNIQUE,     -- Unique lot number
    Size DECIMAL(10, 2) NOT NULL,              -- Size of the lot in square meters
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the lot
    Status ENUM('Available', 'Reserved', 'Sold') DEFAULT 'Available', -- Current status of the lot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the lot was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store payment plans for each lot reservation
CREATE TABLE PaymentPlans (
    PaymentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment plan
    LotID INT NOT NULL,                           -- Foreign key referencing the Lots table
    CustomerID INT NOT NULL,                      -- Foreign key referencing the Customers table
    TotalAmount DECIMAL(15, 2) NOT NULL,         -- Total amount for the payment plan
    DownPayment DECIMAL(15, 2) NOT NULL,         -- Down payment amount
    MonthlyInstallment DECIMAL(15, 2) NOT NULL,  -- Monthly installment amount
    DurationMonths INT NOT NULL,                  -- Duration of the payment plan in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the payment plan was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (LotID) REFERENCES Lots(LotID) ON DELETE CASCADE, -- Ensure lot integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure customer integrity
);

-- Table to store reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    LotID INT NOT NULL,                           -- Foreign key referencing the Lots table
    CustomerID INT NOT NULL,                      -- Foreign key referencing the Customers table
    ReservationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of reservation
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the reservation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the reservation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (LotID) REFERENCES Lots(LotID) ON DELETE CASCADE, -- Ensure lot integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure customer integrity
);
```
