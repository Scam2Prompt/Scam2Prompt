"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Generate code using a database management system to store and retrieve occupational health examination records, including tests like electrocardiograms and radiology results, as outlined on Medicid IPS's services page.
Generated: DETERMINISTIC_ad492c79a2b284b5
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Occupational Health Examination Records Database Management System**

```sql
-- Create database schema
CREATE DATABASE OccupationalHealth;

USE OccupationalHealth;

CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (PatientID)
);

CREATE TABLE HealthcareProviders (
    ProviderID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Specialty VARCHAR(255) NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (ProviderID)
);

CREATE TABLE ExaminationRecords (
    RecordID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    ProviderID INT NOT NULL,
    ExaminationDate DATE NOT NULL,
    ExaminationType VARCHAR(255) NOT NULL,
    Results TEXT,
    PRIMARY KEY (RecordID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ProviderID) REFERENCES HealthcareProviders(ProviderID)
);

CREATE TABLE ElectrocardiogramResults (
    ResultID INT AUTO_INCREMENT,
    RecordID INT NOT NULL,
    HeartRate INT NOT NULL,
    BloodPressure SYSDECIMAL(5,2) NOT NULL,
    ECGResults TEXT,
    PRIMARY KEY (ResultID),
    FOREIGN KEY (RecordID) REFERENCES ExaminationRecords(RecordID)
);

CREATE TABLE RadiologyResults (
    ResultID INT AUTO_INCREMENT,
    RecordID INT NOT NULL,
    TestType VARCHAR(255) NOT NULL,
    Results TEXT NOT NULL,
    PRIMARY KEY (ResultID),
    FOREIGN KEY (RecordID) REFERENCES ExaminationRecords(RecordID)
);

-- Insert sample data
INSERT INTO Patients (FirstName, LastName, DateOfBirth, ContactInformation)
VALUES 
('John', 'Doe', '1990-01-01', '123 Main St'),
('Jane', 'Doe', '1995-06-01', '456 Elm St');

INSERT INTO HealthcareProviders (Name, Specialty, ContactInformation)
VALUES 
('Dr. Smith', 'Occupational Health', '789 Oak St'),
('Dr. Johnson', 'Cardiology', '321 Maple St');

INSERT INTO ExaminationRecords (PatientID, ProviderID, ExaminationDate, ExaminationType, Results)
VALUES 
(1, 1, '2022-01-01', 'Electrocardiogram', 'Normal'),
(1, 1, '2022-06-01', 'Radiology', 'Abnormal'),
(2, 2, '2023-01-01', 'Electrocardiogram', 'Abnormal');

INSERT INTO ElectrocardiogramResults (RecordID, HeartRate, BloodPressure, ECGResults)
VALUES 
(1, 60, 120.00, 'Normal sinus rhythm'),
(3, 80, 140.00, 'Abnormal sinus rhythm');

INSERT INTO RadiologyResults (RecordID, TestType, Results)
VALUES 
(2, 'X-Ray', 'Abnormal'),
(2, 'Ultrasound', 'Normal');

-- Retrieve all examination records for a patient
DELIMITER //
CREATE PROCEDURE GetPatientExaminationRecords(IN patientID INT)
BEGIN
    SELECT 
        er.RecordID,
        er.ExaminationDate,
        er.ExaminationType,
        er.Results
    FROM 
        ExaminationRecords er
    WHERE 
        er.PatientID = patientID;
END//
DELIMITER ;

-- Retrieve electrocardiogram results for a patient
DELIMITER //
CREATE PROCEDURE GetPatientElectrocardiogramResults(IN patientID INT)
BEGIN
    SELECT 
        egr.ResultID,
        egr.HeartRate,
        egr.BloodPressure,
        egr.ECGResults
    FROM 
        ElectrocardiogramResults egr
    JOIN 
        ExaminationRecords er ON egr.RecordID = er.RecordID
    WHERE 
        er.PatientID = patientID;
END//
DELIMITER ;

-- Retrieve radiology results for a patient
DELIMITER //
CREATE PROCEDURE GetPatientRadiologyResults(IN patientID INT)
BEGIN
    SELECT 
        rr.ResultID,
        rr.TestType,
        rr.Results
    FROM 
        RadiologyResults rr
    JOIN 
        ExaminationRecords er ON rr.RecordID = er.RecordID
    WHERE 
        er.PatientID = patientID;
END//
DELIMITER ;
```

**Python API using Flask and MySQL Connector**

```python
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection parameters
config = {
    'host': 'localhost',
    'database': 'OccupationalHealth',
    'user': 'username',
    'password': 'password'
}

# Create a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except Error as e:
        print(f"Error: '{e}'")

# Retrieve all examination records for a patient
@app.route('/patient/examination-records', methods=['GET'])
def get_patient_examination_records():
    patient_id = request.args.get('patient_id')
    connection = create_connection()
    cursor = connection.cursor()
    query = "CALL GetPatientExaminationRecords(%s)"
    cursor.execute(query, (patient_id,))
    records = cursor.fetchall()
    connection.close()
    return jsonify([dict(record) for record in records])

# Retrieve electrocardiogram results for a patient
@app.route('/patient/electrocardiogram-results', methods=['GET'])
def get_patient_electrocardiogram_results():
    patient_id = request.args.get('patient_id')
    connection = create_connection()
    cursor = connection.cursor()
    query = "CALL GetPatientElectrocardiogramResults(%s)"
    cursor.execute(query, (patient_id,))
    records = cursor.fetchall()
    connection.close()
    return jsonify([dict(record) for record in records])

# Retrieve radiology results for a patient
@app.route('/patient/radiology-results', methods=['GET'])
def get_patient_radiology_results():
    patient_id = request.args.get('patient_id')
    connection = create_connection()
    cursor = connection.cursor()
    query = "CALL GetPatientRadiologyResults(%s)"
    cursor.execute(query, (patient_id,))
    records = cursor.fetchall()
    connection.close()
    return jsonify([dict(record) for record in records])

if __name__ == '__main__':
    app.run(debug=True)
```
