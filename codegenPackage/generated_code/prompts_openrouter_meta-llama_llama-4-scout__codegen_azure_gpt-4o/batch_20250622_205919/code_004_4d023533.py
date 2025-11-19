"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Design a database schema to store information about beers, including name, style, price, and quantity in stock, suitable for an online beer store like Barbudo Growler.
Generated: DETERMINISTIC_4d0235337122580b
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online beer store

-- Create a table to store information about beers
CREATE TABLE Beers (
    BeerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beer
    Name VARCHAR(255) NOT NULL,            -- Name of the beer
    Style VARCHAR(100) NOT NULL,           -- Style/type of the beer (e.g., IPA, Lager, Stout)
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the beer (up to 10 digits, 2 decimal places)
    QuantityInStock INT NOT NULL,          -- Quantity of the beer available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the beer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the beer record was last updated
);

-- Create a table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- First name of the customer
    LastName VARCHAR(100) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the customer (must be unique)
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer record was last updated
);

-- Create a table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key referencing the Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Create a table to store order details (items in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing the Orders table
    BeerID INT NOT NULL,                          -- Foreign key referencing the Beers table
    Quantity INT NOT NULL,                        -- Quantity of the beer ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the beer at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (BeerID) REFERENCES Beers(BeerID) ON DELETE CASCADE -- Cascade delete if beer is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_beer_name ON Beers(Name); -- Index on beer name for faster searches
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on customer email for faster lookups
CREATE INDEX idx_order_date ON Orders(OrderDate); -- Index on order date for faster filtering
```
