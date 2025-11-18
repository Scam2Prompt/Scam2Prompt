"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Create a database schema for managing private label cleaning tool production, inspired by PDC Brush's operational model.
Generated: DETERMINISTIC_5465e921e19b876b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema: Private Label Cleaning Tool Production Management
-- Inspired by PDC Brush's operational model

-- Table: Users
-- Description: Stores information about users such as administrators, production managers, etc.
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for a user
    Username VARCHAR(50) NOT NULL UNIQUE,        -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,          -- Securely hashed password
    FullName VARCHAR(100) NOT NULL,              -- Full name of the user
    Role ENUM('Admin', 'Manager', 'Worker') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Clients
-- Description: Stores information about clients for private label products.
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for a client
    ClientName VARCHAR(100) NOT NULL,            -- Name of the client
    ContactPerson VARCHAR(100),                  -- Contact person's name
    Email VARCHAR(100),                          -- Contact email
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    Address TEXT,                                -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: ProductCategories
-- Description: Stores different categories of cleaning tools.
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for a category
    CategoryName VARCHAR(50) NOT NULL UNIQUE,    -- Name of the product category (e.g., Brushes, Mops, etc.)
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Products
-- Description: Stores information about each cleaning tool product.
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for a product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    CategoryID INT NOT NULL,                     -- Foreign key referencing ProductCategories
    ClientID INT,                                -- Foreign key referencing Clients (if custom/private label)
    BaseCost DECIMAL(10, 2) NOT NULL,            -- Base cost of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Selling price of the product
    Description TEXT,                            -- Product description
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE SET NULL
);

-- Table: RawMaterials
-- Description: Stores information about raw materials used in production.
CREATE TABLE RawMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for a raw material
    MaterialName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the raw material
    UnitOfMeasure VARCHAR(20) NOT NULL,          -- Unit of measure (e.g., kg, liters, etc.)
    CostPerUnit DECIMAL(10, 2) NOT NULL,         -- Cost per unit of the material
    StockQuantity DECIMAL(10, 2) NOT NULL,       -- Current stock quantity
    ReorderLevel DECIMAL(10, 2) NOT NULL,        -- Stock level to trigger reorder
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: ProductMaterials
-- Description: Defines the raw materials required for each product.
CREATE TABLE ProductMaterials (
    ProductMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    MaterialID INT NOT NULL,                         -- Foreign key referencing RawMaterials
    QuantityRequired DECIMAL(10, 2) NOT NULL,        -- Quantity of material required for the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES RawMaterials(MaterialID) ON DELETE CASCADE
);

-- Table: ProductionOrders
-- Description: Stores information about production orders for products.
CREATE TABLE ProductionOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for a production order
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    Quantity INT NOT NULL,                           -- Quantity of the product to produce
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    ScheduledDate DATE NOT NULL,                     -- Date when production is scheduled
    CompletedDate DATE,                              -- Date when production was completed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Inventory
-- Description: Tracks inventory of finished products.
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for an inventory record
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    StockQuantity INT NOT NULL,                      -- Quantity of stock available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Shipments
-- Description: Tracks shipments of completed orders.
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for a shipment
    OrderID INT NOT NULL,                            -- Foreign key referencing ProductionOrders
    ShippedDate DATE NOT NULL,                       -- Date when the shipment was sent
    DeliveredDate DATE,                              -- Date when the shipment was delivered
    TrackingNumber VARCHAR(100),                    -- Tracking number for the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (OrderID) REFERENCES ProductionOrders(OrderID) ON DELETE CASCADE
);
```
