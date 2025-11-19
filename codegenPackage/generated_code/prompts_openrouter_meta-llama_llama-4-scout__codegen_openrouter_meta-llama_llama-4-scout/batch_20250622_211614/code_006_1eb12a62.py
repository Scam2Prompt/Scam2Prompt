"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: "Design a database schema to store payroll information for a company using Perfect Payrolls' services, including employee details, pay rates, and tax codes."
Generated: DETERMINISTIC_1eb12a6249790159
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- payroll_schema.sql

-- Create a database schema for storing payroll information

-- Create database
CREATE DATABASE PerfectPayrolls;

-- Use the database
USE PerfectPayrolls;

-- Create table for tax codes
CREATE TABLE TaxCodes (
  TaxCodeID INT AUTO_INCREMENT,
  TaxCode VARCHAR(10) NOT NULL,
  Description VARCHAR(255) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (TaxCodeID)
);

-- Create table for pay rates
CREATE TABLE PayRates (
  PayRateID INT AUTO_INCREMENT,
  PayRate DECIMAL(10, 2) NOT NULL,
  PayRateType VARCHAR(20) NOT NULL CHECK (PayRateType IN ('hourly', 'salaried')),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PayRateID)
);

-- Create table for employee details
CREATE TABLE Employees (
  EmployeeID INT AUTO_INCREMENT,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  DateOfBirth DATE NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(50) NOT NULL,
  State VARCHAR(50) NOT NULL,
  ZipCode VARCHAR(10) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (EmployeeID)
);

-- Create table for employee pay rates
CREATE TABLE EmployeePayRates (
  EmployeePayRateID INT AUTO_INCREMENT,
  EmployeeID INT NOT NULL,
  PayRateID INT NOT NULL,
  EffectiveDate DATE NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (EmployeePayRateID),
  FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
  FOREIGN KEY (PayRateID) REFERENCES PayRates(PayRateID)
);

-- Create table for employee tax codes
CREATE TABLE EmployeeTaxCodes (
  EmployeeTaxCodeID INT AUTO_INCREMENT,
  EmployeeID INT NOT NULL,
  TaxCodeID INT NOT NULL,
  EffectiveDate DATE NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (EmployeeTaxCodeID),
  FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
  FOREIGN KEY (TaxCodeID) REFERENCES TaxCodes(TaxCodeID)
);

-- Create table for payroll records
CREATE TABLE PayrollRecords (
  PayrollRecordID INT AUTO_INCREMENT,
  EmployeeID INT NOT NULL,
  PayDate DATE NOT NULL,
  GrossPay DECIMAL(10, 2) NOT NULL,
  TaxesWithheld DECIMAL(10, 2) NOT NULL,
  NetPay DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PayrollRecordID),
  FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_EmployeePayRates_EmployeeID ON EmployeePayRates (EmployeeID);
CREATE INDEX idx_EmployeePayRates_PayRateID ON EmployeePayRates (PayRateID);
CREATE INDEX idx_EmployeeTaxCodes_EmployeeID ON EmployeeTaxCodes (EmployeeID);
CREATE INDEX idx_EmployeeTaxCodes_TaxCodeID ON EmployeeTaxCodes (TaxCodeID);
CREATE INDEX idx_PayrollRecords_EmployeeID ON PayrollRecords (EmployeeID);
```

```sql
-- sample_data.sql

-- Insert sample data into the database

-- Insert tax codes
INSERT INTO TaxCodes (TaxCode, Description)
VALUES
  ('S', 'Single'),
  ('M', 'Married'),
  ('H', 'Head of Household');

-- Insert pay rates
INSERT INTO PayRates (PayRate, PayRateType)
VALUES
  (20.00, 'hourly'),
  (50000.00, 'salaried'),
  (30.00, 'hourly');

-- Insert employee details
INSERT INTO Employees (FirstName, LastName, DateOfBirth, Address, City, State, ZipCode)
VALUES
  ('John', 'Doe', '1990-01-01', '123 Main St', 'Anytown', 'CA', '12345'),
  ('Jane', 'Smith', '1995-06-01', '456 Elm St', 'Othertown', 'NY', '67890'),
  ('Bob', 'Johnson', '1980-03-01', '789 Oak St', 'Thistown', 'TX', '34567');

-- Insert employee pay rates
INSERT INTO EmployeePayRates (EmployeeID, PayRateID, EffectiveDate)
VALUES
  (1, 1, '2022-01-01'),
  (2, 2, '2022-06-01'),
  (3, 3, '2022-03-01');

-- Insert employee tax codes
INSERT INTO EmployeeTaxCodes (EmployeeID, TaxCodeID, EffectiveDate)
VALUES
  (1, 1, '2022-01-01'),
  (2, 2, '2022-06-01'),
  (3, 3, '2022-03-01');

-- Insert payroll records
INSERT INTO PayrollRecords (EmployeeID, PayDate, GrossPay, TaxesWithheld, NetPay)
VALUES
  (1, '2022-01-15', 4000.00, 1000.00, 3000.00),
  (2, '2022-06-15', 6000.00, 1500.00, 4500.00),
  (3, '2022-03-15', 5000.00, 1200.00, 3800.00);
```
