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
-- Database schema for polygraph test results
-- Inspired by Euro Poligraf Center services

CREATE TABLE examiners (
    examiner_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    license_expiry DATE NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    contact_email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (contact_email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
    contact_phone VARCHAR(20) NOT NULL,
    contact_email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (contact_email IS NULL OR contact_email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

CREATE TABLE test_types (
    test_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    standard_duration_minutes INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test_sessions (
    session_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE RESTRICT,
    examiner_id INTEGER REFERENCES examiners(examiner_id) ON DELETE RESTRICT,
    test_type_id INTEGER REFERENCES test_types(test_type_id) ON DELETE RESTRICT,
    session_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(100) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test_results (
    result_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES test_sessions(session_id) ON DELETE CASCADE,
    conclusion TEXT NOT NULL,
    confidence_level VARCHAR(50) CHECK (confidence_level IN ('Low', 'Medium', 'High', 'Very High')),
    detailed_report TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE physiological_measurements (
    measurement_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES test_sessions(session_id) ON DELETE CASCADE,
    measurement_type VARCHAR(50) NOT NULL,
    value NUMERIC NOT NULL,
    unit VARCHAR(20) NOT NULL,
    recorded_at TIMESTAMP WITH TIME ZONE NOT NULL,
    notes TEXT
);

CREATE TABLE test_questions (
    question_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES test_sessions(session_id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) CHECK (question_type IN ('Relevant', 'Control', 'Neutral')),
    response_analysis TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create triggers for automatic updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_examiner_timestamp
BEFORE UPDATE ON examiners
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_test_session_timestamp
BEFORE UPDATE ON test_sessions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_test_result_timestamp
BEFORE UPDATE ON test_results
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
