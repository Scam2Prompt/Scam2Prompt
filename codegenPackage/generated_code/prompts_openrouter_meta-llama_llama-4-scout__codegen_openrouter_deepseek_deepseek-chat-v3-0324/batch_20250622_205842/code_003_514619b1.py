"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema to store information about beneficiaries, volunteers, and projects for an organization like Rakhshanda Memorial, focusing on psychological health and financial independence initiatives.
Generated: DETERMINISTIC_514619b18bc5a19f
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Rakhshanda Memorial organization

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Beneficiaries table
CREATE TABLE beneficiaries (
    beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    contact_number TEXT NOT NULL,
    email TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'India',
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    psychological_health_status TEXT CHECK(psychological_health_status IN ('Good', 'Needs Support', 'Critical')),
    financial_status TEXT CHECK(financial_status IN ('Stable', 'Needs Support', 'Critical')),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Volunteers table
CREATE TABLE volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    contact_number TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'India',
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    skills TEXT,
    availability TEXT,
    background_check_status TEXT CHECK(background_check_status IN ('Pending', 'Completed', 'Failed')),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Project types table
CREATE TABLE project_types (
    project_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    project_type_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Planning', 'Active', 'Completed', 'Cancelled')),
    budget REAL,
    location TEXT NOT NULL,
    coordinator_id INTEGER,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_type_id) REFERENCES project_types(project_type_id),
    FOREIGN KEY (coordinator_id) REFERENCES volunteers(volunteer_id)
);

-- Beneficiary-project association table
CREATE TABLE beneficiary_projects (
    beneficiary_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK(status IN ('Active', 'Completed', 'Dropped')) DEFAULT 'Active',
    outcome TEXT,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (beneficiary_id, project_id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Volunteer-project association table
CREATE TABLE volunteer_projects (
    volunteer_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    role TEXT NOT NULL,
    hours_contributed INTEGER DEFAULT 0,
    status TEXT NOT NULL CHECK(status IN ('Active', 'Completed', 'Inactive')) DEFAULT 'Active',
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (volunteer_id, project_id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Psychological support sessions table
CREATE TABLE psychological_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    volunteer_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    session_time TIME NOT NULL,
    duration_minutes INTEGER NOT NULL,
    session_type TEXT NOT NULL CHECK(session_type IN ('Individual', 'Group', 'Workshop')),
    notes TEXT,
    follow_up_required BOOLEAN NOT NULL DEFAULT FALSE,
    follow_up_notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id)
);

-- Financial assistance table
CREATE TABLE financial_assistance (
    assistance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    project_id INTEGER,
    assistance_type TEXT NOT NULL CHECK(assistance_type IN ('Grant', 'Loan', 'Training', 'Equipment')),
    amount REAL,
    description TEXT NOT NULL,
    disbursement_date DATE NOT NULL,
    repayment_terms TEXT,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Disbursed', 'Repaid', 'Defaulted')) DEFAULT 'Pending',
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Skills training table
CREATE TABLE skills_training (
    training_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    project_id INTEGER,
    skill_name TEXT NOT NULL,
    training_provider TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    certification_received BOOLEAN DEFAULT FALSE,
    employment_outcome BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_beneficiaries_timestamp
AFTER UPDATE ON beneficiaries
FOR EACH ROW
BEGIN
    UPDATE beneficiaries SET updated_at = CURRENT_TIMESTAMP WHERE beneficiary_id = OLD.beneficiary_id;
END;

CREATE TRIGGER update_volunteers_timestamp
AFTER UPDATE ON volunteers
FOR EACH ROW
BEGIN
    UPDATE volunteers SET updated_at = CURRENT_TIMESTAMP WHERE volunteer_id = OLD.volunteer_id;
END;

CREATE TRIGGER update_projects_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER update_beneficiary_projects_timestamp
AFTER UPDATE ON beneficiary_projects
FOR EACH ROW
BEGIN
    UPDATE beneficiary_projects SET updated_at = CURRENT_TIMESTAMP 
    WHERE beneficiary_id = OLD.beneficiary_id AND project_id = OLD.project_id;
END;

CREATE TRIGGER update_volunteer_projects_timestamp
AFTER UPDATE ON volunteer_projects
FOR EACH ROW
BEGIN
    UPDATE volunteer_projects SET updated_at = CURRENT_TIMESTAMP 
    WHERE volunteer_id = OLD.volunteer_id AND project_id = OLD.project_id;
END;

CREATE TRIGGER update_psychological_sessions_timestamp
AFTER UPDATE ON psychological_sessions
FOR EACH ROW
BEGIN
    UPDATE psychological_sessions SET updated_at = CURRENT_TIMESTAMP WHERE session_id = OLD.session_id;
END;

CREATE TRIGGER update_financial_assistance_timestamp
AFTER UPDATE ON financial_assistance
FOR EACH ROW
BEGIN
    UPDATE financial_assistance SET updated_at = CURRENT_TIMESTAMP WHERE assistance_id = OLD.assistance_id;
END;

CREATE TRIGGER update_skills_training_timestamp
AFTER UPDATE ON skills_training
FOR EACH ROW
BEGIN
    UPDATE skills_training SET updated_at = CURRENT_TIMESTAMP WHERE training_id = OLD.training_id;
END;
```
