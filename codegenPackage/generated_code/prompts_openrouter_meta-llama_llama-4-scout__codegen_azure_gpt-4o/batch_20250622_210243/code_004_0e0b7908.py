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
-- Database Schema for Printing Services

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store order history
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    Notes TEXT,                                -- Additional notes for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store material specifications
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(100) NOT NULL,                -- Name of the material
    Type VARCHAR(50) NOT NULL,                 -- Type of material (e.g., paper, vinyl, fabric)
    Description TEXT,                          -- Description of the material
    PricePerUnit DECIMAL(10, 2) NOT NULL,      -- Price per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store order items (linking orders and materials)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    MaterialID INT NOT NULL,                    -- Foreign key referencing Materials table
    Quantity INT NOT NULL,                      -- Quantity of the material ordered
    Subtotal DECIMAL(10, 2) NOT NULL,           -- Subtotal for this item (Quantity * PricePerUnit)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Cascade delete if material is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_order_date ON Orders(OrderDate);    -- Index for quick lookup by order date
CREATE INDEX idx_material_name ON Materials(Name);   -- Index for quick lookup by material name
```
