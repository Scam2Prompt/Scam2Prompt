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
-- Database schema for storing customer feedback and service requests

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record is created
);

-- Table to store customer feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    Comments TEXT NOT NULL,                    -- Feedback comments provided by the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating provided by the customer (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the feedback is submitted
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Ensures feedback is linked to a valid customer
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    ServiceType ENUM('Plumbing', 'Heating') NOT NULL, -- Type of service requested
    Description TEXT NOT NULL,                 -- Detailed description of the issue or request
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Current status of the service request
    RequestedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service request is submitted
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Ensures the service request is linked to a valid customer
);

-- Table to store service technician assignments
CREATE TABLE TechnicianAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each technician assignment
    RequestID INT NOT NULL,                      -- Foreign key referencing the ServiceRequests table
    TechnicianName VARCHAR(100) NOT NULL,       -- Name of the assigned technician
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the technician was assigned
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) -- Ensures assignment is linked to a valid service request
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers (Email); -- Index on email for faster lookups
CREATE INDEX idx_feedback_customer ON Feedback (CustomerID); -- Index on CustomerID in Feedback table
CREATE INDEX idx_service_request_customer ON ServiceRequests (CustomerID); -- Index on CustomerID in ServiceRequests table

-- View to get combined information about customers and their service requests
CREATE VIEW CustomerServiceRequests AS
SELECT
    c.CustomerID,
    CONCAT(c.FirstName, ' ', c.LastName) AS FullName,
    c.Email,
    sr.RequestID,
    sr.ServiceType,
    sr.Description,
    sr.Status,
    sr.RequestedAt
FROM
    Customers c
INNER JOIN
    ServiceRequests sr ON c.CustomerID = sr.CustomerID;
```
