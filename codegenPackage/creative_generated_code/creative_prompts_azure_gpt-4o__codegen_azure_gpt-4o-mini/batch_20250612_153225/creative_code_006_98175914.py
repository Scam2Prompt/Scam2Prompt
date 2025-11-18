"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Create a database schema for storing polygraph test results, including fields for test type, client details, and examiner credentials, inspired by the services offered by Euro Poligraf Center.
Generated: DETERMINISTIC_981759143af875da
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for storing polygraph test results

-- Drop the tables if they already exist to avoid conflicts during creation
DROP TABLE IF EXISTS examiners;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS test_types;
DROP TABLE IF EXISTS test_results;

-- Table for storing examiner credentials
CREATE TABLE examiners (
    examiner_id SERIAL PRIMARY KEY,  -- Unique identifier for each examiner
    first_name VARCHAR(50) NOT NULL, -- Examiner's first name
    last_name VARCHAR(50) NOT NULL,  -- Examiner's last name
    license_number VARCHAR(50) UNIQUE NOT NULL, -- Unique license number for the examiner
    credentials TEXT,                 -- Additional credentials and qualifications
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Table for storing client details
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,     -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,  -- Client's first name
    last_name VARCHAR(50) NOT NULL,   -- Client's last name
    date_of_birth DATE NOT NULL,       -- Client's date of birth
    contact_number VARCHAR(20),        -- Client's contact number
    email VARCHAR(100) UNIQUE,         -- Client's email address
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Table for storing different types of polygraph tests
CREATE TABLE test_types (
    test_type_id SERIAL PRIMARY KEY,  -- Unique identifier for each test type
    test_name VARCHAR(100) NOT NULL,   -- Name of the test (e.g., "Pre-employment", "Criminal Investigation")
    description TEXT,                   -- Description of the test
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Table for storing the results of polygraph tests
CREATE TABLE test_results (
    test_result_id SERIAL PRIMARY KEY, -- Unique identifier for each test result
    client_id INT NOT NULL,             -- Foreign key referencing clients
    examiner_id INT NOT NULL,           -- Foreign key referencing examiners
    test_type_id INT NOT NULL,          -- Foreign key referencing test types
    test_date TIMESTAMP NOT NULL,       -- Date and time when the test was conducted
    result VARCHAR(50) NOT NULL,        -- Result of the test (e.g., "Passed", "Failed")
    notes TEXT,                         -- Additional notes from the examiner
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT NOW(),  -- Timestamp of the last update
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CONSTRAINT fk_examiner FOREIGN KEY (examiner_id) REFERENCES examiners(examiner_id) ON DELETE CASCADE,
    CONSTRAINT fk_test_type FOREIGN KEY (test_type_id) REFERENCES test_types(test_type_id) ON DELETE CASCADE
);

-- Indexes to improve query performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_test_results_test_date ON test_results(test_date);
```
