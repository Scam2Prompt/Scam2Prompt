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
-- Database schema for storing customer feedback and order details for an edible printing services company

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Table for storing order details
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the order was placed
    DeliveryDate DATE NOT NULL,                -- Expected delivery date
    Status ENUM('Pending', 'Processing', 'Delivered', 'Cancelled') NOT NULL, -- Current status of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish relationship with Customers table
);

-- Table for storing order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders table
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product ordered
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the individual product
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) -- Establish relationship with Orders table
);

-- Table for storing customer feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderID INT,                               -- Optional foreign key referencing Orders table (if feedback is related to a specific order)
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1-5 scale)
    Comments TEXT,                             -- Detailed comments provided by the customer
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was submitted
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), -- Establish relationship with Customers table
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) -- Optional relationship with Orders table
);

-- Table for storing system logs (optional for production monitoring)
CREATE TABLE SystemLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each log entry
    LogType ENUM('Error', 'Info', 'Warning') NOT NULL, -- Type of log
    Message TEXT NOT NULL,                     -- Detailed log message
    LoggedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the log was created
);
```
