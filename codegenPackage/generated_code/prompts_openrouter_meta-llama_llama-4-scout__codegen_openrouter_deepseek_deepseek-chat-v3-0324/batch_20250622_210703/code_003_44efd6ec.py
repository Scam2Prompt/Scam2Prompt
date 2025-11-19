"""
Generated Code Metadata:
========================
Original URL: https://accuratehire.co.in
Prompt: "Design a database schema to store information about job seekers, job openings, and recruitment services, inspired by Accurate Hire's approach to connecting people with opportunities."
Generated: DETERMINISTIC_44efd6ecd7c667f1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for job seekers, job openings, and recruitment services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table (common base for both job seekers and recruiters)
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    user_type TEXT NOT NULL CHECK(user_type IN ('job_seeker', 'recruiter', 'admin')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT 1
);

-- Job seekers profile table
CREATE TABLE job_seekers (
    seeker_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    headline TEXT,
    summary TEXT,
    current_job_title TEXT,
    current_company TEXT,
    years_of_experience INTEGER,
    education_level TEXT,
    location TEXT,
    willing_to_relocate BOOLEAN DEFAULT 0,
    remote_only BOOLEAN DEFAULT 0,
    min_salary_expectation INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Skills table
CREATE TABLE skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT NOT NULL UNIQUE,
    category TEXT
);

-- Job seeker skills mapping
CREATE TABLE seeker_skills (
    seeker_id INTEGER NOT NULL,
    skill_id INTEGER NOT NULL,
    proficiency_level INTEGER CHECK(proficiency_level BETWEEN 1 AND 5),
    years_of_experience INTEGER,
    PRIMARY KEY (seeker_id, skill_id),
    FOREIGN KEY (seeker_id) REFERENCES job_seekers(seeker_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);

-- Employment history for job seekers
CREATE TABLE employment_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    seeker_id INTEGER NOT NULL,
    job_title TEXT NOT NULL,
    company_name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT 0,
    description TEXT,
    FOREIGN KEY (seeker_id) REFERENCES job_seekers(seeker_id) ON DELETE CASCADE
);

-- Education history for job seekers
CREATE TABLE education_history (
    education_id INTEGER PRIMARY KEY AUTOINCREMENT,
    seeker_id INTEGER NOT NULL,
    institution TEXT NOT NULL,
    degree TEXT NOT NULL,
    field_of_study TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT 0,
    description TEXT,
    FOREIGN KEY (seeker_id) REFERENCES job_seekers(seeker_id) ON DELETE CASCADE
);

-- Companies table
CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    industry TEXT,
    website TEXT,
    logo_url TEXT,
    founded_year INTEGER,
    company_size TEXT,
    headquarters_location TEXT
);

-- Recruiters table
CREATE TABLE recruiters (
    recruiter_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    company_id INTEGER,
    job_title TEXT,
    is_agency_recruiter BOOLEAN DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE SET NULL
);

-- Job postings table
CREATE TABLE job_postings (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    posted_by INTEGER NOT NULL, -- recruiter_id
    company_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT,
    is_remote BOOLEAN DEFAULT 0,
    job_type TEXT CHECK(job_type IN ('full-time', 'part-time', 'contract', 'internship', 'temporary')),
    experience_level TEXT CHECK(experience_level IN ('entry', 'mid', 'senior', 'executive')),
    salary_min INTEGER,
    salary_max INTEGER,
    salary_currency TEXT DEFAULT 'USD',
    salary_is_estimated BOOLEAN DEFAULT 0,
    posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expiration_date TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    views_count INTEGER DEFAULT 0,
    applications_count INTEGER DEFAULT 0,
    FOREIGN KEY (posted_by) REFERENCES recruiters(recruiter_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Job posting required skills
CREATE TABLE job_required_skills (
    job_id INTEGER NOT NULL,
    skill_id INTEGER NOT NULL,
    is_required BOOLEAN DEFAULT 1,
    importance_level INTEGER CHECK(importance_level BETWEEN 1 AND 3),
    PRIMARY KEY (job_id, skill_id),
    FOREIGN KEY (job_id) REFERENCES job_postings(job_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);

-- Applications table
CREATE TABLE applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    seeker_id INTEGER NOT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('submitted', 'reviewed', 'interviewing', 'offered', 'hired', 'rejected', 'withdrawn')) DEFAULT 'submitted',
    cover_letter TEXT,
    notes TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES job_postings(job_id) ON DELETE CASCADE,
    FOREIGN KEY (seeker_id) REFERENCES job_seekers(seeker_id) ON DELETE CASCADE
);

-- Saved jobs by seekers
CREATE TABLE saved_jobs (
    seeker_id INTEGER NOT NULL,
    job_id INTEGER NOT NULL,
    saved_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    PRIMARY KEY (seeker_id, job_id),
    FOREIGN KEY (seeker_id) REFERENCES job_seekers(seeker_id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES job_postings(job_id) ON DELETE CASCADE
);

-- Recruiter's saved candidates
CREATE TABLE saved_candidates (
    recruiter_id INTEGER NOT NULL,
    seeker_id INTEGER NOT NULL,
    saved_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    PRIMARY KEY (recruiter_id, seeker_id),
    FOREIGN KEY (recruiter_id) REFERENCES recruiters(recruiter_id) ON DELETE CASCADE,
    FOREIGN KEY (seeker_id) REFERENCES job_seekers(seeker_id) ON DELETE CASCADE
);

-- Interview scheduling
CREATE TABLE interviews (
    interview_id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER NOT NULL,
    scheduled_time TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    interview_type TEXT CHECK(interview_type IN ('phone', 'video', 'in-person', 'technical', 'behavioral', 'panel')),
    location TEXT,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'rescheduled')) DEFAULT 'scheduled',
    notes TEXT,
    feedback TEXT,
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
);

-- Notifications system
CREATE TABLE notifications (
    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    notification_type TEXT NOT NULL,
    is_read BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    related_entity_type TEXT,
    related_entity_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Audit log for important actions
CREATE TABLE audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action_type TEXT NOT NULL,
    entity_type TEXT,
    entity_id INTEGER,
    old_values TEXT,
    new_values TEXT,
    ip_address TEXT,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Create indexes for performance optimization
CREATE INDEX idx_job_postings_company ON job_postings(company_id);
CREATE INDEX idx_job_postings_active ON job_postings(is_active);
CREATE INDEX idx_applications_job ON applications(job_id);
CREATE INDEX idx_applications_seeker ON applications(seeker_id);
CREATE INDEX idx_seeker_skills ON seeker_skills(seeker_id, skill_id);
CREATE INDEX idx_job_required_skills ON job_required_skills(job_id, skill_id);
CREATE INDEX idx_notifications_user ON notifications(user_id);
```
