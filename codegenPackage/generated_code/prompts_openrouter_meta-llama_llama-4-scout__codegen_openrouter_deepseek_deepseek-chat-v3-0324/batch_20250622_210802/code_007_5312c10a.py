"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Design a database schema to store financial data for a company, inspired by Lund & Kieck's accounting and bookkeeping services.
Generated: DETERMINISTIC_5312c10afb404ee3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for financial data management system

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create tables
CREATE TABLE accounts (
    account_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    account_name VARCHAR(100) NOT NULL,
    account_type VARCHAR(50) NOT NULL CHECK (account_type IN ('Asset', 'Liability', 'Equity', 'Revenue', 'Expense')),
    account_code VARCHAR(20) NOT NULL UNIQUE,
    description TEXT,
    parent_account_id UUID REFERENCES accounts(account_id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fiscal_periods (
    period_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    period_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_closed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_period CHECK (end_date > start_date)
);

CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_date DATE NOT NULL,
    reference_number VARCHAR(50),
    description TEXT,
    period_id UUID NOT NULL REFERENCES fiscal_periods(period_id),
    created_by VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE journal_entries (
    entry_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id UUID NOT NULL REFERENCES transactions(transaction_id),
    account_id UUID NOT NULL REFERENCES accounts(account_id),
    amount DECIMAL(19,4) NOT NULL,
    entry_type VARCHAR(10) NOT NULL CHECK (entry_type IN ('Debit', 'Credit')),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_amount CHECK (amount > 0)
);

CREATE TABLE vendors (
    vendor_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    vendor_name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(50),
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(50),
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    credit_limit DECIMAL(19,4),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE invoices (
    invoice_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    customer_id UUID REFERENCES customers(customer_id),
    vendor_id UUID REFERENCES vendors(vendor_id),
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(19,4) NOT NULL,
    tax_amount DECIMAL(19,4) DEFAULT 0,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Draft', 'Sent', 'Paid', 'Overdue', 'Cancelled')),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (due_date >= issue_date)
);

CREATE TABLE invoice_items (
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id),
    description TEXT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(19,4) NOT NULL,
    account_id UUID REFERENCES accounts(account_id),
    tax_rate DECIMAL(5,2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_quantity CHECK (quantity > 0),
    CONSTRAINT valid_price CHECK (unit_price >= 0)
);

CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    payment_date DATE NOT NULL,
    payment_method VARCHAR(50) NOT NULL CHECK (payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Other')),
    reference_number VARCHAR(50),
    amount DECIMAL(19,4) NOT NULL,
    account_id UUID REFERENCES accounts(account_id),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_payment_amount CHECK (amount > 0)
);

CREATE TABLE invoice_payments (
    invoice_payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id),
    payment_id UUID NOT NULL REFERENCES payments(payment_id),
    amount_applied DECIMAL(19,4) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_applied_amount CHECK (amount_applied > 0)
);

CREATE TABLE financial_reports (
    report_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_name VARCHAR(100) NOT NULL,
    report_type VARCHAR(50) NOT NULL CHECK (report_type IN ('Balance Sheet', 'Income Statement', 'Cash Flow', 'Trial Balance', 'Custom')),
    period_id UUID REFERENCES fiscal_periods(period_id),
    start_date DATE,
    end_date DATE,
    generated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    generated_by VARCHAR(100) NOT NULL,
    report_data JSONB,
    CONSTRAINT valid_report_dates CHECK (end_date >= start_date)
);

-- Create indexes for performance
CREATE INDEX idx_accounts_account_type ON accounts(account_type);
CREATE INDEX idx_transactions_period_id ON transactions(period_id);
CREATE INDEX idx_journal_entries_transaction_id ON journal_entries(transaction_id);
CREATE INDEX idx_journal_entries_account_id ON journal_entries(account_id);
CREATE INDEX idx_invoices_customer_id ON invoices(customer_id);
CREATE INDEX idx_invoices_vendor_id ON invoices(vendor_id);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_invoice_items_invoice_id ON invoice_items(invoice_id);
CREATE INDEX idx_payments_account_id ON payments(account_id);
CREATE INDEX idx_invoice_payments_invoice_id ON invoice_payments(invoice_id);
CREATE INDEX idx_invoice_payments_payment_id ON invoice_payments(payment_id);

-- Create triggers for timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_accounts_timestamp
BEFORE UPDATE ON accounts
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_fiscal_periods_timestamp
BEFORE UPDATE ON fiscal_periods
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_transactions_timestamp
BEFORE UPDATE ON transactions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_vendors_timestamp
BEFORE UPDATE ON vendors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_customers_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_invoices_timestamp
BEFORE UPDATE ON invoices
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_payments_timestamp
BEFORE UPDATE ON payments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
