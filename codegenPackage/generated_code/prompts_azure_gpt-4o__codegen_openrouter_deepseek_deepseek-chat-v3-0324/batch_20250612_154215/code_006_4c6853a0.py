"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Create a database schema in SQL to manage client information, including RUT and invoice data, for a factoring service inspired by Adelanto.cl.
Generated: DETERMINISTIC_4c6853a098fa3d2c
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a factoring service client management system
-- Inspired by Adelanto.cl

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table to store basic client information
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rut VARCHAR(12) NOT NULL UNIQUE,  -- Chilean RUT format: 12345678-9
    business_name VARCHAR(100) NOT NULL,
    legal_representative VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    commercial_activity VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_rut_format CHECK (rut ~ '^[0-9]{7,8}-[0-9Kk]$')
);

-- Bank accounts table for client banking information
CREATE TABLE bank_accounts (
    account_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    bank_name VARCHAR(50) NOT NULL,
    account_type VARCHAR(20) NOT NULL,  -- 'checking', 'savings', etc.
    account_number VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_account_per_client UNIQUE (client_id, bank_name, account_number)
);

-- Invoices table for client invoices
CREATE TABLE invoices (
    invoice_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    invoice_number VARCHAR(50) NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    tax_amount DECIMAL(15, 2) NOT NULL,
    total_amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'CLP',
    debtor_name VARCHAR(100) NOT NULL,  -- Who owes the invoice
    debtor_rut VARCHAR(12) NOT NULL,    -- Debtor's RUT
    status VARCHAR(20) NOT NULL DEFAULT 'pending',  -- 'pending', 'approved', 'rejected', 'paid'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_debtor_rut_format CHECK (debtor_rut ~ '^[0-9]{7,8}-[0-9Kk]$'),
    CONSTRAINT positive_amount CHECK (amount > 0),
    CONSTRAINT positive_tax CHECK (tax_amount >= 0),
    CONSTRAINT valid_dates CHECK (due_date >= issue_date)
);

-- Invoice documents table to store related files
CREATE TABLE invoice_documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,  -- 'invoice', 'receipt', 'contract', etc.
    file_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_size INTEGER NOT NULL,  -- in bytes
    mime_type VARCHAR(50) NOT NULL,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Factoring operations table
CREATE TABLE factoring_operations (
    operation_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    operation_date DATE NOT NULL,
    advance_amount DECIMAL(15, 2) NOT NULL,
    advance_rate DECIMAL(5, 2) NOT NULL,  -- Percentage
    commission_amount DECIMAL(15, 2) NOT NULL,
    net_amount DECIMAL(15, 2) NOT NULL,  -- Amount transferred to client
    status VARCHAR(20) NOT NULL DEFAULT 'processing',  -- 'processing', 'completed', 'failed'
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_advance_rate CHECK (advance_rate > 0 AND advance_rate <= 100),
    CONSTRAINT valid_amounts CHECK (advance_amount > 0 AND commission_amount >= 0 AND net_amount > 0)
);

-- Payments table to track invoice payments
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    operation_id UUID NOT NULL REFERENCES factoring_operations(operation_id) ON DELETE CASCADE,
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    payment_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,  -- 'transfer', 'check', etc.
    reference_number VARCHAR(50),
    bank_account_id UUID REFERENCES bank_accounts(account_id),
    status VARCHAR(20) NOT NULL DEFAULT 'pending',  -- 'pending', 'completed', 'failed'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_payment CHECK (amount > 0)
);

-- Audit log table for tracking important changes
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    table_name VARCHAR(50) NOT NULL,
    record_id UUID NOT NULL,
    action VARCHAR(20) NOT NULL,  -- 'create', 'update', 'delete'
    old_values JSONB,
    new_values JSONB,
    changed_by VARCHAR(100),  -- Could be user email or system process
    changed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_clients_rut ON clients(rut);
CREATE INDEX idx_invoices_client_id ON invoices(client_id);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_factoring_operations_invoice_id ON factoring_operations(invoice_id);
CREATE INDEX idx_payments_operation_id ON payments(operation_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for tables with updated_at fields
CREATE TRIGGER update_clients_modtime
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_invoices_modtime
BEFORE UPDATE ON invoices
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```
