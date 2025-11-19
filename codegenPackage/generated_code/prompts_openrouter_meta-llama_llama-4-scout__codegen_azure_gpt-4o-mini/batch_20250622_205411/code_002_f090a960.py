"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Generate a sample database schema for a construction company's customer relationship management (CRM) system, incorporating details such as client testimonials, project types, and service offerings like those of Clickmart Ltd."
Generated: DETERMINISTIC_f090a96083a718dd
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for a Construction Company's CRM System

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing project types
CREATE TABLE ProjectTypes (
    ProjectTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project type
    TypeName VARCHAR(100) NOT NULL,                -- Name of the project type (e.g., Residential, Commercial)
    Description TEXT                                -- Description of the project type
);

-- Create a table for storing service offerings
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,             -- Name of the service (e.g., Renovation, Landscaping)
    Description TEXT                                -- Description of the service
);

-- Create a table for storing client testimonials
CREATE TABLE Testimonials (
    TestimonialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each testimonial
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    Testimonial TEXT NOT NULL,                      -- The testimonial text
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating given by the client (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each project
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ProjectTypeID INT NOT NULL,                     -- Foreign key referencing ProjectTypes
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services
    ProjectName VARCHAR(100) NOT NULL,             -- Name of the project
    StartDate DATE NOT NULL,                        -- Start date of the project
    EndDate DATE,                                   -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProjectTypeID) REFERENCES ProjectTypes(ProjectTypeID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing project updates
CREATE TABLE ProjectUpdates (
    UpdateID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each update
    ProjectID INT NOT NULL,                         -- Foreign key referencing Projects
    UpdateText TEXT NOT NULL,                       -- Text of the update
    UpdateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
