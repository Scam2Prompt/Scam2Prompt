"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Design a database schema for an NDIS provider that tracks client goals, support services, and community engagement, reflecting the tailored services provided by Shareth Homecare.
Generated: DETERMINISTIC_a8aa5596c86a478d
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for NDIS provider
CREATE DATABASE ndis_provider;

-- Use the database
USE ndis_provider;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  contact_number VARCHAR(20),
  email VARCHAR(255) UNIQUE,
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for client goals
CREATE TABLE client_goals (
  goal_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  goal_description TEXT NOT NULL,
  goal_status ENUM('pending', 'in_progress', 'achieved', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (goal_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for support services
CREATE TABLE support_services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for client support services
CREATE TABLE client_support_services (
  client_service_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  service_status ENUM('allocated', 'in_progress', 'completed', 'cancelled') DEFAULT 'allocated',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_service_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES support_services(service_id) ON DELETE CASCADE,
  UNIQUE KEY (client_id, service_id)
);

-- Create table for community engagement activities
CREATE TABLE community_activities (
  activity_id INT AUTO_INCREMENT,
  activity_name VARCHAR(255) NOT NULL,
  activity_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (activity_id)
);

-- Create table for client community engagement
CREATE TABLE client_community_engagement (
  client_activity_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  activity_id INT NOT NULL,
  participation_status ENUM('pending', 'participated', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_activity_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (activity_id) REFERENCES community_activities(activity_id) ON DELETE CASCADE,
  UNIQUE KEY (client_id, activity_id)
);

-- Create table for service providers
CREATE TABLE service_providers (
  provider_id INT AUTO_INCREMENT,
  provider_name VARCHAR(255) NOT NULL,
  contact_number VARCHAR(20),
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (provider_id)
);

-- Create table for service provider allocations
CREATE TABLE service_provider_allocations (
  allocation_id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  provider_id INT NOT NULL,
  allocation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (allocation_id),
  FOREIGN KEY (service_id) REFERENCES support_services(service_id) ON DELETE CASCADE,
  FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id) ON DELETE CASCADE,
  UNIQUE KEY (service_id, provider_id)
);

-- Example data for testing
INSERT INTO clients (first_name, last_name, date_of_birth, contact_number, email, address)
VALUES 
('John', 'Doe', '1990-01-01', '1234567890', 'john.doe@example.com', '123 Main St');

INSERT INTO client_goals (client_id, goal_description)
VALUES 
(1, 'Improve mobility');

INSERT INTO support_services (service_name, service_description)
VALUES 
('Physiotherapy', 'Physical therapy sessions');

INSERT INTO client_support_services (client_id, service_id)
VALUES 
(1, 1);

INSERT INTO community_activities (activity_name, activity_description)
VALUES 
('Community outing', 'Outing to local park');

INSERT INTO client_community_engagement (client_id, activity_id)
VALUES 
(1, 1);

INSERT INTO service_providers (provider_name, contact_number, email)
VALUES 
('Provider1', '0987654321', 'provider1@example.com');

INSERT INTO service_provider_allocations (service_id, provider_id, allocation_date)
VALUES 
(1, 1, '2024-01-01');
```
