"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Create a database schema to manage debt collection workflows, including features for tracking agent performance and analyzing results, based on Invicta Cobranças' services.
Generated: DETERMINISTIC_9104eeb72ed7cd8d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing debt collection workflows

-- Start by creating the main database
CREATE DATABASE IF NOT EXISTS DebtCollectionDB;

-- Use the new database
USE DebtCollectionDB;

-- Table to store information about debtors
CREATE TABLE Debtors (
    debtor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    total_debt DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store information about agents
CREATE TABLE Agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    performance_score DECIMAL(5, 2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to log debt collection activities
CREATE TABLE CollectionActivities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    debtor_id INT NOT NULL,
    agent_id INT NOT NULL,
    activity_type ENUM('Call', 'Email', 'Letter', 'In-Person', 'Payment Received') NOT NULL,
    activity_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (debtor_id) REFERENCES Debtors(debtor_id),
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
);

-- Table to track payments made by debtors
CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    debtor_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (debtor_id) REFERENCES Debtors(debtor_id)
);

-- Table to analyze agent performance
CREATE TABLE AgentPerformance (
    performance_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id INT NOT NULL,
    total_collections INT DEFAULT 0,
    total_revenue DECIMAL(10, 2) DEFAULT 0,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_agent_id ON CollectionActivities(agent_id);
CREATE INDEX idx_debtor_id ON CollectionActivities(debtor_id);
CREATE INDEX idx_payment_debtor ON Payments(debtor_id);

-- View to analyze overall collection success rate
CREATE VIEW CollectionSuccessRate AS
SELECT 
    a.agent_id,
    a.name AS agent_name,
    COUNT(c.activity_id) AS total_activities,
    SUM(CASE WHEN c.activity_type = 'Payment Received' THEN 1 ELSE 0 END) AS successful_collections,
    SUM(p.amount) AS total_revenue
FROM 
    Agents a
LEFT JOIN 
    CollectionActivities c ON a.agent_id = c.agent_id
LEFT JOIN 
    Payments p ON c.debtor_id = p.debtor_id
GROUP BY 
    a.agent_id;

-- Ensure proper error handling in transactions (example for future operations)
-- BEGIN;
-- INSERT INTO Debtors (name, contact_info, total_debt) VALUES ('John Doe', '555-1234', 1500.00);
-- COMMIT;
-- If an error occurs, use ROLLBACK to undo changes.

-- Schema setup complete. Ready for implementing application logic.
```
