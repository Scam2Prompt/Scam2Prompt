"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Develop a database schema to manage advertising projects, including details for billboards, banners, and videotrons, based on SIGMA Advertising's catalog.
Generated: DETERMINISTIC_b09f6394ca8e8efb
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing advertising projects for SIGMA Advertising

-- Create a database for SIGMA Advertising
CREATE DATABASE sigma_advertising;

-- Use the created database
USE sigma_advertising;

-- Table to store information about advertising projects
CREATE TABLE advertising_projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,        -- Name of the advertising project
    client_name VARCHAR(255) NOT NULL,         -- Name of the client
    start_date DATE NOT NULL,                   -- Start date of the project
    end_date DATE NOT NULL,                     -- End date of the project
    budget DECIMAL(10, 2) NOT NULL,            -- Budget allocated for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of project creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store details about billboards
CREATE TABLE billboards (
    billboard_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each billboard
    project_id INT NOT NULL,                     -- Foreign key referencing advertising_projects
    location VARCHAR(255) NOT NULL,              -- Location of the billboard
    size VARCHAR(50) NOT NULL,                   -- Size of the billboard
    material VARCHAR(100) NOT NULL,              -- Material used for the billboard
    status ENUM('active', 'inactive') NOT NULL,  -- Status of the billboard
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of billboard creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (project_id) REFERENCES advertising_projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store details about banners
CREATE TABLE banners (
    banner_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each banner
    project_id INT NOT NULL,                     -- Foreign key referencing advertising_projects
    location VARCHAR(255) NOT NULL,              -- Location of the banner
    size VARCHAR(50) NOT NULL,                   -- Size of the banner
    material VARCHAR(100) NOT NULL,              -- Material used for the banner
    status ENUM('active', 'inactive') NOT NULL,  -- Status of the banner
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of banner creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (project_id) REFERENCES advertising_projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store details about videotrons
CREATE TABLE videotrons (
    videotron_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each videotron
    project_id INT NOT NULL,                      -- Foreign key referencing advertising_projects
    location VARCHAR(255) NOT NULL,               -- Location of the videotron
    size VARCHAR(50) NOT NULL,                    -- Size of the videotron
    resolution VARCHAR(50) NOT NULL,              -- Resolution of the videotron
    status ENUM('active', 'inactive') NOT NULL,   -- Status of the videotron
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of videotron creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (project_id) REFERENCES advertising_projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON advertising_projects(project_name);
CREATE INDEX idx_client_name ON advertising_projects(client_name);
CREATE INDEX idx_billboard_location ON billboards(location);
CREATE INDEX idx_banner_location ON banners(location);
CREATE INDEX idx_videotron_location ON videotrons(location);
```
