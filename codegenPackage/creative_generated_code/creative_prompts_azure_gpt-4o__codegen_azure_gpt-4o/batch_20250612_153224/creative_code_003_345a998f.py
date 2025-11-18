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

-- Table to store information about governance policies
CREATE TABLE GovernancePolicies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each policy
    PolicyName VARCHAR(255) NOT NULL,        -- Name of the policy
    PolicyDescription TEXT,                 -- Detailed description of the policy
    CreatedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date the policy was created
    LastUpdatedDate DATETIME DEFAULT NULL,  -- Date the policy was last updated
    IsActive BOOLEAN NOT NULL DEFAULT TRUE  -- Whether the policy is active or not
);

-- Table to store organizational decisions
CREATE TABLE OrganizationalDecisions (
    DecisionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each decision
    DecisionTitle VARCHAR(255) NOT NULL,       -- Title of the decision
    DecisionDetails TEXT NOT NULL,             -- Detailed explanation of the decision
    DecisionDate DATETIME NOT NULL,            -- Date the decision was made
    PolicyID INT,                              -- Foreign key linking to GovernancePolicies
    ApprovedBy VARCHAR(255) NOT NULL,          -- Name or identifier of the approver
    Status ENUM('Pending', 'Approved', 'Rejected') NOT NULL DEFAULT 'Pending', -- Status of the decision
    FOREIGN KEY (PolicyID) REFERENCES GovernancePolicies(PolicyID) ON DELETE SET NULL
);

-- Table to store meeting records where decisions are made
CREATE TABLE Meetings (
    MeetingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each meeting
    MeetingDate DATETIME NOT NULL,            -- Date and time of the meeting
    Organizer VARCHAR(255) NOT NULL,          -- Name or identifier of the meeting organizer
    Agenda TEXT NOT NULL,                     -- Agenda of the meeting
    Notes TEXT,                               -- Additional notes or outcomes from the meeting
);

-- Table to link decisions to specific meetings
CREATE TABLE DecisionMeetingLink (
    LinkID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each link record
    DecisionID INT NOT NULL,               -- Foreign key linking to OrganizationalDecisions
    MeetingID INT NOT NULL,                -- Foreign key linking to Meetings
    FOREIGN KEY (DecisionID) REFERENCES OrganizationalDecisions(DecisionID) ON DELETE CASCADE,
    FOREIGN KEY (MeetingID) REFERENCES Meetings(MeetingID) ON DELETE CASCADE
);

-- Table to record users participating in the governance process
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- User email for contact
    Role ENUM('Admin', 'Member', 'Guest') NOT NULL DEFAULT 'Member', -- Role in the organization
    CreatedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date the user was added
    IsActive BOOLEAN NOT NULL DEFAULT TRUE -- Whether the user is active
);

-- Table to record user interactions with policies and decisions
CREATE TABLE UserInteractions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    UserID INT NOT NULL,                          -- Foreign key linking to Users
    PolicyID INT,                                 -- Foreign key linking to GovernancePolicies
    DecisionID INT,                               -- Foreign key linking to OrganizationalDecisions
    InteractionType ENUM('View', 'Edit', 'Approve', 'Reject') NOT NULL, -- Type of interaction
    InteractionDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date and time of the interaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (PolicyID) REFERENCES GovernancePolicies(PolicyID) ON DELETE SET NULL,
    FOREIGN KEY (DecisionID) REFERENCES OrganizationalDecisions(DecisionID) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX idx_GovernancePolicies_IsActive ON GovernancePolicies(IsActive);
CREATE INDEX idx_OrganizationalDecisions_Status ON OrganizationalDecisions(Status);
CREATE INDEX idx_Meetings_MeetingDate ON Meetings(MeetingDate);
CREATE INDEX idx_UserInteractions_InteractionDate ON UserInteractions(InteractionDate);
```
