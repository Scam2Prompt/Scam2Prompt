"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Design a database schema for a small accounting firm in Peru, using a database management system like MySQL or PostgreSQL to manage client data, financial statements, and tax returns."
Generated: DETERMINISTIC_d7d72cbcfbec5c28
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a small accounting firm in Peru
-- Using PostgreSQL syntax

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create enum types
CREATE TYPE document_type AS ENUM ('DNI', 'RUC', 'CE', 'PASAPORTE');
CREATE TYPE tax_category AS ENUM ('RER', 'NRUS', 'RUS', 'RMT', 'RG');
CREATE TYPE filing_status AS ENUM ('PENDING', 'FILED', 'APPROVED', 'REJECTED');

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    legal_name VARCHAR(100) NOT NULL,
    trade_name VARCHAR(100),
    document_type document_type NOT NULL,
    document_number VARCHAR(20) NOT NULL,
    tax_category tax_category NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_document UNIQUE (document_type, document_number)
);

-- Contacts table
CREATE TABLE contacts (
    contact_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    full_name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Financial periods table
CREATE TABLE financial_periods (
    period_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    period_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_closed BOOLEAN DEFAULT FALSE,
    closing_date TIMESTAMP WITH TIME ZONE,
    CONSTRAINT valid_period_dates CHECK (end_date > start_date)
);

-- Financial statements table
CREATE TABLE financial_statements (
    statement_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    period_id UUID NOT NULL REFERENCES financial_periods(period_id) ON DELETE CASCADE,
    statement_type VARCHAR(50) NOT NULL, -- 'Balance Sheet', 'Income Statement', etc.
    file_path TEXT NOT NULL,
    prepared_by VARCHAR(100),
    reviewed_by VARCHAR(100),
    preparation_date DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    version INTEGER DEFAULT 1
);

-- Tax declarations table
CREATE TABLE tax_declarations (
    declaration_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    period_id UUID NOT NULL REFERENCES financial_periods(period_id) ON DELETE CASCADE,
    tax_type VARCHAR(50) NOT NULL, -- 'IGV', 'Renta', etc.
    filing_status filing_status DEFAULT 'PENDING',
    filing_date DATE,
    due_date DATE NOT NULL,
    amount DECIMAL(15, 2),
    penalty DECIMAL(15, 2) DEFAULT 0,
    interest DECIMAL(15, 2) DEFAULT 0,
    sunat_code VARCHAR(20),
    notes TEXT,
    CONSTRAINT valid_filing_date CHECK (filing_date <= CURRENT_DATE)
);

-- Payments table
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    declaration_id UUID REFERENCES tax_declarations(declaration_id) ON DELETE SET NULL,
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    payment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    amount DECIMAL(15, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    reference_number VARCHAR(50),
    bank_name VARCHAR(100),
    notes TEXT
);

-- Documents table
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expiration_date DATE,
    description TEXT,
    is_archived BOOLEAN DEFAULT FALSE
);

-- Services table
CREATE TABLE services (
    service_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(15, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Client services table
CREATE TABLE client_services (
    client_service_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    service_id UUID NOT NULL REFERENCES services(service_id) ON DELETE RESTRICT,
    start_date DATE NOT NULL,
    end_date DATE,
    agreed_price DECIMAL(15, 2) NOT NULL,
    payment_frequency VARCHAR(50), -- 'Monthly', 'Quarterly', etc.
    notes TEXT,
    CONSTRAINT valid_service_period CHECK (end_date IS NULL OR end_date > start_date)
);

-- Invoices table
CREATE TABLE invoices (
    invoice_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    invoice_number VARCHAR(20) NOT NULL,
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    subtotal DECIMAL(15, 2) NOT NULL,
    tax_amount DECIMAL(15, 2) NOT NULL,
    total_amount DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING', -- 'PENDING', 'PAID', 'CANCELLED'
    payment_date DATE,
    notes TEXT,
    CONSTRAINT valid_invoice_dates CHECK (due_date >= issue_date),
    CONSTRAINT valid_payment_date CHECK (payment_date IS NULL OR payment_date >= issue_date)
);

-- Invoice items table
CREATE TABLE invoice_items (
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    service_id UUID REFERENCES services(service_id) ON DELETE SET NULL,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(15, 2) NOT NULL,
    tax_rate DECIMAL(5, 2) NOT NULL DEFAULT 0.18, -- Default IGV rate in Peru
    amount DECIMAL(15, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    tax_amount DECIMAL(15, 2) GENERATED ALWAYS AS (quantity * unit_price * tax_rate) STORED,
    total_amount DECIMAL(15, 2) GENERATED ALWAYS AS (quantity * unit_price * (1 + tax_rate)) STORED
);

-- Users table for system access
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Audit log table
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id) ON DELETE SET NULL,
    action_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    action_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(50)
);

-- Create indexes for performance
CREATE INDEX idx_clients_document ON clients(document_type, document_number);
CREATE INDEX idx_financial_periods_client ON financial_periods(client_id);
CREATE INDEX idx_tax_declarations_period ON tax_declarations(period_id);
CREATE INDEX idx_tax_declarations_status ON tax_declarations(filing_status);
CREATE INDEX idx_invoices_client ON invoices(client_id);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_client_services_client ON client_services(client_id);
```
