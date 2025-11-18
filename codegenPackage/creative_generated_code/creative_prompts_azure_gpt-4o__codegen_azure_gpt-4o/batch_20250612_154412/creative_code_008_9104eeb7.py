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
-- Database schema for managing debt collection workflows

-- Table to store information about debt collection agents
CREATE TABLE Agents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the agent
    FullName VARCHAR(100) NOT NULL,         -- Full name of the agent
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Email of the agent
    PhoneNumber VARCHAR(15),                -- Contact number of the agent
    HireDate DATE NOT NULL,                 -- Date the agent was hired
    Status ENUM('Active', 'Inactive') DEFAULT 'Active', -- Current status of the agent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Table to store debt collection cases
CREATE TABLE DebtCases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the case
    DebtorName VARCHAR(100) NOT NULL,       -- Full name of the debtor
    DebtorEmail VARCHAR(100),               -- Email of the debtor
    DebtorPhone VARCHAR(15),                -- Contact number of the debtor
    AmountDue DECIMAL(10, 2) NOT NULL,      -- Amount owed by the debtor
    DueDate DATE NOT NULL,                  -- Due date for payment
    AgentID INT,                            -- Foreign key referencing the agent handling the case
    Status ENUM('Open', 'Closed', 'In Progress', 'Failed') DEFAULT 'Open', -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) ON DELETE SET NULL ON UPDATE CASCADE -- Maintaining referential integrity
);

-- Table to track actions taken by agents on debt cases
CREATE TABLE CaseActions (
    ActionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the action
    CaseID INT NOT NULL,                     -- Foreign key referencing the case
    AgentID INT NOT NULL,                    -- Foreign key referencing the agent
    ActionType ENUM('Call', 'Email', 'Follow-Up', 'Negotiation', 'Closure') NOT NULL, -- Type of action
    Notes TEXT,                              -- Additional notes about the action
    ActionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the action was performed
    FOREIGN KEY (CaseID) REFERENCES DebtCases(CaseID) ON DELETE CASCADE ON UPDATE CASCADE, -- Ensuring case integrity
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensuring agent integrity
);

-- Table to store performance metrics of agents
CREATE TABLE AgentPerformance (
    PerformanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for performance record
    AgentID INT NOT NULL,                         -- Foreign key referencing the agent
    TotalCasesHandled INT NOT NULL,               -- Total number of cases handled by the agent
    SuccessfulRecoveries INT NOT NULL,            -- Number of successfully recovered debts
    FailedRecoveries INT NOT NULL,                -- Number of failed recoveries
    AverageRecoveryTime DECIMAL(5, 2),            -- Average time (in days) to recover debts
    ReportDate DATE NOT NULL,                     -- Date of the performance report
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintaining referential integrity
);

-- Table to store analytics data for operational insights
CREATE TABLE Analytics (
    AnalyticsID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for analytics record
    MetricName VARCHAR(100) NOT NULL,               -- Name of the metric (e.g., 'Recovery Rate', 'Average Case Time')
    MetricValue DECIMAL(10, 2) NOT NULL,            -- Value of the metric
    ReportDate DATE NOT NULL,                       -- Date the metric was calculated
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Indexes to improve performance
CREATE INDEX idx_agent_status ON Agents(Status); -- Index for querying agents by status
CREATE INDEX idx_case_status ON DebtCases(Status); -- Index for querying cases by status
CREATE INDEX idx_action_date ON CaseActions(ActionDate); -- Index for querying actions by date
CREATE INDEX idx_performance_agent ON AgentPerformance(AgentID); -- Index for querying agent performance

-- Error handling notes:
-- - Ensure the database engine supports foreign key constraints (e.g., InnoDB for MySQL).
-- - Use appropriate data validation in the application layer to prevent invalid data entry.
-- - Implement logging mechanisms in the application for troubleshooting database-related issues.
```
