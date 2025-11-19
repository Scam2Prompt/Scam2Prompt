"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Create a database schema to store information about humanitarian interventions, including details about affected regions, displaced persons, and medical aid, as described in Jusoor International's work."
Generated: DETERMINISTIC_401463d59ecf17ca
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- humanitarian_interventions_schema.sql

-- Create a database schema for humanitarian interventions
CREATE DATABASE humanitarian_interventions;

-- Use the database
USE humanitarian_interventions;

-- Create a table for regions
CREATE TABLE regions (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for humanitarian interventions
CREATE TABLE interventions (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  region_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (region_id) REFERENCES regions(id) ON DELETE CASCADE
);

-- Create a table for displaced persons
CREATE TABLE displaced_persons (
  id INT AUTO_INCREMENT,
  intervention_id INT,
  name VARCHAR(255),
  age INT,
  gender ENUM('male', 'female', 'other'),
  status ENUM('displaced', 'relocated', 'assisted'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (intervention_id) REFERENCES interventions(id) ON DELETE CASCADE
);

-- Create a table for medical aid
CREATE TABLE medical_aid (
  id INT AUTO_INCREMENT,
  intervention_id INT,
  type ENUM('food', 'water', 'shelter', 'medical_supplies', 'other'),
  quantity INT,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (intervention_id) REFERENCES interventions(id) ON DELETE CASCADE
);

-- Create a table for intervention personnel
CREATE TABLE personnel (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  role ENUM('doctor', 'nurse', 'logistics', 'other'),
  intervention_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (intervention_id) REFERENCES interventions(id) ON DELETE CASCADE
);

-- Create a table for donations
CREATE TABLE donations (
  id INT AUTO_INCREMENT,
  intervention_id INT,
  donor_name VARCHAR(255),
  amount DECIMAL(10, 2),
  currency ENUM('USD', 'EUR', 'GBP', 'other'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (intervention_id) REFERENCES interventions(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO regions (name, description, latitude, longitude)
VALUES 
('Syria', 'Conflict zone', 33.8883, 36.2333),
('Turkey', 'Host country', 41.0082, 28.9750);

INSERT INTO interventions (name, description, start_date, end_date, region_id)
VALUES 
('Syria Relief', 'Providing aid to Syria', '2022-01-01', '2022-12-31', 1),
('Turkey Support', 'Supporting refugees in Turkey', '2022-01-01', '2022-12-31', 2);

INSERT INTO displaced_persons (intervention_id, name, age, gender, status)
VALUES 
(1, 'John Doe', 30, 'male', 'displaced'),
(1, 'Jane Doe', 25, 'female', 'relocated'),
(2, 'Ali Refugee', 40, 'male', 'assisted');

INSERT INTO medical_aid (intervention_id, type, quantity, description)
VALUES 
(1, 'food', 1000, 'Food parcels'),
(1, 'medical_supplies', 500, 'Medicines and medical equipment'),
(2, 'shelter', 200, 'Tent and shelter materials');

INSERT INTO personnel (name, role, intervention_id)
VALUES 
('Dr. Smith', 'doctor', 1),
('Ms. Johnson', 'nurse', 1),
('Mr. Davis', 'logistics', 2);

INSERT INTO donations (intervention_id, donor_name, amount, currency)
VALUES 
(1, 'Anonymous', 10000.00, 'USD'),
(1, 'Red Cross', 5000.00, 'EUR'),
(2, 'Private Donor', 2000.00, 'GBP');
```
