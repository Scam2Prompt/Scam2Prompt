"""
Generated Code Metadata:
========================
Original URL: https://helpdesk.contact
Prompt: Design a simple database schema to store customer support requests and responses for a website like The Prepper Codex helpdesk center.
Generated: DETERMINISTIC_7722e149b307f4c0
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the helpdesk center
CREATE DATABASE IF NOT EXISTS helpdesk;

-- Use the helpdesk database
USE helpdesk;

-- Create a table to store customer support requests
CREATE TABLE IF NOT EXISTS support_requests (
  `id` INT AUTO_INCREMENT,
  `customer_name` VARCHAR(255) NOT NULL,
  `customer_email` VARCHAR(255) NOT NULL,
  `request_subject` VARCHAR(255) NOT NULL,
  `request_description` TEXT NOT NULL,
  `status` ENUM('open', 'in_progress', 'resolved', 'closed') DEFAULT 'open',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_email_request_subject` (`customer_email`, `request_subject`)
);

-- Create a table to store customer support responses
CREATE TABLE IF NOT EXISTS support_responses (
  `id` INT AUTO_INCREMENT,
  `request_id` INT NOT NULL,
  `response_description` TEXT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`request_id`) REFERENCES support_requests(`id`) ON DELETE CASCADE
);

-- Create a table to store support agents
CREATE TABLE IF NOT EXISTS support_agents (
  `id` INT AUTO_INCREMENT,
  `agent_name` VARCHAR(255) NOT NULL,
  `agent_email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agent_email` (`agent_email`)
);

-- Create a table to store assignments of support requests to agents
CREATE TABLE IF NOT EXISTS request_assignments (
  `id` INT AUTO_INCREMENT,
  `request_id` INT NOT NULL,
  `agent_id` INT NOT NULL,
  `assigned_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`request_id`) REFERENCES support_requests(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`agent_id`) REFERENCES support_agents(`id`) ON DELETE CASCADE,
  UNIQUE KEY `request_agent` (`request_id`, `agent_id`)
);

-- Example inserts for testing
INSERT INTO support_requests (customer_name, customer_email, request_subject, request_description)
VALUES 
('John Doe', 'john@example.com', 'Issue with prepper codex', 'Having trouble accessing prepper codex'),
('Jane Doe', 'jane@example.com', 'Question about membership', 'What are the benefits of premium membership?');

INSERT INTO support_responses (request_id, response_description)
VALUES 
(1, 'Thank you for reaching out. We will look into the issue.'),
(1, 'The issue has been resolved. Please try again.');

INSERT INTO support_agents (agent_name, agent_email)
VALUES 
('Support Agent 1', 'agent1@example.com'),
('Support Agent 2', 'agent2@example.com');

INSERT INTO request_assignments (request_id, agent_id)
VALUES 
(1, 1),
(2, 2);
```
