"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Design a database schema for storing information about tennis club members, their membership types, and contributions, and provide SQL code to create the schema.
Generated: DETERMINISTIC_34c8936850902a5e
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Tennis Club

-- Table to store information about members
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,          -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL,      -- Member's first name
    last_name VARCHAR(50) NOT NULL,       -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL,    -- Member's email address (unique)
    phone_number VARCHAR(15),               -- Member's phone number
    membership_type_id INT NOT NULL,       -- Foreign key to MembershipTypes
    join_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date when the member joined
    status VARCHAR(20) NOT NULL DEFAULT 'active', -- Membership status (active, inactive)
    CONSTRAINT fk_membership_type FOREIGN KEY (membership_type_id) 
        REFERENCES MembershipTypes(membership_type_id) 
        ON DELETE CASCADE                     -- Delete members if membership type is deleted
);

-- Table to store different types of memberships
CREATE TABLE MembershipTypes (
    membership_type_id SERIAL PRIMARY KEY,  -- Unique identifier for each membership type
    type_name VARCHAR(50) NOT NULL UNIQUE,   -- Name of the membership type (e.g., 'Annual', 'Monthly')
    description TEXT,                         -- Description of the membership type
    fee DECIMAL(10, 2) NOT NULL               -- Fee associated with the membership type
);

-- Table to store contributions made by members
CREATE TABLE Contributions (
    contribution_id SERIAL PRIMARY KEY,       -- Unique identifier for each contribution
    member_id INT NOT NULL,                   -- Foreign key to Members
    amount DECIMAL(10, 2) NOT NULL,           -- Amount contributed
    contribution_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of contribution
    description TEXT,                         -- Description of the contribution
    CONSTRAINT fk_member FOREIGN KEY (member_id) 
        REFERENCES Members(member_id) 
        ON DELETE CASCADE                      -- Delete contributions if the member is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_contribution_date ON Contributions(contribution_date);
```
