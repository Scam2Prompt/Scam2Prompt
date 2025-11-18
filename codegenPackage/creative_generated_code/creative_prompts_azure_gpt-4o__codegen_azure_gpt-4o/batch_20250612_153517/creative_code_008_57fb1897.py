"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Recommend a database schema for storing information about schools, locations, and extracurricular programs (e.g., STEM, Dance Stars) based on the structure of the Endeavor Schools Plus website.
Generated: DETERMINISTIC_57fb1897469c724a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Schools, Locations, and Extracurricular Programs

-- Table: schools
-- This table stores information about schools.
CREATE TABLE schools (
    school_id SERIAL PRIMARY KEY, -- Unique identifier for each school
    name VARCHAR(255) NOT NULL,  -- Name of the school
    description TEXT,            -- Description of the school
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: locations
-- This table stores information about school locations.
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY, -- Unique identifier for each location
    school_id INT NOT NULL,         -- Foreign key referencing the school
    address VARCHAR(255) NOT NULL,  -- Street address of the location
    city VARCHAR(100) NOT NULL,     -- City where the school location is based
    state VARCHAR(100) NOT NULL,    -- State where the school location is based
    zip_code VARCHAR(15) NOT NULL,  -- Zip code for the location
    phone_number VARCHAR(20),       -- Contact phone number for the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT fk_school FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Index to improve search performance for locations based on city and state
CREATE INDEX idx_city_state ON locations(city, state);

-- Table: programs
-- This table stores information about extracurricular programs.
CREATE TABLE programs (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    name VARCHAR(255) NOT NULL,   -- Name of the program (e.g., STEM, Dance Stars)
    description TEXT,             -- Description of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: school_programs
-- This table represents the many-to-many relationship between schools and programs.
CREATE TABLE school_programs (
    school_id INT NOT NULL,       -- Foreign key referencing schools
    program_id INT NOT NULL,      -- Foreign key referencing programs
    PRIMARY KEY (school_id, program_id), -- Composite primary key
    CONSTRAINT fk_school_programs_school FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE, -- Ensures data integrity
    CONSTRAINT fk_school_programs_program FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Index to improve search performance for associations between schools and programs
CREATE INDEX idx_school_programs ON school_programs(school_id, program_id);

-- Sample error handling for creating the schema
DO
$$
BEGIN
    -- If any step fails, roll back the transaction
    BEGIN
        -- Create tables
        -- Raise an exception if something goes wrong
    EXCEPTION WHEN others THEN
        RAISE NOTICE 'Error while creating schema: %', SQLERRM;
        ROLLBACK;
    END;
END;
$$;
```
