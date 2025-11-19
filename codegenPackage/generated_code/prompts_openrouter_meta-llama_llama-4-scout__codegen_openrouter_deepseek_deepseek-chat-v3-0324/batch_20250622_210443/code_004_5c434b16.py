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
-- SQL script to create a database schema for women's rights organizations
-- Inspired by Conseil Consultatif de la Femme structure

-- Create database
CREATE DATABASE IF NOT EXISTS womens_rights_organizations;
USE womens_rights_organizations;

-- Organizations table
CREATE TABLE IF NOT EXISTS organizations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    acronym VARCHAR(50),
    description TEXT,
    founding_date DATE,
    headquarters_location VARCHAR(255),
    website_url VARCHAR(255),
    email VARCHAR(100),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Organization focus areas (many-to-many relationship)
CREATE TABLE IF NOT EXISTS focus_areas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Junction table for organization-focus area relationship
CREATE TABLE IF NOT EXISTS organization_focus_areas (
    organization_id INT NOT NULL,
    focus_area_id INT NOT NULL,
    PRIMARY KEY (organization_id, focus_area_id),
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE,
    FOREIGN KEY (focus_area_id) REFERENCES focus_areas(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Organization members table
CREATE TABLE IF NOT EXISTS members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    join_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE,
    CONSTRAINT chk_member_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status ENUM('planned', 'ongoing', 'completed', 'cancelled') DEFAULT 'planned',
    budget DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR start_date <= end_date)
) ENGINE=InnoDB;

-- Events table
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    start_time TIME,
    end_time TIME,
    location VARCHAR(255),
    is_virtual BOOLEAN DEFAULT FALSE,
    registration_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE,
    CONSTRAINT chk_event_times CHECK (end_time IS NULL OR start_time <= end_time)
) ENGINE=InnoDB;

-- Resources table (publications, reports, etc.)
CREATE TABLE IF NOT EXISTS resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    type ENUM('report', 'publication', 'video', 'podcast', 'other') NOT NULL,
    publication_date DATE,
    file_url VARCHAR(255),
    external_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Partners table (other organizations this org collaborates with)
CREATE TABLE IF NOT EXISTS partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT NOT NULL,
    partner_name VARCHAR(255) NOT NULL,
    partner_type ENUM('ngo', 'government', 'private', 'academic', 'other') NOT NULL,
    description TEXT,
    partnership_start_date DATE,
    partnership_end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE,
    CONSTRAINT chk_partnership_dates CHECK (partnership_end_date IS NULL OR partnership_start_date <= partnership_end_date)
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_org_name ON organizations(name);
CREATE INDEX idx_member_name ON members(last_name, first_name);
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_event_date ON events(event_date);
CREATE INDEX idx_resource_type ON resources(type);
```
