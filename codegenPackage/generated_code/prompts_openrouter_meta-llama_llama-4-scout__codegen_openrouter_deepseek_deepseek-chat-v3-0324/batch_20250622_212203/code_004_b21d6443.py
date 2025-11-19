"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Design a database schema to store information about underprivileged children and their education progress, similar to Indological India's education empowerment programs.
Generated: DETERMINISTIC_b21d644357eec457
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking underprivileged children's education progress

CREATE TABLE children (
    child_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'India',
    contact_number VARCHAR(15),
    is_orphan BOOLEAN DEFAULT FALSE,
    has_disability BOOLEAN DEFAULT FALSE,
    disability_details TEXT,
    family_income DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_age CHECK (date_of_birth <= CURRENT_DATE - INTERVAL '3 years')
);

CREATE TABLE guardians (
    guardian_id SERIAL PRIMARY KEY,
    child_id INTEGER REFERENCES children(child_id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    relationship VARCHAR(50) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    occupation VARCHAR(100),
    is_primary BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE schools (
    school_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'India',
    type VARCHAR(50) CHECK (type IN ('Government', 'Private', 'NGO-run', 'Other')),
    contact_number VARCHAR(15),
    email VARCHAR(100),
    principal_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE education_progress (
    progress_id SERIAL PRIMARY KEY,
    child_id INTEGER REFERENCES children(child_id) ON DELETE CASCADE,
    school_id INTEGER REFERENCES schools(school_id) ON DELETE SET NULL,
    academic_year VARCHAR(20) NOT NULL,
    grade_level VARCHAR(20) NOT NULL,
    enrollment_date DATE NOT NULL,
    dropout_date DATE,
    dropout_reason TEXT,
    attendance_percentage DECIMAL(5, 2),
    performance_notes TEXT,
    scholarship_amount DECIMAL(10, 2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_dates CHECK (dropout_date IS NULL OR dropout_date >= enrollment_date)
);

CREATE TABLE interventions (
    intervention_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) CHECK (category IN ('Financial', 'Educational', 'Health', 'Nutrition', 'Other')),
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE child_interventions (
    child_intervention_id SERIAL PRIMARY KEY,
    child_id INTEGER REFERENCES children(child_id) ON DELETE CASCADE,
    intervention_id INTEGER REFERENCES interventions(intervention_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE,
    benefits_received TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_intervention_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE volunteers (
    volunteer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    skills TEXT,
    availability TEXT,
    join_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE child_volunteers (
    child_volunteer_id SERIAL PRIMARY KEY,
    child_id INTEGER REFERENCES children(child_id) ON DELETE CASCADE,
    volunteer_id INTEGER REFERENCES volunteers(volunteer_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE,
    role VARCHAR(100),
    hours_per_week INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_volunteer_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE assessments (
    assessment_id SERIAL PRIMARY KEY,
    child_id INTEGER REFERENCES children(child_id) ON DELETE CASCADE,
    assessment_date DATE NOT NULL,
    assessment_type VARCHAR(50) NOT NULL,
    conducted_by VARCHAR(100),
    academic_level VARCHAR(50),
    cognitive_level VARCHAR(50),
    emotional_wellbeing TEXT,
    health_notes TEXT,
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    child_id INTEGER REFERENCES children(child_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    document_number VARCHAR(50),
    issue_date DATE,
    expiry_date DATE,
    issuing_authority VARCHAR(100),
    file_path TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_child_name ON children(last_name, first_name);
CREATE INDEX idx_child_location ON children(city, state);
CREATE INDEX idx_education_progress_child ON education_progress(child_id);
CREATE INDEX idx_education_progress_school ON education_progress(school_id);
CREATE INDEX idx_child_interventions ON child_interventions(child_id, intervention_id);
CREATE INDEX idx_assessments_child ON assessments(child_id);
```
