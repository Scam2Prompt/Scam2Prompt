"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Provide an example of a database schema for managing governance policies and organizational decisions, inspired by the "الحوكمة السياسات واللوائح" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_345a998f4a95907b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Governance Policies and Organizational Decisions

-- Create a table to store governance policies
CREATE TABLE GovernancePolicies (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each policy
    Title VARCHAR(255) NOT NULL, -- Title of the policy
    Description TEXT, -- Detailed description of the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the policy was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the policy was last updated
    CreatedBy INT, -- User ID of the creator
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID) -- Reference to the Users table
);

-- Create a table to store organizational decisions
CREATE TABLE OrganizationalDecisions (
    DecisionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each decision
    Title VARCHAR(255) NOT NULL, -- Title of the decision
    Description TEXT, -- Detailed description of the decision
    DecisionDate DATE NOT NULL, -- Date when the decision was made
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the decision was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the decision was last updated
    CreatedBy INT, -- User ID of the creator
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID) -- Reference to the Users table
);

-- Create a table to store users who can create policies and decisions
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each user
    Username VARCHAR(100) NOT NULL UNIQUE, -- Username of the user
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(255) NOT NULL UNIQUE, -- User's email address
    Role ENUM('admin', 'editor', 'viewer') NOT NULL, -- Role of the user in the organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Create a table to link policies and decisions for better traceability
CREATE TABLE PolicyDecisionLinks (
    LinkID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each link
    PolicyID INT NOT NULL, -- Foreign key reference to GovernancePolicies
    DecisionID INT NOT NULL, -- Foreign key reference to OrganizationalDecisions
    FOREIGN KEY (PolicyID) REFERENCES GovernancePolicies(PolicyID) ON DELETE CASCADE, -- Ensure policy is deleted if no longer linked
    FOREIGN KEY (DecisionID) REFERENCES OrganizationalDecisions(DecisionID) ON DELETE CASCADE -- Ensure decision is deleted if no longer linked
);

-- Create a table for storing audit logs for changes made to policies and decisions
CREATE TABLE AuditLogs (
    LogID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each log entry
    Action ENUM('CREATE', 'UPDATE', 'DELETE') NOT NULL, -- Type of action performed
    TableAffected ENUM('GovernancePolicies', 'OrganizationalDecisions') NOT NULL, -- Table that was affected
    RecordID INT NOT NULL, -- ID of the record affected
    PerformedBy INT NOT NULL, -- User who performed the action
    PerformedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (PerformedBy) REFERENCES Users(UserID) -- Reference to the Users table
);
```
