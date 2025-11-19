"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Design a database schema to store information about elevator modernization projects, including details about replaced parts, such as COP/LOP panels with VEGA touchscreens, and upgrades to open protocol controls from Beta Control."
Generated: DETERMINISTIC_cae88eda6725c29e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about elevator modernization projects

CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the modernization project
    project_start_date DATE NOT NULL, -- Start date of the project
    project_end_date DATE, -- End date of the project (nullable)
    client_name VARCHAR(255) NOT NULL, -- Name of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Parts (
    part_id SERIAL PRIMARY KEY, -- Unique identifier for each part
    part_name VARCHAR(255) NOT NULL, -- Name of the part (e.g., COP panel, LOP panel)
    part_type VARCHAR(100) NOT NULL, -- Type of the part (e.g., touchscreen, control system)
    manufacturer VARCHAR(255), -- Manufacturer of the part (nullable)
    model_number VARCHAR(100), -- Model number of the part (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE ProjectParts (
    project_part_id SERIAL PRIMARY KEY, -- Unique identifier for each project-part relationship
    project_id INT NOT NULL, -- Foreign key referencing Projects
    part_id INT NOT NULL, -- Foreign key referencing Parts
    quantity INT NOT NULL DEFAULT 1, -- Quantity of the part used in the project
    installation_date DATE, -- Date when the part was installed (nullable)
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (part_id) REFERENCES Parts(part_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Upgrades (
    upgrade_id SERIAL PRIMARY KEY, -- Unique identifier for each upgrade
    project_id INT NOT NULL, -- Foreign key referencing Projects
    upgrade_description TEXT NOT NULL, -- Description of the upgrade (e.g., open protocol controls)
    upgrade_date DATE NOT NULL, -- Date when the upgrade was performed
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON Projects(project_name);
CREATE INDEX idx_part_name ON Parts(part_name);
CREATE INDEX idx_upgrade_date ON Upgrades(upgrade_date);
```
