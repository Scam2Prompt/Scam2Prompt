"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: "Design a database schema for a laundry service business, incorporating customer, service, and payment information, as seen on lavanderiacallezaragoza.com."
Generated: DETERMINISTIC_a8438f5deb29f92c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Laundry Service Business

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table: Services
-- Stores information about laundry services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service (e.g., "Wash & Fold")
    Description TEXT,                          -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    DurationInHours INT NOT NULL,              -- Estimated duration of the service in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table: Payments
-- Stores payment information for completed services
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    AmountPaid DECIMAL(10, 2) NOT NULL,        -- Amount paid by the customer
    PaymentMethod ENUM('Cash', 'Card', 'Online') NOT NULL, -- Payment method used
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the payment was made
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE    -- Cascade delete
);

-- Table: Orders
-- Stores information about service orders placed by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    OrderStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    CompletionDate TIMESTAMP NULL,             -- Timestamp of when the order was completed
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE    -- Cascade delete
);

-- Indexes for faster queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on email for quick lookups
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index on service name for quick lookups
CREATE INDEX idx_order_status ON Orders(OrderStatus); -- Index on order status for quick filtering
```
