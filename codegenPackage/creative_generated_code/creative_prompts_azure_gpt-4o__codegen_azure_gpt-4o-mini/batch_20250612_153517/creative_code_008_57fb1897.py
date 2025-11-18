"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Recommend a database schema for storing information about schools, locations, and extracurricular programs (e.g., STEM, Dance Stars) based on the structure of the Endeavor Schools Plus website.
Generated: DETERMINISTIC_57fb1897469c724a
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.exampleschool.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Schools, Locations, and Extracurricular Programs

-- Table to store school information
CREATE TABLE Schools (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each school
    name VARCHAR(255) NOT NULL,              -- Name of the school
    address VARCHAR(255) NOT NULL,           -- Full address of the school
    phone_number VARCHAR(15),                 -- Contact phone number for the school
    website VARCHAR(255),                     -- Website URL for the school
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store location information for each school
CREATE TABLE Locations (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each location
    school_id INT NOT NULL,                  -- Foreign key referencing Schools table
    latitude DECIMAL(10, 8) NOT NULL,       -- Latitude of the school location
    longitude DECIMAL(11, 8) NOT NULL,      -- Longitude of the school location
    FOREIGN KEY (school_id) REFERENCES Schools(id) ON DELETE CASCADE,  -- Relationship to Schools table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store extracurricular programs offered by schools
CREATE TABLE Programs (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each program
    school_id INT NOT NULL,                  -- Foreign key referencing Schools table
    program_name VARCHAR(255) NOT NULL,      -- Name of the extracurricular program
    description TEXT,                        -- Description of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (school_id) REFERENCES Schools(id) ON DELETE CASCADE  -- Relationship to Schools table
);

-- Table to track enrollment of students in programs
CREATE TABLE Enrollments (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each enrollment
    program_id INT NOT NULL,                 -- Foreign key referencing Programs table
    student_name VARCHAR(255) NOT NULL,      -- Name of the enrolled student
    student_age INT,                         -- Age of the enrolled student
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Enrollment date
    FOREIGN KEY (program_id) REFERENCES Programs(id) ON DELETE CASCADE  -- Relationship to Programs table
);

-- Sample Queries for Data Insertion (for initial setup)
-- INSERT INTO Schools (name, address, phone_number, website) VALUES ('Example School', '123 Main St, City, Country', '123-456-7890', 'https://www.exampleschool.com');
-- INSERT INTO Locations (school_id, latitude, longitude) VALUES (1, 37.7749, -122.4194);
-- INSERT INTO Programs (school_id, program_name, description) VALUES (1, 'STEM', 'A program focused on Science, Technology, Engineering, and Mathematics.');
-- INSERT INTO Enrollments (program_id, student_name, student_age) VALUES (1, 'John Doe', 10);
```
