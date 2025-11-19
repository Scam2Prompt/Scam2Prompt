"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Recommend a suitable database schema for managing plumbing services, including customer information, service requests, and payment history, similar to Certified Plumbers Graham, TX's operations."
Generated: DETERMINISTIC_096113c6936f4a6b
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Plumbing Services

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    Address TEXT NOT NULL,                     -- Customer's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Table: ServiceRequests
-- Stores information about service requests made by customers
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceType VARCHAR(100) NOT NULL,         -- Type of service requested (e.g., pipe repair, installation)
    Description TEXT,                          -- Detailed description of the service request
    RequestDate DATE NOT NULL,                 -- Date when the service was requested
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    AssignedTechnician VARCHAR(100),           -- Name of the technician assigned to the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service request was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table: Payments
-- Stores payment history for service requests
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    RequestID INT NOT NULL,                    -- Foreign key referencing ServiceRequests table
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    Amount DECIMAL(10, 2) NOT NULL,            -- Payment amount
    PaymentDate DATE NOT NULL,                 -- Date when the payment was made
    PaymentMethod ENUM('Cash', 'Credit Card', 'Debit Card', 'Online') NOT NULL, -- Payment method used
    TransactionID VARCHAR(100) UNIQUE,         -- Unique transaction ID for the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment record was created
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Cascade delete if service request is deleted
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_request_status ON ServiceRequests(Status); -- Index for filtering by request status
CREATE INDEX idx_payment_date ON Payments(PaymentDate); -- Index for filtering payments by date
```
