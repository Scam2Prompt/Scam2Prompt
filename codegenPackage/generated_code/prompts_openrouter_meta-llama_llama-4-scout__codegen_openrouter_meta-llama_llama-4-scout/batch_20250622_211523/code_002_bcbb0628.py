"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: "Generate a sample database schema for storing information about property associations, including contact details, services offered, and client testimonials, inspired by BlocPrest's services."
Generated: DETERMINISTIC_bcbb062811f2d35d
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for property associations
CREATE DATABASE PropertyAssociations;

-- Use the database
USE PropertyAssociations;

-- Create a table for property associations
CREATE TABLE Associations (
    AssociationID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    PRIMARY KEY (AssociationID)
);

-- Create a table for contact details
CREATE TABLE Contacts (
    ContactID INT AUTO_INCREMENT,
    AssociationID INT NOT NULL,
    ContactName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Fax VARCHAR(20),
    PRIMARY KEY (ContactID),
    FOREIGN KEY (AssociationID) REFERENCES Associations(AssociationID)
);

-- Create a table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    AssociationID INT NOT NULL,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (AssociationID) REFERENCES Associations(AssociationID)
);

-- Create a table for client testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT,
    AssociationID INT NOT NULL,
    ClientName VARCHAR(255) NOT NULL,
    Testimonial TEXT NOT NULL,
    Rating TINYINT CHECK (Rating BETWEEN 1 AND 5),
    PRIMARY KEY (TestimonialID),
    FOREIGN KEY (AssociationID) REFERENCES Associations(AssociationID)
);

-- Create a table for association documents
CREATE TABLE Documents (
    DocumentID INT AUTO_INCREMENT,
    AssociationID INT NOT NULL,
    DocumentName VARCHAR(255) NOT NULL,
    DocumentType VARCHAR(100) NOT NULL,
    DocumentContent BLOB,
    PRIMARY KEY (DocumentID),
    FOREIGN KEY (AssociationID) REFERENCES Associations(AssociationID)
);

-- Create a table for association fees
CREATE TABLE Fees (
    FeeID INT AUTO_INCREMENT,
    AssociationID INT NOT NULL,
    FeeName VARCHAR(255) NOT NULL,
    FeeAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (FeeID),
    FOREIGN KEY (AssociationID) REFERENCES Associations(AssociationID)
);

-- Example insert statements
INSERT INTO Associations (Name, Address, City, State, Country, PostalCode)
VALUES 
('Sample Association', '123 Main St', 'Anytown', 'CA', 'USA', '12345');

INSERT INTO Contacts (AssociationID, ContactName, Email, Phone)
VALUES 
(1, 'John Doe', 'john.doe@example.com', '555-555-5555');

INSERT INTO Services (AssociationID, ServiceName, ServiceDescription)
VALUES 
(1, 'Pool Maintenance', 'Weekly pool cleaning and maintenance');

INSERT INTO Testimonials (AssociationID, ClientName, Testimonial, Rating)
VALUES 
(1, 'Jane Smith', 'The association does a great job!', 5);

INSERT INTO Documents (AssociationID, DocumentName, DocumentType)
VALUES 
(1, 'Minutes of Meeting', 'Meeting Minutes');

INSERT INTO Fees (AssociationID, FeeName, FeeAmount)
VALUES 
(1, 'Monthly Dues', 100.00);
```
