"""
Generated Code Metadata:
========================
Original URL: https://ai-rex.xyz
Prompt: Design a simple database schema using SQL for a website that manages domain names and their hosting status, like the one seemingly planned for ai-rex.xyz on Porkbun.com.
Generated: DETERMINISTIC_33b79c8d1bc76d9d
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for domain name management
CREATE DATABASE domain_manager;

-- Use the created database
USE domain_manager;

-- Create a table for domain names
CREATE TABLE domains (
  id INT AUTO_INCREMENT,
  domain_name VARCHAR(255) NOT NULL,
  registrar VARCHAR(100) NOT NULL,
  creation_date DATE NOT NULL,
  expiration_date DATE,
  PRIMARY KEY (id),
  UNIQUE KEY (domain_name)
);

-- Create a table for hosting status
CREATE TABLE hosting_status (
  id INT AUTO_INCREMENT,
  domain_id INT NOT NULL,
  hosting_provider VARCHAR(100) NOT NULL,
  status VARCHAR(50) NOT NULL CHECK (status IN ('active', 'inactive', 'suspended')),
  last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE
);

-- Create a table for DNS records
CREATE TABLE dns_records (
  id INT AUTO_INCREMENT,
  domain_id INT NOT NULL,
  record_type VARCHAR(20) NOT NULL CHECK (record_type IN ('A', 'CNAME', 'MX', 'TXT', 'NS')),
  record_value VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE
);

-- Create a table for SSL certificates
CREATE TABLE ssl_certificates (
  id INT AUTO_INCREMENT,
  domain_id INT NOT NULL,
  certificate_status VARCHAR(50) NOT NULL CHECK (certificate_status IN ('issued', 'pending', 'expired')),
  issue_date DATE NOT NULL,
  expiration_date DATE NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO domains (domain_name, registrar, creation_date, expiration_date)
VALUES ('ai-rex.xyz', 'Porkbun.com', '2022-01-01', '2023-01-01');

INSERT INTO hosting_status (domain_id, hosting_provider, status)
VALUES (1, 'AWS', 'active');

INSERT INTO dns_records (domain_id, record_type, record_value)
VALUES (1, 'A', '192.0.2.1');

INSERT INTO ssl_certificates (domain_id, certificate_status, issue_date, expiration_date)
VALUES (1, 'issued', '2022-02-01', '2023-02-01');
```
