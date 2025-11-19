"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Design a basic database schema to store information gathered during forensic investigations, including evidence and case details."
Generated: DETERMINISTIC_4fceb0bb900e5f27
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing forensic investigation information

-- Table to store case details
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each case
    CaseName VARCHAR(255) NOT NULL,        -- Name or title of the case
    InvestigatorName VARCHAR(255),         -- Name of the lead investigator
    DateOpened DATE NOT NULL,              -- Date the case was opened
    DateClosed DATE,                       -- Date the case was closed (nullable for ongoing cases)
    Status ENUM('Open', 'Closed', 'Pending') NOT NULL DEFAULT 'Open', -- Current status of the case
    Description TEXT                       -- Detailed description of the case
);

-- Table to store evidence details
CREATE TABLE Evidence (
    EvidenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each piece of evidence
    CaseID INT NOT NULL,                       -- Foreign key linking evidence to a case
    EvidenceType VARCHAR(255) NOT NULL,        -- Type of evidence (e.g., document, photo, video)
    Description TEXT,                          -- Detailed description of the evidence
    DateCollected DATE NOT NULL,               -- Date the evidence was collected
    LocationCollected VARCHAR(255),            -- Location where the evidence was collected
    IsAnalyzed BOOLEAN NOT NULL DEFAULT FALSE, -- Whether the evidence has been analyzed
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Cascade delete if case is deleted
);

-- Table to store analysis results for evidence
CREATE TABLE EvidenceAnalysis (
    AnalysisID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each analysis record
    EvidenceID INT NOT NULL,                   -- Foreign key linking analysis to evidence
    AnalystName VARCHAR(255) NOT NULL,         -- Name of the analyst who performed the analysis
    DateAnalyzed DATE NOT NULL,                -- Date the analysis was performed
    Findings TEXT,                             -- Findings from the analysis
    FOREIGN KEY (EvidenceID) REFERENCES Evidence(EvidenceID) ON DELETE CASCADE -- Cascade delete if evidence is deleted
);

-- Table to store case notes
CREATE TABLE CaseNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each note
    CaseID INT NOT NULL,                   -- Foreign key linking note to a case
    AuthorName VARCHAR(255) NOT NULL,      -- Name of the person who wrote the note
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the note was created
    NoteContent TEXT NOT NULL,             -- Content of the note
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Cascade delete if case is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_case_status ON Cases(Status); -- Index for querying cases by status
CREATE INDEX idx_evidence_type ON Evidence(EvidenceType); -- Index for querying evidence by type
CREATE INDEX idx_analysis_date ON EvidenceAnalysis(DateAnalyzed); -- Index for querying analysis by date
```
