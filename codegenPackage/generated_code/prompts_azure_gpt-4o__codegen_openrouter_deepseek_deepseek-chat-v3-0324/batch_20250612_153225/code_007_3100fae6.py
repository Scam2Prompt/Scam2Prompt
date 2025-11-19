"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Recommend a database schema for storing DBT therapy session details, including individual and group sessions, participant age groups, and progress milestones, based on the structure outlined on the Mente Sana Psicología site.
Generated: DETERMINISTIC_3100fae6081e5795
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for DBT Therapy Sessions

```sql
-- Database schema for DBT therapy sessions management
-- Supports individual/group sessions, participant tracking, and progress milestones

CREATE TABLE participants (
    participant_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    active_status BOOLEAN NOT NULL DEFAULT TRUE,
    notes TEXT,
    CHECK (contact_phone IS NOT NULL OR contact_email IS NOT NULL)
);

CREATE TABLE age_groups (
    age_group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL UNIQUE,
    min_age INTEGER NOT NULL,
    max_age INTEGER NOT NULL,
    description TEXT,
    CHECK (min_age <= max_age)
);

CREATE TABLE therapists (
    therapist_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    specialization VARCHAR(100),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100) NOT NULL,
    active_status BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE session_types (
    session_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    is_group_session BOOLEAN NOT NULL,
    max_participants INTEGER,
    CHECK ((is_group_session = TRUE AND max_participants > 1) OR 
           (is_group_session = FALSE AND max_participants IS NULL))
);

CREATE TABLE therapy_sessions (
    session_id SERIAL PRIMARY KEY,
    session_type_id INTEGER NOT NULL REFERENCES session_types(session_type_id),
    therapist_id INTEGER NOT NULL REFERENCES therapists(therapist_id),
    session_date TIMESTAMP NOT NULL,
    location VARCHAR(100),
    notes TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'SCHEDULED',
    CHECK (status IN ('SCHEDULED', 'COMPLETED', 'CANCELLED', 'RESCHEDULED'))
);

CREATE TABLE session_participants (
    session_participant_id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES therapy_sessions(session_id),
    participant_id INTEGER NOT NULL REFERENCES participants(participant_id),
    attendance_status VARCHAR(20) NOT NULL DEFAULT 'REGISTERED',
    notes TEXT,
    CHECK (attendance_status IN ('REGISTERED', 'ATTENDED', 'NO_SHOW', 'CANCELLED')),
    UNIQUE (session_id, participant_id)
);

CREATE TABLE dbt_modules (
    module_id SERIAL PRIMARY KEY,
    module_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    recommended_order INTEGER NOT NULL UNIQUE
);

CREATE TABLE progress_milestones (
    milestone_id SERIAL PRIMARY KEY,
    participant_id INTEGER NOT NULL REFERENCES participants(participant_id),
    module_id INTEGER NOT NULL REFERENCES dbt_modules(module_id),
    achieved_date DATE NOT NULL DEFAULT CURRENT_DATE,
    therapist_id INTEGER NOT NULL REFERENCES therapists(therapist_id),
    notes TEXT,
    proficiency_level VARCHAR(20) NOT NULL,
    CHECK (proficiency_level IN ('BEGINNER', 'INTERMEDIATE', 'ADVANCED', 'MASTERED'))
);

CREATE TABLE participant_age_groups (
    participant_id INTEGER NOT NULL REFERENCES participants(participant_id),
    age_group_id INTEGER NOT NULL REFERENCES age_groups(age_group_id),
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (participant_id, age_group_id)
);

CREATE TABLE session_materials (
    material_id SERIAL PRIMARY KEY,
    session_type_id INTEGER REFERENCES session_types(session_type_id),
    module_id INTEGER REFERENCES dbt_modules(module_id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (session_type_id IS NOT NULL OR module_id IS NOT NULL)
);

CREATE TABLE treatment_plans (
    plan_id SERIAL PRIMARY KEY,
    participant_id INTEGER NOT NULL REFERENCES participants(participant_id),
    therapist_id INTEGER NOT NULL REFERENCES therapists(therapist_id),
    start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    end_date DATE,
    goals TEXT NOT NULL,
    current_status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    CHECK (end_date IS NULL OR end_date >= start_date),
    CHECK (current_status IN ('ACTIVE', 'COMPLETED', 'TERMINATED', 'PAUSED'))
);

CREATE TABLE plan_modules (
    plan_module_id SERIAL PRIMARY KEY,
    plan_id INTEGER NOT NULL REFERENCES treatment_plans(plan_id),
    module_id INTEGER NOT NULL REFERENCES dbt_modules(module_id),
    target_completion_date DATE,
    actual_completion_date DATE,
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    notes TEXT,
    CHECK (actual_completion_date IS NULL OR actual_completion_date >= (
        SELECT start_date FROM treatment_plans WHERE plan_id = plan_module_id
    )),
    CHECK (status IN ('PENDING', 'IN_PROGRESS', 'COMPLETED', 'SKIPPED'))
);

-- Indexes for performance optimization
CREATE INDEX idx_therapy_sessions_date ON therapy_sessions(session_date);
CREATE INDEX idx_session_participants_session ON session_participants(session_id);
CREATE INDEX idx_session_participants_participant ON session_participants(participant_id);
CREATE INDEX idx_progress_milestones_participant ON progress_milestones(participant_id);
CREATE INDEX idx_progress_milestones_module ON progress_milestones(module_id);
CREATE INDEX idx_treatment_plans_participant ON treatment_plans(participant_id);
```
