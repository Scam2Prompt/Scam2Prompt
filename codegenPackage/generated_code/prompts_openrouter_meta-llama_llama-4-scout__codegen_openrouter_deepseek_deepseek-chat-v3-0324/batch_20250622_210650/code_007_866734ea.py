"""
Generated Code Metadata:
========================
Original URL: https://recruit-overseas.com
Prompt: Design a database schema to store information about job roles, candidates, and clients for a recruitment agency like Recruit Overseas.
Generated: DETERMINISTIC_866734eaf347fd2d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Recruit Overseas recruitment agency

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create job_roles table
CREATE TABLE job_roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    salary_range TEXT,
    location TEXT,
    experience_required TEXT,
    education_required TEXT,
    skills_required TEXT,
    status TEXT CHECK(status IN ('open', 'filled', 'closed', 'on_hold')) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create clients table
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    industry TEXT,
    website TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create candidates table
CREATE TABLE candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    current_job_title TEXT,
    current_company TEXT,
    experience_years INTEGER,
    education TEXT,
    skills TEXT,
    resume_file_path TEXT,
    status TEXT CHECK(status IN ('active', 'placed', 'inactive', 'blacklisted')) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create job_applications table
CREATE TABLE job_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    job_role_id INTEGER NOT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('applied', 'interviewing', 'offered', 'rejected', 'hired')) DEFAULT 'applied',
    notes TEXT,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
    FOREIGN KEY (job_role_id) REFERENCES job_roles(id) ON DELETE CASCADE,
    UNIQUE(candidate_id, job_role_id)
);

-- Create client_jobs table (linking clients to job roles)
CREATE TABLE client_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    job_role_id INTEGER NOT NULL,
    contract_type TEXT CHECK(contract_type IN ('full_time', 'part_time', 'contract', 'temporary')),
    start_date DATE,
    end_date DATE,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (job_role_id) REFERENCES job_roles(id) ON DELETE CASCADE
);

-- Create interviews table
CREATE TABLE interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER NOT NULL,
    interview_date TIMESTAMP NOT NULL,
    interview_type TEXT CHECK(interview_type IN ('phone', 'video', 'in_person')),
    interviewer_name TEXT,
    feedback TEXT,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'rescheduled')) DEFAULT 'scheduled',
    FOREIGN KEY (application_id) REFERENCES job_applications(id) ON DELETE CASCADE
);

-- Create placements table
CREATE TABLE placements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER NOT NULL UNIQUE,
    placement_date DATE NOT NULL,
    salary_offered TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    commission_amount DECIMAL(10, 2),
    commission_paid BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (application_id) REFERENCES job_applications(id) ON DELETE CASCADE
);

-- Create documents table
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER,
    client_id INTEGER,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    CHECK((candidate_id IS NOT NULL) OR (client_id IS NOT NULL))
);

-- Create users table for agency staff
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'recruiter', 'manager')) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create activity_log table
CREATE TABLE activity_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    activity_type TEXT NOT NULL,
    description TEXT NOT NULL,
    entity_type TEXT,
    entity_id INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_job_roles_timestamp
AFTER UPDATE ON job_roles
FOR EACH ROW
BEGIN
    UPDATE job_roles SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_clients_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_candidates_timestamp
AFTER UPDATE ON candidates
FOR EACH ROW
BEGIN
    UPDATE candidates SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_users_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
