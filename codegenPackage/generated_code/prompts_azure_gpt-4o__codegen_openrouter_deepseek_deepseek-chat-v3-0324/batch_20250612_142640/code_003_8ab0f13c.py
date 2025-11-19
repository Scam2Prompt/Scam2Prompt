"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a database schema for managing award nominations and winners based on the structure described in MN SWAP's award nomination information.
Generated: DETERMINISTIC_8ab0f13c8c464f78
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing award nominations and winners

-- Create the database
CREATE DATABASE IF NOT EXISTS award_management;
USE award_management;

-- Award categories table
CREATE TABLE IF NOT EXISTS award_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_category_name UNIQUE (category_name)
) ENGINE=InnoDB;

-- Nominators table
CREATE TABLE IF NOT EXISTS nominators (
    nominator_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    organization VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_email UNIQUE (email)
) ENGINE=InnoDB;

-- Nominees table
CREATE TABLE IF NOT EXISTS nominees (
    nominee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    organization VARCHAR(100) NOT NULL,
    position VARCHAR(100),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Nominations table
CREATE TABLE IF NOT EXISTS nominations (
    nomination_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    nominator_id INT NOT NULL,
    nominee_id INT NOT NULL,
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statement TEXT NOT NULL,
    supporting_documents TEXT,
    status ENUM('submitted', 'under_review', 'shortlisted', 'winner', 'not_selected') DEFAULT 'submitted',
    year INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES award_categories(category_id) ON DELETE RESTRICT,
    FOREIGN KEY (nominator_id) REFERENCES nominators(nominator_id) ON DELETE RESTRICT,
    FOREIGN KEY (nominee_id) REFERENCES nominees(nominee_id) ON DELETE RESTRICT,
    CONSTRAINT uc_nomination UNIQUE (category_id, nominee_id, year)
) ENGINE=InnoDB;

-- Winners table
CREATE TABLE IF NOT EXISTS winners (
    winner_id INT AUTO_INCREMENT PRIMARY KEY,
    nomination_id INT NOT NULL,
    award_date DATE NOT NULL,
    prize_details TEXT,
    acceptance_speech TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (nomination_id) REFERENCES nominations(nomination_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Judges table
CREATE TABLE IF NOT EXISTS judges (
    judge_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    organization VARCHAR(100),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_judge_email UNIQUE (email)
) ENGINE=InnoDB;

-- Judging assignments table
CREATE TABLE IF NOT EXISTS judging_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    judge_id INT NOT NULL,
    category_id INT NOT NULL,
    year INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (judge_id) REFERENCES judges(judge_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES award_categories(category_id) ON DELETE CASCADE,
    CONSTRAINT uc_judge_assignment UNIQUE (judge_id, category_id, year)
) ENGINE=InnoDB;

-- Judging scores table
CREATE TABLE IF NOT EXISTS judging_scores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT NOT NULL,
    nomination_id INT NOT NULL,
    score INT NOT NULL CHECK (score BETWEEN 1 AND 10),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES judging_assignments(assignment_id) ON DELETE CASCADE,
    FOREIGN KEY (nomination_id) REFERENCES nominations(nomination_id) ON DELETE CASCADE,
    CONSTRAINT uc_judge_nomination_score UNIQUE (assignment_id, nomination_id)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_nominations_category ON nominations(category_id);
CREATE INDEX idx_nominations_status ON nominations(status);
CREATE INDEX idx_nominations_year ON nominations(year);
CREATE INDEX idx_nominations_nominee ON nominations(nominee_id);
CREATE INDEX idx_nominations_nominator ON nominations(nominator_id);
CREATE INDEX idx_winners_nomination ON winners(nomination_id);
CREATE INDEX idx_judging_assignments_judge ON judging_assignments(judge_id);
CREATE INDEX idx_judging_assignments_category ON judging_assignments(category_id);
CREATE INDEX idx_judging_scores_assignment ON judging_scores(assignment_id);
CREATE INDEX idx_judging_scores_nomination ON judging_scores(nomination_id);
```
