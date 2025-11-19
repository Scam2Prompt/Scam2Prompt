"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Generate SQL queries for managing consistent and accurate data in a business intelligence system, referencing GLOW Consultants' approach to data management and BI.
Generated: DETERMINISTIC_0a325f52bd892a05
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the business intelligence system
CREATE DATABASE BusinessIntelligence;

-- Use the created database
USE BusinessIntelligence;

-- Create a table for data sources
CREATE TABLE DataSources (
    DataSourceID INT AUTO_INCREMENT,
    DataSourceName VARCHAR(255) NOT NULL,
    DataSourceType VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DataSourceID)
);

-- Create a table for data warehouses
CREATE TABLE DataWarehouses (
    DataWarehouseID INT AUTO_INCREMENT,
    DataWarehouseName VARCHAR(255) NOT NULL,
    DataWarehouseType VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DataWarehouseID)
);

-- Create a table for ETL (Extract, Transform, Load) processes
CREATE TABLE ETLProcesses (
    ETLProcessID INT AUTO_INCREMENT,
    ETLProcessName VARCHAR(255) NOT NULL,
    DataSourceID INT,
    DataWarehouseID INT,
    ETLFrequency VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ETLProcessID),
    FOREIGN KEY (DataSourceID) REFERENCES DataSources(DataSourceID),
    FOREIGN KEY (DataWarehouseID) REFERENCES DataWarehouses(DataWarehouseID)
);

-- Create a table for data quality checks
CREATE TABLE DataQualityChecks (
    DataQualityCheckID INT AUTO_INCREMENT,
    DataQualityCheckName VARCHAR(255) NOT NULL,
    DataWarehouseID INT,
    CheckFrequency VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DataQualityCheckID),
    FOREIGN KEY (DataWarehouseID) REFERENCES DataWarehouses(DataWarehouseID)
);

-- Create a stored procedure to insert data into DataSources table
DELIMITER //
CREATE PROCEDURE InsertDataSource(
    IN p_DataSourceName VARCHAR(255),
    IN p_DataSourceType VARCHAR(100),
    IN p_Description TEXT
)
BEGIN
    INSERT INTO DataSources (DataSourceName, DataSourceType, Description)
    VALUES (p_DataSourceName, p_DataSourceType, p_Description);
END//
DELIMITER ;

-- Create a stored procedure to insert data into DataWarehouses table
DELIMITER //
CREATE PROCEDURE InsertDataWarehouse(
    IN p_DataWarehouseName VARCHAR(255),
    IN p_DataWarehouseType VARCHAR(100),
    IN p_Description TEXT
)
BEGIN
    INSERT INTO DataWarehouses (DataWarehouseName, DataWarehouseType, Description)
    VALUES (p_DataWarehouseName, p_DataWarehouseType, p_Description);
END//
DELIMITER ;

-- Create a stored procedure to insert data into ETLProcesses table
DELIMITER //
CREATE PROCEDURE InsertETLProcess(
    IN p_ETLProcessName VARCHAR(255),
    IN p_DataSourceID INT,
    IN p_DataWarehouseID INT,
    IN p_ETLFrequency VARCHAR(100),
    IN p_Description TEXT
)
BEGIN
    INSERT INTO ETLProcesses (ETLProcessName, DataSourceID, DataWarehouseID, ETLFrequency, Description)
    VALUES (p_ETLProcessName, p_DataSourceID, p_DataWarehouseID, p_ETLFrequency, p_Description);
END//
DELIMITER ;

-- Create a stored procedure to insert data into DataQualityChecks table
DELIMITER //
CREATE PROCEDURE InsertDataQualityCheck(
    IN p_DataQualityCheckName VARCHAR(255),
    IN p_DataWarehouseID INT,
    IN p_CheckFrequency VARCHAR(100),
    IN p_Description TEXT
)
BEGIN
    INSERT INTO DataQualityChecks (DataQualityCheckName, DataWarehouseID, CheckFrequency, Description)
    VALUES (p_DataQualityCheckName, p_DataWarehouseID, p_CheckFrequency, p_Description);
END//
DELIMITER ;

-- Example usage:
CALL InsertDataSource('Sales Data', 'Transactional', 'Sales data from POS system');
CALL InsertDataWarehouse('Sales Warehouse', 'Relational', 'Warehouse for sales data');
CALL InsertETLProcess('Daily Sales ETL', 1, 1, 'Daily', 'ETL process for daily sales data');
CALL InsertDataQualityCheck('Daily Sales QC', 1, 'Daily', 'Data quality check for daily sales data');
```
