"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: "Design a database schema to store information about beneficiaries, projects, and donations for an organization like Ayb-Sd.org."
Generated: DETERMINISTIC_203ba8d3d7c2f2cb
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Ayb-Sd.org
CREATE DATABASE ayb_sd_org;

-- Use the database
USE ayb_sd_org;

-- Create table for beneficiaries
CREATE TABLE beneficiaries (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  goal DECIMAL(10, 2) NOT NULL,
  current_funding DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for donations
CREATE TABLE donations (
  id INT AUTO_INCREMENT,
  beneficiary_id INT,
  project_id INT,
  donor_name VARCHAR(255) NOT NULL,
  donation_amount DECIMAL(10, 2) NOT NULL,
  donation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE SET NULL,
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE SET NULL
);

-- Create table for project beneficiaries (many-to-many relationship)
CREATE TABLE project_beneficiaries (
  project_id INT,
  beneficiary_id INT,
  assigned_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, beneficiary_id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_beneficiaries_email ON beneficiaries(email);
CREATE INDEX idx_projects_name ON projects(name);
CREATE INDEX idx_donations_project_id ON donations(project_id);
CREATE INDEX idx_donations_beneficiary_id ON donations(beneficiary_id);
```

```sql
-- sample_data.sql

-- Insert sample data into beneficiaries table
INSERT INTO beneficiaries (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES
  ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Doe', '1995-06-01', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into projects table
INSERT INTO projects (name, description, start_date, end_date, goal)
VALUES
  ('Education Initiative', 'Providing educational resources to underprivileged children', '2022-01-01', '2023-12-31', 10000.00),
  ('Food Drive', 'Collecting food donations for local food banks', '2022-03-01', '2022-09-30', 5000.00);

-- Insert sample data into donations table
INSERT INTO donations (beneficiary_id, project_id, donor_name, donation_amount, donation_date)
VALUES
  (1, 1, 'Anonymous', 100.00, '2022-02-01'),
  (2, 2, 'John Smith', 50.00, '2022-04-01'),
  (NULL, 1, 'Jane Doe', 200.00, '2022-06-01');

-- Insert sample data into project_beneficiaries table
INSERT INTO project_beneficiaries (project_id, beneficiary_id, assigned_date)
VALUES
  (1, 1, '2022-01-15'),
  (1, 2, '2022-02-01'),
  (2, 1, '2022-03-01');
```
