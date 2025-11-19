"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Suggest a database schema for storing information about Child Nepal's milestones, partnerships, and operational districts. Include tables for projects, beneficiaries, and impact metrics.
Generated: DETERMINISTIC_115c9909b41cf497
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Child Nepal's milestones, partnerships, and operational districts

-- Table to store information about operational districts
CREATE TABLE OperationalDistricts (
    district_id SERIAL PRIMARY KEY, -- Unique identifier for each district
    district_name VARCHAR(255) NOT NULL, -- Name of the district
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about beneficiaries
CREATE TABLE Beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    name VARCHAR(255) NOT NULL, -- Name of the beneficiary
    age INT CHECK (age >= 0), -- Age of the beneficiary, must be non-negative
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')), -- Gender of the beneficiary
    district_id INT REFERENCES OperationalDistricts(district_id) ON DELETE CASCADE, -- Foreign key to OperationalDistricts
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    district_id INT REFERENCES OperationalDistricts(district_id) ON DELETE SET NULL, -- Foreign key to OperationalDistricts
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about partnerships
CREATE TABLE Partnerships (
    partnership_id SERIAL PRIMARY KEY, -- Unique identifier for each partnership
    partner_name VARCHAR(255) NOT NULL, -- Name of the partner organization
    contact_info VARCHAR(255), -- Contact information for the partner
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store impact metrics related to projects
CREATE TABLE ImpactMetrics (
    metric_id SERIAL PRIMARY KEY, -- Unique identifier for each metric
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE, -- Foreign key to Projects
    beneficiaries_served INT CHECK (beneficiaries_served >= 0), -- Number of beneficiaries served
    impact_description TEXT, -- Description of the impact
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to link projects and partnerships (many-to-many relationship)
CREATE TABLE ProjectPartnerships (
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE, -- Foreign key to Projects
    partnership_id INT REFERENCES Partnerships(partnership_id) ON DELETE CASCADE, -- Foreign key to Partnerships
    PRIMARY KEY (project_id, partnership_id) -- Composite primary key
);
```
