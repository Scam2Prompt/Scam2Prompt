"""
Generated Code Metadata:
========================
Original URL: https://nassauccw.com
Prompt: Design a database schema to store information about CCW permit applicants and their application status, inspired by the services offered by Trigon Tactics for managing the application process.
Generated: DETERMINISTIC_2d9ef9a9f8466020
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing CCW permit applicant information

-- Create a database
CREATE DATABASE ccw_permit;

-- Use the database
USE ccw_permit;

-- Create a table for counties
CREATE TABLE counties (
  county_id INT AUTO_INCREMENT,
  county_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (county_id)
);

-- Create a table for applicants
CREATE TABLE applicants (
  applicant_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  county_id INT,
  FOREIGN KEY (county_id) REFERENCES counties(county_id),
  PRIMARY KEY (applicant_id)
);

-- Create a table for application status
CREATE TABLE application_status (
  status_id INT AUTO_INCREMENT,
  status_name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (status_id)
);

-- Create a table for applications
CREATE TABLE applications (
  application_id INT AUTO_INCREMENT,
  applicant_id INT NOT NULL,
  application_date DATE NOT NULL,
  status_id INT NOT NULL DEFAULT 1,
  permit_number VARCHAR(100),
  issue_date DATE,
  expiration_date DATE,
  county_id INT,
  FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id),
  FOREIGN KEY (status_id) REFERENCES application_status(status_id),
  FOREIGN KEY (county_id) REFERENCES counties(county_id),
  PRIMARY KEY (application_id)
);

-- Create a table for application documents
CREATE TABLE application_documents (
  document_id INT AUTO_INCREMENT,
  application_id INT NOT NULL,
  document_type VARCHAR(100) NOT NULL,
  document_data BLOB NOT NULL,
  uploaded_date DATE NOT NULL,
  PRIMARY KEY (document_id),
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

-- Create a table for application comments
CREATE TABLE application_comments (
  comment_id INT AUTO_INCREMENT,
  application_id INT NOT NULL,
  comment TEXT NOT NULL,
  comment_date DATE NOT NULL,
  PRIMARY KEY (comment_id),
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

-- Insert initial application status
INSERT INTO application_status (status_name, description) 
VALUES 
('New', 'New application submitted'),
('In Progress', 'Application is being processed'),
('Approved', 'Application approved'),
('Denied', 'Application denied'),
('Expired', 'Permit has expired');

-- Example data for testing
INSERT INTO counties (county_name) 
VALUES 
('Los Angeles'),
('Orange'),
('San Diego');

INSERT INTO applicants (first_name, last_name, date_of_birth, email, phone_number, address, city, state, zip_code, county_id) 
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345', 1);

INSERT INTO applications (applicant_id, application_date, status_id, county_id) 
VALUES 
(1, '2022-01-01', 1, 1);

INSERT INTO application_documents (application_id, document_type, document_data, uploaded_date) 
VALUES 
(1, 'Identification', 'example document data', '2022-01-01');

INSERT INTO application_comments (application_id, comment, comment_date) 
VALUES 
(1, 'Application received', '2022-01-01');
```
