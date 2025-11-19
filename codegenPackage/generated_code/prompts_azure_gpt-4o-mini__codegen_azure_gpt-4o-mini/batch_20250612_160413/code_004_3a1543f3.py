"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Design a data model in SQL to manage the records of girls impacted by menstrual health initiatives, similar to the tracking done by My Flow Foundation.
Generated: DETERMINISTIC_3a1543f3ceb01dfb
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a data model for managing records of girls impacted by menstrual health initiatives

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Girls;
DROP TABLE IF EXISTS Initiatives;
DROP TABLE IF EXISTS HealthRecords;

-- Table to store information about girls
CREATE TABLE Girls (
    girl_id SERIAL PRIMARY KEY, -- Unique identifier for each girl
    name VARCHAR(100) NOT NULL, -- Name of the girl
    date_of_birth DATE NOT NULL, -- Date of birth
    school VARCHAR(100), -- School name
    contact_number VARCHAR(15), -- Contact number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about health initiatives
CREATE TABLE Initiatives (
    initiative_id SERIAL PRIMARY KEY, -- Unique identifier for each initiative
    initiative_name VARCHAR(100) NOT NULL, -- Name of the initiative
    description TEXT, -- Description of the initiative
    start_date DATE NOT NULL, -- Start date of the initiative
    end_date DATE, -- End date of the initiative (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store health records related to girls and initiatives
CREATE TABLE HealthRecords (
    record_id SERIAL PRIMARY KEY, -- Unique identifier for each health record
    girl_id INT NOT NULL, -- Foreign key referencing the girl
    initiative_id INT NOT NULL, -- Foreign key referencing the initiative
    record_date DATE NOT NULL, -- Date of the health record
    notes TEXT, -- Additional notes regarding the health record
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (girl_id) REFERENCES Girls(girl_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (initiative_id) REFERENCES Initiatives(initiative_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion (uncomment to use)
-- INSERT INTO Girls (name, date_of_birth, school, contact_number) VALUES
-- ('Alice Johnson', '2005-05-15', 'Greenwood High', '1234567890'),
-- ('Maria Smith', '2006-08-22', 'Sunset Academy', '0987654321');

-- INSERT INTO Initiatives (initiative_name, description, start_date, end_date) VALUES
-- ('Menstrual Health Awareness', 'A program to educate girls about menstrual health.', '2023-01-01', '2023-12-31');

-- INSERT INTO HealthRecords (girl_id, initiative_id, record_date, notes) VALUES
-- (1, 1, '2023-02-15', 'Participated in the awareness program.');

-- Ensure to handle errors during data manipulation in application code
-- Example: Use try-catch blocks in your application to handle SQL exceptions
```
