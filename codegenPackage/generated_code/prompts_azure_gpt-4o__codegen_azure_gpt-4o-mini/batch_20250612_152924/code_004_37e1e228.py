"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Create a database schema for tracking pharmacy member benefits, including profit sharing, transparency, and accountability, based on the cooperative model described by PharmaChoice Canada.
Generated: DETERMINISTIC_37e1e22800cfd834
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking pharmacy member benefits based on the cooperative model

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Benefits;
DROP TABLE IF EXISTS ProfitSharing;
DROP TABLE IF EXISTS Transactions;

-- Table to store member information
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY, -- Unique identifier for each member
    name VARCHAR(100) NOT NULL, -- Member's name
    email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the member joined
    status VARCHAR(20) DEFAULT 'active' -- Status of the member (active, inactive)
);

-- Table to store different types of benefits available to members
CREATE TABLE Benefits (
    benefit_id SERIAL PRIMARY KEY, -- Unique identifier for each benefit
    benefit_name VARCHAR(100) NOT NULL, -- Name of the benefit
    description TEXT, -- Description of the benefit
    eligibility_criteria TEXT -- Criteria for eligibility for the benefit
);

-- Table to track profit sharing among members
CREATE TABLE ProfitSharing (
    profit_sharing_id SERIAL PRIMARY KEY, -- Unique identifier for each profit sharing record
    member_id INT NOT NULL, -- Foreign key referencing Members
    benefit_id INT NOT NULL, -- Foreign key referencing Benefits
    profit_amount DECIMAL(10, 2) NOT NULL, -- Amount of profit shared
    sharing_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of profit sharing
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (benefit_id) REFERENCES Benefits(benefit_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to track transactions related to benefits
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    member_id INT NOT NULL, -- Foreign key referencing Members
    benefit_id INT NOT NULL, -- Foreign key referencing Benefits
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    amount DECIMAL(10, 2) NOT NULL, -- Amount involved in the transaction
    status VARCHAR(20) DEFAULT 'completed', -- Status of the transaction (completed, pending, failed)
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (benefit_id) REFERENCES Benefits(benefit_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_benefit_name ON Benefits(benefit_name);
CREATE INDEX idx_transaction_date ON Transactions(transaction_date);
```
