"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Create a database schema for managing custom box orders, including fields for "Box Type," "Material," "Size," "Customization Details," and "Client Information."
Generated: DETERMINISTIC_d8681748157c517c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing custom box orders

-- Table to store information about box types
CREATE TABLE BoxTypes (
    BoxTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each box type
    TypeName VARCHAR(100) NOT NULL,           -- Name of the box type
    Description TEXT                          -- Optional description of the box type
);

-- Table to store information about box materials
CREATE TABLE BoxMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,        -- Name of the material
    Description TEXT                           -- Optional description of the material
);

-- Table to store box sizes
CREATE TABLE BoxSizes (
    SizeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each box size
    Dimension VARCHAR(50) NOT NULL,        -- Dimension of the box (e.g., "10x10x10 cm")
    Description TEXT                       -- Optional description for the size
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- First name of the client
    LastName VARCHAR(100) NOT NULL,          -- Last name of the client
    Email VARCHAR(150) NOT NULL UNIQUE,      -- Email address of the client (must be unique)
    PhoneNumber VARCHAR(50),                 -- Optional phone number
    Address TEXT                             -- Optional address for the client
);

-- Table to store customization details for box orders
CREATE TABLE Customizations (
    CustomizationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customization
    Details TEXT NOT NULL                            -- Customization details (e.g., "Logo placement, color preferences")
);

-- Table to store box orders
CREATE TABLE BoxOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    ClientID INT NOT NULL,                  -- Foreign key to Clients table
    BoxTypeID INT NOT NULL,                 -- Foreign key to BoxTypes table
    MaterialID INT NOT NULL,                -- Foreign key to BoxMaterials table
    SizeID INT NOT NULL,                    -- Foreign key to BoxSizes table
    CustomizationID INT,                    -- Foreign key to Customizations table (optional)
    OrderDate DATE NOT NULL,                -- Date the order was placed
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of boxes ordered (must be positive)
    TotalPrice DECIMAL(10, 2) NOT NULL CHECK (TotalPrice >= 0), -- Total price of the order (must be non-negative)
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., "Pending", "Completed")
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (BoxTypeID) REFERENCES BoxTypes(BoxTypeID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES BoxMaterials(MaterialID) ON DELETE CASCADE,
    FOREIGN KEY (SizeID) REFERENCES BoxSizes(SizeID) ON DELETE CASCADE,
    FOREIGN KEY (CustomizationID) REFERENCES Customizations(CustomizationID) ON DELETE SET NULL
);

-- Indexes for faster queries
CREATE INDEX idx_ClientID ON BoxOrders(ClientID);
CREATE INDEX idx_OrderStatus ON BoxOrders(Status);
CREATE INDEX idx_OrderDate ON BoxOrders(OrderDate);

-- Ensure proper charset for supporting international data
ALTER DATABASE MyDatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
