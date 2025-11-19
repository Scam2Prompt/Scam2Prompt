"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: "Design a database schema to store client information, financial records, and company registration details for a fiduciary services provider in Switzerland, ensuring data security and compliance with local regulations."
Generated: DETERMINISTIC_b106015698b24ef7
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Swiss fiduciary services provider
-- Compliant with Swiss data protection laws and financial regulations

-- Enable encryption extension for sensitive data
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Clients table (natural persons)
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    marital_status VARCHAR(50),
    tax_number VARCHAR(50),
    ahv_number VARCHAR(50) NOT NULL, -- Swiss social security number
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    address_street VARCHAR(255) NOT NULL,
    address_postal_code VARCHAR(20) NOT NULL,
    address_city VARCHAR(100) NOT NULL,
    address_country VARCHAR(100) NOT NULL DEFAULT 'Switzerland',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Legal entities table (companies)
CREATE TABLE legal_entities (
    entity_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    legal_name VARCHAR(255) NOT NULL,
    legal_form VARCHAR(100) NOT NULL, -- AG, GmbH, etc.
    commercial_register_number VARCHAR(50) NOT NULL, -- Swiss UID/CH number
    vat_number VARCHAR(50),
    establishment_date DATE NOT NULL,
    dissolution_date DATE,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    address_street VARCHAR(255) NOT NULL,
    address_postal_code VARCHAR(20) NOT NULL,
    address_city VARCHAR(100) NOT NULL,
    address_country VARCHAR(100) NOT NULL DEFAULT 'Switzerland',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    CONSTRAINT valid_entity_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Client-entity relationship table
CREATE TABLE client_entity_relationships (
    relationship_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    entity_id UUID NOT NULL REFERENCES legal_entities(entity_id) ON DELETE CASCADE,
    relationship_type VARCHAR(100) NOT NULL, -- shareholder, director, beneficiary, etc.
    share_percentage DECIMAL(5,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(client_id, entity_id, relationship_type)
);

-- Financial accounts table
CREATE TABLE financial_accounts (
    account_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_number VARCHAR(50) NOT NULL UNIQUE,
    account_name VARCHAR(255) NOT NULL,
    account_type VARCHAR(100) NOT NULL, -- bank, investment, crypto, etc.
    currency VARCHAR(3) NOT NULL DEFAULT 'CHF',
    opening_date DATE NOT NULL,
    closing_date DATE,
    current_balance DECIMAL(15,2) NOT NULL DEFAULT 0,
    owner_type VARCHAR(20) NOT NULL, -- 'client' or 'entity'
    owner_id UUID NOT NULL, -- references either client_id or entity_id
    bank_name VARCHAR(255),
    bank_bic VARCHAR(20),
    bank_iban VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT
);

-- Financial transactions table
CREATE TABLE financial_transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES financial_accounts(account_id) ON DELETE CASCADE,
    transaction_date DATE NOT NULL,
    value_date DATE NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'CHF',
    transaction_type VARCHAR(100) NOT NULL, -- deposit, withdrawal, transfer, etc.
    counterparty_name VARCHAR(255),
    counterparty_account VARCHAR(255),
    reference VARCHAR(255),
    category VARCHAR(100),
    status VARCHAR(50) DEFAULT 'completed',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Documents table (for KYC and compliance)
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_type VARCHAR(20) NOT NULL, -- 'client' or 'entity'
    owner_id UUID NOT NULL, -- references either client_id or entity_id
    document_type VARCHAR(100) NOT NULL, -- passport, articles, contract, etc.
    document_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_hash TEXT NOT NULL, -- for integrity verification
    issue_date DATE,
    expiry_date DATE,
    is_verified BOOLEAN DEFAULT FALSE,
    verified_by UUID REFERENCES clients(client_id),
    verification_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Compliance records table
CREATE TABLE compliance_records (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_type VARCHAR(20) NOT NULL, -- 'client' or 'entity'
    owner_id UUID NOT NULL, -- references either client_id or entity_id
    record_type VARCHAR(100) NOT NULL, -- KYC, AML, FATCA, etc.
    status VARCHAR(50) NOT NULL,
    due_date DATE,
    completion_date DATE,
    reviewed_by UUID REFERENCES clients(client_id),
    review_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Audit log table for data protection compliance
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES clients(client_id),
    action VARCHAR(100) NOT NULL,
    table_name VARCHAR(100) NOT NULL,
    record_id UUID NOT NULL,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_clients_last_name ON clients(last_name);
CREATE INDEX idx_legal_entities_name ON legal_entities(legal_name);
CREATE INDEX idx_financial_accounts_owner ON financial_accounts(owner_type, owner_id);
CREATE INDEX idx_financial_transactions_account ON financial_transactions(account_id);
CREATE INDEX idx_financial_transactions_date ON financial_transactions(transaction_date);
CREATE INDEX idx_documents_owner ON documents(owner_type, owner_id);
CREATE INDEX idx_compliance_records_owner ON compliance_records(owner_type, owner_id);

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

CREATE TRIGGER update_legal_entities_timestamp
BEFORE UPDATE ON legal_entities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_client_entity_relationships_timestamp
BEFORE UPDATE ON client_entity_relationships
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_financial_accounts_timestamp
BEFORE UPDATE ON financial_accounts
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_financial_transactions_timestamp
BEFORE UPDATE ON financial_transactions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_documents_timestamp
BEFORE UPDATE ON documents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_compliance_records_timestamp
BEFORE UPDATE ON compliance_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Create view for client financial overview
CREATE VIEW client_financial_overview AS
SELECT 
    c.client_id,
    c.first_name,
    c.last_name,
    COUNT(DISTINCT fa.account_id) AS account_count,
    SUM(CASE WHEN fa.is_active THEN fa.current_balance ELSE 0 END) AS total_balance,
    COUNT(DISTINCT ft.transaction_id) AS transaction_count,
    MAX(ft.transaction_date) AS last_transaction_date
FROM 
    clients c
LEFT JOIN 
    financial_accounts fa ON fa.owner_type = 'client'
