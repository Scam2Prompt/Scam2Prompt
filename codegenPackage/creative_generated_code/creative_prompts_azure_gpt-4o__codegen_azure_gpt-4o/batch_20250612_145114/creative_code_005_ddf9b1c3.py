"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Create a database schema for managing roofing projects, including fields for roof type (tile, shingle, metal, flat), client details, and warranty information, inspired by King Roofing's services.
Generated: DETERMINISTIC_ddf9b1c3ec6a04fb
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Roofing Projects

-- Table: Clients
-- This table stores client details.
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: RoofingProjects
-- This table stores details about roofing projects.
CREATE TABLE RoofingProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing the client
    RoofType ENUM('Tile', 'Shingle', 'Metal', 'Flat') NOT NULL, -- Type of roof
    ProjectStartDate DATE NOT NULL,            -- Start date of the project
    ProjectEndDate DATE,                       -- End date of the project
    TotalCost DECIMAL(10, 2),                  -- Total cost of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Relationship with Clients table
);

-- Table: Warranties
-- This table stores warranty details for roofing projects.
CREATE TABLE Warranties (
    WarrantyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each warranty
    ProjectID INT NOT NULL,                    -- Foreign key referencing the roofing project
    WarrantyPeriod INT NOT NULL,               -- Warranty period in months
    CoverageDetails TEXT,                      -- Details about what the warranty covers
    StartDate DATE NOT NULL,                   -- Start date of the warranty
    EndDate DATE NOT NULL,                     -- End date of the warranty
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES RoofingProjects(ProjectID) ON DELETE CASCADE -- Relationship with RoofingProjects table
);

-- Indexes for optimization
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_roofing_project_status ON RoofingProjects (Status);
CREATE INDEX idx_warranty_dates ON Warranties (StartDate, EndDate);
```
