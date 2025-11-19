"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: "Design a database schema to store information about interior design projects, including client details, project phases, and product information, inspired by Zirciulit Design Firm's workflow."
Generated: DETERMINISTIC_2aee417d3e443547
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about interior design projects
CREATE DATABASE InteriorDesignFirm;

USE InteriorDesignFirm;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Pending',  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store project phases
CREATE TABLE ProjectPhases (
    PhaseID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each phase
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects
    PhaseName VARCHAR(100) NOT NULL,          -- Name of the project phase
    StartDate DATE NOT NULL,                   -- Phase start date
    EndDate DATE,                              -- Phase end date
    Status ENUM('Not Started', 'In Progress', 'Completed') NOT NULL DEFAULT 'Not Started',  -- Current status of the phase
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Supplier VARCHAR(100),                      -- Supplier of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link products to project phases
CREATE TABLE PhaseProducts (
    PhaseProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each phase-product link
    PhaseID INT NOT NULL,                           -- Foreign key referencing ProjectPhases
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    Quantity INT NOT NULL DEFAULT 1,               -- Quantity of the product used in the phase
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PhaseID) REFERENCES ProjectPhases(PhaseID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_client ON Projects(ClientID);
CREATE INDEX idx_phase_project ON ProjectPhases(ProjectID);
CREATE INDEX idx_phase_product ON PhaseProducts(PhaseID, ProductID);
```
