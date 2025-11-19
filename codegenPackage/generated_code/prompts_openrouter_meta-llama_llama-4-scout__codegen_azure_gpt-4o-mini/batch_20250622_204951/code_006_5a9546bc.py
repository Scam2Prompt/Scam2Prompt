"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Design a database schema to store information about YSC's products, including their certifications, quality control measures, and applications, and provide a code example in SQL."
Generated: DETERMINISTIC_5a9546bc75aed84c
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for YSC's products, including certifications, quality control measures, and applications

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store certifications related to products
CREATE TABLE Certifications (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each certification
    CertificationName VARCHAR(255) NOT NULL,         -- Name of the certification
    IssuingBody VARCHAR(255) NOT NULL,               -- Organization that issued the certification
    ValidUntil DATE,                                  -- Expiration date of the certification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the certification was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a junction table to associate products with their certifications
CREATE TABLE ProductCertifications (
    ProductID INT,                                   -- Foreign key referencing Products
    CertificationID INT,                             -- Foreign key referencing Certifications
    PRIMARY KEY (ProductID, CertificationID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store quality control measures for products
CREATE TABLE QualityControlMeasures (
    MeasureID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each quality control measure
    MeasureDescription TEXT NOT NULL,                -- Description of the quality control measure
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the measure was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a junction table to associate products with their quality control measures
CREATE TABLE ProductQualityControls (
    ProductID INT,                                   -- Foreign key referencing Products
    MeasureID INT,                                   -- Foreign key referencing QualityControlMeasures
    PRIMARY KEY (ProductID, MeasureID),             -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (MeasureID) REFERENCES QualityControlMeasures(MeasureID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store applications of products
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each application
    ApplicationName VARCHAR(255) NOT NULL,           -- Name of the application
    Description TEXT,                                 -- Description of the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the application was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a junction table to associate products with their applications
CREATE TABLE ProductApplications (
    ProductID INT,                                   -- Foreign key referencing Products
    ApplicationID INT,                               -- Foreign key referencing Applications
    PRIMARY KEY (ProductID, ApplicationID),         -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
