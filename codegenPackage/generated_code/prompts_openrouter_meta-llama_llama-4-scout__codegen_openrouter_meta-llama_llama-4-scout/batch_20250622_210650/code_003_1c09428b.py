"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Design a database schema to store information about women who have experienced sexual aggression, including their stories, and the services they have received from organizations like Viajeras.
Generated: DETERMINISTIC_1c09428b52217b34
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing information about women who have experienced sexual aggression
CREATE DATABASE sexual_aggression_support;

-- Use the created database
USE sexual_aggression_support;

-- Create a table for storing user information
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for storing stories of women who have experienced sexual aggression
CREATE TABLE stories (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  story TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for storing information about organizations
CREATE TABLE organizations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for storing services provided by organizations
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  organization_id INT NOT NULL,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
);

-- Create a table for storing user services (many-to-many relationship between users and services)
CREATE TABLE user_services (
  user_id INT NOT NULL,
  service_id INT NOT NULL,
  received_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, service_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create a table for storing organization contacts (e.g. phone numbers, emails)
CREATE TABLE organization_contacts (
  id INT AUTO_INCREMENT,
  organization_id INT NOT NULL,
  contact_type VARCHAR(20) NOT NULL CHECK (contact_type IN ('phone', 'email')),
  contact_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO users (name, email, phone_number)
VALUES 
('Jane Doe', 'jane@example.com', '123-456-7890'),
('Maria Rodriguez', 'maria@example.com', '987-654-3210');

INSERT INTO stories (user_id, story)
VALUES 
(1, 'This is a sample story'),
(2, 'This is another sample story');

INSERT INTO organizations (name, description)
VALUES 
('Viajeras', 'An organization providing support to women who have experienced sexual aggression'),
('Another Organization', 'Another organization providing similar support');

INSERT INTO services (organization_id, service_name, service_description)
VALUES 
(1, 'Counseling', 'One-on-one counseling sessions'),
(1, 'Support Group', 'Group support sessions'),
(2, 'Hotline', '24/7 hotline for support');

INSERT INTO user_services (user_id, service_id, received_at)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-02-01'),
(2, 3, '2022-03-01');

INSERT INTO organization_contacts (organization_id, contact_type, contact_value)
VALUES 
(1, 'phone', '123-456-7890'),
(1, 'email', 'info@viajeras.org'),
(2, 'phone', '987-654-3210');
```
