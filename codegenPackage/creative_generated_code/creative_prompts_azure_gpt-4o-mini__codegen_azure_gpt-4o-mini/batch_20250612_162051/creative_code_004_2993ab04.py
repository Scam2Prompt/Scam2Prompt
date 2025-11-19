"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flammedeauinc.ca
Prompt: Design a database schema for storing customer feedback and service requests related to plumbing and heating services in a web application.
Generated: DETERMINISTIC_2993ab04fa6e9f0e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Customer Feedback and Service Requests

-- Create Customers table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL, -- Customer's first name
    LastName VARCHAR(50) NOT NULL,  -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE, -- Customer's email (must be unique)
    Phone VARCHAR(15), -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the record was created
);

-- Create Services table to store plumbing and heating service types
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL, -- Name of the service
    Description TEXT, -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the record was created
);

-- Create Feedback table to store customer feedback
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each feedback entry
    CustomerID INT NOT NULL, -- Foreign key to associate feedback with a customer
    ServiceID INT NOT NULL, -- Foreign key to associate feedback with a service
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    Comments TEXT, -- Additional comments provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feedback was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure feedback is deleted if customer is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure feedback is deleted if service is removed
);

-- Create ServiceRequests table to track service requests by customers
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service request
    CustomerID INT NOT NULL, -- Foreign key to associate the request with a customer
    ServiceID INT NOT NULL, -- Foreign key to associate the request with a service
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the request was made
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure request is deleted if customer is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure request is deleted if service is removed
);
```
