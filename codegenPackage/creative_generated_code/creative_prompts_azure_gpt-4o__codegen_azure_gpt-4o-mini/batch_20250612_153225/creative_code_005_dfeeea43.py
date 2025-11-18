"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Create a database schema for storing client health data, including lab results, dietary preferences, and consultation history, inspired by the personalized approach described on Olga Stepanova's website.
Generated: DETERMINISTIC_dfeeea4391ce6451
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing client health data

-- Drop existing tables if they exist to prevent conflicts
DROP TABLE IF EXISTS ConsultationHistory;
DROP TABLE IF EXISTS DietaryPreferences;
DROP TABLE IF EXISTS LabResults;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,           -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,       -- Client's first name
    last_name VARCHAR(50) NOT NULL,        -- Client's last name
    date_of_birth DATE NOT NULL,            -- Client's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,     -- Client's email address
    phone VARCHAR(15),                      -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store lab results related to clients
CREATE TABLE LabResults (
    lab_result_id SERIAL PRIMARY KEY,       -- Unique identifier for each lab result
    client_id INT REFERENCES Clients(client_id) ON DELETE CASCADE, -- Foreign key reference
    test_name VARCHAR(100) NOT NULL,        -- Name of the lab test
    test_date DATE NOT NULL,                 -- Date the test was conducted
    result_value VARCHAR(50),                -- Result value of the test
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store dietary preferences of clients
CREATE TABLE DietaryPreferences (
    preference_id SERIAL PRIMARY KEY,       -- Unique identifier for each dietary preference
    client_id INT REFERENCES Clients(client_id) ON DELETE CASCADE, -- Foreign key reference
    preference_description VARCHAR(255) NOT NULL, -- Description of dietary preference
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store consultation history of clients
CREATE TABLE ConsultationHistory (
    consultation_id SERIAL PRIMARY KEY,     -- Unique identifier for each consultation
    client_id INT REFERENCES Clients(client_id) ON DELETE CASCADE, -- Foreign key reference
    consultation_date DATE NOT NULL,        -- Date of the consultation
    notes TEXT,                             -- Notes taken during the consultation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);
```
