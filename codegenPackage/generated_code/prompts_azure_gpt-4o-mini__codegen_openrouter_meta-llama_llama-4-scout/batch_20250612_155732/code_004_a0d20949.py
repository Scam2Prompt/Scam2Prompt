"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Illustrate how to implement a database schema in SQL to manage healthcare professional records for a placement agency like Seanda Healthcare.
Generated: DETERMINISTIC_a0d20949e3805fca
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for healthcare professional records
CREATE DATABASE HealthcareProfessionalDB;

-- Use the created database
USE HealthcareProfessionalDB;

-- Create a table for healthcare professional categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for healthcare professional specialties
CREATE TABLE Specialties (
    SpecialtyID INT AUTO_INCREMENT,
    SpecialtyName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SpecialtyID)
);

-- Create a table for healthcare professionals
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CategoryID INT,
    SpecialtyID INT,
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProfessionalID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (SpecialtyID) REFERENCES Specialties(SpecialtyID)
);

-- Create a table for professional certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT,
    ProfessionalID INT,
    CertificationName VARCHAR(255) NOT NULL,
    IssuingOrganization VARCHAR(255) NOT NULL,
    IssueDate DATE,
    ExpirationDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CertificationID),
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID)
);

-- Create a table for professional experience
CREATE TABLE Experience (
    ExperienceID INT AUTO_INCREMENT,
    ProfessionalID INT,
    Employer VARCHAR(255) NOT NULL,
    JobTitle VARCHAR(255) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ExperienceID),
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID)
);

-- Create a table for professional education
CREATE TABLE Education (
    EducationID INT AUTO_INCREMENT,
    ProfessionalID INT,
    Institution VARCHAR(255) NOT NULL,
    Degree VARCHAR(100) NOT NULL,
    FieldOfStudy VARCHAR(255) NOT NULL,
    GraduationDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (EducationID),
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID)
);

-- Create a stored procedure to insert a new healthcare professional
DELIMITER //
CREATE PROCEDURE InsertHealthcareProfessional(
    IN pFirstName VARCHAR(100),
    IN pLastName VARCHAR(100),
    IN pEmail VARCHAR(255),
    IN pPhone VARCHAR(20),
    IN pCategoryID INT,
    IN pSpecialtyID INT,
    IN pAddress VARCHAR(255),
    IN pCity VARCHAR(100),
    IN pState VARCHAR(100),
    IN pCountry VARCHAR(100),
    IN pPostalCode VARCHAR(20)
)
BEGIN
    INSERT INTO HealthcareProfessionals (
        FirstName,
        LastName,
        Email,
        Phone,
        CategoryID,
        SpecialtyID,
        Address,
        City,
        State,
        Country,
        PostalCode
    ) VALUES (
        pFirstName,
        pLastName,
        pEmail,
        pPhone,
        pCategoryID,
        pSpecialtyID,
        pAddress,
        pCity,
        pState,
        pCountry,
        pPostalCode
    );
END//
DELIMITER ;

-- Create a stored procedure to update a healthcare professional
DELIMITER //
CREATE PROCEDURE UpdateHealthcareProfessional(
    IN pProfessionalID INT,
    IN pFirstName VARCHAR(100),
    IN pLastName VARCHAR(100),
    IN pEmail VARCHAR(255),
    IN pPhone VARCHAR(20),
    IN pCategoryID INT,
    IN pSpecialtyID INT,
    IN pAddress VARCHAR(255),
    IN pCity VARCHAR(100),
    IN pState VARCHAR(100),
    IN pCountry VARCHAR(100),
    IN pPostalCode VARCHAR(20)
)
BEGIN
    UPDATE HealthcareProfessionals
    SET
        FirstName = pFirstName,
        LastName = pLastName,
        Email = pEmail,
        Phone = pPhone,
        CategoryID = pCategoryID,
        SpecialtyID = pSpecialtyID,
        Address = pAddress,
        City = pCity,
        State = pState,
        Country = pCountry,
        PostalCode = pPostalCode
    WHERE ProfessionalID = pProfessionalID;
END//
DELIMITER ;

-- Create a stored procedure to delete a healthcare professional
DELIMITER //
CREATE PROCEDURE DeleteHealthcareProfessional(
    IN pProfessionalID INT
)
BEGIN
    DELETE FROM HealthcareProfessionals
    WHERE ProfessionalID = pProfessionalID;
END//
DELIMITER ;
```
