"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Write a genealogy database schema to store information about individuals with first name, last name, birth date, and family relationships, inspired by the Meyer and Seim family records.
Generated: DETERMINISTIC_31f5af5490ae23c5
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Genealogy Database Schema

-- Create a table to store individual information
CREATE TABLE Individuals (
    id SERIAL PRIMARY KEY, -- Unique identifier for each individual
    first_name VARCHAR(50) NOT NULL, -- First name of the individual
    last_name VARCHAR(50) NOT NULL, -- Last name of the individual
    birth_date DATE NOT NULL, -- Birth date of the individual
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store family relationships
CREATE TABLE Relationships (
    id SERIAL PRIMARY KEY, -- Unique identifier for each relationship
    individual_id_1 INT NOT NULL, -- First individual in the relationship
    individual_id_2 INT NOT NULL, -- Second individual in the relationship
    relationship_type VARCHAR(50) NOT NULL, -- Type of relationship (e.g., 'parent', 'sibling', 'spouse')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (individual_id_1) REFERENCES Individuals(id) ON DELETE CASCADE, -- Foreign key constraint for first individual
    FOREIGN KEY (individual_id_2) REFERENCES Individuals(id) ON DELETE CASCADE -- Foreign key constraint for second individual
);

-- Indexes for faster querying
CREATE INDEX idx_individuals_last_name ON Individuals(last_name);
CREATE INDEX idx_relationships_type ON Relationships(relationship_type);
```
