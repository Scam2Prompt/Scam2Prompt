"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Create a SQL database schema for storing information about industrial construction projects, including client details, project timelines, and material usage, similar to what Tether SARL might use."
Generated: DETERMINISTIC_5d94ca79189a3ec6
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for industrial construction projects

-- Create database
CREATE DATABASE IndustrialConstruction;

-- Use database
USE IndustrialConstruction;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Planned', 'In Progress', 'Completed', 'Cancelled')),
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for project timelines
CREATE TABLE ProjectTimelines (
    TimelineID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    Milestone VARCHAR(255) NOT NULL,
    TargetDate DATE NOT NULL,
    ActualDate DATE,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Planned', 'In Progress', 'Completed')),
    PRIMARY KEY (TimelineID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Create table for materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT,
    MaterialName VARCHAR(255) NOT NULL,
    Unit VARCHAR(50) NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (MaterialID)
);

-- Create table for project material usage
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    MaterialID INT NOT NULL,
    Quantity DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ProjectMaterialID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE
);

-- Create table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (SupplierID)
);

-- Create table for purchase orders
CREATE TABLE PurchaseOrders (
    PurchaseOrderID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    SupplierID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PurchaseOrderID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Create table for purchase order items
CREATE TABLE PurchaseOrderItems (
    PurchaseOrderItemID INT AUTO_INCREMENT,
    PurchaseOrderID INT NOT NULL,
    MaterialID INT NOT NULL,
    Quantity DECIMAL(10, 2) NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PurchaseOrderItemID),
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrders(PurchaseOrderID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_Projects_ClientID ON Projects (ClientID);
CREATE INDEX idx_ProjectTimelines_ProjectID ON ProjectTimelines (ProjectID);
CREATE INDEX idx_ProjectMaterials_ProjectID ON ProjectMaterials (ProjectID);
CREATE INDEX idx_ProjectMaterials_MaterialID ON ProjectMaterials (MaterialID);
CREATE INDEX idx_PurchaseOrders_ProjectID ON PurchaseOrders (ProjectID);
CREATE INDEX idx_PurchaseOrders_SupplierID ON PurchaseOrders (SupplierID);
CREATE INDEX idx_PurchaseOrderItems_PurchaseOrderID ON PurchaseOrderItems (PurchaseOrderID);
CREATE INDEX idx_PurchaseOrderItems_MaterialID ON PurchaseOrderItems (MaterialID);
```
