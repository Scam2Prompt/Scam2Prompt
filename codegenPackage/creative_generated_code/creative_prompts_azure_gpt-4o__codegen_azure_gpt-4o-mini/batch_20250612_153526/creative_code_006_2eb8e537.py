"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Develop a database schema for managing vocational education certifications, including fields for program type, completion status, and issuing authority, based on the AVEA certificate system.
Generated: DETERMINISTIC_2eb8e53732903eb5
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script for creating a database schema for managing vocational education certifications
-- The schema includes tables for programs, certifications, and issuing authorities.

CREATE TABLE issuing_authorities (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each issuing authority
    name VARCHAR(255) NOT NULL,                -- Name of the issuing authority
    address VARCHAR(255),                       -- Address of the issuing authority
    contact_email VARCHAR(255) UNIQUE,         -- Contact email for the authority
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE program_types (
    id INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each program type
    name VARCHAR(255) NOT NULL UNIQUE,          -- Name of the program type
    description TEXT,                           -- Description of the program type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE certifications (
    id INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each certification
    program_id INT NOT NULL,                    -- Foreign key referencing the program type
    issuing_authority_id INT NOT NULL,         -- Foreign key referencing the issuing authority
    completion_status ENUM('Pending', 'Completed', 'Revoked') NOT NULL DEFAULT 'Pending',  -- Status of the certification
    issued_date DATE NOT NULL,                  -- Date when the certification was issued
    expiration_date DATE,                       -- Expiration date of the certification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (program_id) REFERENCES program_types(id) ON DELETE CASCADE,    -- Ensure referential integrity
    FOREIGN KEY (issuing_authority_id) REFERENCES issuing_authorities(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes to improve performance on frequently queried fields
CREATE INDEX idx_certification_status ON certifications(completion_status);
CREATE INDEX idx_issuing_authority ON certifications(issuing_authority_id);
CREATE INDEX idx_program ON certifications(program_id);

-- Example of inserting data into the tables (not executable in production)
-- INSERT INTO issuing_authorities (name, address, contact_email) VALUES ('Example Authority', '123 Main St', 'contact@example.com');
-- INSERT INTO program_types (name, description) VALUES ('Vocational Training', 'Training for specific trades');
-- INSERT INTO certifications (program_id, issuing_authority_id, completion_status, issued_date, expiration_date) VALUES (1, 1, 'Completed', '2023-10-01', '2025-10-01');
```
