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
-- Create database for IGEOG
CREATE DATABASE igeog;

-- Use the igeog database
USE igeog;

-- Create table for professor positions
CREATE TABLE professor_positions (
    position_id INT AUTO_INCREMENT,
    department VARCHAR(255) NOT NULL,
    position_title VARCHAR(255) NOT NULL,
    job_description TEXT,
    application_deadline DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (position_id)
);

-- Create table for applicants
CREATE TABLE applicants (
    applicant_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    cv TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (applicant_id)
);

-- Create table for applications
CREATE TABLE applications (
    application_id INT AUTO_INCREMENT,
    applicant_id INT NOT NULL,
    position_id INT NOT NULL,
    application_date DATE NOT NULL,
    cover_letter TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (application_id),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES professor_positions(position_id) ON DELETE CASCADE
);

-- Create table for selection results
CREATE TABLE selection_results (
    result_id INT AUTO_INCREMENT,
    application_id INT NOT NULL,
    interview_date DATE,
    interview_result VARCHAR(50),
    selected BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (result_id),
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_professor_positions_department ON professor_positions (department);
CREATE INDEX idx_applicants_email ON applicants (email);
CREATE INDEX idx_applications_applicant_id ON applications (applicant_id);
CREATE INDEX idx_applications_position_id ON applications (position_id);
CREATE INDEX idx_selection_results_application_id ON selection_results (application_id);
```

**Recommended DBMS:** 
MySQL, PostgreSQL, or MariaDB 

**DBMS Rationale:**
- **MySQL**: Popular open-source relational database management system, widely used, and well-documented.
- **PostgreSQL**: Powerful, open-source object-relational database system with a strong focus on reliability, data integrity, and concurrency support.
- **MariaDB**: A MySQL fork with high performance, reliability, and ease of use, offering high scalability and support.

**Example Use Cases:**

```sql
-- Insert a new professor position
INSERT INTO professor_positions (department, position_title, job_description, application_deadline)
VALUES ('Computer Science', 'Professor', 'Teach computer science courses', '2024-09-01');

-- Insert a new applicant
INSERT INTO applicants (first_name, last_name, email, phone_number, cv)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Attached CV');

-- Insert a new application
INSERT INTO applications (applicant_id, position_id, application_date, cover_letter)
VALUES (1, 1, '2024-08-01', 'Attached cover letter');

-- Update selection result
UPDATE selection_results
SET interview_result = 'Passed', selected = TRUE
WHERE application_id = 1;
```
