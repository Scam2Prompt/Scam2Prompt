"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Design a database schema for managing client projects in a cosmetic manufacturing business, reflecting the full-service approach outlined by Fabricare Cosmeticos.
Generated: DETERMINISTIC_250a8f375eaeb49d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Client Projects in a Cosmetic Manufacturing Business

-- Create table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,              -- Name of the client
    ContactEmail VARCHAR(150),               -- Email address for client communication
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    Address TEXT,                            -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key linking to Clients table
    Name VARCHAR(100) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (optional)
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure data integrity
);

-- Create table to store manufacturing details for each project
CREATE TABLE ManufacturingDetails (
    ManufacturingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for manufacturing details
    ProjectID INT NOT NULL,                          -- Foreign key linking to Projects table
    Formula VARCHAR(255) NOT NULL,                  -- Formula used for cosmetic manufacturing
    Ingredients TEXT NOT NULL,                      -- List of ingredients used in the project
    BatchSize INT NOT NULL CHECK (BatchSize > 0),   -- Batch size for manufacturing (must be positive)
    ProductionDate DATE NOT NULL,                   -- Date of production
    ExpiryDate DATE,                                -- Expiry date of the manufactured product (optional)
    Notes TEXT,                                     -- Additional notes or observations
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the manufacturing details are added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure data integrity
);

-- Create table to store quality assurance details
CREATE TABLE QualityAssurance (
    QAID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for QA record
    ManufacturingID INT NOT NULL,                 -- Foreign key linking to ManufacturingDetails table
    InspectionDate DATE NOT NULL,                 -- Date of quality assurance inspection
    PassedInspection BOOLEAN NOT NULL DEFAULT 0,  -- Whether the manufacturing batch passed inspection (0 = No, 1 = Yes)
    Issues TEXT,                                  -- List of issues found during inspection (if any)
    Notes TEXT,                                   -- Additional notes from the QA team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the QA record is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ManufacturingID) REFERENCES ManufacturingDetails(ManufacturingID) ON DELETE CASCADE -- Ensure data integrity
);

-- Create table to track shipments to clients
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for shipment record
    ProjectID INT NOT NULL,                       -- Foreign key linking to Projects table
    ShipmentDate DATE NOT NULL,                   -- Date of shipment
    Carrier VARCHAR(100) NOT NULL,                -- Name of the shipping carrier
    TrackingNumber VARCHAR(50),                   -- Tracking number provided by carrier (optional)
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Delayed') NOT NULL DEFAULT 'Pending', -- Shipment status
    Notes TEXT,                                   -- Additional notes about the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the shipment record is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure data integrity
);

-- Create table to store invoices for client payments
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for invoice record
    ClientID INT NOT NULL,                       -- Foreign key linking to Clients table
    ProjectID INT NOT NULL,                      -- Foreign key linking to Projects table
    Amount DECIMAL(10, 2) NOT NULL CHECK (Amount > 0), -- Invoice amount (must be positive)
    InvoiceDate DATE NOT NULL,                   -- Date the invoice is issued
    DueDate DATE NOT NULL,                       -- Due date for payment
    Status ENUM('Pending', 'Paid', 'Overdue') NOT NULL DEFAULT 'Pending', -- Payment status
    Notes TEXT,                                  -- Additional notes about the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the invoice record is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure data integrity
);
```
