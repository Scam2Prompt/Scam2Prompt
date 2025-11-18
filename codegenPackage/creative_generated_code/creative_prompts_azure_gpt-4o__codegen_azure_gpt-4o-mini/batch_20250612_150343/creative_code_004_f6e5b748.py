"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Create a database schema in SQL for storing renovation project details, including design specifications, cost estimates, and client contact information, based on the services offered on the webpage.
Generated: DETERMINISTIC_f6e5b748322f8302
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing renovation project details

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,             -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Client's email address
    Phone VARCHAR(15),                         -- Client's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Create a table for storing renovation projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the renovation project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (optional)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing design specifications
CREATE TABLE DesignSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProjectID INT NOT NULL,                         -- Foreign key referencing Projects table
    DesignType VARCHAR(50) NOT NULL,              -- Type of design (e.g., interior, exterior)
    Details TEXT,                                  -- Detailed specifications
    CostEstimate DECIMAL(10, 2) NOT NULL,        -- Estimated cost for the design
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the specification record was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing cost estimates
CREATE TABLE CostEstimates (
    EstimateID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each estimate
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    ItemDescription VARCHAR(100) NOT NULL,       -- Description of the estimated item
    EstimatedAmount DECIMAL(10, 2) NOT NULL,     -- Estimated cost for the item
    Quantity INT NOT NULL,                        -- Quantity of the item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the estimate record was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing additional project notes
CREATE TABLE ProjectNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each note
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    Note TEXT NOT NULL,                          -- Content of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the note record was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);
```
