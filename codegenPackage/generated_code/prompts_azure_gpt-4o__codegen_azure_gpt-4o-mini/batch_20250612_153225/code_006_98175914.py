"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Create a database schema for storing polygraph test results, including fields for test type, client details, and examiner credentials, inspired by the services offered by Euro Poligraf Center.
Generated: DETERMINISTIC_981759143af875da
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing polygraph test results

CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    date_of_birth DATE NOT NULL, -- Client's date of birth
    contact_number VARCHAR(15), -- Client's contact number
    email VARCHAR(100) UNIQUE, -- Client's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE Examiners (
    examiner_id SERIAL PRIMARY KEY, -- Unique identifier for each examiner
    first_name VARCHAR(50) NOT NULL, -- Examiner's first name
    last_name VARCHAR(50) NOT NULL, -- Examiner's last name
    certification_number VARCHAR(50) UNIQUE NOT NULL, -- Unique certification number
    contact_number VARCHAR(15), -- Examiner's contact number
    email VARCHAR(100) UNIQUE, -- Examiner's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE TestTypes (
    test_type_id SERIAL PRIMARY KEY, -- Unique identifier for each test type
    test_name VARCHAR(100) NOT NULL, -- Name of the test
    description TEXT, -- Description of the test
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE PolygraphTests (
    test_id SERIAL PRIMARY KEY, -- Unique identifier for each test
    client_id INT NOT NULL, -- Foreign key referencing Clients
    examiner_id INT NOT NULL, -- Foreign key referencing Examiners
    test_type_id INT NOT NULL, -- Foreign key referencing TestTypes
    test_date TIMESTAMP NOT NULL, -- Date and time of the test
    results TEXT, -- Results of the polygraph test
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (examiner_id) REFERENCES Examiners(examiner_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (test_type_id) REFERENCES TestTypes(test_type_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_examiner_email ON Examiners(email);
CREATE INDEX idx_test_date ON PolygraphTests(test_date);
```
