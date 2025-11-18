"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Create a database schema for managing RM's projects, including tables for tracking beneficiaries, volunteers, donations, and event schedules.
Generated: DETERMINISTIC_657f750a50ed29cc
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for managing RM's projects

-- Table: projects
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    name VARCHAR(255) NOT NULL, -- Name of the project
    description TEXT, -- Detailed description of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    status VARCHAR(50) NOT NULL -- Status: e.g., 'Active', 'Completed', 'On Hold'
);

-- Table: beneficiaries
CREATE TABLE beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique ID for each beneficiary
    name VARCHAR(255) NOT NULL, -- Name of the beneficiary
    contact_info VARCHAR(255), -- Contact info of the beneficiary
    project_id INT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE -- Associated project
);

-- Table: volunteers
CREATE TABLE volunteers (
    volunteer_id SERIAL PRIMARY KEY, -- Unique ID for each volunteer
    name VARCHAR(255) NOT NULL, -- Name of the volunteer
    contact_info VARCHAR(255), -- Contact info of the volunteer
    project_id INT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE -- Associated project
);

-- Table: donations
CREATE TABLE donations (
    donation_id SERIAL PRIMARY KEY, -- Unique ID for each donation
    amount DECIMAL(10, 2) NOT NULL, -- Amount of donation
    donor_name VARCHAR(255), -- Name of the donor (nullable)
    donation_date DATE NOT NULL, -- Date of donation
    project_id INT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE -- Associated project
);

-- Table: event_schedules
CREATE TABLE event_schedules (
    event_id SERIAL PRIMARY KEY, -- Unique ID for each event
    project_id INT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE, -- Associated project
    event_name VARCHAR(255) NOT NULL, -- Name of the event
    event_date DATE NOT NULL, -- Date of the event
    location VARCHAR(255), -- Location of the event
    description TEXT -- Detailed description of the event
);

-- Additional indexes for efficient lookups
CREATE INDEX idx_project_id_beneficiaries ON beneficiaries(project_id);
CREATE INDEX idx_project_id_volunteers ON volunteers(project_id);
CREATE INDEX idx_project_id_donations ON donations(project_id);
CREATE INDEX idx_project_id_event_schedules ON event_schedules(project_id);

-- End of schema
```
