"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Develop a database schema to manage advertising projects, including details for billboards, banners, and videotrons, based on SIGMA Advertising's catalog.
Generated: DETERMINISTIC_b09f6394ca8e8efb
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for SIGMA Advertising's catalog to manage advertising projects
-- Includes details for billboards, banners, and videotrons

-- Create the advertising_projects table to store project details
CREATE TABLE advertising_projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the advertising project
    client_name VARCHAR(255) NOT NULL, -- Name of the client
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE NOT NULL, -- End date of the project
    budget DECIMAL(15, 2) NOT NULL, -- Budget allocated for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of project creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create the billboard_ads table to store details of billboard advertisements
CREATE TABLE billboard_ads (
    billboard_id SERIAL PRIMARY KEY, -- Unique identifier for each billboard ad
    project_id INT NOT NULL, -- Foreign key referencing advertising_projects
    location VARCHAR(255) NOT NULL, -- Location of the billboard
    dimensions VARCHAR(50) NOT NULL, -- Dimensions of the billboard (e.g., "10x20 feet")
    material VARCHAR(50) NOT NULL, -- Material used for the billboard
    price DECIMAL(15, 2) NOT NULL, -- Cost of the billboard ad
    FOREIGN KEY (project_id) REFERENCES advertising_projects(project_id) ON DELETE CASCADE -- Cascade delete
);

-- Create the banner_ads table to store details of banner advertisements
CREATE TABLE banner_ads (
    banner_id SERIAL PRIMARY KEY, -- Unique identifier for each banner ad
    project_id INT NOT NULL, -- Foreign key referencing advertising_projects
    location VARCHAR(255) NOT NULL, -- Location where the banner is displayed
    dimensions VARCHAR(50) NOT NULL, -- Dimensions of the banner (e.g., "5x10 feet")
    material VARCHAR(50) NOT NULL, -- Material used for the banner
    price DECIMAL(15, 2) NOT NULL, -- Cost of the banner ad
    FOREIGN KEY (project_id) REFERENCES advertising_projects(project_id) ON DELETE CASCADE -- Cascade delete
);

-- Create the videotron_ads table to store details of videotron advertisements
CREATE TABLE videotron_ads (
    videotron_id SERIAL PRIMARY KEY, -- Unique identifier for each videotron ad
    project_id INT NOT NULL, -- Foreign key referencing advertising_projects
    location VARCHAR(255) NOT NULL, -- Location of the videotron display
    resolution VARCHAR(50) NOT NULL, -- Resolution of the videotron (e.g., "1920x1080")
    playback_duration INT NOT NULL, -- Playback duration in seconds
    price DECIMAL(15, 2) NOT NULL, -- Cost of the videotron ad
    FOREIGN KEY (project_id) REFERENCES advertising_projects(project_id) ON DELETE CASCADE -- Cascade delete
);

-- Create the logs table to record activity or error logs for auditing purposes
CREATE TABLE logs (
    log_id SERIAL PRIMARY KEY, -- Unique identifier for each log entry
    log_level VARCHAR(50) NOT NULL, -- Level of the log (e.g., "INFO", "ERROR")
    message TEXT NOT NULL, -- Details of the log message
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of log creation
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_name ON advertising_projects(project_name);
CREATE INDEX idx_client_name ON advertising_projects(client_name);
CREATE INDEX idx_billboard_location ON billboard_ads(location);
CREATE INDEX idx_banner_location ON banner_ads(location);
CREATE INDEX idx_videotron_location ON videotron_ads(location);

-- Ensure all tables are created with strict integrity and relationships properly defined.
```
