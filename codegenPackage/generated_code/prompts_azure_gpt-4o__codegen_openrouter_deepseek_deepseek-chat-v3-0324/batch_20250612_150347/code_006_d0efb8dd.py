"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Create a database schema for managing client accounts, including tracking insolvency cases, tax filings, and debt restructuring plans, inspired by Arbitum Consulting's services.
Generated: DETERMINISTIC_d0efb8dd6fb3c7aa
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for client account management with insolvency tracking
-- Inspired by Arbitum Consulting's services

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_name VARCHAR(255) NOT NULL,
    registration_number VARCHAR(50) UNIQUE NOT NULL,
    incorporation_date DATE,
    legal_form VARCHAR(100),
    industry_sector VARCHAR(100),
    contact_person VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Insolvency cases table
CREATE TABLE insolvency_cases (
    case_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    case_reference VARCHAR(50) UNIQUE NOT NULL,
    case_type VARCHAR(50) NOT NULL CHECK (case_type IN ('Bankruptcy', 'Liquidation', 'Administration', 'CVA', 'IVA', 'Other')),
    filing_date DATE NOT NULL,
    court_name VARCHAR(255),
    case_number VARCHAR(100),
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'Active', 'Closed', 'Dismissed', 'Appealed')),
    outcome VARCHAR(255),
    closure_date DATE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (filing_date <= COALESCE(closure_date, CURRENT_DATE))
);

-- Tax filings table
CREATE TABLE tax_filings (
    filing_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    tax_type VARCHAR(50) NOT NULL CHECK (tax_type IN ('VAT', 'Corporation Tax', 'PAYE', 'Self Assessment', 'Other')),
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    filing_date DATE,
    due_date DATE NOT NULL,
    amount_owed DECIMAL(15, 2),
    amount_paid DECIMAL(15, 2),
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'Filed', 'Paid', 'Overdue', 'In Dispute')),
    hmrc_reference VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_period CHECK (period_start < period_end),
    CONSTRAINT valid_filing_date CHECK (filing_date IS NULL OR filing_date >= period_end)
);

-- Debt restructuring plans table
CREATE TABLE debt_restructuring_plans (
    plan_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    case_id UUID REFERENCES insolvency_cases(case_id) ON DELETE SET NULL,
    plan_name VARCHAR(255) NOT NULL,
    plan_type VARCHAR(50) NOT NULL CHECK (plan_type IN ('CVA', 'IVA', 'Scheme of Arrangement', 'Time to Pay', 'Other')),
    proposal_date DATE NOT NULL,
    approval_date DATE,
    duration_months INTEGER,
    total_debt DECIMAL(15, 2) NOT NULL,
    monthly_payment DECIMAL(15, 2),
    creditors_meeting_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Draft', 'Proposed', 'Approved', 'Rejected', 'Completed', 'Breached')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_approval_date CHECK (approval_date IS NULL OR approval_date >= proposal_date)
);

-- Creditors table
CREATE TABLE creditors (
    creditor_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creditor_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    registration_number VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_creditor_email CHECK (email IS NULL OR email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Client-Creditor relationships
CREATE TABLE client_creditors (
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    creditor_id UUID NOT NULL REFERENCES creditors(creditor_id) ON DELETE CASCADE,
    debt_amount DECIMAL(15, 2) NOT NULL,
    debt_description TEXT,
    date_incurred DATE,
    is_secured BOOLEAN DEFAULT FALSE,
    security_details TEXT,
    PRIMARY KEY (client_id, creditor_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Plan-Creditor relationships (for debt restructuring)
CREATE TABLE plan_creditors (
    plan_id UUID NOT NULL REFERENCES debt_restructuring_plans(plan_id) ON DELETE CASCADE,
    creditor_id UUID NOT NULL REFERENCES creditors(creditor_id) ON DELETE CASCADE,
    original_debt DECIMAL(15, 2) NOT NULL,
    agreed_debt DECIMAL(15, 2) NOT NULL,
    voting_status VARCHAR(50) CHECK (voting_status IN ('For', 'Against', 'Abstained', 'Not Voted')),
    PRIMARY KEY (plan_id, creditor_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Documents table
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID REFERENCES clients(client_id) ON DELETE CASCADE,
    case_id UUID REFERENCES insolvency_cases(case_id) ON DELETE CASCADE,
    plan_id UUID REFERENCES debt_restructuring_plans(plan_id) ON DELETE CASCADE,
    filing_id UUID REFERENCES tax_filings(filing_id) ON DELETE CASCADE,
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(100) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size BIGINT NOT NULL,
    mime_type VARCHAR(100),
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_reference CHECK (
        (client_id IS NOT NULL) OR
        (case_id IS NOT NULL) OR
        (plan_id IS NOT NULL) OR
        (filing_id IS NOT NULL)
    )
);

-- Case notes table
CREATE TABLE case_notes (
    note_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    case_id UUID REFERENCES insolvency_cases(case_id) ON DELETE CASCADE,
    plan_id UUID REFERENCES debt_restructuring_plans(plan_id) ON DELETE CASCADE,
    author VARCHAR(255) NOT NULL,
    note_text TEXT NOT NULL,
    is_important BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_reference CHECK (
        (case_id IS NOT NULL) OR
        (plan_id IS NOT NULL)
    )
);

-- Triggers for automatic updated_at timestamps
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

CREATE TRIGGER update_insolvency_cases_timestamp
BEFORE UPDATE ON insolvency_cases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_tax_filings_timestamp
BEFORE UPDATE ON tax_filings
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_debt_restructuring_plans_timestamp
BEFORE UPDATE ON debt_restructuring_plans
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update
