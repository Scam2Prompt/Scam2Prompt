"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Design a database schema to store information about Cartório Justiniano's clients, services, and documents, and provide a SQL script to populate the database with sample data.
Generated: DETERMINISTIC_b97f8c2f0d826848
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Cartório Justiniano

-- Create a database
CREATE DATABASE CartorioJustiniano;

-- Use the created database
USE CartorioJustiniano;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FullName VARCHAR(255) NOT NULL,          -- Full name of the client
    Email VARCHAR(255) UNIQUE,               -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store services offered by the cartório
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table to store documents related to clients
CREATE TABLE Documents (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    DocumentName VARCHAR(255) NOT NULL,        -- Name of the document
    DocumentType VARCHAR(50),                  -- Type of the document (e.g., ID, contract)
    IssuedDate DATE,                           -- Date the document was issued
    ExpiryDate DATE,                           -- Expiry date of the document (if applicable)
    FilePath VARCHAR(255),                     -- Path to the document file
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the document was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store transactions between clients and services
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the transaction
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Sample Data Population

-- Insert sample clients
INSERT INTO Clients (FullName, Email, PhoneNumber, Address) VALUES
('Maria Silva', 'maria.silva@example.com', '555-1234', '123 Main St, Cityville'),
('João Pereira', 'joao.pereira@example.com', '555-5678', '456 Elm St, Townsville'),
('Ana Costa', 'ana.costa@example.com', '555-9101', '789 Oak St, Villageville');

-- Insert sample services
INSERT INTO Services (ServiceName, Description, Price) VALUES
('Notarization', 'Official notarization of documents', 50.00),
('Authentication', 'Authentication of signatures and documents', 30.00),
('Document Translation', 'Translation of official documents', 100.00);

-- Insert sample documents
INSERT INTO Documents (ClientID, DocumentName, DocumentType, IssuedDate, ExpiryDate, FilePath) VALUES
(1, 'Maria ID', 'ID', '2020-01-01', '2030-01-01', '/documents/maria_id.pdf'),
(2, 'João Contract', 'Contract', '2022-05-15', NULL, '/documents/joao_contract.pdf'),
(3, 'Ana Passport', 'Passport', '2019-08-20', '2029-08-20', '/documents/ana_passport.pdf');

-- Insert sample transactions
INSERT INTO Transactions (ClientID, ServiceID, TotalAmount) VALUES
(1, 1, 50.00), -- Maria Silva used Notarization service
(2, 2, 30.00), -- João Pereira used Authentication service
(3, 3, 100.00); -- Ana Costa used Document Translation service
```
