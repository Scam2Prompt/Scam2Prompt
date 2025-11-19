"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Design a database schema for managing customer inquiries and service requests for a cleaning company, inspired by the contact methods used by Star Cleaning Services.
Generated: DETERMINISTIC_5211ce42a09ac979
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing customer inquiries and service requests for a cleaning company

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store inquiries made by customers
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    InquiryType ENUM('General', 'Pricing', 'Service', 'Other') NOT NULL, -- Type of inquiry
    Message TEXT NOT NULL,                     -- Detailed message from the customer
    Status ENUM('Pending', 'Resolved', 'Closed') DEFAULT 'Pending', -- Status of the inquiry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inquiry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store service requests made by customers
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    ServiceType ENUM('Residential', 'Commercial', 'Deep Cleaning', 'Move-Out Cleaning') NOT NULL, -- Type of cleaning service requested
    ScheduledDate DATE NOT NULL,               -- Date when the service is scheduled
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the service request
    Notes TEXT,                                -- Additional notes or instructions from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store communication logs between the company and customers
CREATE TABLE CommunicationLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each communication log
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    CommunicationMethod ENUM('Email', 'Phone', 'SMS', 'In-Person') NOT NULL, -- Method of communication
    Message TEXT NOT NULL,                     -- Content of the communication
    CommunicatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the communication occurred
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_inquiry_status ON Inquiries(Status); -- Index for filtering inquiries by status
CREATE INDEX idx_request_status ON ServiceRequests(Status); -- Index for filtering service requests by status
CREATE INDEX idx_communication_method ON CommunicationLogs(CommunicationMethod); -- Index for filtering communication logs by method
```
