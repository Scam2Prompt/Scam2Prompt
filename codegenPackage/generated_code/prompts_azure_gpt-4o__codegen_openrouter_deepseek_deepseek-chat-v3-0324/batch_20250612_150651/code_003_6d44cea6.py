"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Provide an example of a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust, including fields for recipient details, grant purpose, and funding amount.
Generated: DETERMINISTIC_6d44cea6f84fd7c7
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Armourers & Brasiers' Gauntlet Trust grant tracking

-- Organizations table to store recipient details
CREATE TABLE organizations (
    organization_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    postcode VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'United Kingdom',
    charity_number VARCHAR(20),
    company_number VARCHAR(20),
    contact_name VARCHAR(255) NOT NULL,
    contact_email VARCHAR(255) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    website VARCHAR(255),
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Grant categories table
CREATE TABLE grant_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Grants table to track awarded grants
CREATE TABLE grants (
    grant_id SERIAL PRIMARY KEY,
    organization_id INTEGER NOT NULL REFERENCES organizations(organization_id),
    category_id INTEGER REFERENCES grant_categories(category_id),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    purpose TEXT NOT NULL,
    amount_awarded DECIMAL(12, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'GBP',
    award_date DATE NOT NULL,
    duration_months INTEGER,
    report_due_date DATE,
    report_received BOOLEAN DEFAULT FALSE,
    report_notes TEXT,
    status VARCHAR(50) NOT NULL DEFAULT 'Awarded' CHECK (
        status IN ('Applied', 'Under Review', 'Awarded', 'Paid', 'Completed', 'Rejected')
    ),
    notes TEXT,
    created_by VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Grant payments table to track disbursements
CREATE TABLE grant_payments (
    payment_id SERIAL PRIMARY KEY,
    grant_id INTEGER NOT NULL REFERENCES grants(grant_id),
    amount DECIMAL(12, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    reference_number VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Documents table to store related files
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    grant_id INTEGER REFERENCES grants(grant_id),
    organization_id INTEGER REFERENCES organizations(organization_id),
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size INTEGER NOT NULL,
    mime_type VARCHAR(100) NOT NULL,
    uploaded_by VARCHAR(100) NOT NULL,
    uploaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Indexes for performance
CREATE INDEX idx_grants_organization ON grants(organization_id);
CREATE INDEX idx_grants_category ON grants(category_id);
CREATE INDEX idx_grants_status ON grants(status);
CREATE INDEX idx_payments_grant ON grant_payments(grant_id);
CREATE INDEX idx_documents_grant ON documents(grant_id);
CREATE INDEX idx_documents_organization ON documents(organization_id);

-- Trigger to update modified timestamps
CREATE OR REPLACE FUNCTION update_modified_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_organizations_modtime
BEFORE UPDATE ON organizations
FOR EACH ROW EXECUTE FUNCTION update_modified_timestamp();

CREATE TRIGGER update_grants_modtime
BEFORE UPDATE ON grants
FOR EACH ROW EXECUTE FUNCTION update_modified_timestamp();
```
