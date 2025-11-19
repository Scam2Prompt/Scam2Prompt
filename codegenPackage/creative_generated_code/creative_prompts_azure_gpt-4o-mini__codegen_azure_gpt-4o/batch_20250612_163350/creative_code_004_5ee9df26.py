"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Design a database schema for managing dumpster rental services, including fields for customer inquiries and service areas, based on the structure used by Junk in The Box ATL.
Generated: DETERMINISTIC_5ee9df261a42344c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Dumpster Rental Services

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the customer
    FirstName VARCHAR(50) NOT NULL,             -- First name of the customer
    LastName VARCHAR(50) NOT NULL,              -- Last name of the customer
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Contact email of the customer
    PhoneNumber VARCHAR(15),                    -- Contact phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer record was created
);

-- Table: CustomerInquiries
-- Stores inquiries made by customers about dumpster rental services
CREATE TABLE CustomerInquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the inquiry
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    InquiryDetails TEXT NOT NULL,               -- Description of the customer's inquiry
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the inquiry
    Status ENUM('Open', 'In Progress', 'Closed') DEFAULT 'Open', -- Inquiry status tracker
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table: ServiceAreas
-- Stores information about areas covered for dumpster rental services
CREATE TABLE ServiceAreas (
    AreaID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the service area
    AreaName VARCHAR(100) NOT NULL,             -- Name of the service area (e.g., city, neighborhood)
    ZipCode VARCHAR(10),                        -- Zip Code for the service area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service area record was created
);

-- Table: DumpsterRentals
-- Stores information about dumpster rentals
CREATE TABLE DumpsterRentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the dumpster rental
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    AreaID INT NOT NULL,                        -- Foreign key referencing ServiceAreas table
    DumpsterType ENUM('Small', 'Medium', 'Large') NOT NULL, -- Type of dumpster rented
    StartDate DATE NOT NULL,                    -- Start date of the rental
    EndDate DATE NOT NULL,                      -- End date of the rental
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost for the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the rental record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (AreaID) REFERENCES ServiceAreas(AreaID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_area_zipcode ON ServiceAreas(ZipCode);
CREATE INDEX idx_rental_dates ON DumpsterRentals(StartDate, EndDate);

-- Error handling for transactional operations should be implemented in application code
-- Backups and security policies are recommended for production environments
```
