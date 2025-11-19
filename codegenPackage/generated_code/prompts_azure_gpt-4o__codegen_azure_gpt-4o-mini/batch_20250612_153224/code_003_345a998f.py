"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Provide an example of a database schema for managing governance policies and organizational decisions, inspired by the "الحوكمة السياسات واللوائح" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_345a998f4a95907b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing governance policies and organizational decisions

CREATE TABLE Organizations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each organization
    name VARCHAR(255) NOT NULL, -- Name of the organization
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the organization was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE Policies (
    id SERIAL PRIMARY KEY, -- Unique identifier for each policy
    organization_id INT NOT NULL, -- Foreign key referencing the Organizations table
    title VARCHAR(255) NOT NULL, -- Title of the policy
    description TEXT, -- Detailed description of the policy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the policy was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (organization_id) REFERENCES Organizations(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Decisions (
    id SERIAL PRIMARY KEY, -- Unique identifier for each decision
    policy_id INT NOT NULL, -- Foreign key referencing the Policies table
    decision_maker VARCHAR(255) NOT NULL, -- Name of the person or group making the decision
    decision_date TIMESTAMP NOT NULL, -- Date when the decision was made
    outcome TEXT, -- Outcome of the decision
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the decision was recorded
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (policy_id) REFERENCES Policies(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Compliance (
    id SERIAL PRIMARY KEY, -- Unique identifier for each compliance record
    policy_id INT NOT NULL, -- Foreign key referencing the Policies table
    compliance_status VARCHAR(50) NOT NULL, -- Status of compliance (e.g., 'Compliant', 'Non-Compliant')
    compliance_date TIMESTAMP NOT NULL, -- Date of compliance check
    notes TEXT, -- Additional notes regarding compliance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the compliance record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (policy_id) REFERENCES Policies(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_organization_name ON Organizations(name);
CREATE INDEX idx_policy_title ON Policies(title);
CREATE INDEX idx_decision_maker ON Decisions(decision_maker);
CREATE INDEX idx_compliance_status ON Compliance(compliance_status);
```
