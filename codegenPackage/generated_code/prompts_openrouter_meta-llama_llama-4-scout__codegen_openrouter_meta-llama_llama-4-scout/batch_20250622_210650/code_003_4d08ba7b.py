"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Design a database schema for storing polygraph test results, including fields for test type (e.g., pre-employment, fidelity), client information, and test outcomes."
Generated: DETERMINISTIC_4d08ba7b7d618723
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- polygraph_test_results_schema.sql

-- Create a database schema for storing polygraph test results

CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address VARCHAR(255),
  PRIMARY KEY (ClientID)
);

CREATE TABLE TestTypes (
  TestTypeID INT AUTO_INCREMENT,
  TestType VARCHAR(100) NOT NULL,
  Description TEXT,
  PRIMARY KEY (TestTypeID)
);

CREATE TABLE PolygraphTestResults (
  TestResultID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  TestTypeID INT NOT NULL,
  TestDate DATE NOT NULL,
  TestOutcome VARCHAR(100) NOT NULL,
  AdditionalNotes TEXT,
  PRIMARY KEY (TestResultID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
  FOREIGN KEY (TestTypeID) REFERENCES TestTypes(TestTypeID)
);

CREATE TABLE TestOutcomes (
  OutcomeID INT AUTO_INCREMENT,
  Outcome VARCHAR(100) NOT NULL,
  Description TEXT,
  PRIMARY KEY (OutcomeID)
);

ALTER TABLE PolygraphTestResults
ADD COLUMN OutcomeID INT,
ADD CONSTRAINT fk_outcome FOREIGN KEY (OutcomeID) REFERENCES TestOutcomes(OutcomeID);

-- Insert sample data for testing
INSERT INTO Clients (Name, Email, Phone, Address)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO TestTypes (TestType, Description)
VALUES 
('Pre-Employment', 'Polygraph test for employment screening'),
('Fidelity', 'Polygraph test for relationship verification');

INSERT INTO TestOutcomes (Outcome)
VALUES 
('No Deception Indicated'),
('Deception Indicated'),
('Inconclusive');

INSERT INTO PolygraphTestResults (ClientID, TestTypeID, TestDate, OutcomeID, AdditionalNotes)
VALUES 
(1, 1, '2022-01-01', 1, 'Test was administered without incident'),
(2, 2, '2022-02-01', 2, 'Test results indicated deception');

-- Indexing for performance optimization
CREATE INDEX idx_client_id ON PolygraphTestResults (ClientID);
CREATE INDEX idx_test_type_id ON PolygraphTestResults (TestTypeID);
CREATE INDEX idx_outcome_id ON PolygraphTestResults (OutcomeID);
```
