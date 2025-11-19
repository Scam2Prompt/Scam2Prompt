"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Design a database schema for an NDIS provider that tracks client goals, support services, and community engagement, reflecting the tailored services provided by Shareth Homecare.
Generated: DETERMINISTIC_a8aa5596c86a478d
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- 
-- Database schema for an NDIS provider to track client goals, 
-- support services, and community engagement.
--

CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    NDISNumber VARCHAR(50) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Goals (
    GoalID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT NOT NULL,
    GoalDescription TEXT NOT NULL,
    TargetDate DATE NOT NULL,
    Status ENUM('Pending', 'In Progress', 'Achieved', 'Not Achieved') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

CREATE TABLE SupportServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceType VARCHAR(100) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Provider VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

CREATE TABLE CommunityEngagement (
    EngagementID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT NOT NULL,
    EngagementDescription TEXT NOT NULL,
    EngagementDate DATE NOT NULL,
    Outcome VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_client_ndis_number ON Clients(NDISNumber);
CREATE INDEX idx_client_goals ON Goals(ClientID);
CREATE INDEX idx_client_support_services ON SupportServices(ClientID);
CREATE INDEX idx_client_engagement ON CommunityEngagement(ClientID);
```
