"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Create a database schema for managing merchant acquisition and activation data, inspired by Paradigm Group's MTN Momo projects in South Africa.
Generated: DETERMINISTIC_c56bde002fbc6d67
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for merchant acquisition and activation management
-- Inspired by Paradigm Group's MTN Momo projects in South Africa

CREATE TABLE merchants (
    merchant_id SERIAL PRIMARY KEY,
    business_name VARCHAR(100) NOT NULL,
    trading_name VARCHAR(100) NOT NULL,
    business_registration_number VARCHAR(50) UNIQUE,
    vat_number VARCHAR(50),
    business_type VARCHAR(50) NOT NULL,
    industry_category VARCHAR(50) NOT NULL,
    date_established DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_contacts (
    contact_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    id_number VARCHAR(20) NOT NULL,
    id_type VARCHAR(20) NOT NULL,
    is_primary_contact BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_addresses (
    address_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    address_type VARCHAR(20) NOT NULL CHECK (address_type IN ('business', 'physical', 'postal')),
    street_address VARCHAR(100) NOT NULL,
    suburb VARCHAR(50),
    city VARCHAR(50) NOT NULL,
    province VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    country VARCHAR(50) DEFAULT 'South Africa',
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_bank_details (
    bank_detail_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    bank_name VARCHAR(50) NOT NULL,
    branch_code VARCHAR(10) NOT NULL,
    account_number VARCHAR(20) NOT NULL,
    account_type VARCHAR(20) NOT NULL CHECK (account_type IN ('cheque', 'savings', 'transmission')),
    account_holder_name VARCHAR(100) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_documents (
    document_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL CHECK (document_type IN ('id_copy', 'proof_of_address', 'business_registration', 'vat_certificate', 'bank_confirmation')),
    document_url VARCHAR(255) NOT NULL,
    verification_status VARCHAR(20) DEFAULT 'pending' CHECK (verification_status IN ('pending', 'approved', 'rejected')),
    verified_by INTEGER,
    verified_at TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_activation (
    activation_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    activation_status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (activation_status IN ('pending', 'approved', 'rejected', 'activated')),
    activation_date TIMESTAMP WITH TIME ZONE,
    activated_by INTEGER,
    rejection_reason TEXT,
    msisdn VARCHAR(20) UNIQUE,
    agent_code VARCHAR(20),
    terminal_id VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_transactions (
    transaction_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    transaction_reference VARCHAR(50) NOT NULL UNIQUE,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal', 'payment', 'reversal')),
    amount DECIMAL(15, 2) NOT NULL,
    fee DECIMAL(15, 2) DEFAULT 0.00,
    balance_before DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    transaction_status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (transaction_status IN ('pending', 'completed', 'failed', 'reversed')),
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE merchant_activity_logs (
    log_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE,
    user_id INTEGER,
    activity_type VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    ip_address VARCHAR(50),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_merchant_contacts_merchant_id ON merchant_contacts(merchant_id);
CREATE INDEX idx_merchant_addresses_merchant_id ON merchant_addresses(merchant_id);
CREATE INDEX idx_merchant_bank_details_merchant_id ON merchant_bank_details(merchant_id);
CREATE INDEX idx_merchant_documents_merchant_id ON merchant_documents(merchant_id);
CREATE INDEX idx_merchant_activation_merchant_id ON merchant_activation(merchant_id);
CREATE INDEX idx_merchant_transactions_merchant_id ON merchant_transactions(merchant_id);
CREATE INDEX idx_merchant_activity_logs_merchant_id ON merchant_activity_logs(merchant_id);
CREATE INDEX idx_merchant_activation_status ON merchant_activation(activation_status);
CREATE INDEX idx_merchant_trans
