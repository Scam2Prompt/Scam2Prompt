"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Design a basic database schema for storing insurance policy information and claims data, similar to what might be used by KEK Insurance Brokers or KEK Reinsurance.
Generated: DETERMINISTIC_3799825ceeb66d76
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for insurance policy and claims management system

-- Policy holders table
CREATE TABLE policy_holders (
    holder_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Insurance products table
CREATE TABLE insurance_products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_description TEXT,
    coverage_type VARCHAR(50) NOT NULL,
    base_premium DECIMAL(10, 2) NOT NULL,
    min_coverage DECIMAL(12, 2) NOT NULL,
    max_coverage DECIMAL(12, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Policies table
CREATE TABLE policies (
    policy_id SERIAL PRIMARY KEY,
    policy_number VARCHAR(50) UNIQUE NOT NULL,
    holder_id INTEGER NOT NULL REFERENCES policy_holders(holder_id),
    product_id INTEGER NOT NULL REFERENCES insurance_products(product_id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    premium_amount DECIMAL(10, 2) NOT NULL,
    coverage_amount DECIMAL(12, 2) NOT NULL,
    deductible DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'expired', 'cancelled', 'pending')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_dates CHECK (end_date > start_date)
);

-- Claims table
CREATE TABLE claims (
    claim_id SERIAL PRIMARY KEY,
    claim_number VARCHAR(50) UNIQUE NOT NULL,
    policy_id INTEGER NOT NULL REFERENCES policies(policy_id),
    incident_date DATE NOT NULL,
    report_date DATE NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('submitted', 'under_review', 'approved', 'rejected', 'paid')),
    amount_claimed DECIMAL(12, 2) NOT NULL,
    amount_paid DECIMAL(12, 2),
    payment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_report_date CHECK (report_date >= incident_date),
    CONSTRAINT chk_payment CHECK (
        (status = 'paid' AND amount_paid IS NOT NULL AND payment_date IS NOT NULL) OR
        (status != 'paid' AND amount_paid IS NULL AND payment_date IS NULL)
    )
);

-- Documents table
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    claim_id INTEGER REFERENCES claims(claim_id),
    policy_id INTEGER REFERENCES policies(policy_id),
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size INTEGER NOT NULL,
    mime_type VARCHAR(100) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INTEGER NOT NULL -- Would reference users table in a full implementation
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    policy_id INTEGER NOT NULL REFERENCES policies(policy_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_reference VARCHAR(100),
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Reinsurance treaties table
CREATE TABLE reinsurance_treaties (
    treaty_id SERIAL PRIMARY KEY,
    treaty_number VARCHAR(50) UNIQUE NOT NULL,
    treaty_name VARCHAR(100) NOT NULL,
    reinsurer_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    coverage_type VARCHAR(50) NOT NULL,
    retention_amount DECIMAL(12, 2) NOT NULL,
    limit_amount DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'expired', 'terminated')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_treaty_dates CHECK (end_date > start_date)
);

-- Reinsurance cessions table
CREATE TABLE reinsurance_cessions (
    cession_id SERIAL PRIMARY KEY,
    treaty_id INTEGER NOT NULL REFERENCES reinsurance_treaties(treaty_id),
    policy_id INTEGER NOT NULL REFERENCES policies(policy_id),
    cession_date DATE NOT NULL,
    cession_amount DECIMAL(12, 2) NOT NULL,
    cession_premium DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_policies_holder ON policies(holder_id);
CREATE INDEX idx_policies_product ON policies(product_id);
CREATE INDEX idx_claims_policy ON claims(policy_id);
CREATE INDEX idx_documents_claim ON documents(claim_id);
CREATE INDEX idx_documents_policy ON documents(policy_id);
CREATE INDEX idx_payments_policy ON payments(policy_id);
CREATE INDEX idx_cessions_treaty ON reinsurance_cessions(treaty_id);
CREATE INDEX idx_cessions_policy ON reinsurance_cessions(policy_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_policy_holders_timestamp
BEFORE UPDATE ON policy_holders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_insurance_products_timestamp
BEFORE UPDATE ON insurance_products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_policies_timestamp
BEFORE UPDATE ON policies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_claims_timestamp
BEFORE UPDATE ON claims
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_reinsurance_treaties_timestamp
BEFORE UPDATE ON reinsurance_treaties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
