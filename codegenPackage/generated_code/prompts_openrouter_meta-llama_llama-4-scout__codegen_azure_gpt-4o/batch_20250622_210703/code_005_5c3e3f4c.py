"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Design a database schema to store information about engraved products, including materials, designs, and customer orders.
Generated: DETERMINISTIC_5c3e3f4c9f611969
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about engraved products, materials, designs, and customer orders

-- Table to store information about materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(100) NOT NULL,                -- Name of the material (e.g., wood, metal, glass)
    Description TEXT,                          -- Description of the material
    PricePerUnit DECIMAL(10, 2) NOT NULL,      -- Price per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about designs
CREATE TABLE Designs (
    DesignID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each design
    Name VARCHAR(100) NOT NULL,                -- Name of the design (e.g., floral, geometric)
    Description TEXT,                          -- Description of the design
    ImageURL VARCHAR(255),                     -- URL to an image of the design
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the design was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(150) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store engraved products
CREATE TABLE EngravedProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each engraved product
    MaterialID INT NOT NULL,                   -- Foreign key referencing Materials table
    DesignID INT NOT NULL,                     -- Foreign key referencing Designs table
    Name VARCHAR(100) NOT NULL,                -- Name of the engraved product
    Description TEXT,                          -- Description of the engraved product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the engraved product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE,
    FOREIGN KEY (DesignID) REFERENCES Designs(DesignID) ON DELETE CASCADE
);

-- Table to store order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing EngravedProducts table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Subtotal for this product (Quantity * Product Price)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order detail was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES EngravedProducts(ProductID) ON DELETE CASCADE
);
```
