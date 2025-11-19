"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: "Design a database schema for storing information about interior design projects, including details about project types (residential, commercial, etc.), client information, and project awards, similar to Meezan Interior Solutions' project management needs."
Generated: DETERMINISTIC_1f09ca9d8582438c
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about interior design projects

-- Create a table for project types
CREATE TABLE ProjectTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each project type
    name VARCHAR(50) NOT NULL UNIQUE, -- Name of the project type (e.g., Residential, Commercial)
    description TEXT -- Description of the project type
);

-- Create a table for clients
CREATE TABLE Clients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) NOT NULL UNIQUE, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT -- Client's address
);

-- Create a table for projects
CREATE TABLE Projects (
    id SERIAL PRIMARY KEY, -- Unique identifier for each project
    name VARCHAR(100) NOT NULL, -- Name of the project
    project_type_id INT NOT NULL, -- Foreign key referencing ProjectTypes
    client_id INT NOT NULL, -- Foreign key referencing Clients
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    budget DECIMAL(10, 2), -- Budget for the project
    status VARCHAR(20) NOT NULL, -- Current status of the project (e.g., In Progress, Completed)
    FOREIGN KEY (project_type_id) REFERENCES ProjectTypes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for project awards
CREATE TABLE ProjectAwards (
    id SERIAL PRIMARY KEY, -- Unique identifier for each award
    project_id INT NOT NULL, -- Foreign key referencing Projects
    award_name VARCHAR(100) NOT NULL, -- Name of the award
    award_year INT NOT NULL, -- Year the award was received
    FOREIGN KEY (project_id) REFERENCES Projects(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for project images (optional)
CREATE TABLE ProjectImages (
    id SERIAL PRIMARY KEY, -- Unique identifier for each image
    project_id INT NOT NULL, -- Foreign key referencing Projects
    image_url VARCHAR(255) NOT NULL, -- URL of the image
    description TEXT, -- Description of the image
    FOREIGN KEY (project_id) REFERENCES Projects(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_type ON Projects(project_type_id);
CREATE INDEX idx_client ON Projects(client_id);
CREATE INDEX idx_project_award ON ProjectAwards(project_id);
```
