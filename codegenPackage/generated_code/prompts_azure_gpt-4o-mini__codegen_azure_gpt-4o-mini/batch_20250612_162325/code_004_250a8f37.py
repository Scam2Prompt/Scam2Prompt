"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Design a database schema for managing client projects in a cosmetic manufacturing business, reflecting the full-service approach outlined by Fabricare Cosmeticos.
Generated: DETERMINISTIC_250a8f375eaeb49d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client projects in a cosmetic manufacturing business

-- Create a database for the cosmetic manufacturing business
CREATE DATABASE IF NOT EXISTS FabricareCosmeticos;

-- Use the created database
USE FabricareCosmeticos;

-- Table to store client information
CREATE TABLE IF NOT EXISTS Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactEmail VARCHAR(255) NOT NULL UNIQUE, -- Email address of the client
    PhoneNumber VARCHAR(15),                   -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store project information
CREATE TABLE IF NOT EXISTS Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store product information related to projects
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Quantity INT NOT NULL,                       -- Quantity of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store project milestones
CREATE TABLE IF NOT EXISTS Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects
    MilestoneDescription VARCHAR(255) NOT NULL,  -- Description of the milestone
    DueDate DATE NOT NULL,                        -- Due date for the milestone
    Status ENUM('Not Started', 'In Progress', 'Completed') NOT NULL DEFAULT 'Not Started', -- Current status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the milestone was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store project notes
CREATE TABLE IF NOT EXISTS ProjectNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each note
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects
    NoteText TEXT NOT NULL,                      -- Content of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the note was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_milestone_due_date ON Milestones(DueDate);
```
