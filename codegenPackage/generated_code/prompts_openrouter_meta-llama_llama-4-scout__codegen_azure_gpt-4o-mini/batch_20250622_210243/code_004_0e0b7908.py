"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Design a database schema to store information about printing services, including customer details, order history, and material specifications, for a company like Detalj Reklam & Tryckeri."
Generated: DETERMINISTIC_0e0b7908de6ef795
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a printing services company

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    Address VARCHAR(255),                        -- Customer's address
    City VARCHAR(50),                           -- Customer's city
    State VARCHAR(50),                          -- Customer's state
    ZipCode VARCHAR(10),                        -- Customer's postal code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Create a table to store material specifications
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,         -- Name of the material
    MaterialType VARCHAR(50) NOT NULL,          -- Type of material (e.g., paper, vinyl)
    Thickness DECIMAL(5, 2),                    -- Thickness of the material in mm
    Color VARCHAR(50),                          -- Color of the material
    PricePerUnit DECIMAL(10, 2) NOT NULL,      -- Price per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the material was added
);

-- Create a table to store order history
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store order details (linking orders to materials)
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                          -- Foreign key referencing Orders
    MaterialID INT NOT NULL,                       -- Foreign key referencing Materials
    Quantity INT NOT NULL,                         -- Quantity of the material ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price for the quantity ordered
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the email column in the Customers table for faster lookups
CREATE INDEX idx_email ON Customers(Email);

-- Create an index on the OrderDate column in the Orders table for faster queries
CREATE INDEX idx_order_date ON Orders(OrderDate);
```
