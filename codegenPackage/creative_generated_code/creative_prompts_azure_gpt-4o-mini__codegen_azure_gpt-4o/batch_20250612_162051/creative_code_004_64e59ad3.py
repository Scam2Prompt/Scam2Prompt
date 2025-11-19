"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Design a database schema for a home services management system that tracks customer requests for services like air conditioning cleaning and water leakage detection, as offered by شركة انجاز.
Generated: DETERMINISTIC_64e59ad3c1dd6ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Home Services Management System
-- Tracks customer requests and services offered by شركة انجاز

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the customer
    FullName VARCHAR(255) NOT NULL,            -- Full name of the customer
    Email VARCHAR(255) NOT NULL,               -- Email address of the customer
    PhoneNumber VARCHAR(15) NOT NULL,          -- Phone number of the customer
    Address TEXT NOT NULL,                     -- Physical address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service categories offered by شركة انجاز
CREATE TABLE ServiceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the service category
    CategoryName VARCHAR(255) NOT NULL UNIQUE, -- Name of the service category (e.g., Air Conditioning Cleaning)
    Description TEXT,                          -- Description of the service category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store detailed services under each category
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the service
    CategoryID INT NOT NULL,                      -- Foreign key linking to the service category
    ServiceName VARCHAR(255) NOT NULL,            -- Name of the specific service (e.g., AC Filter Cleaning)
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the service
    Description TEXT,                             -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CategoryID) REFERENCES ServiceCategories(CategoryID) ON DELETE CASCADE
);

-- Table to track customer service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the service request
    CustomerID INT NOT NULL,                      -- Foreign key linking to the customer
    ServiceID INT NOT NULL,                       -- Foreign key linking to the service
    RequestStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    RequestedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the service request
    CompletionDate TIMESTAMP NULL,                -- Date and time when the request was completed
    Notes TEXT,                                   -- Additional notes for the request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Indexes for improving query performance
CREATE INDEX idx_customer_email ON Customers (Email); -- Index on customer email for quick lookup
CREATE INDEX idx_service_category ON Services (CategoryID); -- Index on service category for quick lookup
CREATE INDEX idx_request_status ON ServiceRequests (RequestStatus); -- Index on request status for filtering requests

-- Error handling is performed at the application level to ensure transactional consistency.
-- Ensure proper validation is implemented when inserting/updating data to maintain data integrity.
```
