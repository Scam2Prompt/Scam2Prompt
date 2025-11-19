"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Design a database schema to store information about professor positions, applicants, and selection results at IGEOG, and provide recommendations for suitable database management systems (DBMS).
Generated: DETERMINISTIC_70eeea9969328d3e
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for IGEOG professor positions, applicants, and selection results

-- Table for storing professor positions
CREATE TABLE positions (
    position_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    position_level VARCHAR(50) NOT NULL CHECK (position_level IN ('Assistant', 'Associate', 'Full')),
    opening_date DATE NOT NULL,
    closing_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Open', 'Closed', 'Cancelled')),
    description TEXT,
    requirements TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (closing_date >= opening_date)
);

-- Table for storing applicants
CREATE TABLE applicants (
    applicant_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    current_institution VARCHAR(100),
    current_position VARCHAR(100),
    highest_degree VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    years_of_experience INTEGER NOT NULL,
    cv_path VARCHAR(255),
    research_statement_path VARCHAR(255),
    teaching_statement_path VARCHAR(255),
    reference_letters_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for applications (many-to-many between positions and applicants)
CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    position_id INTEGER NOT NULL REFERENCES positions(position_id) ON DELETE CASCADE,
    applicant_id INTEGER NOT NULL REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    application_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Submitted', 'Under Review', 'Shortlisted', 'Rejected', 'Selected')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(position_id, applicant_id)
);

-- Table for selection committee members
CREATE TABLE committee_members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    is_chair BOOLEAN DEFAULT FALSE
);

-- Table for position-committee assignments
CREATE TABLE position_committee (
    assignment_id SERIAL PRIMARY KEY,
    position_id INTEGER NOT NULL REFERENCES positions(position_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES committee_members(member_id) ON DELETE CASCADE,
    UNIQUE(position_id, member_id)
);

-- Table for interview records
CREATE TABLE interviews (
    interview_id SERIAL PRIMARY KEY,
    application_id INTEGER NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    interview_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER NOT NULL,
    format VARCHAR(50) NOT NULL CHECK (format IN ('In-Person', 'Video', 'Phone')),
    notes TEXT,
    average_score DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for evaluation criteria
CREATE TABLE evaluation_criteria (
    criterion_id SERIAL PRIMARY KEY,
    position_id INTEGER NOT NULL REFERENCES positions(position_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    weight DECIMAL(5,2) NOT NULL CHECK (weight > 0 AND weight <= 100),
    max_score INTEGER NOT NULL CHECK (max_score > 0)
);

-- Table for individual evaluations
CREATE TABLE evaluations (
    evaluation_id SERIAL PRIMARY KEY,
    interview_id INTEGER REFERENCES interviews(interview_id) ON DELETE CASCADE,
    application_id INTEGER NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES committee_members(member_id) ON DELETE CASCADE,
    criterion_id INTEGER NOT NULL REFERENCES evaluation_criteria(criterion_id) ON DELETE CASCADE,
    score INTEGER NOT NULL CHECK (score >= 0),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(application_id, member_id, criterion_id)
);

-- Table for final selection results
CREATE TABLE selection_results (
    result_id SERIAL PRIMARY KEY,
    position_id INTEGER NOT NULL REFERENCES positions(position_id) ON DELETE CASCADE,
    application_id INTEGER NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    final_decision VARCHAR(20) NOT NULL CHECK (final_decision IN ('Selected', 'Rejected', 'Waitlisted')),
    decision_date DATE NOT NULL,
    offer_sent_date DATE,
    offer_accepted_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_applications_position ON applications(position_id);
CREATE INDEX idx_applications_applicant ON applications(applicant_id);
CREATE INDEX idx_applications_status ON applications(status);
CREATE INDEX idx_interviews_application ON interviews(application_id);
CREATE INDEX idx_evaluations_application ON evaluations(application_id);
CREATE INDEX idx_evaluations_criterion ON evaluations(criterion_id);
CREATE INDEX idx_selection_results_position ON selection_results(position_id);

-- Triggers for automatic updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_position_timestamp
BEFORE UPDATE ON positions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_application_timestamp
BEFORE UPDATE ON applications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_interview_timestamp
BEFORE UPDATE ON interviews
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_evaluation_timestamp
BEFORE UPDATE ON evaluations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_selection_result_timestamp
BEFORE UPDATE ON selection_results
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- DBMS Recommendations:
-- 1. PostgreSQL (recommended for complex queries and data integrity)
-- 2. MySQL/MariaDB (good alternative with good performance)
-- 3. Microsoft SQL Server (if integration with other MS products is needed)
-- 4. Oracle Database (for enterprise-level requirements)
```
