"""
Generated Code Metadata:
========================
Original URL: https://conseil-consultatif-femme.cg
Prompt: "Design a simple database schema for storing information about organizations focused on women's rights, inspired by the structure and mission of the Conseil Consultatif de la Femme."
Generated: DETERMINISTIC_5c434b16e0228613
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about organizations focused on women's rights

-- Create a database named 'women_rights_organizations'
CREATE DATABASE women_rights_organizations;

-- Use the created database
USE women_rights_organizations;

-- Table to store information about organizations
CREATE TABLE organizations (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each organization
    name VARCHAR(255) NOT NULL, -- Name of the organization
    mission TEXT NOT NULL, -- Mission statement of the organization
    website VARCHAR(255), -- Website URL of the organization
    contact_email VARCHAR(255), -- Contact email for the organization
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the record was last updated
);

-- Table to store information about members of the organizations
CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    organization_id INT NOT NULL, -- Foreign key referencing the organization
    name VARCHAR(255) NOT NULL, -- Name of the member
    role VARCHAR(100), -- Role of the member within the organization
    email VARCHAR(255), -- Email of the member
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the member joined
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store events organized by the organizations
CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    organization_id INT NOT NULL, -- Foreign key referencing the organization
    title VARCHAR(255) NOT NULL, -- Title of the event
    description TEXT, -- Description of the event
    event_date DATETIME NOT NULL, -- Date and time of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of when the record was last updated
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store donations made to the organizations
CREATE TABLE donations (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    organization_id INT NOT NULL, -- Foreign key referencing the organization
    donor_name VARCHAR(255) NOT NULL, -- Name of the donor
    amount DECIMAL(10, 2) NOT NULL, -- Amount donated
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the donation was made
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_organization_name ON organizations(name);
CREATE INDEX idx_member_email ON members(email);
CREATE INDEX idx_event_date ON events(event_date);
CREATE INDEX idx_donation_date ON donations(donation_date);
```
