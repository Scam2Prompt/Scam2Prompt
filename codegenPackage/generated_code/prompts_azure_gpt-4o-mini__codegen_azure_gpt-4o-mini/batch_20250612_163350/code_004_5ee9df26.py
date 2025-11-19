"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Design a database schema for managing dumpster rental services, including fields for customer inquiries and service areas, based on the structure used by Junk in The Box ATL.
Generated: DETERMINISTIC_5ee9df261a42344c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing dumpster rental services

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address
    Phone VARCHAR(15),                        -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

-- Create a table for service areas
CREATE TABLE ServiceAreas (
    AreaID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service area
    AreaName VARCHAR(100) NOT NULL,           -- Name of the service area
    ZipCode VARCHAR(10) NOT NULL,             -- Zip code for the service area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service area was created
);

-- Create a table for dumpster rentals
CREATE TABLE DumpsterRentals (
    RentalID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each rental
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers
    AreaID INT NOT NULL,                       -- Foreign key referencing ServiceAreas
    RentalStartDate DATE NOT NULL,             -- Start date of the rental
    RentalEndDate DATE NOT NULL,               -- End date of the rental
    DumpsterSize VARCHAR(20) NOT NULL,         -- Size of the dumpster (e.g., 10 yard, 20 yard)
    RentalPrice DECIMAL(10, 2) NOT NULL,      -- Price for the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rental was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (AreaID) REFERENCES ServiceAreas(AreaID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for customer inquiries
CREATE TABLE CustomerInquiries (
    InquiryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the inquiry
    InquiryMessage TEXT NOT NULL,               -- Message from the customer
    Status ENUM('Pending', 'Resolved', 'Closed') DEFAULT 'Pending', -- Status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for payment records
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each payment
    RentalID INT NOT NULL,                      -- Foreign key referencing DumpsterRentals
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the payment
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'Check') NOT NULL, -- Method of payment
    FOREIGN KEY (RentalID) REFERENCES DumpsterRentals(RentalID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_area_zip ON ServiceAreas(ZipCode);
CREATE INDEX idx_rental_customer ON DumpsterRentals(CustomerID);
CREATE INDEX idx_inquiry_customer ON CustomerInquiries(CustomerID);
CREATE INDEX idx_payment_rental ON Payments(RentalID);
```
