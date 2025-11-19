"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Design a database schema for managing high-quality legal leads, incorporating the specific types of cases highlighted on ClaimLink, such as truck and motorcycle accidents.
Generated: DETERMINISTIC_38236c49d08ebb89
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Legal Leads Database Schema

```sql
-- Database schema for managing high-quality legal leads
-- Supports case types like truck accidents, motorcycle accidents, and other personal injury claims

CREATE TABLE leads (
    lead_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'new' CHECK (status IN ('new', 'contacted', 'qualified', 'converted', 'rejected')),
    source VARCHAR(50),
    is_high_priority BOOLEAN DEFAULT FALSE,
    notes TEXT
);

CREATE TABLE case_types (
    case_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Pre-populate common case types
INSERT INTO case_types (name, description) VALUES
    ('Truck Accident', 'Accidents involving commercial trucks'),
    ('Motorcycle Accident', 'Accidents involving motorcycles'),
    ('Car Accident', 'Standard automobile accidents'),
    ('Slip and Fall', 'Premises liability cases'),
    ('Medical Malpractice', 'Negligence by healthcare professionals'),
    ('Workplace Injury', 'Workers compensation claims');

CREATE TABLE lead_cases (
    lead_case_id SERIAL PRIMARY KEY,
    lead_id INTEGER REFERENCES leads(lead_id) ON DELETE CASCADE,
    case_type_id INTEGER REFERENCES case_types(case_type_id),
    incident_date DATE,
    incident_location TEXT,
    description TEXT,
    injuries TEXT,
    estimated_value DECIMAL(12, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_lead_case_type UNIQUE (lead_id, case_type_id)
);

CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    lead_id INTEGER REFERENCES leads(lead_id) ON DELETE CASCADE,
    lead_case_id INTEGER REFERENCES lead_cases(lead_case_id) ON DELETE SET NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_type VARCHAR(50),
    file_size INTEGER,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

CREATE TABLE communications (
    communication_id SERIAL PRIMARY KEY,
    lead_id INTEGER REFERENCES leads(lead_id) ON DELETE CASCADE,
    communication_type VARCHAR(20) NOT NULL CHECK (communication_type IN ('call', 'email', 'sms', 'meeting', 'letter')),
    direction VARCHAR(10) NOT NULL CHECK (direction IN ('inbound', 'outbound')),
    subject VARCHAR(255),
    content TEXT,
    occurred_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER, -- Would reference a users table in a complete system
    is_followup_required BOOLEAN DEFAULT FALSE,
    followup_date TIMESTAMP WITH TIME ZONE
);

CREATE TABLE attorneys (
    attorney_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    specialization TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lead_assignments (
    assignment_id SERIAL PRIMARY KEY,
    lead_id INTEGER REFERENCES leads(lead_id) ON DELETE CASCADE,
    attorney_id INTEGER REFERENCES attorneys(attorney_id) ON DELETE SET NULL,
    assigned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    assigned_by INTEGER, -- Would reference a users table in a complete system
    notes TEXT
);

-- Indexes for performance
CREATE INDEX idx_leads_status ON leads(status);
CREATE INDEX idx_leads_priority ON leads(is_high_priority);
CREATE INDEX idx_lead_cases_type ON lead_cases(case_type_id);
CREATE INDEX idx_lead_cases_lead ON lead_cases(lead_id);
CREATE INDEX idx_communications_lead ON communications(lead_id);
CREATE INDEX idx_communications_date ON communications(occurred_at);
CREATE INDEX idx_lead_assignments_attorney ON lead_assignments(attorney_id);

-- Trigger to update the updated_at timestamp on lead updates
CREATE OR REPLACE FUNCTION update_lead_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_lead_timestamp
BEFORE UPDATE ON leads
FOR EACH ROW
EXECUTE FUNCTION update_lead_timestamp();
```
