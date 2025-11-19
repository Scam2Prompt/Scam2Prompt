"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azarlegal.com
Prompt: Create a sample database schema for storing client information and case details for a law firm like AZAR & Associates, focusing on corporate and real estate law.
Generated: DETERMINISTIC_e192d70186bb480f
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing client information and case details for a law firm like AZAR & Associates

-- Create the `clients` table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,                 -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,             -- Client's first name
    last_name VARCHAR(50) NOT NULL,              -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,          -- Client's email (must be unique)
    phone_number VARCHAR(15),                    -- Client's phone number
    address TEXT,                                -- Client's physical address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last modification
);

-- Create the `cases` table to store case details
CREATE TABLE cases (
    case_id SERIAL PRIMARY KEY,                  -- Unique identifier for each case
    client_id INT NOT NULL,                      -- Foreign key referencing the `clients` table
    case_type VARCHAR(50) NOT NULL,              -- Type of case (e.g., 'Corporate', 'Real Estate', etc.)
    case_description TEXT NOT NULL,             -- Detailed description of the case
    case_status VARCHAR(30) DEFAULT 'Open',     -- Status of the case ('Open', 'Closed', 'Pending', etc.)
    opened_date DATE NOT NULL,                   -- Date when the case was opened
    closed_date DATE,                            -- Date when the case was closed (nullable if not closed yet)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the case record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last modification
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create the `users` table to store information about law firm employees managing cases
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                  -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,        -- Username for login (must be unique)
    password_hash TEXT NOT NULL,                 -- Hashed password for security
    first_name VARCHAR(50) NOT NULL,             -- User's first name
    last_name VARCHAR(50) NOT NULL,              -- User's last name
    role VARCHAR(30) NOT NULL,                   -- Role of the user (e.g., 'Admin', 'Lawyer', 'Assistant')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last modification
);

-- Create the `case_assignments` table to track case assignments to employees
CREATE TABLE case_assignments (
    assignment_id SERIAL PRIMARY KEY,            -- Unique identifier for each assignment
    case_id INT NOT NULL,                        -- Foreign key referencing the `cases` table
    user_id INT NOT NULL,                        -- Foreign key referencing the `users` table
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the case was assigned
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create indexes to improve query performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_cases_client_id ON cases(client_id);
CREATE INDEX idx_case_assignments_case_id ON case_assignments(case_id);
CREATE INDEX idx_case_assignments_user_id ON case_assignments(user_id);
```
