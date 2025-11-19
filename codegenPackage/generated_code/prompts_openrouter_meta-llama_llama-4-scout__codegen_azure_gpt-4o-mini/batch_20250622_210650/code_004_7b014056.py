"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: "Design a database schema for storing information about real estate projects, including details about lots, financing options, and construction progress."
Generated: DETERMINISTIC_7b014056642aaf2e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about real estate projects

-- Table to store information about real estate projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    location VARCHAR(255) NOT NULL, -- Location of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planning', 'In Progress', 'Completed', 'On Hold')), -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the project was last updated
);

-- Table to store information about lots within each project
CREATE TABLE Lots (
    lot_id SERIAL PRIMARY KEY, -- Unique identifier for each lot
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    lot_number VARCHAR(50) NOT NULL, -- Lot number
    size DECIMAL(10, 2) NOT NULL, -- Size of the lot in square feet
    price DECIMAL(10, 2) NOT NULL, -- Price of the lot
    status VARCHAR(50) NOT NULL CHECK (status IN ('Available', 'Sold', 'Reserved')), -- Current status of the lot
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the lot was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the lot was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures lots are deleted if the project is deleted
);

-- Table to store financing options for each project
CREATE TABLE FinancingOptions (
    financing_id SERIAL PRIMARY KEY, -- Unique identifier for each financing option
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    option_name VARCHAR(255) NOT NULL, -- Name of the financing option
    interest_rate DECIMAL(5, 2) NOT NULL, -- Interest rate for the financing option
    terms VARCHAR(255) NOT NULL, -- Terms of the financing option
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the financing option was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the financing option was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures financing options are deleted if the project is deleted
);

-- Table to store construction progress for each project
CREATE TABLE ConstructionProgress (
    progress_id SERIAL PRIMARY KEY, -- Unique identifier for each progress entry
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    progress_date DATE NOT NULL, -- Date of the progress update
    description TEXT NOT NULL, -- Description of the progress made
    percentage_complete DECIMAL(5, 2) CHECK (percentage_complete >= 0 AND percentage_complete <= 100), -- Percentage of completion
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the progress entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the progress entry was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures progress entries are deleted if the project is deleted
);
```
