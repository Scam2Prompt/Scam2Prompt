"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Create a database schema to manage debt collection workflows, including features for tracking agent performance and analyzing results, based on Invicta Cobranças' services.
Generated: DETERMINISTIC_9104eeb72ed7cd8d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for debt collection workflow management
CREATE DATABASE debt_collection;

-- Use the database schema
USE debt_collection;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for debts
CREATE TABLE debts (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  debt_amount DECIMAL(10, 2) NOT NULL,
  debt_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  due_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Create table for agents
CREATE TABLE agents (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for agent assignments
CREATE TABLE agent_assignments (
  id INT AUTO_INCREMENT,
  agent_id INT NOT NULL,
  debt_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (agent_id) REFERENCES agents(id),
  FOREIGN KEY (debt_id) REFERENCES debts(id)
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  debt_id INT NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_date DATE NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (debt_id) REFERENCES debts(id)
);

-- Create table for agent performance metrics
CREATE TABLE agent_performance (
  id INT AUTO_INCREMENT,
  agent_id INT NOT NULL,
  debt_id INT NOT NULL,
  outcome VARCHAR(50) NOT NULL,
  outcome_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (agent_id) REFERENCES agents(id),
  FOREIGN KEY (debt_id) REFERENCES debts(id)
);

-- Create views for analyzing results
CREATE VIEW debt_collection_summary AS
SELECT 
  c.name AS client_name,
  d.debt_amount AS debt_amount,
  COALESCE(p.payment_amount, 0) AS payment_amount,
  d.debt_status AS debt_status
FROM 
  clients c
  JOIN debts d ON c.id = d.client_id
  LEFT JOIN payments p ON d.id = p.debt_id;

CREATE VIEW agent_performance_summary AS
SELECT 
  a.name AS agent_name,
  COUNT(aa.id) AS debts_assigned,
  SUM(CASE WHEN ap.outcome = 'paid' THEN 1 ELSE 0 END) AS debts_paid,
  SUM(CASE WHEN ap.outcome = 'unpaid' THEN 1 ELSE 0 END) AS debts_unpaid
FROM 
  agents a
  LEFT JOIN agent_assignments aa ON a.id = aa.agent_id
  LEFT JOIN agent_performance ap ON aa.debt_id = ap.debt_id AND aa.agent_id = ap.agent_id
GROUP BY 
  a.name;

-- Create stored procedure to update debt status
DELIMITER //
CREATE PROCEDURE update_debt_status(IN debt_id INT, IN new_status VARCHAR(50))
BEGIN
  UPDATE debts SET debt_status = new_status WHERE id = debt_id;
END//
DELIMITER ;

-- Create stored procedure to assign debt to agent
DELIMITER //
CREATE PROCEDURE assign_debt_to_agent(IN agent_id INT, IN debt_id INT)
BEGIN
  INSERT INTO agent_assignments (agent_id, debt_id) VALUES (agent_id, debt_id);
END//
DELIMITER ;
```
