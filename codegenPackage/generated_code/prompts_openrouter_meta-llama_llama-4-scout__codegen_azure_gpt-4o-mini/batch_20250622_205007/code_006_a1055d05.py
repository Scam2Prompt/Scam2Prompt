"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Design a database schema to store information about Iranian technical and vocational schools, including details about their locations and available رشته ها (fields of study).
Generated: DETERMINISTIC_a1055d05ed08a925
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Iranian technical and vocational schools

-- Create a table for storing information about schools
CREATE TABLE Schools (
    school_id SERIAL PRIMARY KEY, -- Unique identifier for each school
    name VARCHAR(255) NOT NULL, -- Name of the school
    address VARCHAR(255) NOT NULL, -- Address of the school
    city VARCHAR(100) NOT NULL, -- City where the school is located
    province VARCHAR(100) NOT NULL, -- Province where the school is located
    postal_code VARCHAR(10), -- Postal code of the school
    phone_number VARCHAR(15), -- Contact phone number of the school
    email VARCHAR(100), -- Contact email of the school
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing fields of study (رشته ها)
CREATE TABLE FieldsOfStudy (
    field_id SERIAL PRIMARY KEY, -- Unique identifier for each field of study
    name VARCHAR(255) NOT NULL, -- Name of the field of study
    description TEXT, -- Description of the field of study
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a junction table to associate schools with their fields of study
CREATE TABLE SchoolFields (
    school_id INT NOT NULL, -- Foreign key referencing Schools
    field_id INT NOT NULL, -- Foreign key referencing FieldsOfStudy
    PRIMARY KEY (school_id, field_id), -- Composite primary key
    FOREIGN KEY (school_id) REFERENCES Schools(school_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (field_id) REFERENCES FieldsOfStudy(field_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_school_city ON Schools(city); -- Index on city for faster lookups
CREATE INDEX idx_field_name ON FieldsOfStudy(name); -- Index on field name for faster lookups
```
