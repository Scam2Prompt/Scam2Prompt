"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Design a database schema to store information about NDIS services, including supported independent living, assistance with travel and transport, and community participation activities."
Generated: DETERMINISTIC_0e38bf9fc20e36d9
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for NDIS services
CREATE DATABASE ndis_services;

-- Use the ndis_services database
USE ndis_services;

-- Create table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for service types
CREATE TABLE service_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  service_provider_id INT NOT NULL,
  service_type_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id),
  FOREIGN KEY (service_type_id) REFERENCES service_types(id)
);

-- Create table for supported independent living services
CREATE TABLE supported_independent_living_services (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  daily_living_skills BOOLEAN NOT NULL DEFAULT FALSE,
  household_management BOOLEAN NOT NULL DEFAULT FALSE,
  medication_management BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for travel and transport services
CREATE TABLE travel_and_transport_services (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  transport_type VARCHAR(255) NOT NULL,
  assistance_type VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for community participation activities
CREATE TABLE community_participation_activities (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  activity_name VARCHAR(255) NOT NULL,
  activity_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for service bookings
CREATE TABLE service_bookings (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  participant_name VARCHAR(255) NOT NULL,
  booking_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_service_providers_email ON service_providers (email);
CREATE INDEX idx_services_service_provider_id ON services (service_provider_id);
CREATE INDEX idx_services_service_type_id ON services (service_type_id);
CREATE INDEX idx_supported_independent_living_services_service_id ON supported_independent_living_services (service_id);
CREATE INDEX idx_travel_and_transport_services_service_id ON travel_and_transport_services (service_id);
CREATE INDEX idx_community_participation_activities_service_id ON community_participation_activities (service_id);
CREATE INDEX idx_service_bookings_service_id ON service_bookings (service_id);
```

```sql
-- Example data insertion
INSERT INTO service_providers (name, email, phone_number, address)
VALUES 
('Provider 1', 'provider1@example.com', '1234567890', '123 Main St'),
('Provider 2', 'provider2@example.com', '9876543210', '456 Elm St');

INSERT INTO service_types (name, description)
VALUES 
('Supported Independent Living', 'Assistance with daily living skills'),
('Travel and Transport', 'Assistance with travel and transport'),
('Community Participation', 'Activities to promote community participation');

INSERT INTO services (service_provider_id, service_type_id, name, description)
VALUES 
(1, 1, 'SIL Service', 'Supported Independent Living service'),
(1, 2, 'Travel Service', 'Travel and transport service'),
(2, 3, 'Community Activity', 'Community participation activity');

INSERT INTO supported_independent_living_services (service_id, daily_living_skills, household_management, medication_management)
VALUES 
(1, TRUE, TRUE, TRUE);

INSERT INTO travel_and_transport_services (service_id, transport_type, assistance_type)
VALUES 
(2, 'Taxi', 'Wheelchair accessible');

INSERT INTO community_participation_activities (service_id, activity_name, activity_description)
VALUES 
(3, 'Volunteer Day', 'Volunteer day at local charity');

INSERT INTO service_bookings (service_id, participant_name, booking_date, start_time, end_time)
VALUES 
(1, 'John Doe', '2024-09-16', '09:00:00', '17:00:00');
```
