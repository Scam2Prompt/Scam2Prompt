"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Create a database schema for managing car rental services, including categories like luxury cars, wedding cars, and trip vehicles, based on the offerings of Micro Rent a Car.
Generated: DETERMINISTIC_f448ae1321f8c406
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing car rental services

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS RentalCategories;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Rentals;

-- Table to store different categories of rental cars
CREATE TABLE RentalCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL,          -- Name of the car category (e.g., Luxury, Wedding, Trip)
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about cars available for rent
CREATE TABLE Cars (
    CarID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each car
    CategoryID INT NOT NULL,                     -- Foreign key referencing RentalCategories
    Make VARCHAR(50) NOT NULL,                   -- Manufacturer of the car
    Model VARCHAR(50) NOT NULL,                  -- Model of the car
    Year INT NOT NULL,                           -- Year of manufacture
    LicensePlate VARCHAR(20) NOT NULL UNIQUE,    -- Unique license plate number
    DailyRate DECIMAL(10, 2) NOT NULL,          -- Daily rental rate
    Availability BOOLEAN DEFAULT TRUE,           -- Availability status of the car
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the car was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES RentalCategories(CategoryID) -- Foreign key constraint
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,              -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Customer's email address
    Phone VARCHAR(15),                            -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store rental transactions
CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each rental transaction
    CarID INT NOT NULL,                           -- Foreign key referencing Cars
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    RentalStartDate DATETIME NOT NULL,           -- Start date and time of the rental
    RentalEndDate DATETIME NOT NULL,             -- End date and time of the rental
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rental was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CarID) REFERENCES Cars(CarID),  -- Foreign key constraint
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Foreign key constraint
);

-- Sample data insertion for RentalCategories
INSERT INTO RentalCategories (CategoryName, Description) VALUES
('Luxury Cars', 'High-end luxury vehicles for premium experiences.'),
('Wedding Cars', 'Special vehicles for wedding ceremonies.'),
('Trip Vehicles', 'Cars suitable for long trips and vacations.');

-- Sample data insertion for Cars
INSERT INTO Cars (CategoryID, Make, Model, Year, LicensePlate, DailyRate) VALUES
(1, 'Mercedes-Benz', 'S-Class', 2022, 'ABC123', 200.00),
(2, 'Rolls-Royce', 'Phantom', 2021, 'XYZ789', 500.00),
(3, 'Toyota', 'Camry', 2020, 'LMN456', 50.00);

-- Sample data insertion for Customers
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

-- Sample data insertion for Rentals
INSERT INTO Rentals (CarID, CustomerID, RentalStartDate, RentalEndDate, TotalAmount) VALUES
(1, 1, '2023-10-01 10:00:00', '2023-10-05 10:00:00', 1000.00),
(2, 2, '2023-10-10 12:00:00', '2023-10-12 12:00:00', 1000.00);
```
