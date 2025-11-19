"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Design a database schema for managing member information and benefits for an association like AFUNABB Chillán, focusing on community engagement and support.
Generated: DETERMINISTIC_e7cb8bccf11a9f6b
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing member information and benefits for an association

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS MemberBenefits;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Benefits;

-- Table to store member information
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY, -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL, -- Member's first name
    last_name VARCHAR(50) NOT NULL, -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    phone_number VARCHAR(15), -- Member's phone number
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the member joined
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'suspended')) DEFAULT 'active' -- Member status
);

-- Table to store benefits offered by the association
CREATE TABLE Benefits (
    benefit_id SERIAL PRIMARY KEY, -- Unique identifier for each benefit
    benefit_name VARCHAR(100) NOT NULL, -- Name of the benefit
    description TEXT, -- Description of the benefit
    eligibility_criteria TEXT, -- Criteria for eligibility for the benefit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the benefit was created
);

-- Table to manage the relationship between members and benefits
CREATE TABLE MemberBenefits (
    member_benefit_id SERIAL PRIMARY KEY, -- Unique identifier for each member-benefit relationship
    member_id INT NOT NULL, -- Foreign key referencing Members
    benefit_id INT NOT NULL, -- Foreign key referencing Benefits
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the benefit was assigned to the member
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (benefit_id) REFERENCES Benefits(benefit_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_benefit_name ON Benefits(benefit_name);
CREATE INDEX idx_member_benefit ON MemberBenefits(member_id, benefit_id);

-- Sample data insertion (for demonstration purposes)
INSERT INTO Members (first_name, last_name, email, phone_number) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321');

INSERT INTO Benefits (benefit_name, description, eligibility_criteria) VALUES
('Discount on Events', 'Members receive a 20% discount on all events.', 'Must be an active member.'),
('Monthly Newsletter', 'Receive updates and news about the association.', 'All members.');

INSERT INTO MemberBenefits (member_id, benefit_id) VALUES
(1, 1), -- John Doe receives Discount on Events
(2, 2); -- Jane Smith receives Monthly Newsletter
```
