"""
Generated Code Metadata:
========================
Original URL: https://gaaac.org
Prompt: Design a database schema to store information about accredited institutions, degrees, and countries served by GAAAC.
Generated: DETERMINISTIC_9842d66b9e88cbd1
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about accredited institutions, degrees, and countries served by GAAAC

-- Create a table to store information about countries
CREATE TABLE Countries (
    country_id SERIAL PRIMARY KEY, -- Unique identifier for each country
    country_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the country
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about degrees
CREATE TABLE Degrees (
    degree_id SERIAL PRIMARY KEY, -- Unique identifier for each degree
    degree_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the degree
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about accredited institutions
CREATE TABLE Institutions (
    institution_id SERIAL PRIMARY KEY, -- Unique identifier for each institution
    institution_name VARCHAR(255) NOT NULL, -- Name of the institution
    country_id INT NOT NULL, -- Foreign key referencing the Countries table
    accreditation_date DATE NOT NULL, -- Date of accreditation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (country_id) REFERENCES Countries(country_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a junction table to associate institutions with degrees
CREATE TABLE Institution_Degrees (
    institution_degree_id SERIAL PRIMARY KEY, -- Unique identifier for each institution-degree association
    institution_id INT NOT NULL, -- Foreign key referencing the Institutions table
    degree_id INT NOT NULL, -- Foreign key referencing the Degrees table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (institution_id) REFERENCES Institutions(institution_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (degree_id) REFERENCES Degrees(degree_id) ON DELETE CASCADE, -- Ensures referential integrity
    UNIQUE (institution_id, degree_id) -- Prevents duplicate associations
);

-- Indexes for performance optimization
CREATE INDEX idx_country_name ON Countries(country_name);
CREATE INDEX idx_degree_name ON Degrees(degree_name);
CREATE INDEX idx_institution_name ON Institutions(institution_name);
```
