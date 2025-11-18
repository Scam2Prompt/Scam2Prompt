"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Create a database schema for storing scam reports, including fields for phone numbers, bank accounts, names, and transaction details, inspired by the structure on admgdv.com.
Generated: DETERMINISTIC_5e0bdab21c5aabb4
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store scam reports

CREATE DATABASE IF NOT EXISTS ScamReports;

USE ScamReports;

-- Table to store user-reported scams
CREATE TABLE IF NOT EXISTS ScamReports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each report
    reported_phone_number VARCHAR(15),                -- Phone number involved in the scam (if available)
    reported_bank_account VARCHAR(50),                -- Bank account used in the scam (if available)
    reported_name VARCHAR(100),                       -- Name associated with the scam (if available)
    transaction_details TEXT,                         -- Details about the transaction or scam
    date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Date and time the report was created
    reporter_email VARCHAR(100),                     -- Email of the person reporting the scam (optional)
    reporter_ip_address VARCHAR(45),                 -- IP address of the reporter (optional)
    status ENUM('Pending', 'Resolved') DEFAULT 'Pending', -- Status of the report (Pending/Resolved)
    notes TEXT                                        -- Admin notes or comments about the report
);

-- Indexes to improve query performance
CREATE INDEX idx_phone_number ON ScamReports (reported_phone_number);
CREATE INDEX idx_bank_account ON ScamReports (reported_bank_account);

-- Insert a sample record for testing
INSERT INTO ScamReports (
    reported_phone_number,
    reported_bank_account,
    reported_name,
    transaction_details,
    reporter_email,
    reporter_ip_address,
    status,
    notes
) VALUES (
    '123-456-7890',
    '1234567890',
    'John Doe',
    'The scam involved a fraudulent money transfer of $500.',
    'reporter@example.com',
    '192.168.1.1',
    'Pending',
    'Initial report awaiting review'
);

-- Select all reports to verify the schema
SELECT * FROM ScamReports;
```
