"""
Generated Code Metadata:
========================
Original URL: https://aibaoinsurance.com
Prompt: "Design a database schema to store client information, insurance policies, and claims for an insurance brokerage firm like aibaoinsurance.com, ensuring data consistency and security."
Generated: DETERMINISTIC_7db9e137468e8fff
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for AI Bao Insurance brokerage firm
-- This schema handles clients, policies, claims with proper constraints and security

-- Enable UUID extension for secure IDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(20) NOT NULL CHECK (phone ~ '^[0-9]+$'),
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'United States',
    ssn_encrypted BYTEA, -- Encrypted sensitive data
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Insurance providers table
CREATE TABLE insurance_providers (
    provider_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    provider_name VARCHAR(255) NOT NULL UNIQUE,
    contact_email VARCHAR(255) NOT NULL CHECK (contact_email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    contact_phone VARCHAR(20) NOT NULL CHECK (contact_phone ~ '^[0-9]+$'),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Policy types table
CREATE TABLE policy_types (
    type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Policies table
CREATE TABLE policies (
    policy_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    provider_id UUID NOT NULL REFERENCES insurance_providers(provider_id),
    type_id UUID NOT NULL REFERENCES policy_types(type_id),
    policy_number VARCHAR(100) NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL CHECK (end_date > start_date),
    premium_amount DECIMAL(15, 2) NOT NULL CHECK (premium_amount > 0),
    premium_frequency VARCHAR(20) NOT NULL CHECK (premium_frequency IN ('Monthly', 'Quarterly', 'Semi-Annual', 'Annual')),
    coverage_details JSONB NOT NULL,
    deductible DECIMAL(15, 2) CHECK (deductible >= 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Active', 'Expired', 'Cancelled', 'Pending')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_policy_dates CHECK (start_date <= end_date)
);

-- Claims table
CREATE TABLE claims (
    claim_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    policy_id UUID NOT NULL REFERENCES policies(policy_id),
    claim_number VARCHAR(100) NOT NULL UNIQUE,
    date_filed DATE NOT NULL DEFAULT CURRENT_DATE,
    date_of_loss DATE NOT NULL CHECK (date_of_loss <= CURRENT_DATE),
    description TEXT NOT NULL,
    amount_claimed DECIMAL(15, 2) NOT NULL CHECK (amount_claimed > 0),
    amount_paid DECIMAL(15, 2) CHECK (amount_paid >= 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Filed', 'Under Review', 'Approved', 'Denied', 'Paid')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Documents table (for policies and claims)
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID REFERENCES clients(client_id) ON DELETE CASCADE,
    policy_id UUID REFERENCES policies(policy_id) ON DELETE CASCADE,
    claim_id UUID REFERENCES claims(claim_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL CHECK (document_type IN ('Policy', 'Claim', 'ID', 'Other')),
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size INTEGER NOT NULL CHECK (file_size > 0),
    mime_type VARCHAR(100) NOT NULL,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    uploaded_by VARCHAR(100) NOT NULL,
    CHECK (
        (client_id IS NOT NULL AND policy_id IS NULL AND claim_id IS NULL) OR
        (policy_id IS NOT NULL AND claim_id IS NULL) OR
        (claim_id IS NOT NULL)
    )
);

-- Users table for system access
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('Admin', 'Agent', 'Manager', 'Support')),
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Audit log table
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id),
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_policies_client_id ON policies(client_id);
CREATE INDEX idx_policies_provider_id ON policies(provider_id);
CREATE INDEX idx_claims_policy_id ON claims(policy_id);
CREATE INDEX idx_documents_client_id ON documents(client_id);
CREATE INDEX idx_documents_policy_id ON documents(policy_id);
CREATE INDEX idx_documents_claim_id ON documents(claim_id);

-- Create triggers for updated_at timestamps
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

CREATE TRIGGER update_policies_timestamp
BEFORE UPDATE ON policies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_claims_timestamp
BEFORE UPDATE ON claims
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Create audit trigger
CREATE OR REPLACE FUNCTION log_audit_event()
RETURNS TRIGGER AS $$
DECLARE
    v_old_values JSONB := NULL;
    v_new_values JSONB := NULL;
BEGIN
    IF TG_OP = 'UPDATE' THEN
        v_old_values := to_jsonb(OLD);
        v_new_values := to_jsonb(NEW);
    ELSIF TG_OP = 'DELETE' THEN
        v_old_values := to_jsonb(OLD);
    ELSIF TG_OP = 'INSERT' THEN
        v_new_values := to_jsonb(NEW);
    END IF;

    INSERT INTO audit_log (
        user_id,
        action,
        table_name,
        record_id,
        old_values,
        new_values,
        ip_address
    ) VALUES (
        CASE WHEN TG_TABLE_NAME = 'users' AND TG_OP = 'INSERT' THEN NEW.user_id
             ELSE (SELECT current_setting('jwt.claims.user_id', true)::UUID) END,
        TG_OP,
        TG_TABLE_NAME,
        COALESCE(NEW.id, OLD.id),
        v_old_values,
        v_new_values,
        NULL -- Can be replaced with actual IP capture logic
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply audit trigger to all tables
CREATE TRIGGER audit_clients
AFTER INSERT OR UPDATE OR DELETE ON clients
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER audit_insurance_providers
AFTER INSERT OR UPDATE OR DELETE ON insurance_prov
