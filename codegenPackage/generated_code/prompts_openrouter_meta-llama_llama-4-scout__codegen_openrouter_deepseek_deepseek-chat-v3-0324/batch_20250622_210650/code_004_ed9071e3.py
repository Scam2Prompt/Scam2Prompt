"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about a lawyer's cases, including client data, case types (e.g., criminal, civil), and court information, similar to the experience section on fachriahyani.com.
Generated: DETERMINISTIC_ed9071e3164a372e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for lawyer case management system

-- Clients table
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Case types table
CREATE TABLE case_types (
    case_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Courts table
CREATE TABLE courts (
    court_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    jurisdiction VARCHAR(100),
    phone VARCHAR(20)
);

-- Cases table
CREATE TABLE cases (
    case_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    case_type_id INTEGER NOT NULL REFERENCES case_types(case_type_id),
    court_id INTEGER REFERENCES courts(court_id),
    case_number VARCHAR(100),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Open', 'Closed', 'Pending', 'Dismissed')),
    open_date DATE NOT NULL,
    close_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Case documents table
CREATE TABLE case_documents (
    document_id SERIAL PRIMARY KEY,
    case_id INTEGER NOT NULL REFERENCES cases(case_id) ON DELETE CASCADE,
    document_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    document_type VARCHAR(100),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Case notes table
CREATE TABLE case_notes (
    note_id SERIAL PRIMARY KEY,
    case_id INTEGER NOT NULL REFERENCES cases(case_id) ON DELETE CASCADE,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    created_by VARCHAR(100) NOT NULL
);

-- Case hearings table
CREATE TABLE case_hearings (
    hearing_id SERIAL PRIMARY KEY,
    case_id INTEGER NOT NULL REFERENCES cases(case_id) ON DELETE CASCADE,
    hearing_date TIMESTAMP NOT NULL,
    hearing_type VARCHAR(100),
    location VARCHAR(255),
    outcome TEXT,
    notes TEXT
);

-- Case expenses table
CREATE TABLE case_expenses (
    expense_id SERIAL PRIMARY KEY,
    case_id INTEGER NOT NULL REFERENCES cases(case_id) ON DELETE CASCADE,
    expense_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100)
);

-- Indexes for performance
CREATE INDEX idx_cases_client_id ON cases(client_id);
CREATE INDEX idx_cases_case_type_id ON cases(case_type_id);
CREATE INDEX idx_cases_court_id ON cases(court_id);
CREATE INDEX idx_case_documents_case_id ON case_documents(case_id);
CREATE INDEX idx_case_notes_case_id ON case_notes(case_id);
CREATE INDEX idx_case_hearings_case_id ON case_hearings(case_id);
CREATE INDEX idx_case_expenses_case_id ON case_expenses(case_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_case_timestamp
BEFORE UPDATE ON cases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
