"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Design a database schema to store property inspection data, including photos, user information, and inspection reports, for an application like App Vistoria."
Generated: DETERMINISTIC_a6dee2c7e9d8ed2f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing property inspection data

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store property information
CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY,       -- Unique identifier for each property
    user_id INT NOT NULL,                 -- Foreign key referencing Users
    address VARCHAR(255) NOT NULL,        -- Address of the property
    city VARCHAR(100) NOT NULL,           -- City where the property is located
    state VARCHAR(100) NOT NULL,          -- State where the property is located
    zip_code VARCHAR(20) NOT NULL,       -- Zip code of the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of property creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store inspection reports
CREATE TABLE InspectionReports (
    report_id SERIAL PRIMARY KEY,         -- Unique identifier for each inspection report
    property_id INT NOT NULL,             -- Foreign key referencing Properties
    inspection_date TIMESTAMP NOT NULL,   -- Date of the inspection
    inspector_name VARCHAR(100) NOT NULL, -- Name of the inspector
    report_details TEXT NOT NULL,         -- Detailed report of the inspection
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of report creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store photos related to inspections
CREATE TABLE InspectionPhotos (
    photo_id SERIAL PRIMARY KEY,          -- Unique identifier for each photo
    report_id INT NOT NULL,               -- Foreign key referencing InspectionReports
    photo_url VARCHAR(255) NOT NULL,      -- URL of the photo
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of photo upload
    FOREIGN KEY (report_id) REFERENCES InspectionReports(report_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the inspection date for faster queries
CREATE INDEX idx_inspection_date ON InspectionReports(inspection_date);
```
