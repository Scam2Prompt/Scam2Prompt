"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Provide an example of a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust, including fields for recipient details, grant purpose, and funding amount.
Generated: DETERMINISTIC_6d44cea6f84fd7c7
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust

CREATE TABLE Recipients (
    recipient_id SERIAL PRIMARY KEY,          -- Unique identifier for each recipient
    name VARCHAR(255) NOT NULL,               -- Name of the recipient organization or individual
    contact_person VARCHAR(255),               -- Name of the contact person at the recipient organization
    email VARCHAR(255),                        -- Email address for the contact person
    phone_number VARCHAR(20),                  -- Phone number for the contact person
    address TEXT,                              -- Address of the recipient organization
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp when the record was last updated
);

CREATE TABLE Grants (
    grant_id SERIAL PRIMARY KEY,               -- Unique identifier for each grant
    recipient_id INT NOT NULL,                 -- Foreign key referencing the recipient
    grant_purpose TEXT NOT NULL,               -- Purpose of the grant
    funding_amount DECIMAL(10, 2) NOT NULL,   -- Amount of funding awarded
    date_awarded DATE NOT NULL,                -- Date when the grant was awarded
    status VARCHAR(50) DEFAULT 'Pending',      -- Status of the grant (e.g., Pending, Approved, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    CONSTRAINT fk_recipient FOREIGN KEY (recipient_id) REFERENCES Recipients(recipient_id) 
        ON DELETE CASCADE                        -- Cascade delete grants if a recipient is deleted
);

-- Ensure to add necessary indexes for better performance
CREATE INDEX idx_recipient_name ON Recipients(name);
CREATE INDEX idx_grant_date ON Grants(date_awarded);
CREATE INDEX idx_grant_status ON Grants(status);
```
