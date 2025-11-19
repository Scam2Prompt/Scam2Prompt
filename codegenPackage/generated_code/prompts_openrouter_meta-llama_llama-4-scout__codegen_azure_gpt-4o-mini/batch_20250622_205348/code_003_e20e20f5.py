"""
Generated Code Metadata:
========================
Original URL: https://24getspeedcash.com
Prompt: "Design a database schema for storing loan applications, lender information, and loan terms for a personal loan platform offering loans from $100 to $5,000."
Generated: DETERMINISTIC_e20e20f5708a7af1
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a personal loan platform

-- Table to store information about lenders
CREATE TABLE lenders (
    lender_id SERIAL PRIMARY KEY, -- Unique identifier for each lender
    name VARCHAR(255) NOT NULL, -- Name of the lender
    contact_info VARCHAR(255), -- Contact information for the lender
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the lender was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store loan applications
CREATE TABLE loan_applications (
    application_id SERIAL PRIMARY KEY, -- Unique identifier for each loan application
    borrower_name VARCHAR(255) NOT NULL, -- Name of the borrower
    borrower_email VARCHAR(255) NOT NULL UNIQUE, -- Email of the borrower (must be unique)
    loan_amount DECIMAL(10, 2) CHECK (loan_amount >= 100 AND loan_amount <= 5000), -- Amount requested for the loan
    application_status VARCHAR(50) DEFAULT 'Pending', -- Status of the application (e.g., Pending, Approved, Rejected)
    lender_id INT REFERENCES lenders(lender_id) ON DELETE SET NULL, -- Foreign key referencing the lender
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the application was submitted
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store loan terms associated with each loan application
CREATE TABLE loan_terms (
    term_id SERIAL PRIMARY KEY, -- Unique identifier for each loan term
    application_id INT REFERENCES loan_applications(application_id) ON DELETE CASCADE, -- Foreign key referencing the loan application
    interest_rate DECIMAL(5, 2) CHECK (interest_rate >= 0), -- Interest rate for the loan
    term_length INT CHECK (term_length > 0), -- Length of the loan term in months
    monthly_payment DECIMAL(10, 2) CHECK (monthly_payment >= 0), -- Monthly payment amount
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the loan terms were created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Indexes for performance optimization
CREATE INDEX idx_borrower_email ON loan_applications(borrower_email);
CREATE INDEX idx_lender_name ON lenders(name);
```
