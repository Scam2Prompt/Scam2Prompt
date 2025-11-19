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

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Table to store customer inquiries
CREATE TABLE CustomerInquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    InquiryDetails TEXT NOT NULL,              -- Details of the customer's inquiry
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the inquiry was made
    Status ENUM('Pending', 'Resolved', 'Closed') DEFAULT 'Pending', -- Status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store dumpster rental services
CREATE TABLE DumpsterServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT NOT NULL,                 -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service record was created
);

-- Table to store service areas
CREATE TABLE ServiceAreas (
    AreaID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each service area
    AreaName VARCHAR(100) NOT NULL,            -- Name of the service area
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code of the service area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service area record was created
);

-- Table to store dumpster rental bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing the DumpsterServices table
    AreaID INT NOT NULL,                       -- Foreign key referencing the ServiceAreas table
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was made
    RentalStartDate DATE NOT NULL,             -- Start date of the rental
    RentalEndDate DATE NOT NULL,               -- End date of the rental
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES DumpsterServices(ServiceID) ON DELETE CASCADE,
    FOREIGN KEY (AreaID) REFERENCES ServiceAreas(AreaID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_service_area_zip ON ServiceAreas(ZipCode); -- Index for quick lookup by zip code
```
