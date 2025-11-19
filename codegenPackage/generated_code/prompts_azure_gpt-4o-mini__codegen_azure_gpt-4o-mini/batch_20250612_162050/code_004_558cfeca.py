"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Design a database schema for storing information about residents in a Kallimos community, ensuring it supports multi-generational and multi-ability inclusivity.
Generated: DETERMINISTIC_558cfecaa0260f13
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kallimos community residents

CREATE TABLE Residents (
    resident_id SERIAL PRIMARY KEY, -- Unique identifier for each resident
    first_name VARCHAR(50) NOT NULL, -- Resident's first name
    last_name VARCHAR(50) NOT NULL, -- Resident's last name
    date_of_birth DATE NOT NULL, -- Resident's date of birth
    gender VARCHAR(10), -- Resident's gender
    address VARCHAR(255) NOT NULL, -- Resident's address
    phone_number VARCHAR(15), -- Resident's phone number
    email VARCHAR(100), -- Resident's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Abilities (
    ability_id SERIAL PRIMARY KEY, -- Unique identifier for each ability
    ability_name VARCHAR(100) NOT NULL UNIQUE -- Name of the ability (e.g., "Visual Impairment", "Hearing Impairment")
);

CREATE TABLE ResidentAbilities (
    resident_ability_id SERIAL PRIMARY KEY, -- Unique identifier for the resident-ability relationship
    resident_id INT NOT NULL, -- Foreign key referencing Residents
    ability_id INT NOT NULL, -- Foreign key referencing Abilities
    FOREIGN KEY (resident_id) REFERENCES Residents(resident_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ability_id) REFERENCES Abilities(ability_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE FamilyGroups (
    family_group_id SERIAL PRIMARY KEY, -- Unique identifier for each family group
    group_name VARCHAR(100) NOT NULL, -- Name of the family group
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE FamilyMembers (
    family_member_id SERIAL PRIMARY KEY, -- Unique identifier for each family member
    family_group_id INT NOT NULL, -- Foreign key referencing FamilyGroups
    resident_id INT NOT NULL, -- Foreign key referencing Residents
    relationship VARCHAR(50), -- Relationship to the family group (e.g., "Parent", "Child", "Sibling")
    FOREIGN KEY (family_group_id) REFERENCES FamilyGroups(family_group_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (resident_id) REFERENCES Residents(resident_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_resident_last_name ON Residents(last_name);
CREATE INDEX idx_family_group_name ON FamilyGroups(group_name);
CREATE INDEX idx_ability_name ON Abilities(ability_name);
```
