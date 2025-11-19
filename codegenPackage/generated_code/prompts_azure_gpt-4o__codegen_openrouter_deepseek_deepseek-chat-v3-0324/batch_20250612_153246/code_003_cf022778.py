"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Suggest a database schema for storing information about Morahs and their placement options, as described by ZKCS.
Generated: DETERMINISTIC_cf022778168eb17c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Morahs and their placement options

-- Table to store Morah information
CREATE TABLE morahs (
    morah_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    years_experience INTEGER,
    certification_status VARCHAR(50),
    preferred_grade_levels VARCHAR(100),
    preferred_subjects VARCHAR(200),
    availability_status VARCHAR(50) DEFAULT 'Available',
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store schools/institutions
CREATE TABLE institutions (
    institution_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20),
    contact_name VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    institution_type VARCHAR(50),
    grade_levels VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store placement options
CREATE TABLE placement_options (
    placement_id SERIAL PRIMARY KEY,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    position_title VARCHAR(100) NOT NULL,
    grade_level VARCHAR(50),
    subject_area VARCHAR(100),
    hours_per_week INTEGER,
    start_date DATE,
    end_date DATE,
    compensation_type VARCHAR(50),
    compensation_amount DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    requirements TEXT,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for Morah-Placement matches
CREATE TABLE morah_placements (
    morah_placement_id SERIAL PRIMARY KEY,
    morah_id INTEGER REFERENCES morahs(morah_id) ON DELETE CASCADE,
    placement_id INTEGER REFERENCES placement_options(placement_id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- e.g., Pending, Approved, Rejected, Completed
    match_score INTEGER, -- Numeric score representing match quality
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(morah_id, placement_id)
);

-- Table to store interview/meeting records
CREATE TABLE interviews (
    interview_id SERIAL PRIMARY KEY,
    morah_placement_id INTEGER REFERENCES morah_placements(morah_placement_id) ON DELETE CASCADE,
    interview_date TIMESTAMP WITH TIME ZONE NOT NULL,
    interviewer_name VARCHAR(100),
    interview_notes TEXT,
    outcome VARCHAR(50), -- e.g., Successful, Unsuccessful, Pending
    follow_up_actions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store user accounts for system access
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100),
    role VARCHAR(50) NOT NULL, -- e.g., Admin, Coordinator, Viewer
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for audit logging
CREATE TABLE audit_logs (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    action_type VARCHAR(50) NOT NULL, -- e.g., CREATE, UPDATE, DELETE
    table_name VARCHAR(50) NOT NULL,
    record_id INTEGER,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(50),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_morahs_availability ON morahs(availability_status);
CREATE INDEX idx_placements_institution ON placement_options(institution_id);
CREATE INDEX idx_placements_active ON placement_options(is_active);
CREATE INDEX idx_morah_placements_status ON morah_placements(status);
CREATE INDEX idx_morah_placements_morah ON morah_placements(morah_id);
CREATE INDEX idx_morah_placements_placement ON morah_placements(placement_id);
```
