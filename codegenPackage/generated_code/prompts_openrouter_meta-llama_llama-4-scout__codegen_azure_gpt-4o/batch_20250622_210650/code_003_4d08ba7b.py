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

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE,                        -- Client's date of birth
    Email VARCHAR(100),                      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store polygraph test types
CREATE TABLE TestTypes (
    TestTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each test type
    TestTypeName VARCHAR(50) NOT NULL,         -- Name of the test type (e.g., pre-employment, fidelity)
    Description TEXT,                          -- Description of the test type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store polygraph test results
CREATE TABLE PolygraphTests (
    TestID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each test
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    TestTypeID INT NOT NULL,                  -- Foreign key referencing TestTypes table
    TestDate DATE NOT NULL,                   -- Date the test was conducted
    Outcome VARCHAR(50) NOT NULL,             -- Outcome of the test (e.g., passed, failed, inconclusive)
    Notes TEXT,                               -- Additional notes about the test
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (TestTypeID) REFERENCES TestTypes(TestTypeID) ON DELETE CASCADE -- Cascade delete for test type
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_id ON PolygraphTests(ClientID); -- Index for ClientID in PolygraphTests
CREATE INDEX idx_test_type_id ON PolygraphTests(TestTypeID); -- Index for TestTypeID in PolygraphTests
CREATE INDEX idx_test_date ON PolygraphTests(TestDate); -- Index for TestDate in PolygraphTests
```
