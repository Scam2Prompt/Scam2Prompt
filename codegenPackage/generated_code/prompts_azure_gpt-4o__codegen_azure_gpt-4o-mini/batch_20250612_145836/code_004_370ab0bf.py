"""
Generated Code Metadata:
========================
Original URL: https://comestim.com.co
Prompt: Suggest a database schema for storing customer feedback and order details for a company offering edible printing services.
Generated: DETERMINISTIC_370ab0bf698829b7
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer feedback and order details
CREATE DATABASE EdiblePrintingService;

USE EdiblePrintingService;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address (unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store order details
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each feedback entry
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating from 1 to 5
    Comments TEXT,                               -- Additional comments from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feedback was submitted
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_order_customer ON Orders(CustomerID);
CREATE INDEX idx_feedback_order ON Feedback(OrderID);
CREATE INDEX idx_feedback_customer ON Feedback(CustomerID);
```
