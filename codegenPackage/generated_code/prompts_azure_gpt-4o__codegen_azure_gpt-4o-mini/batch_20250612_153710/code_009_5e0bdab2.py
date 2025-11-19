"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Create a database schema for storing scam reports, including fields for phone numbers, bank accounts, names, and transaction details, inspired by the structure on admgdv.com.
Generated: DETERMINISTIC_5e0bdab21c5aabb4
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing scam reports

CREATE DATABASE IF NOT EXISTS ScamReportsDB;

USE ScamReportsDB;

-- Table to store scam report details
CREATE TABLE IF NOT EXISTS ScamReports (
    report_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each report
    phone_number VARCHAR(15) NOT NULL,        -- Phone number associated with the scam
    bank_account VARCHAR(20) NOT NULL,        -- Bank account involved in the scam
    name VARCHAR(100) NOT NULL,                -- Name of the victim or scammer
    transaction_details TEXT NOT NULL,         -- Details of the transaction
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the report
    status ENUM('Pending', 'Reviewed', 'Resolved') DEFAULT 'Pending', -- Status of the report
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT chk_phone_number CHECK (phone_number REGEXP '^[0-9]{10,15}$'), -- Validate phone number format
    CONSTRAINT chk_bank_account CHECK (bank_account REGEXP '^[0-9]{10,20}$') -- Validate bank account format
);

-- Indexes for faster querying
CREATE INDEX idx_phone_number ON ScamReports(phone_number);
CREATE INDEX idx_bank_account ON ScamReports(bank_account);
CREATE INDEX idx_report_date ON ScamReports(report_date);

-- Example of inserting a scam report
-- INSERT INTO ScamReports (phone_number, bank_account, name, transaction_details)
-- VALUES ('1234567890', '12345678901234567890', 'John Doe', 'Details of the scam transaction');

-- Example of selecting all scam reports
-- SELECT * FROM ScamReports;

-- Example of updating a scam report status
-- UPDATE ScamReports SET status = 'Reviewed' WHERE report_id = 1;

-- Example of deleting a scam report
-- DELETE FROM ScamReports WHERE report_id = 1;
```
