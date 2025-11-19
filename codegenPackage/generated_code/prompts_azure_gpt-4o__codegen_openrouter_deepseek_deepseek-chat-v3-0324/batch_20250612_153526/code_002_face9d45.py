"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Generate code for a database schema to manage business and investment clubs, including entrepreneurship training sessions and funding opportunities, as described in the "Inua Pato" sustainable livelihood program.
Generated: DETERMINISTIC_face9d45b73ffb9f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Inua Pato program management

-- Create database
CREATE DATABASE IF NOT EXISTS inua_pato;
USE inua_pato;

-- Users table (for all system users)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    role ENUM('admin', 'trainer', 'member', 'investor') NOT NULL,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    is_active BOOLEAN DEFAULT TRUE,
    profile_picture VARCHAR(255),
    bio TEXT,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Business clubs table
CREATE TABLE IF NOT EXISTS business_clubs (
    club_id INT AUTO_INCREMENT PRIMARY KEY,
    club_name VARCHAR(100) NOT NULL,
    description TEXT,
    founded_date DATE,
    location VARCHAR(100),
    meeting_schedule VARCHAR(255),
    president_id INT,
    vice_president_id INT,
    treasurer_id INT,
    secretary_id INT,
    logo_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (president_id) REFERENCES users(user_id),
    FOREIGN KEY (vice_president_id) REFERENCES users(user_id),
    FOREIGN KEY (treasurer_id) REFERENCES users(user_id),
    FOREIGN KEY (secretary_id) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Club members mapping table
CREATE TABLE IF NOT EXISTS club_members (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    club_id INT NOT NULL,
    user_id INT NOT NULL,
    join_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (club_id) REFERENCES business_clubs(club_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE KEY unique_membership (club_id, user_id)
) ENGINE=InnoDB;

-- Training sessions table
CREATE TABLE IF NOT EXISTS training_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    trainer_id INT,
    club_id INT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location VARCHAR(100),
    max_participants INT,
    is_online BOOLEAN DEFAULT FALSE,
    meeting_link VARCHAR(255),
    materials_url VARCHAR(255),
    status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trainer_id) REFERENCES users(user_id),
    FOREIGN KEY (club_id) REFERENCES business_clubs(club_id),
    CONSTRAINT chk_datetime CHECK (end_datetime > start_datetime)
) ENGINE=InnoDB;

-- Session participants mapping table
CREATE TABLE IF NOT EXISTS session_participants (
    participation_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    user_id INT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    attendance_status ENUM('registered', 'attended', 'absent') DEFAULT 'registered',
    feedback TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    FOREIGN KEY (session_id) REFERENCES training_sessions(session_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE KEY unique_participation (session_id, user_id)
) ENGINE=InnoDB;

-- Business ideas/projects table
CREATE TABLE IF NOT EXISTS business_projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    owner_id INT NOT NULL,
    club_id INT,
    category VARCHAR(50),
    stage ENUM('idea', 'prototype', 'early-stage', 'growth', 'mature') DEFAULT 'idea',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (owner_id) REFERENCES users(user_id),
    FOREIGN KEY (club_id) REFERENCES business_clubs(club_id)
) ENGINE=InnoDB;

-- Funding opportunities table
CREATE TABLE IF NOT EXISTS funding_opportunities (
    opportunity_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    provider VARCHAR(100) NOT NULL,
    funding_type ENUM('grant', 'loan', 'equity', 'prize') NOT NULL,
    amount_min DECIMAL(15,2),
    amount_max DECIMAL(15,2),
    currency VARCHAR(3) DEFAULT 'KES',
    application_deadline DATE,
    eligibility_criteria TEXT,
    application_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_by INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Funding applications table
CREATE TABLE IF NOT EXISTS funding_applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    opportunity_id INT NOT NULL,
    applicant_id INT NOT NULL,
    project_id INT,
    application_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('draft', 'submitted', 'under_review', 'approved', 'rejected') DEFAULT 'draft',
    amount_requested DECIMAL(15,2),
    proposal_text TEXT,
    supporting_docs_url VARCHAR(255),
    decision_date DATETIME,
    decision_notes TEXT,
    FOREIGN KEY (opportunity_id) REFERENCES funding_opportunities(opportunity_id),
    FOREIGN KEY (applicant_id) REFERENCES users(user_id),
    FOREIGN KEY (project_id) REFERENCES business_projects(project_id)
) ENGINE=InnoDB;

-- Investment club table
CREATE TABLE IF NOT EXISTS investment_clubs (
    investment_club_id INT AUTO_INCREMENT PRIMARY KEY,
    club_name VARCHAR(100) NOT NULL,
    description TEXT,
    founded_date DATE,
    location VARCHAR(100),
    meeting_schedule VARCHAR(255),
    president_id INT,
    vice_president_id INT,
    treasurer_id INT,
    secretary_id INT,
    logo_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (president_id) REFERENCES users(user_id),
    FOREIGN KEY (vice_president_id) REFERENCES users(user_id),
    FOREIGN KEY (treasurer_id) REFERENCES users(user_id),
    FOREIGN KEY (secretary_id) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Investment club members mapping table
CREATE TABLE IF NOT EXISTS investment_club_members (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    club_id INT NOT NULL,
    user_id INT NOT NULL,
    join_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(50),
    contribution_amount DECIMAL(15,2),
    contribution_frequency ENUM('weekly', 'monthly', 'quarterly', 'annually'),
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (club_id) REFERENCES investment_clubs(investment_club_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE KEY unique_membership (club_id, user_id)
) ENGINE=InnoDB;

-- Investment portfolio table
CREATE TABLE IF NOT EXISTS investment_portfolio (
    investment_id INT AUTO_INCREMENT PRIMARY KEY,
    club_id INT NOT NULL,
    project_id INT,
    investment_date DATE NOT NULL,
    amount_invested DECIMAL(15,2) NOT NULL,
    equity_percentage DECIMAL(5,2),
    expected_return DECIMAL(15,2),
    return_date DATE,
    status ENUM('active', 'exited', 'defaulted') DEFAULT 'active',
    notes TEXT,
    FOREIGN KEY (club_id) REFERENCES investment_clubs(investment_club_id),
    FOREIGN KEY (project_id) REFERENCES business_projects(project_id)
) ENGINE=InnoDB;

-- Meeting minutes table
CREATE TABLE IF NOT EXISTS meeting_minutes (
    minutes_id INT AUTO_INCREMENT PRIMARY KEY,
    club_type ENUM('business', 'investment') NOT NULL,
    club_id INT NOT NULL,
    meeting_date DATETIME NOT NULL,
    location VARCHAR(100),
    chairperson_id INT,
    secretary_id INT,
    agenda TEXT,
    minutes_text TEXT NOT NULL,
    decisions_made TEXT,
    action_items TEXT,
    next_meeting_date DATETIME,
    document_url VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chairperson_id) REFERENCES users(user_id),
    FOREIGN KEY (secretary_id) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id INT,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (
