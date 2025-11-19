"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Design a database schema for a home services management system that tracks customer requests for services like air conditioning cleaning and water leakage detection, as offered by شركة انجاز.
Generated: DETERMINISTIC_64e59ad3c1dd6ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Home Services Management System

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Full name of the customer
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the customer
    PhoneNumber VARCHAR(15) NOT NULL,          -- Contact number of the customer
    Address TEXT NOT NULL,                     -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Table to store service types offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., Air Conditioning Cleaning)
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service record was created
);

-- Table to store customer service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service request
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    RequestDate DATE NOT NULL,                -- Date when the service was requested
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    Notes TEXT,                               -- Additional notes or instructions from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the service request was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE     -- Cascade delete if service is removed
);

-- Table to store service providers (e.g., technicians)
CREATE TABLE ServiceProviders (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service provider
    FullName VARCHAR(100) NOT NULL,            -- Full name of the service provider
    PhoneNumber VARCHAR(15) NOT NULL,          -- Contact number of the service provider
    Email VARCHAR(100) UNIQUE,                 -- Email address of the service provider
    Specialization VARCHAR(100),               -- Area of expertise (e.g., plumbing, air conditioning)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service provider record was created
);

-- Table to assign service providers to service requests
CREATE TABLE ProviderAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    RequestID INT NOT NULL,                      -- Foreign key referencing ServiceRequests table
    ProviderID INT NOT NULL,                     -- Foreign key referencing ServiceProviders table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the provider was assigned
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Cascade delete if service request is removed
    FOREIGN KEY (ProviderID) REFERENCES ServiceProviders(ProviderID) ON DELETE CASCADE -- Cascade delete if service provider is removed
);

-- Table to store payment information for service requests
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    RequestID INT NOT NULL,                   -- Foreign key referencing ServiceRequests table
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid by the customer
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment was made
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL, -- Payment method used
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Cascade delete if service request is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup of services by name
CREATE INDEX idx_request_status ON ServiceRequests(Status); -- Index for quick lookup of service requests by status
```
