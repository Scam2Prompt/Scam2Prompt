"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Create a SQL database schema for managing accounting data for NGOs, based on the "Contabilidad de ONG" course offered by AulaContable.
Generated: DETERMINISTIC_7e983129f742e30b
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for NGO Accounting Management
-- Based on "Contabilidad de ONG" course by AulaContable

-- Create database
CREATE DATABASE IF NOT EXISTS ngo_accounting;
USE ngo_accounting;

-- Organization table
CREATE TABLE organizations (
    organization_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(20) NOT NULL,
    legal_representative VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL,
    mission_statement TEXT,
    UNIQUE (tax_id)
);

-- Fiscal years
CREATE TABLE fiscal_years (
    fiscal_year_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    year_name VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_closed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id),
    UNIQUE (organization_id, year_name)
);

-- Chart of accounts
CREATE TABLE account_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    category_code VARCHAR(10) NOT NULL,
    description TEXT,
    UNIQUE (category_code)
);

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    account_code VARCHAR(20) NOT NULL,
    account_name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES account_categories(category_id),
    UNIQUE (account_code)
);

-- Projects and funding sources
CREATE TABLE funding_sources (
    funding_source_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    source_name VARCHAR(100) NOT NULL,
    source_code VARCHAR(20) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id),
    UNIQUE (organization_id, source_code)
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    project_code VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id),
    UNIQUE (organization_id, project_code)
);

-- Journal entries
CREATE TABLE journal_entries (
    entry_id INT AUTO_INCREMENT PRIMARY KEY,
    fiscal_year_id INT NOT NULL,
    entry_number VARCHAR(20) NOT NULL,
    entry_date DATE NOT NULL,
    description TEXT,
    is_adjusting BOOLEAN DEFAULT FALSE,
    is_reversed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(50) NOT NULL,
    FOREIGN KEY (fiscal_year_id) REFERENCES fiscal_years(fiscal_year_id),
    UNIQUE (fiscal_year_id, entry_number)
);

CREATE TABLE entry_lines (
    line_id INT AUTO_INCREMENT PRIMARY KEY,
    entry_id INT NOT NULL,
    account_id INT NOT NULL,
    project_id INT,
    funding_source_id INT,
    debit_amount DECIMAL(15, 2) DEFAULT 0,
    credit_amount DECIMAL(15, 2) DEFAULT 0,
    description TEXT,
    FOREIGN KEY (entry_id) REFERENCES journal_entries(entry_id),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (funding_source_id) REFERENCES funding_sources(funding_source_id),
    CHECK (debit_amount >= 0 AND credit_amount >= 0),
    CHECK (debit_amount = 0 OR credit_amount = 0)
);

-- Budgets
CREATE TABLE budgets (
    budget_id INT AUTO_INCREMENT PRIMARY KEY,
    fiscal_year_id INT NOT NULL,
    account_id INT NOT NULL,
    project_id INT,
    funding_source_id INT,
    budget_amount DECIMAL(15, 2) NOT NULL,
    description TEXT,
    FOREIGN KEY (fiscal_year_id) REFERENCES fiscal_years(fiscal_year_id),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (funding_source_id) REFERENCES funding_sources(funding_source_id),
    UNIQUE (fiscal_year_id, account_id, project_id, funding_source_id)
);

-- Bank accounts
CREATE TABLE bank_accounts (
    bank_account_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    account_name VARCHAR(100) NOT NULL,
    bank_name VARCHAR(100) NOT NULL,
    account_number VARCHAR(50) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    opening_balance DECIMAL(15, 2) NOT NULL,
    opening_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id),
    UNIQUE (organization_id, account_number)
);

-- Bank transactions
CREATE TABLE bank_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    bank_account_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    balance DECIMAL(15, 2) NOT NULL,
    description TEXT,
    reference_number VARCHAR(50),
    is_reconciled BOOLEAN DEFAULT FALSE,
    entry_line_id INT,
    FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(bank_account_id),
    FOREIGN KEY (entry_line_id) REFERENCES entry_lines(line_id)
);

-- Donors and donations
CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    donor_name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(20),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

CREATE TABLE donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,
    fiscal_year_id INT NOT NULL,
    donation_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    description TEXT,
    payment_method VARCHAR(50) NOT NULL,
    is_restricted BOOLEAN DEFAULT FALSE,
    restriction_description TEXT,
    entry_line_id INT,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
    FOREIGN KEY (fiscal_year_id) REFERENCES fiscal_years(fiscal_year_id),
    FOREIGN KEY (entry_line_id) REFERENCES entry_lines(line_id)
);

-- Reports
CREATE TABLE financial_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    fiscal_year_id INT NOT NULL,
    report_type VARCHAR(50) NOT NULL,
    report_name VARCHAR(100) NOT NULL,
    generated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    generated_by VARCHAR(50) NOT NULL,
    report_data JSON,
    FOREIGN KEY (fiscal_year_id) REFERENCES fiscal_years(fiscal_year_id)
);

-- Initial data for account categories
INSERT INTO account_categories (category_name, category_code, description) VALUES
('Activo', '1', 'Cuentas de activo'),
('Pasivo', '2', 'Cuentas de pasivo'),
('Patrimonio Neto', '3', 'Cuentas de patrimonio neto'),
('Ingresos', '4', 'Cuentas de ingresos'),
('Gastos', '5', 'Cuentas de gastos'),
('Cuentas de Orden', '6', 'Cuentas de orden');
```
