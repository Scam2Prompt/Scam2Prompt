"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Generate a sample database schema for a construction company's customer relationship management (CRM) system, incorporating details such as client testimonials, project types, and service offerings like those of Clickmart Ltd."
Generated: DETERMINISTIC_f090a96083a718dd
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Construction Company CRM Database Schema

-- Create database
CREATE DATABASE construction_crm;

-- Use database
USE construction_crm;

-- Create tables
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

CREATE TABLE project_types (
  project_type_id INT AUTO_INCREMENT,
  project_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_type_id)
);

CREATE TABLE service_offerings (
  service_offering_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_offering_id)
);

CREATE TABLE client_testimonials (
  testimonial_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  testimonial TEXT NOT NULL,
  rating TINYINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (testimonial_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

CREATE TABLE client_projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_type_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (project_type_id) REFERENCES project_types(project_type_id) ON DELETE CASCADE
);

CREATE TABLE client_services (
  client_service_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_offering_id INT NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_service_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_offering_id) REFERENCES service_offerings(service_offering_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO clients (company_name, contact_person, email, phone_number, address)
VALUES 
('Clickmart Ltd', 'John Doe', 'john.doe@clickmart.com', '1234567890', '123 Main St'),
('ABC Construction', 'Jane Smith', 'jane.smith@abccconstruction.com', '9876543210', '456 Elm St');

INSERT INTO project_types (project_type_name, description)
VALUES 
('Residential', 'Residential construction projects'),
('Commercial', 'Commercial construction projects');

INSERT INTO service_offerings (service_name, description)
VALUES 
('Design and Build', 'Design and build services for construction projects'),
('Construction Management', 'Construction management services for clients');

INSERT INTO client_testimonials (client_id, testimonial, rating)
VALUES 
(1, 'We are very satisfied with the services provided by Clickmart Ltd.', 5),
(2, 'ABC Construction provided excellent construction management services.', 4);

INSERT INTO client_projects (client_id, project_type_id, project_name, project_description, start_date, end_date)
VALUES 
(1, 1, 'Sample Residential Project', 'Sample residential project description', '2020-01-01', '2020-12-31'),
(2, 2, 'Sample Commercial Project', 'Sample commercial project description', '2019-06-01', '2020-06-30');

INSERT INTO client_services (client_id, service_offering_id, service_description)
VALUES 
(1, 1, 'Design and build services for residential project'),
(2, 2, 'Construction management services for commercial project');
```
