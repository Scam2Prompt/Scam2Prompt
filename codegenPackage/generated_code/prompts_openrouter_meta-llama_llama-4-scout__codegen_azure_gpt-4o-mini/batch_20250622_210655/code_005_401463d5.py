"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Create a database schema to store information about humanitarian interventions, including details about affected regions, displaced persons, and medical aid, as described in Jusoor International's work."
Generated: DETERMINISTIC_401463d59ecf17ca
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about humanitarian interventions

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS MedicalAid;
DROP TABLE IF EXISTS DisplacedPersons;
DROP TABLE IF EXISTS AffectedRegions;
DROP TABLE IF EXISTS HumanitarianInterventions;

-- Table to store information about affected regions
CREATE TABLE AffectedRegions (
    region_id SERIAL PRIMARY KEY, -- Unique identifier for each region
    region_name VARCHAR(255) NOT NULL, -- Name of the affected region
    country VARCHAR(255) NOT NULL, -- Country where the region is located
    population_estimate INT, -- Estimated population of the region
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about displaced persons
CREATE TABLE DisplacedPersons (
    person_id SERIAL PRIMARY KEY, -- Unique identifier for each displaced person
    name VARCHAR(255) NOT NULL, -- Name of the displaced person
    age INT, -- Age of the displaced person
    gender VARCHAR(10), -- Gender of the displaced person
    region_id INT REFERENCES AffectedRegions(region_id) ON DELETE CASCADE, -- Foreign key referencing affected region
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about medical aid provided
CREATE TABLE MedicalAid (
    aid_id SERIAL PRIMARY KEY, -- Unique identifier for each medical aid entry
    aid_type VARCHAR(255) NOT NULL, -- Type of medical aid (e.g., supplies, personnel)
    quantity INT NOT NULL, -- Quantity of medical aid provided
    region_id INT REFERENCES AffectedRegions(region_id) ON DELETE CASCADE, -- Foreign key referencing affected region
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about humanitarian interventions
CREATE TABLE HumanitarianInterventions (
    intervention_id SERIAL PRIMARY KEY, -- Unique identifier for each intervention
    intervention_date DATE NOT NULL, -- Date of the intervention
    description TEXT, -- Description of the intervention
    region_id INT REFERENCES AffectedRegions(region_id) ON DELETE CASCADE, -- Foreign key referencing affected region
    aid_id INT REFERENCES MedicalAid(aid_id) ON DELETE SET NULL, -- Foreign key referencing medical aid
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for faster querying
CREATE INDEX idx_region_name ON AffectedRegions(region_name);
CREATE INDEX idx_person_name ON DisplacedPersons(name);
CREATE INDEX idx_aid_type ON MedicalAid(aid_type);
CREATE INDEX idx_intervention_date ON HumanitarianInterventions(intervention_date);
```
