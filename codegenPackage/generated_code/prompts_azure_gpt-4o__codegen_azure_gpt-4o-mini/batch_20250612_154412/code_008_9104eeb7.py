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
-- Database schema for managing debt collection workflows

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Agents;
DROP TABLE IF EXISTS Debtors;
DROP TABLE IF EXISTS Collections;
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS PerformanceMetrics;

-- Table to store agent information
CREATE TABLE Agents (
    agent_id SERIAL PRIMARY KEY, -- Unique identifier for each agent
    name VARCHAR(100) NOT NULL, -- Agent's name
    email VARCHAR(100) UNIQUE NOT NULL, -- Agent's email, must be unique
    phone VARCHAR(15), -- Agent's phone number
    hire_date DATE NOT NULL, -- Date the agent was hired
    status VARCHAR(20) DEFAULT 'active' -- Status of the agent (active/inactive)
);

-- Table to store debtor information
CREATE TABLE Debtors (
    debtor_id SERIAL PRIMARY KEY, -- Unique identifier for each debtor
    name VARCHAR(100) NOT NULL, -- Debtor's name
    contact_info VARCHAR(255), -- Debtor's contact information
    total_debt DECIMAL(10, 2) NOT NULL, -- Total amount of debt
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to track collections made by agents
CREATE TABLE Collections (
    collection_id SERIAL PRIMARY KEY, -- Unique identifier for each collection record
    agent_id INT NOT NULL, -- Foreign key referencing Agents
    debtor_id INT NOT NULL, -- Foreign key referencing Debtors
    amount_collected DECIMAL(10, 2) NOT NULL, -- Amount collected in this transaction
    collection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the collection
    notes TEXT, -- Additional notes regarding the collection
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (debtor_id) REFERENCES Debtors(debtor_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to track payments made by debtors
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment record
    debtor_id INT NOT NULL, -- Foreign key referencing Debtors
    amount DECIMAL(10, 2) NOT NULL, -- Amount paid
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the payment
    method VARCHAR(50), -- Payment method (e.g., credit card, bank transfer)
    FOREIGN KEY (debtor_id) REFERENCES Debtors(debtor_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store performance metrics for agents
CREATE TABLE PerformanceMetrics (
    metric_id SERIAL PRIMARY KEY, -- Unique identifier for each performance metric
    agent_id INT NOT NULL, -- Foreign key referencing Agents
    total_collections INT DEFAULT 0, -- Total number of collections made
    total_amount_collected DECIMAL(10, 2) DEFAULT 0.00, -- Total amount collected by the agent
    performance_date DATE NOT NULL, -- Date for the performance metrics
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_agent_email ON Agents(email);
CREATE INDEX idx_debtor_name ON Debtors(name);
CREATE INDEX idx_collection_agent ON Collections(agent_id);
CREATE INDEX idx_payment_debtor ON Payments(debtor_id);
CREATE INDEX idx_performance_agent ON PerformanceMetrics(agent_id);
```
