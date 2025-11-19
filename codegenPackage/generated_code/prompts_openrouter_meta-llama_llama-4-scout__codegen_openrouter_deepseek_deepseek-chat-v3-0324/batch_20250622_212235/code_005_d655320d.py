"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Design a database schema to store information about GIAC1's members, financing applications, and reimbursement records, ensuring data integrity and scalability.
Generated: DETERMINISTIC_d655320ded7021d8
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for GIAC1 member management system

-- Members table to store member information
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (membership_status IN ('active', 'inactive', 'suspended', 'terminated')),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Financing applications table
CREATE TABLE financing_applications (
    application_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    application_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    purpose TEXT NOT NULL,
    amount_requested DECIMAL(15, 2) NOT NULL CHECK (amount_requested > 0),
    amount_approved DECIMAL(15, 2),
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'processing', 'completed')),
    approval_date TIMESTAMP,
    approved_by INTEGER REFERENCES members(member_id),
    notes TEXT,
    terms TEXT,
    repayment_period_months INTEGER CHECK (repayment_period_months > 0),
    interest_rate DECIMAL(5, 2) CHECK (interest_rate >= 0),
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Reimbursement records table
CREATE TABLE reimbursement_records (
    reimbursement_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    application_id INTEGER REFERENCES financing_applications(application_id),
    request_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    purpose TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'paid')),
    approval_date TIMESTAMP,
    approved_by INTEGER REFERENCES members(member_id),
    payment_date TIMESTAMP,
    payment_method VARCHAR(50),
    payment_reference VARCHAR(100),
    notes TEXT,
    supporting_documents JSONB,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Payment history table
CREATE TABLE payment_history (
    payment_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    application_id INTEGER REFERENCES financing_applications(application_id),
    reimbursement_id INTEGER REFERENCES reimbursement_records(reimbursement_id),
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    payment_type VARCHAR(20) NOT NULL CHECK (payment_type IN ('repayment', 'reimbursement', 'membership_fee', 'other')),
    payment_method VARCHAR(50) NOT NULL,
    reference_number VARCHAR(100),
    status VARCHAR(20) NOT NULL DEFAULT 'completed' CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    notes TEXT,
    processed_by INTEGER REFERENCES members(member_id)
);

-- Audit log table for tracking changes
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    table_name VARCHAR(50) NOT NULL,
    record_id INTEGER NOT NULL,
    action VARCHAR(10) NOT NULL CHECK (action IN ('INSERT', 'UPDATE', 'DELETE')),
    old_values JSONB,
    new_values JSONB,
    changed_by INTEGER REFERENCES members(member_id),
    change_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_members_status ON members(membership_status);
CREATE INDEX idx_applications_member ON financing_applications(member_id);
CREATE INDEX idx_applications_status ON financing_applications(status);
CREATE INDEX idx_reimbursements_member ON reimbursement_records(member_id);
CREATE INDEX idx_reimbursements_status ON reimbursement_records(status);
CREATE INDEX idx_payments_member ON payment_history(member_id);
CREATE INDEX idx_payments_date ON payment_history(payment_date);

-- Function to update last_updated timestamp
CREATE OR REPLACE FUNCTION update_last_updated()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_updated = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic last_updated
CREATE TRIGGER members_last_updated
BEFORE UPDATE ON members
FOR EACH ROW EXECUTE FUNCTION update_last_updated();

CREATE TRIGGER applications_last_updated
BEFORE UPDATE ON financing_applications
FOR EACH ROW EXECUTE FUNCTION update_last_updated();

CREATE TRIGGER reimbursements_last_updated
BEFORE UPDATE ON reimbursement_records
FOR EACH ROW EXECUTE FUNCTION update_last_updated();
```
