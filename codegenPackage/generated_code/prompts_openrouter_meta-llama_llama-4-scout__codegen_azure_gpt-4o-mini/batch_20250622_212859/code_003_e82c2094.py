"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: "Design a data model for tracking employee progress and engagement in a company-wide training program, similar to Virtual5's solutions for organizational development, and provide a sample SQL schema."
Generated: DETERMINISTIC_e82c2094c4de1e26
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Tracking Employee Progress and Engagement in a Training Program

-- Table to store employee information
CREATE TABLE Employees (
    employee_id SERIAL PRIMARY KEY,  -- Unique identifier for each employee
    first_name VARCHAR(50) NOT NULL, -- Employee's first name
    last_name VARCHAR(50) NOT NULL,  -- Employee's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Employee's email address
    hire_date DATE NOT NULL,          -- Date the employee was hired
    department VARCHAR(50) NOT NULL   -- Department the employee belongs to
);

-- Table to store training program information
CREATE TABLE TrainingPrograms (
    program_id SERIAL PRIMARY KEY,    -- Unique identifier for each training program
    program_name VARCHAR(100) NOT NULL, -- Name of the training program
    description TEXT,                  -- Description of the training program
    start_date DATE NOT NULL,         -- Start date of the training program
    end_date DATE NOT NULL             -- End date of the training program
);

-- Table to track employee enrollment in training programs
CREATE TABLE EmployeeTrainingEnrollments (
    enrollment_id SERIAL PRIMARY KEY,  -- Unique identifier for each enrollment
    employee_id INT NOT NULL REFERENCES Employees(employee_id) ON DELETE CASCADE, -- Foreign key to Employees
    program_id INT NOT NULL REFERENCES TrainingPrograms(program_id) ON DELETE CASCADE, -- Foreign key to TrainingPrograms
    enrollment_date DATE NOT NULL,     -- Date the employee enrolled in the program
    completion_status VARCHAR(20) NOT NULL CHECK (completion_status IN ('Not Started', 'In Progress', 'Completed')), -- Status of the enrollment
    progress_percentage INT CHECK (progress_percentage BETWEEN 0 AND 100) DEFAULT 0 -- Progress percentage of the training
);

-- Table to store feedback from employees about training programs
CREATE TABLE TrainingFeedback (
    feedback_id SERIAL PRIMARY KEY,    -- Unique identifier for each feedback entry
    enrollment_id INT NOT NULL REFERENCES EmployeeTrainingEnrollments(enrollment_id) ON DELETE CASCADE, -- Foreign key to EmployeeTrainingEnrollments
    feedback_date DATE NOT NULL,       -- Date the feedback was provided
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating given by the employee
    comments TEXT                      -- Additional comments from the employee
);

-- Indexes for performance optimization
CREATE INDEX idx_employee_email ON Employees(email);
CREATE INDEX idx_program_name ON TrainingPrograms(program_name);
CREATE INDEX idx_enrollment_status ON EmployeeTrainingEnrollments(completion_status);
```
