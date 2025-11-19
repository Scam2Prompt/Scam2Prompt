"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Provide an example of a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust, including fields for recipient details, grant purpose, and funding amount.
Generated: DETERMINISTIC_6d44cea6f84fd7c7
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust

CREATE TABLE Recipients (
    recipient_id SERIAL PRIMARY KEY, -- Unique identifier for each recipient
    name VARCHAR(255) NOT NULL, -- Name of the recipient organization or individual
    contact_email VARCHAR(255), -- Contact email for the recipient
    phone_number VARCHAR(20), -- Contact phone number for the recipient
    address TEXT, -- Address of the recipient
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the recipient was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the recipient was last updated
);

CREATE TABLE Grants (
    grant_id SERIAL PRIMARY KEY, -- Unique identifier for each grant
    recipient_id INT NOT NULL, -- Foreign key referencing the recipient
    purpose TEXT NOT NULL, -- Purpose of the grant
    funding_amount DECIMAL(15, 2) NOT NULL CHECK (funding_amount > 0), -- Amount of funding awarded
    grant_date DATE NOT NULL, -- Date the grant was awarded
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the grant (e.g., Pending, Approved, Denied)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the grant was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the grant was last updated
    FOREIGN KEY (recipient_id) REFERENCES Recipients(recipient_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_recipient_name ON Recipients(name);
CREATE INDEX idx_grant_status ON Grants(status);
CREATE INDEX idx_grant_date ON Grants(grant_date);
```
