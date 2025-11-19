"""
Generated Code Metadata:
========================
Original URL: https://ketoantoandien889.com
Prompt: "Design a database schema for storing financial data and tax information for businesses in Vietnam, considering the requirements of KTTD 889."
Generated: DETERMINISTIC_6171ad6d7ab081f6
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Vietnamese Financial and Tax Data (KTTD 889 Compliance)

```sql
-- Database: vietnam_financial_data

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Companies table (business entities)
CREATE TABLE companies (
    company_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tax_code VARCHAR(20) NOT NULL UNIQUE CHECK (tax_code ~ '^[0-9]{10}$'),
    company_name VARCHAR(255) NOT NULL,
    legal_representative VARCHAR(100) NOT NULL,
    establishment_date DATE NOT NULL,
    business_registration_number VARCHAR(20),
    business_type VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    phone_number VARCHAR(15) CHECK (phone_number ~ '^\+?[0-9]{9,15}$'),
    email VARCHAR(255) CHECK (email ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_establishment_date CHECK (establishment_date <= CURRENT_DATE)
);

-- Financial periods (accounting periods)
CREATE TABLE financial_periods (
    period_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    period_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_closed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_period_dates CHECK (start_date < end_date),
    UNIQUE (company_id, period_name)
);

-- Chart of Accounts (Vietnamese standard)
CREATE TABLE chart_of_accounts (
    account_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    account_code VARCHAR(20) NOT NULL CHECK (account_code ~ '^[0-9]{3,6}$'),
    account_name VARCHAR(100) NOT NULL,
    account_type VARCHAR(50) NOT NULL CHECK (account_type IN ('Asset', 'Liability', 'Equity', 'Revenue', 'Expense')),
    parent_account_id UUID REFERENCES chart_of_accounts(account_id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (company_id, account_code)
);

-- Financial transactions
CREATE TABLE financial_transactions (
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    period_id UUID NOT NULL REFERENCES financial_periods(period_id),
    transaction_date DATE NOT NULL,
    voucher_number VARCHAR(50) NOT NULL,
    voucher_type VARCHAR(20) NOT NULL,
    description TEXT,
    total_amount DECIMAL(18, 2) NOT NULL CHECK (total_amount >= 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_transaction_date CHECK (transaction_date <= CURRENT_DATE)
);

-- Transaction details (line items)
CREATE TABLE transaction_details (
    detail_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id UUID NOT NULL REFERENCES financial_transactions(transaction_id) ON DELETE CASCADE,
    account_id UUID NOT NULL REFERENCES chart_of_accounts(account_id),
    debit_amount DECIMAL(18, 2) DEFAULT 0 CHECK (debit_amount >= 0),
    credit_amount DECIMAL(18, 2) DEFAULT 0 CHECK (credit_amount >= 0),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_amount CHECK (
        (debit_amount > 0 AND credit_amount = 0) OR 
        (credit_amount > 0 AND debit_amount = 0)
    )
);

-- Tax declarations (KTTD 889 compliance)
CREATE TABLE tax_declarations (
    declaration_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    period_id UUID NOT NULL REFERENCES financial_periods(period_id),
    tax_type VARCHAR(50) NOT NULL CHECK (tax_type IN ('VAT', 'CIT', 'PIT', 'FCT', 'Other')),
    declaration_form VARCHAR(20) NOT NULL,
    declaration_number VARCHAR(50) NOT NULL,
    submission_date DATE NOT NULL,
    tax_authority VARCHAR(100) NOT NULL,
    tax_amount DECIMAL(18, 2) NOT NULL CHECK (tax_amount >= 0),
    penalty_amount DECIMAL(18, 2) DEFAULT 0 CHECK (penalty_amount >= 0),
    late_fee_amount DECIMAL(18, 2) DEFAULT 0 CHECK (late_fee_amount >= 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'Submitted', 'Approved', 'Rejected', 'Paid')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_submission_date CHECK (submission_date <= CURRENT_DATE),
    UNIQUE (company_id, declaration_number)
);

-- Tax rates (current Vietnamese tax rates)
CREATE TABLE tax_rates (
    rate_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tax_type VARCHAR(50) NOT NULL CHECK (tax_type IN ('VAT', 'CIT', 'PIT', 'FCT', 'Other')),
    rate_name VARCHAR(100) NOT NULL,
    rate_value DECIMAL(5, 2) NOT NULL CHECK (rate_value >= 0),
    effective_from DATE NOT NULL,
    effective_to DATE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_effective_dates CHECK (effective_from <= COALESCE(effective_to, '9999-12-31'))
);

-- Invoice information (for VAT compliance)
CREATE TABLE invoices (
    invoice_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    invoice_number VARCHAR(50) NOT NULL,
    invoice_date DATE NOT NULL,
    invoice_type VARCHAR(20) NOT NULL CHECK (invoice_type IN ('Sale', 'Purchase', 'Other')),
    customer_tax_code VARCHAR(20) CHECK (customer_tax_code ~ '^[0-9]{10}$'),
    customer_name VARCHAR(255),
    total_amount DECIMAL(18, 2) NOT NULL CHECK (total_amount >= 0),
    tax_amount DECIMAL(18, 2) NOT NULL CHECK (tax_amount >= 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Draft', 'Issued', 'Cancelled', 'Adjusted')),
    transaction_id UUID REFERENCES financial_transactions(transaction_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_invoice_date CHECK (invoice_date <= CURRENT_DATE),
    UNIQUE (company_id, invoice_number)
);

-- Invoice items
CREATE TABLE invoice_items (
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    item_name VARCHAR(255) NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(18, 2) NOT NULL CHECK (unit_price >= 0),
    amount DECIMAL(18, 2) NOT NULL CHECK (amount >= 0),
    tax_rate_id UUID REFERENCES tax_rates(rate_id),
    tax_amount DECIMAL(18, 2) NOT NULL CHECK (tax_amount >= 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Financial reports
CREATE TABLE financial_reports (
    report_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    period_id UUID NOT NULL REFERENCES financial_periods(period_id),
    report_type VARCHAR(50) NOT NULL CHECK (report_type IN ('BalanceSheet', 'IncomeStatement', 'CashFlow', 'Other')),
    report_name VARCHAR(100) NOT NULL,
    generated_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    file_path TEXT,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (company_id, period_id, report_type)
);

-- Audit logs for compliance
CREATE TABLE audit_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID REFERENCES companies(company_id) ON DELETE SET NULL,
    user_id UUID,
    action_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT
