"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: "Design a simple database schema to store information about Capina Elétrica's applications, including client feedback and results from different sectors (e.g., agricultural, urban)."
Generated: DETERMINISTIC_059fcbc2ee1c9032
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Capina Elétrica's applications

-- Table to store information about applications
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    ApplicationName VARCHAR(255) NOT NULL,        -- Name of the application
    Description TEXT,                             -- Description of the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the application was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store client feedback
CREATE TABLE ClientFeedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each feedback entry
    ApplicationID INT NOT NULL,                  -- Foreign key referencing the application
    ClientName VARCHAR(255),                     -- Name of the client providing feedback
    FeedbackText TEXT NOT NULL,                  -- Feedback content
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating provided by the client (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the feedback was created
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store results from different sectors
CREATE TABLE SectorResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each result entry
    ApplicationID INT NOT NULL,                  -- Foreign key referencing the application
    SectorName ENUM('Agricultural', 'Urban', 'Industrial', 'Other') NOT NULL, -- Sector name
    ResultDescription TEXT NOT NULL,             -- Description of the result
    SuccessRate DECIMAL(5, 2) CHECK (SuccessRate BETWEEN 0 AND 100), -- Success rate (percentage)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the result was created
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for performance optimization
CREATE INDEX idx_application_name ON Applications(ApplicationName); -- Index for quick lookup by application name
CREATE INDEX idx_client_feedback_application ON ClientFeedback(ApplicationID); -- Index for feedback lookup by application
CREATE INDEX idx_sector_results_application ON SectorResults(ApplicationID); -- Index for results lookup by application
```
