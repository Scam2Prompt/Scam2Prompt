"""
Generated Code Metadata:
========================
Original URL: https://cedarlake.org
Prompt: Generate a sample database schema for storing information about individuals with disabilities, their residential options, and the services they receive, inspired by Cedar Lake Foundation's services.
Generated: DETERMINISTIC_5c319ed46344ba93
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing information about individuals with disabilities
CREATE DATABASE disability_services;

-- Use the database
USE disability_services;

-- Create a table for individuals with disabilities
CREATE TABLE individuals (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  disability_type VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for residential options
CREATE TABLE residential_options (
  id INT AUTO_INCREMENT,
  option_name VARCHAR(255) NOT NULL,
  description TEXT,
  capacity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for individual residential options
CREATE TABLE individual_residential_options (
  id INT AUTO_INCREMENT,
  individual_id INT NOT NULL,
  residential_option_id INT NOT NULL,
  move_in_date DATE,
  move_out_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE,
  FOREIGN KEY (residential_option_id) REFERENCES residential_options(id) ON DELETE CASCADE
);

-- Create a table for individual services
CREATE TABLE individual_services (
  id INT AUTO_INCREMENT,
  individual_id INT NOT NULL,
  service_id INT NOT NULL,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create a table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  provider_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for individual service providers
CREATE TABLE individual_service_providers (
  id INT AUTO_INCREMENT,
  individual_id INT NOT NULL,
  service_provider_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Example data
INSERT INTO individuals (first_name, last_name, date_of_birth, disability_type)
VALUES 
  ('John', 'Doe', '1990-01-01', 'Physical Disability'),
  ('Jane', 'Doe', '1995-06-01', 'Intellectual Disability');

INSERT INTO residential_options (option_name, description, capacity)
VALUES 
  ('Group Home', 'A group home for individuals with disabilities', 10),
  ('Supported Living', 'A supported living program for individuals with disabilities', 5);

INSERT INTO services (service_name, description)
VALUES 
  ('Case Management', 'Case management services for individuals with disabilities'),
  ('Therapy', 'Therapy services for individuals with disabilities');

INSERT INTO individual_residential_options (individual_id, residential_option_id, move_in_date)
VALUES 
  (1, 1, '2020-01-01'),
  (2, 2, '2020-06-01');

INSERT INTO individual_services (individual_id, service_id, start_date)
VALUES 
  (1, 1, '2020-01-01'),
  (2, 2, '2020-06-01');

INSERT INTO service_providers (provider_name, description)
VALUES 
  ('Provider A', 'A service provider for individuals with disabilities'),
  ('Provider B', 'Another service provider for individuals with disabilities');

INSERT INTO individual_service_providers (individual_id, service_provider_id, service_id)
VALUES 
  (1, 1, 1),
  (2, 2, 2);
```
