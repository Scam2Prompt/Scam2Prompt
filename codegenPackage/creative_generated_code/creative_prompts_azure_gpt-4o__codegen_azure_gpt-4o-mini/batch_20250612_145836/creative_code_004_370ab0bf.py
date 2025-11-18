"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Suggest a database schema for storing customer feedback and order details for a company offering edible printing services.
Generated: DETERMINISTIC_370ab0bf698829b7
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer feedback and order details for an edible printing services company.

-- Table to store customers' information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Customer's email address (unique)
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer record was created
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Reference to the customer placing the order
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Foreign key constraint
);

-- Table to store feedback provided by customers
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each feedback entry
    OrderID INT NOT NULL,                       -- Reference to the related order
    CustomerID INT NOT NULL,                    -- Reference to the customer providing feedback
    FeedbackText TEXT NOT NULL,                 -- The actual feedback content
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating given by the customer (1 to 5)
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feedback was submitted
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Foreign key constraint to orders
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Foreign key constraint to customers
);

-- Example index to speed up lookups on email in Customers table
CREATE INDEX idx_email ON Customers(Email);

-- Example index to speed up lookups on order date in Orders table
CREATE INDEX idx_order_date ON Orders(OrderDate);
```
