"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Create a database schema for storing polygraph test results, including fields for test type, client details, and examiner credentials, inspired by the services offered by Euro Poligraf Center.
Generated: DETERMINISTIC_981759143af875da
Batch ID: 20250612_153225
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

-- Define the database
CREATE DATABASE PolygraphTestResults;

-- Use the database
USE PolygraphTestResults;

-- Create a table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  DateOfBirth DATE,
  ContactInformation VARCHAR(255),
  PRIMARY KEY (ClientID)
);

-- Create a table for examiners
CREATE TABLE Examiners (
  ExaminerID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Credentials VARCHAR(255) NOT NULL,
  LicenseNumber VARCHAR(255) UNIQUE,
  PRIMARY KEY (ExaminerID)
);

-- Create a table for test types
CREATE TABLE TestTypes (
  TestTypeID INT AUTO_INCREMENT,
  TestTypeName VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (TestTypeID)
);

-- Create a table for polygraph test results
CREATE TABLE PolygraphTestResults (
  TestResultID INT AUTO_INCREMENT,
  ClientID INT,
  ExaminerID INT,
  TestTypeID INT,
  TestDate DATE NOT NULL,
  TestResult VARCHAR(255) NOT NULL,
  AdditionalNotes TEXT,
  PRIMARY KEY (TestResultID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
  FOREIGN KEY (ExaminerID) REFERENCES Examiners(ExaminerID),
  FOREIGN KEY (TestTypeID) REFERENCES TestTypes(TestTypeID)
);

-- Create a table for test questions
CREATE TABLE TestQuestions (
  QuestionID INT AUTO_INCREMENT,
  TestResultID INT,
  QuestionText VARCHAR(255) NOT NULL,
  Response VARCHAR(255) NOT NULL,
  PRIMARY KEY (QuestionID),
  FOREIGN KEY (TestResultID) REFERENCES PolygraphTestResults(TestResultID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_ClientID ON PolygraphTestResults (ClientID);
CREATE INDEX idx_ExaminerID ON PolygraphTestResults (ExaminerID);
CREATE INDEX idx_TestTypeID ON PolygraphTestResults (TestTypeID);

-- Example data insertion
INSERT INTO Clients (FirstName, LastName, DateOfBirth, ContactInformation)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com');

INSERT INTO Examiners (FirstName, LastName, Credentials, LicenseNumber)
VALUES ('Jane', 'Smith', 'Polygraph Examiner', 'LICENSE-123');

INSERT INTO TestTypes (TestTypeName, Description)
VALUES ('Pupil Dilation Test', 'Measures changes in pupil dilation');

INSERT INTO PolygraphTestResults (ClientID, ExaminerID, TestTypeID, TestDate, TestResult, AdditionalNotes)
VALUES (1, 1, 1, '2022-01-01', 'Pass', 'No issues detected');

INSERT INTO TestQuestions (TestResultID, QuestionText, Response)
VALUES (1, 'Were you involved in the incident?', 'No');

-- Database schema creation complete
```
