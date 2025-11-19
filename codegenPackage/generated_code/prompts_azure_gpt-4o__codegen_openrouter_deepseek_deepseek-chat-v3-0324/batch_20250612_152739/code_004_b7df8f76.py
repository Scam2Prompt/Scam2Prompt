"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Create a database schema for tracking roof inspections, storm damage assessments, and insurance claims, based on the services offered by JaraEs Construction LLC.
Generated: DETERMINISTIC_b7df8f7622136ab8
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for JaraEs Construction LLC roof inspection and claims tracking

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insurance providers table
CREATE TABLE insurance_providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    email TEXT,
    claims_department_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Roof types table
CREATE TABLE roof_types (
    roof_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Inspection statuses
CREATE TABLE inspection_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Claim statuses
CREATE TABLE claim_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Inspections table
CREATE TABLE inspections (
    inspection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    inspection_date DATE NOT NULL,
    roof_type_id INTEGER NOT NULL,
    inspector_name TEXT NOT NULL,
    findings TEXT,
    recommended_actions TEXT,
    status_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (roof_type_id) REFERENCES roof_types(roof_type_id),
    FOREIGN KEY (status_id) REFERENCES inspection_statuses(status_id)
);

-- Damage assessments table
CREATE TABLE damage_assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inspection_id INTEGER NOT NULL,
    assessment_date DATE NOT NULL,
    damage_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    estimated_repair_cost DECIMAL(10, 2),
    photos_path TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inspection_id) REFERENCES inspections(inspection_id)
);

-- Insurance claims table
CREATE TABLE insurance_claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    claim_number TEXT NOT NULL,
    claim_date DATE NOT NULL,
    policy_number TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    adjuster_name TEXT,
    adjuster_contact TEXT,
    settlement_amount DECIMAL(10, 2),
    settlement_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (provider_id) REFERENCES insurance_providers(provider_id),
    FOREIGN KEY (status_id) REFERENCES claim_statuses(status_id)
);

-- Claim documents table
CREATE TABLE claim_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (claim_id) REFERENCES insurance_claims(claim_id)
);

-- Repair projects table
CREATE TABLE repair_projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id INTEGER,
    customer_id INTEGER NOT NULL,
    start_date DATE,
    completion_date DATE,
    estimated_cost DECIMAL(10, 2),
    actual_cost DECIMAL(10, 2),
    status TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (claim_id) REFERENCES insurance_claims(claim_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Project materials table
CREATE TABLE project_materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (project_id) REFERENCES repair_projects(project_id)
);

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER update_inspection_timestamp
AFTER UPDATE ON inspections
FOR EACH ROW
BEGIN
    UPDATE inspections SET updated_at = CURRENT_TIMESTAMP WHERE inspection_id = OLD.inspection_id;
END;

CREATE TRIGGER update_claim_timestamp
AFTER UPDATE ON insurance_claims
FOR EACH ROW
BEGIN
    UPDATE insurance_claims SET updated_at = CURRENT_TIMESTAMP WHERE claim_id = OLD.claim_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON repair_projects
FOR EACH ROW
BEGIN
    UPDATE repair_projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

-- Initial data for status tables
INSERT INTO inspection_statuses (name, description) VALUES 
('Scheduled', 'Inspection has been scheduled but not yet performed'),
('Completed', 'Inspection has been completed'),
('Report Generated', 'Inspection report has been generated'),
('Follow-up Needed', 'Additional inspection needed');

INSERT INTO claim_statuses (name, description) VALUES 
('Filed', 'Claim has been filed with insurance company'),
('Under Review', 'Insurance company is reviewing the claim'),
('Approved', 'Claim has been approved by insurance'),
('Denied', 'Claim has been denied by insurance'),
('Paid', 'Claim has been paid by insurance'),
('Closed', 'Claim has been closed');

-- Common roof types
INSERT INTO roof_types (name, description) VALUES 
('Asphalt Shingle', 'Standard asphalt shingle roofing'),
('Metal', 'Metal panel roofing'),
('Tile', 'Clay or concrete tile roofing'),
('Flat', 'Flat or low-slope roofing'),
('Wood Shake', 'Wood shingle or shake roofing'),
('Slate', 'Natural slate roofing');
```
