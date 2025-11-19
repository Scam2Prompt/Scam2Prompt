"""
Generated Code Metadata:
========================
Original URL: https://www.lecarolee.it
Prompt: Create a sample database schema for an agriturismo management system, including tables for products, accommodations, and customer information, inspired by the Le Carolee website.
Generated: DETERMINISTIC_738c19faf4e396d2
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Agriturismo Management System Database Schema

-- Table: Products
-- Stores information about products offered by the agriturismo (e.g., olive oil, wine, etc.)
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Accommodations
-- Stores information about accommodations available at the agriturismo
CREATE TABLE Accommodations (
    AccommodationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accommodation
    Name VARCHAR(255) NOT NULL,                     -- Name of the accommodation (e.g., "Room 1")
    Description TEXT,                               -- Detailed description of the accommodation
    Capacity INT NOT NULL,                          -- Maximum number of guests
    PricePerNight DECIMAL(10, 2) NOT NULL,          -- Price per night for the accommodation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the accommodation was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- Customer's first name
    LastName VARCHAR(255) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Reservations
-- Stores information about reservations made by customers
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    AccommodationID INT NOT NULL,                 -- Foreign key referencing Accommodations table
    CheckInDate DATE NOT NULL,                    -- Check-in date for the reservation
    CheckOutDate DATE NOT NULL,                   -- Check-out date for the reservation
    TotalPrice DECIMAL(10, 2) NOT NULL,           -- Total price for the reservation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (AccommodationID) REFERENCES Accommodations(AccommodationID) ON DELETE CASCADE -- Cascade delete if accommodation is removed
);

-- Table: Orders
-- Stores information about product orders made by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key referencing Customers table
    ProductID INT NOT NULL,                 -- Foreign key referencing Products table
    Quantity INT NOT NULL,                  -- Quantity of the product ordered
    TotalPrice DECIMAL(10, 2) NOT NULL,     -- Total price for the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_reservation_dates ON Reservations(CheckInDate, CheckOutDate); -- Index for quick lookup of reservations by date range
CREATE INDEX idx_product_name ON Products(Name); -- Index for quick lookup of products by name
```
