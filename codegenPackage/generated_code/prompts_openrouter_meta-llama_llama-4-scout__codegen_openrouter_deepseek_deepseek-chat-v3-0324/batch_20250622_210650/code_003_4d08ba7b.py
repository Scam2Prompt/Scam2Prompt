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
-- Polygraph Test Results Database Schema

-- Clients Table: Stores information about individuals taking polygraph tests
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(20),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    phone_number VARCHAR(30),
    email VARCHAR(255),
    ssn_or_id VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Examiners Table: Stores information about polygraph examiners
CREATE TABLE examiners (
    examiner_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    license_number VARCHAR(50),
    certification VARCHAR(100),
    contact_number VARCHAR(30),
    email VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Test Types Table: Stores different types of polygraph tests
CREATE TABLE test_types (
    test_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    standard_duration_minutes INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Test Sessions Table: Stores information about each polygraph test session
CREATE TABLE test_sessions (
    session_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    examiner_id INTEGER REFERENCES examiners(examiner_id) ON DELETE SET NULL,
    test_type_id INTEGER REFERENCES test_types(test_type_id) ON DELETE SET NULL,
    session_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(255),
    purpose TEXT,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Test Results Table: Stores the outcomes of polygraph tests
CREATE TABLE test_results (
    result_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES test_sessions(session_id) ON DELETE CASCADE,
    overall_result VARCHAR(50) NOT NULL CHECK (overall_result IN ('Deceptive', 'Non-Deceptive', 'Inconclusive', 'No Opinion')),
    confidence_level VARCHAR(50),
    physiological_data JSONB,
    examiner_notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Questions Table: Stores specific questions asked during polygraph tests
CREATE TABLE questions (
    question_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES test_sessions(session_id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) CHECK (question_type IN ('Relevant', 'Control', 'Irrelevant')),
    response_result VARCHAR(50) CHECK (response_result IN ('Deceptive', 'Non-Deceptive', 'Inconclusive')),
    physiological_data JSONB,
    examiner_notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance optimization
CREATE INDEX idx_clients_name ON clients(last_name, first_name);
CREATE INDEX idx_test_sessions_date ON test_sessions(session_date);
CREATE INDEX idx_test_sessions_client ON test_sessions(client_id);
CREATE INDEX idx_test_results_session ON test_results(session_id);
CREATE INDEX idx_questions_session ON questions(session_id);

-- Insert common test types
INSERT INTO test_types (name, description, standard_duration_minutes) VALUES
    ('Pre-Employment', 'Standard screening for employment purposes', 90),
    ('Fidelity', 'Infidelity or relationship trust issues', 120),
    ('Specific Issue', 'Investigation of a specific incident', 90),
    ('Periodic', 'Regular screening for security clearance', 60),
    ('Post-Conviction', 'Post-conviction sex offender testing', 120);
```
