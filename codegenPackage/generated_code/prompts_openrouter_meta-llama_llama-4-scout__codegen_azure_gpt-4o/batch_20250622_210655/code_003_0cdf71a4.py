"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: "Design a database schema to store information about dry facade system projects, including client details, project timelines, and product usage."
Generated: DETERMINISTIC_0cdf71a4d26a70a1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Dry Facade System Projects

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Client's name
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(20),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed') NOT NULL, -- Project status
    Budget DECIMAL(15, 2),                    -- Project budget
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store product usage details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Product name
    Description TEXT,                         -- Product description
    UnitPrice DECIMAL(10, 2) NOT NULL,        -- Price per unit of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store product usage in projects
CREATE TABLE ProjectProducts (
    ProjectProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects table
    ProductID INT NOT NULL,                          -- Foreign key referencing Products table
    Quantity INT NOT NULL,                           -- Quantity of the product used in the project
    TotalCost DECIMAL(15, 2) GENERATED ALWAYS AS (Quantity * (SELECT UnitPrice FROM Products WHERE Products.ProductID = ProjectProducts.ProductID)) STORED, -- Total cost calculation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Cascade delete if product is removed
);

-- Indexes for optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup of clients by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for quick lookup of projects by status
CREATE INDEX idx_product_name ON Products(Name); -- Index for quick lookup of products by name
```
