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
-- Database Schema for Managing Dumpster Rental Services

-- Table for Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's full name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    Phone VARCHAR(15) NOT NULL,                -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

-- Table for Service Areas
CREATE TABLE ServiceAreas (
    AreaID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service area
    AreaName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the service area (e.g., city or neighborhood)
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code for the service area
    Region VARCHAR(100) NOT NULL                -- Region or state for additional categorization
);

-- Table for Dumpster Rentals
CREATE TABLE DumpsterRentals (
    RentalID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each rental
    CustomerID INT NOT NULL,                    -- Foreign key reference to Customers table
    AreaID INT NOT NULL,                        -- Foreign key reference to ServiceAreas table
    RentalDate DATE NOT NULL,                   -- Date when the rental was made
    ReturnDate DATE,                           -- Date when the dumpster will be returned
    Status ENUM('Pending', 'Active', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the rental
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AreaID) REFERENCES ServiceAreas(AreaID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for Customer Inquiries
CREATE TABLE CustomerInquiries (
    InquiryID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                     -- Foreign key reference to Customers table
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the inquiry was made
    InquiryType ENUM('Question', 'Quote Request', 'Feedback') NOT NULL, -- Type of inquiry
    InquiryDetails TEXT NOT NULL,                -- Details about the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);
```
