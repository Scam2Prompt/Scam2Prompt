"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Design a database schema for storing polygraph test results, including fields for test type (e.g., pre-employment, fidelity), client information, and test outcomes."
Generated: DETERMINISTIC_4d08ba7b7d618723
Batch ID: 20250622_210650
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
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone_number VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE TestTypes (
    test_type_id SERIAL PRIMARY KEY, -- Unique identifier for each test type
    test_type_name VARCHAR(50) NOT NULL UNIQUE -- Name of the test type (e.g., pre-employment, fidelity)
);

CREATE TABLE PolygraphTests (
    test_id SERIAL PRIMARY KEY, -- Unique identifier for each test
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    test_type_id INT NOT NULL, -- Foreign key referencing TestTypes table
    test_date TIMESTAMP NOT NULL, -- Date and time when the test was conducted
    outcome VARCHAR(50) NOT NULL, -- Outcome of the test (e.g., passed, failed)
    notes TEXT, -- Additional notes regarding the test
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (test_type_id) REFERENCES TestTypes(test_type_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_id ON PolygraphTests(client_id);
CREATE INDEX idx_test_type_id ON PolygraphTests(test_type_id);
CREATE INDEX idx_test_date ON PolygraphTests(test_date);
```
