"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Design a database schema for storing client testimonials, project details, and product information for a company specializing in UPVC window and door systems installations."
Generated: DETERMINISTIC_d872e681365a04f7
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for UPVC window and door systems installations company

-- Create database
CREATE DATABASE upvc_installations;

-- Use database
USE upvc_installations;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    ProjectStatus VARCHAR(50) NOT NULL DEFAULT 'In Progress',
    InstallationDate DATE,
    CompletionDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    ProductType VARCHAR(100) NOT NULL CHECK (ProductType IN ('Window', 'Door', 'Frame', 'Accessory')),
    Material VARCHAR(100) NOT NULL CHECK (Material IN ('UPVC', 'Aluminum', 'Wood')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for project products
CREATE TABLE ProjectProducts (
    ProjectID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProjectID, ProductID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create table for testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectID INT,
    Testimonial TEXT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TestimonialID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE SET NULL
);

-- Create indexes for foreign keys
CREATE INDEX idx_Projects_ClientID ON Projects (ClientID);
CREATE INDEX idx_ProjectProducts_ProjectID ON ProjectProducts (ProjectID);
CREATE INDEX idx_ProjectProducts_ProductID ON ProjectProducts (ProductID);
CREATE INDEX idx_Testimonials_ClientID ON Testimonials (ClientID);
CREATE INDEX idx_Testimonials_ProjectID ON Testimonials (ProjectID);
```
