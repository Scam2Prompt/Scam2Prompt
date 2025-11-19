"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Design a database schema for storing information about NGO projects, volunteers, and beneficiaries, using Youngistaan Foundation as a case study."
Generated: DETERMINISTIC_b22033b41ef23c36
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Youngistaan Foundation
CREATE DATABASE youngistaan_foundation;

-- Use the database
USE youngistaan_foundation;

-- Create table for projects
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT,
    project_name VARCHAR(255) NOT NULL,
    project_description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id)
);

-- Create table for volunteers
CREATE TABLE volunteers (
    volunteer_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (volunteer_id)
);

-- Create table for beneficiaries
CREATE TABLE beneficiaries (
    beneficiary_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    address TEXT,
    project_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (beneficiary_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Create table for volunteer project assignments
CREATE TABLE volunteer_project_assignments (
    assignment_id INT AUTO_INCREMENT,
    volunteer_id INT,
    project_id INT,
    assigned_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (assignment_id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for project expenses
CREATE TABLE project_expenses (
    expense_id INT AUTO_INCREMENT,
    project_id INT,
    expense_date DATE,
    expense_amount DECIMAL(10, 2),
    expense_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (expense_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for project donations
CREATE TABLE project_donations (
    donation_id INT AUTO_INCREMENT,
    project_id INT,
    donor_name VARCHAR(100),
    donation_date DATE,
    donation_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (donation_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_beneficiaries_project_id ON beneficiaries (project_id);
CREATE INDEX idx_volunteer_project_assignments_volunteer_id ON volunteer_project_assignments (volunteer_id);
CREATE INDEX idx_volunteer_project_assignments_project_id ON volunteer_project_assignments (project_id);
CREATE INDEX idx_project_expenses_project_id ON project_expenses (project_id);
CREATE INDEX idx_project_donations_project_id ON project_donations (project_id);
```

```sql
-- Example insert statements
INSERT INTO projects (project_name, project_description, start_date, end_date, budget)
VALUES 
('Education for All', 'Providing education to underprivileged children', '2022-01-01', '2023-12-31', 100000.00),
('Healthcare Initiative', 'Providing healthcare services to rural areas', '2022-06-01', '2023-05-31', 50000.00);

INSERT INTO volunteers (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

INSERT INTO beneficiaries (first_name, last_name, email, phone_number, address, project_id)
VALUES 
('Beneficiary1', 'Lastname1', 'beneficiary1@example.com', '1111111111', '111 Main St', 1),
('Beneficiary2', 'Lastname2', 'beneficiary2@example.com', '2222222222', '222 Elm St', 1);

INSERT INTO volunteer_project_assignments (volunteer_id, project_id, assigned_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-06-01');

INSERT INTO project_expenses (project_id, expense_date, expense_amount, expense_description)
VALUES 
(1, '2022-02-01', 5000.00, 'Teacher salaries'),
(2, '2022-07-01', 2000.00, 'Medical supplies');

INSERT INTO project_donations (project_id, donor_name, donation_date, donation_amount)
VALUES 
(1, 'Donor1', '2022-03-01', 10000.00),
(2, 'Donor2', '2022-08-01', 5000.00);
```
