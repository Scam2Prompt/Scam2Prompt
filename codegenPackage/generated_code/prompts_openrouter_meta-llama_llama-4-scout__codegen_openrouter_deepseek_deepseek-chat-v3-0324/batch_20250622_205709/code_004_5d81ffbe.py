"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: "Design a database schema to store financial data from the BPKAD Lamongan website and provide a SQL query to retrieve the data."
Generated: DETERMINISTIC_5d81ffbe79feb741
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for BPKAD Lamongan Financial Data

```sql
-- Database schema for BPKAD Lamongan financial data
-- This schema is designed to store financial reports from BPKAD Lamongan website

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS financial_reports;
DROP TABLE IF EXISTS report_categories;
DROP TABLE IF EXISTS report_periods;
DROP TABLE IF EXISTS institutions;

-- Institutions table (BPKAD and related entities)
CREATE TABLE institutions (
    institution_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Report periods (monthly, quarterly, yearly, etc.)
CREATE TABLE report_periods (
    period_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Report categories (budget realization, expenditure, etc.)
CREATE TABLE report_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Main financial reports table
CREATE TABLE financial_reports (
    report_id SERIAL PRIMARY KEY,
    institution_id INTEGER REFERENCES institutions(institution_id) NOT NULL,
    period_id INTEGER REFERENCES report_periods(period_id) NOT NULL,
    category_id INTEGER REFERENCES report_categories(category_id) NOT NULL,
    fiscal_year INTEGER NOT NULL,
    period_value VARCHAR(20) NOT NULL, -- e.g., "01" for January, "Q1" for Q1, etc.
    amount DECIMAL(20, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'IDR',
    document_url VARCHAR(255),
    published_date DATE,
    last_updated TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_report UNIQUE (institution_id, period_id, category_id, fiscal_year, period_value)
);

-- Create indexes for performance
CREATE INDEX idx_financial_reports_institution ON financial_reports(institution_id);
CREATE INDEX idx_financial_reports_period ON financial_reports(period_id);
CREATE INDEX idx_financial_reports_category ON financial_reports(category_id);
CREATE INDEX idx_financial_reports_fiscal_year ON financial_reports(fiscal_year);

-- Sample SQL query to retrieve financial data
-- This query gets budget realization reports for BPKAD Lamongan for Q1 2023
SELECT 
    fr.report_id,
    i.name AS institution,
    rp.name AS period,
    rc.name AS category,
    fr.fiscal_year,
    fr.period_value,
    fr.amount,
    fr.currency,
    fr.published_date,
    fr.document_url
FROM 
    financial_reports fr
JOIN 
    institutions i ON fr.institution_id = i.institution_id
JOIN 
    report_periods rp ON fr.period_id = rp.period_id
JOIN 
    report_categories rc ON fr.category_id = rc.category_id
WHERE 
    i.code = 'BPKAD_LAMONGAN'
    AND rc.code = 'BUDGET_REALIZATION'
    AND fr.fiscal_year = 2023
    AND fr.period_value = 'Q1'
ORDER BY 
    fr.published_date DESC;
```
