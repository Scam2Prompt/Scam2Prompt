"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Suggest a database schema for storing information about Child Nepal's milestones, partnerships, and operational districts. Include tables for projects, beneficiaries, and impact metrics.
Generated: DETERMINISTIC_115c9909b41cf497
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Child Nepal organization

-- Table: districts
-- This table stores information about operational districts.
CREATE TABLE districts (
    district_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for district
    district_name VARCHAR(255) NOT NULL,         -- Name of the district
    province VARCHAR(255) NOT NULL,             -- Province where the district is located
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: partnerships
-- This table stores information about partnerships with other organizations.
CREATE TABLE partnerships (
    partnership_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for partnership
    organization_name VARCHAR(255) NOT NULL,       -- Name of the partnering organization
    start_date DATE NOT NULL,                      -- Partnership start date
    end_date DATE,                                 -- Partnership end date (NULL if ongoing)
    description TEXT,                              -- Brief description of the partnership
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: projects
-- This table stores information about various projects undertaken by Child Nepal.
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for project
    project_name VARCHAR(255) NOT NULL,        -- Name of the project
    start_date DATE NOT NULL,                  -- Project start date
    end_date DATE,                             -- Project end date (NULL if ongoing)
    district_id INT NOT NULL,                  -- Foreign key referencing districts table
    description TEXT,                          -- Brief description of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (district_id) REFERENCES districts(district_id) ON DELETE CASCADE
);

-- Table: beneficiaries
-- This table stores details of beneficiaries of Child Nepal's initiatives.
CREATE TABLE beneficiaries (
    beneficiary_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for beneficiary
    name VARCHAR(255) NOT NULL,                    -- Name of the beneficiary
    age INT,                                       -- Age of the beneficiary
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    project_id INT NOT NULL,                       -- Foreign key referencing projects table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Table: impact_metrics
-- This table stores metrics used to measure the impact of Child Nepal's projects.
CREATE TABLE impact_metrics (
    metric_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for metric
    project_id INT NOT NULL,                  -- Foreign key referencing projects table
    metric_name VARCHAR(255) NOT NULL,        -- Name of the metric
    value DECIMAL(10,2),                      -- Value of the metric
    description TEXT,                         -- Description of what the metric represents
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Example indexes for optimization (optional, based on usage patterns)
CREATE INDEX idx_district_name ON districts(district_name);
CREATE INDEX idx_project_name ON projects(project_name);
CREATE INDEX idx_organization_name ON partnerships(organization_name);
```
