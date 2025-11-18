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
-- Database schema for Child Nepal's milestones, partnerships, and operational districts

CREATE DATABASE IF NOT EXISTS child_nepal;

USE child_nepal;

-- Table to store information about operational districts
CREATE TABLE IF NOT EXISTS districts (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each district
    name VARCHAR(255) NOT NULL,                 -- Name of the district
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about partners
CREATE TABLE IF NOT EXISTS partners (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each partner
    name VARCHAR(255) NOT NULL,                 -- Name of the partner organization
    contact_info VARCHAR(255),                   -- Contact information of the partner
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about projects
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each project
    name VARCHAR(255) NOT NULL,                 -- Name of the project
    description TEXT,                           -- Description of the project
    start_date DATE NOT NULL,                   -- Start date of the project
    end_date DATE,                              -- End date of the project (nullable)
    district_id INT,                            -- Foreign key referencing districts
    partner_id INT,                             -- Foreign key referencing partners
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (district_id) REFERENCES districts(id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (partner_id) REFERENCES partners(id) ON DELETE SET NULL  -- Nullable relationship with partners
);

-- Table to store information about beneficiaries
CREATE TABLE IF NOT EXISTS beneficiaries (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each beneficiary
    name VARCHAR(255) NOT NULL,                 -- Name of the beneficiary
    age INT,                                    -- Age of the beneficiary
    gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Gender of the beneficiary
    project_id INT,                             -- Foreign key referencing projects
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store impact metrics related to projects
CREATE TABLE IF NOT EXISTS impact_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each impact metric
    project_id INT,                             -- Foreign key referencing projects
    metric_name VARCHAR(255) NOT NULL,         -- Name of the metric measured
    metric_value FLOAT NOT NULL,                -- Value of the metric
    measurement_date DATE NOT NULL,             -- Date when the metric was measured
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for better performance
CREATE INDEX idx_project_district ON projects(district_id);
CREATE INDEX idx_beneficiary_project ON beneficiaries(project_id);
CREATE INDEX idx_impact_project ON impact_metrics(project_id);
```
