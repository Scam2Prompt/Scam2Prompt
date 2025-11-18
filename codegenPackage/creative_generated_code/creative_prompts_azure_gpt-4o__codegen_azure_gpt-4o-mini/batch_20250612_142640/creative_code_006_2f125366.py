"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Develop a database schema for tracking settlement loans, including fields for "litigation status," "loan amount," and "repayment terms," as described by Rhino Finance.
Generated: DETERMINISTIC_2f1253667606af4c
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for tracking settlement loans

-- Drop existing table if it exists to avoid conflicts during creation
DROP TABLE IF EXISTS SettlementLoans;

-- Create the SettlementLoans table
CREATE TABLE SettlementLoans (
    loan_id SERIAL PRIMARY KEY,         -- Unique identifier for each loan
    borrower_id INT NOT NULL,           -- Identifier for the borrower (foreign key)
    loan_amount DECIMAL(15, 2) NOT NULL, -- Amount of the loan, with precision for currency
    repayment_terms VARCHAR(255) NOT NULL, -- Description of repayment terms
    litigation_status VARCHAR(50),      -- Current litigation status of the loan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the loan was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Auto-update timestamp
    FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id) -- Establish relationship to Borrowers table
);

-- Index for faster retrieval based on litigation status
CREATE INDEX idx_litigation_status ON SettlementLoans(litigation_status);

-- Comment on the purpose of the table
COMMENT ON TABLE SettlementLoans IS 'Table to track settlement loans including details about the loan amount, repayment terms, and litigation status.';
```
