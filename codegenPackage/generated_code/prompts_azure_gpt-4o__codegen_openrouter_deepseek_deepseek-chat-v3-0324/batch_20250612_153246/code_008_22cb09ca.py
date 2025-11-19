"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Create a database schema for managing client projects in the healthcare renovation sector, including fields for design specifications, legal compliance, and turnkey delivery, inspired by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_22cb09ca0a81efb6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for healthcare renovation project management
-- Inspired by Pahubel Ibérica S.L.

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2),
    status VARCHAR(20) CHECK (status IN ('planning', 'active', 'on_hold', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE design_specifications (
    specification_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    floor_plans BYTEA,
    materials_list TEXT,
    equipment_specs TEXT,
    special_requirements TEXT,
    approval_status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE legal_compliance (
    compliance_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    building_permit BOOLEAN DEFAULT FALSE,
    healthcare_licenses TEXT,
    safety_certifications TEXT,
    inspections_passed TEXT,
    compliance_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE turnkey_delivery (
    delivery_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    handover_date DATE,
    warranty_period_months INTEGER,
    client_signoff BOOLEAN DEFAULT FALSE,
    final_payment_received BOOLEAN DEFAULT FALSE,
    delivery_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_team (
    team_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Triggers for automatic timestamp updates
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_design_specifications_timestamp
BEFORE UPDATE ON design_specifications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_legal_compliance_timestamp
BEFORE UPDATE ON legal_compliance
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_turnkey_delivery_timestamp
BEFORE UPDATE ON turnkey_delivery
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_team_timestamp
BEFORE UPDATE ON project_team
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
