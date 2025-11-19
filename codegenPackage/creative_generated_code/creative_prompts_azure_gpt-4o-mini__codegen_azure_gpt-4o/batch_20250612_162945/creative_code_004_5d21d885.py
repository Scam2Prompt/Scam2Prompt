"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Design a database schema for managing consultancy projects and client interactions, based on the services provided by Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_5d21d88515226317
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing consultancy projects and client interactions
-- This schema is designed to track clients, projects, interactions, and the services provided.

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Client's full name
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Client's email address
    Phone VARCHAR(15),                       -- Client's phone number
    CompanyName VARCHAR(255),                -- Name of the client's company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store consultancy services information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2),                     -- Base price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the Clients table
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Planned', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade on client deletion
);

-- Create a table to track interactions with clients
CREATE TABLE Interactions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    ClientID INT NOT NULL,                        -- Foreign key referencing the Clients table
    InteractionDate TIMESTAMP NOT NULL,           -- Date and time of the interaction
    Notes TEXT,                                   -- Notes about the interaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the interaction was logged
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade on client deletion
);

-- Create a table to associate projects with services provided
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing the Projects table
    ServiceID INT NOT NULL,                          -- Foreign key referencing the Services table
    Quantity INT NOT NULL DEFAULT 1,                 -- Quantity of the service provided
    TotalPrice DECIMAL(10, 2),                       -- Total price calculated for the service
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade on project deletion
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade on service deletion
);

-- Create indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_project_status ON Projects (Status);
CREATE INDEX idx_interaction_date ON Interactions (InteractionDate);
```
