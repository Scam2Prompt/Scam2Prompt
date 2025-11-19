"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: "Create a simple database schema to store information about environmental testing samples, including sample matrix, turnaround time, and rush charges, inspired by A&B Labs' services."
Generated: DETERMINISTIC_e29e13adc1926784
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- environmental_testing_samples.sql

-- Create a database schema for environmental testing samples
CREATE DATABASE environmental_testing;

-- Use the environmental_testing database
USE environmental_testing;

-- Create a table for sample matrices
CREATE TABLE sample_matrices (
  id INT AUTO_INCREMENT,
  matrix_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for testing samples
CREATE TABLE testing_samples (
  id INT AUTO_INCREMENT,
  sample_matrix_id INT NOT NULL,
  sample_id VARCHAR(255) NOT NULL,
  turnaround_time ENUM('standard', 'rush', 'express') NOT NULL DEFAULT 'standard',
  rush_charge DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  testing_date DATE,
  results_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (sample_matrix_id) REFERENCES sample_matrices(id)
);

-- Create a table for sample test results
CREATE TABLE sample_test_results (
  id INT AUTO_INCREMENT,
  testing_sample_id INT NOT NULL,
  test_name VARCHAR(255) NOT NULL,
  test_result VARCHAR(255) NOT NULL,
  units VARCHAR(50),
  PRIMARY KEY (id),
  FOREIGN KEY (testing_sample_id) REFERENCES testing_samples(id)
);

-- Create a table for rush charge reasons
CREATE TABLE rush_charge_reasons (
  id INT AUTO_INCREMENT,
  reason_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for rush charge reasons and testing samples
CREATE TABLE testing_sample_rush_reasons (
  testing_sample_id INT NOT NULL,
  rush_charge_reason_id INT NOT NULL,
  PRIMARY KEY (testing_sample_id, rush_charge_reason_id),
  FOREIGN KEY (testing_sample_id) REFERENCES testing_samples(id),
  FOREIGN KEY (rush_charge_reason_id) REFERENCES rush_charge_reasons(id)
);

-- Insert sample data for testing
INSERT INTO sample_matrices (matrix_name, description)
VALUES
  ('Soil', 'Environmental soil samples'),
  ('Water', 'Environmental water samples'),
  ('Air', 'Environmental air samples');

INSERT INTO testing_samples (sample_matrix_id, sample_id, turnaround_time, rush_charge)
VALUES
  (1, 'SAMPLE-001', 'rush', 100.00),
  (2, 'SAMPLE-002', 'standard', 0.00),
  (3, 'SAMPLE-003', 'express', 200.00);

INSERT INTO sample_test_results (testing_sample_id, test_name, test_result, units)
VALUES
  (1, 'pH', '7.5', 'pH units'),
  (1, 'Lead', '10.2', 'mg/kg'),
  (2, 'Turbidity', '5.1', 'NTU'),
  (3, 'Particulate Matter', '35.7', 'µg/m³');

INSERT INTO rush_charge_reasons (reason_name, description)
VALUES
  ('Emergency Response', 'Rush charge for emergency response situations'),
  ('Client Request', 'Rush charge for client-requested expedited service');

INSERT INTO testing_sample_rush_reasons (testing_sample_id, rush_charge_reason_id)
VALUES
  (1, 1),
  (3, 2);
```
