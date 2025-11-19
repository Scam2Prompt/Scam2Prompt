"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: "Design a simple database schema for managing orders, including delivery locations and quantities, inspired by utterlybaked.com."
Generated: DETERMINISTIC_5853d0ff631fe4d3
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing orders, delivery locations, and quantities

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to store delivery locations
CREATE TABLE DeliveryLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    AddressLine1 VARCHAR(255) NOT NULL,        -- First line of the address
    AddressLine2 VARCHAR(255),                 -- Second line of the address (optional)
    City VARCHAR(100) NOT NULL,                -- City name
    State VARCHAR(100) NOT NULL,               -- State name
    PostalCode VARCHAR(20) NOT NULL,           -- Postal/ZIP code
    Country VARCHAR(100) NOT NULL,             -- Country name
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the location was added
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    LocationID INT NOT NULL,                   -- Foreign key linking to the DeliveryLocations table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (LocationID) REFERENCES DeliveryLocations(LocationID) ON DELETE CASCADE -- Cascade delete if location is removed
);

-- Table to store order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key linking to the Orders table
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Quantity INT NOT NULL,                      -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price per unit of the product
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_order_status ON Orders(Status);     -- Index for filtering orders by status
CREATE INDEX idx_location_customer ON DeliveryLocations(CustomerID); -- Index for customer-location relationship
```
