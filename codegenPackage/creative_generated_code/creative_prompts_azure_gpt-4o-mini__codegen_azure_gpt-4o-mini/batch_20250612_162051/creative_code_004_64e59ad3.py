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

-- Create a database for the home services management system
CREATE DATABASE HomeServicesManagement;

-- Use the created database
USE HomeServicesManagement;

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Name of the customer
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,   -- Unique phone number of the customer
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address of the customer
    Address VARCHAR(255),                       -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer was added
);

-- Table to store different types of services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the service (e.g., "Air Conditioning Cleaning")
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service was added
);

-- Table to store customer requests for services
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service request
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services table
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the service was requested
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), -- Foreign key constraint
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)    -- Foreign key constraint
);

-- Table to store feedback from customers regarding the services
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each feedback
    RequestID INT NOT NULL,                       -- Foreign key referencing ServiceRequests table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    Comments TEXT,                                -- Additional comments or feedback from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the feedback was submitted
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) -- Foreign key constraint
);

-- Indexes for performance improvement
CREATE INDEX idx_customer_phone ON Customers(PhoneNumber);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_request_customer ON ServiceRequests(CustomerID);
CREATE INDEX idx_feedback_request ON Feedback(RequestID);
```
