"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Design a database schema for storing customer feedback and service requests related to plumbing and heating services in a web application.
Generated: DETERMINISTIC_2993ab04fa6e9f0e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer feedback and service requests
-- related to plumbing and heating services.

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    ServiceType ENUM('Plumbing', 'Heating') NOT NULL, -- Type of service requested
    Description TEXT NOT NULL,                 -- Detailed description of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the request
    RequestedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store customer feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    RequestID INT,                             -- Foreign key referencing the ServiceRequests table (optional)
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Customer rating (1 to 5)
    Comments TEXT,                             -- Additional comments provided by the customer
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the feedback was submitted
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE SET NULL -- Set to NULL if service request is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_service_status ON ServiceRequests(Status); -- Index for filtering by request status
CREATE INDEX idx_feedback_rating ON Feedback(Rating); -- Index for filtering by rating
```
