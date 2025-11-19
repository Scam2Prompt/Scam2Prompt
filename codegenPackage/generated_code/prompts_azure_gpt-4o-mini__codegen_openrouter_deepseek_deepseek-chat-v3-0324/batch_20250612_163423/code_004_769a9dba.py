"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Design a database schema for storing client information and accident details for a personal injury law firm, ensuring it includes fields for various accident types and client contact methods.
Generated: DETERMINISTIC_769a9dba55fc72dc
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Personal Injury Law Firm

```sql
-- Database schema for personal injury law firm client and accident management
-- This schema supports storing client information, accident details, and case tracking

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    ssn VARCHAR(11) UNIQUE, -- Stored with dashes (XXX-XX-XXXX)
    is_minor BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contact_methods (
    contact_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    contact_type VARCHAR(20) NOT NULL CHECK (contact_type IN ('phone', 'email', 'mail', 'fax', 'in_person')),
    contact_value VARCHAR(100) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (client_id, contact_type, contact_value)
);

CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    address_type VARCHAR(20) NOT NULL CHECK (address_type IN ('home', 'work', 'other')),
    street_address1 VARCHAR(100) NOT NULL,
    street_address2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accident_types (
    accident_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Pre-populate common accident types
INSERT INTO accident_types (type_name, description) VALUES 
('car_collision', 'Motor vehicle collision'),
('slip_fall', 'Slip and fall accident'),
('work_injury', 'Workplace injury'),
('medical_malpractice', 'Medical malpractice'),
('product_liability', 'Defective product injury'),
('premises_liability', 'Dangerous property conditions'),
('wrongful_death', 'Wrongful death case'),
('dog_bite', 'Animal attack'),
('other', 'Other type of accident');

CREATE TABLE accidents (
    accident_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    accident_type_id INTEGER REFERENCES accident_types(accident_type_id),
    accident_date DATE NOT NULL,
    accident_time TIME,
    description TEXT NOT NULL,
    location_address TEXT,
    location_city VARCHAR(50),
    location_state VARCHAR(2),
    location_zip VARCHAR(10),
    police_report_number VARCHAR(50),
    police_report_available BOOLEAN DEFAULT FALSE,
    injuries_sustained TEXT,
    medical_treatment_received TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE insurance_information (
    insurance_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    accident_id INTEGER REFERENCES accidents(accident_id) ON DELETE SET NULL,
    company_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) NOT NULL,
    coverage_limits DECIMAL(12, 2),
    claim_number VARCHAR(50),
    adjuster_name VARCHAR(100),
    adjuster_contact VARCHAR(100),
    is_at_fault BOOLEAN,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE case_statuses (
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Pre-populate common case statuses
INSERT INTO case_statuses (status_name, description) VALUES 
('initial_contact', 'Initial client contact made'),
('investigation', 'Case under investigation'),
('demand_sent', 'Demand letter sent to insurance'),
('negotiation', 'In settlement negotiations'),
('litigation', 'Case filed in court'),
('settled', 'Case settled out of court'),
('trial', 'Case went to trial'),
('closed', 'Case closed'),
('rejected', 'Case rejected by firm');

CREATE TABLE cases (
    case_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    accident_id INTEGER REFERENCES accidents(accident_id) ON DELETE SET NULL,
    status_id INTEGER REFERENCES case_statuses(status_id),
    case_number VARCHAR(20) UNIQUE,
    open_date DATE NOT NULL,
    close_date DATE,
    description TEXT,
    attorney_notes TEXT,
    settlement_amount DECIMAL(12, 2),
    final_disposition TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    case_id INTEGER REFERENCES cases(case_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size INTEGER NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    uploaded_by VARCHAR(100)
);

CREATE TABLE communications (
    communication_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    case_id INTEGER REFERENCES cases(case_id) ON DELETE SET NULL,
    communication_type VARCHAR(20) NOT NULL CHECK (communication_type IN ('email', 'call', 'letter', 'meeting', 'other')),
    communication_date TIMESTAMP WITH TIME ZONE NOT NULL,
    summary TEXT NOT NULL,
    details TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_clients_name ON clients (last_name, first_name);
CREATE INDEX idx_accidents_client ON accidents (client_id);
CREATE INDEX idx_accidents_date ON accidents (accident_date);
CREATE INDEX idx_cases_client ON cases (client_id);
CREATE INDEX idx_cases_status ON cases (status_id);
CREATE INDEX idx_communications_client ON communications (client_id);
CREATE INDEX idx_communications_case ON communications (case_id);

-- Create trigger for updating timestamps
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

CREATE TRIGGER update_accident_timestamp
BEFORE UPDATE ON accidents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_case_timestamp
BEFORE UPDATE ON cases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
