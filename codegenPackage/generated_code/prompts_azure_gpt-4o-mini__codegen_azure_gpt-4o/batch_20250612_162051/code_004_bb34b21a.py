"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Design a database schema using SQL for storing customer reviews and service requests for a roofing company, focusing on fields like customer name, service type, and satisfaction rating.
Generated: DETERMINISTIC_bb34b21a6b88fed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing customer reviews and service requests for a roofing company

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's full name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    ServiceType VARCHAR(50) NOT NULL,          -- Type of service requested (e.g., roof repair, installation)
    RequestDate DATE NOT NULL,                 -- Date of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    Notes TEXT,                                -- Additional notes about the service request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service request was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store customer reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    ServiceRequestID INT NOT NULL,             -- Foreign key linking to the ServiceRequests table
    SatisfactionRating INT CHECK (SatisfactionRating BETWEEN 1 AND 5), -- Satisfaction rating (1-5 scale)
    Comments TEXT,                             -- Customer's comments about the service
    ReviewDate DATE NOT NULL,                  -- Date the review was submitted
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (ServiceRequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Cascade delete if service request is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_service_request_status ON ServiceRequests(Status); -- Index for filtering by status
CREATE INDEX idx_review_rating ON Reviews(SatisfactionRating); -- Index for filtering by satisfaction rating
```
