"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Design a database schema for managing records of children and adolescents served by CEFOR, including their situations and the services they receive.
Generated: DETERMINISTIC_00b1c106d2f1ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- cefor_schema.sql

-- Create a database schema for managing records of children and adolescents served by CEFOR

-- Create a database
CREATE DATABASE cefor;

-- Use the database
USE cefor;

-- Create a table for situations
CREATE TABLE situations (
  situation_id INT AUTO_INCREMENT,
  situation_name VARCHAR(255) NOT NULL,
  situation_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (situation_id)
);

-- Create a table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table for children and adolescents
CREATE TABLE beneficiaries (
  beneficiary_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  situation_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (beneficiary_id),
  FOREIGN KEY (situation_id) REFERENCES situations(situation_id) ON DELETE SET NULL
);

-- Create a table for beneficiary services
CREATE TABLE beneficiary_services (
  beneficiary_service_id INT AUTO_INCREMENT,
  beneficiary_id INT NOT NULL,
  service_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (beneficiary_service_id),
  FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
  UNIQUE KEY (beneficiary_id, service_id, start_date)
);

-- Create a table for service providers
CREATE TABLE service_providers (
  service_provider_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_provider_id)
);

-- Create a table for service provider services
CREATE TABLE service_provider_services (
  service_provider_service_id INT AUTO_INCREMENT,
  service_provider_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_provider_service_id),
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(service_provider_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
  UNIQUE KEY (service_provider_id, service_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_beneficiaries_situation_id ON beneficiaries (situation_id);
CREATE INDEX idx_beneficiary_services_beneficiary_id ON beneficiary_services (beneficiary_id);
CREATE INDEX idx_beneficiary_services_service_id ON beneficiary_services (service_id);
CREATE INDEX idx_service_provider_services_service_provider_id ON service_provider_services (service_provider_id);
CREATE INDEX idx_service_provider_services_service_id ON service_provider_services (service_id);
```
