"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aniemaxgroup.com
Prompt: Create a database schema for managing financial services such as debt collection, invoice management, and loan portfolios, referencing Aniemax Capital's offerings.
Generated: DETERMINISTIC_bbd33237a34ac849
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Aniemax Capital Financial Services
-- This schema is designed to manage debt collection, invoice management, and loan portfolios.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Invoices;
DROP TABLE IF EXISTS Debtors;
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Loan_Portfolios;

-- Table to store debtor information
CREATE TABLE Debtors (
    debtor_id SERIAL PRIMARY KEY, -- Unique identifier for each debtor
    name VARCHAR(255) NOT NULL, -- Debtor's name
    contact_info VARCHAR(255), -- Debtor's contact information
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to manage invoices
CREATE TABLE Invoices (
    invoice_id SERIAL PRIMARY KEY, -- Unique identifier for each invoice
    debtor_id INT NOT NULL, -- Reference to the debtor
    amount DECIMAL(10, 2) NOT NULL, -- Invoice amount
    due_date DATE NOT NULL, -- Invoice due date
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Invoice status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    CONSTRAINT fk_debtor FOREIGN KEY (debtor_id) REFERENCES Debtors(debtor_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store loan portfolio information
CREATE TABLE Loan_Portfolios (
    portfolio_id SERIAL PRIMARY KEY, -- Unique identifier for each loan portfolio
    name VARCHAR(255) NOT NULL, -- Name of the loan portfolio
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to manage loans associated with debtors
CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY, -- Unique identifier for each loan
    debtor_id INT NOT NULL, -- Reference to the debtor
    portfolio_id INT NOT NULL, -- Reference to the loan portfolio
    amount DECIMAL(10, 2) NOT NULL, -- Loan amount
    interest_rate DECIMAL(5, 2) NOT NULL, -- Loan interest rate
    term_months INT NOT NULL, -- Loan term in months
    status VARCHAR(50) NOT NULL DEFAULT 'Active', -- Loan status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    CONSTRAINT fk_loan_debtor FOREIGN KEY (debtor_id) REFERENCES Debtors(debtor_id) ON DELETE CASCADE, -- Foreign key constraint
    CONSTRAINT fk_loan_portfolio FOREIGN KEY (portfolio_id) REFERENCES Loan_Portfolios(portfolio_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to manage payments associated with invoices
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    invoice_id INT NOT NULL, -- Reference to the invoice
    amount DECIMAL(10, 2) NOT NULL, -- Payment amount
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Payment date
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    CONSTRAINT fk_payment_invoice FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexing for faster lookups
CREATE INDEX idx_debtor_name ON Debtors(name);
CREATE INDEX idx_invoice_status ON Invoices(status);
CREATE INDEX idx_loan_status ON Loans(status);
```
