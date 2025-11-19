"""
Generated Code Metadata:
========================
Original URL: https://www.khadamy.com
Prompt: Write SQL queries to store and retrieve service data for "تركيب زجاج سيكوريت" and "تلميع سيارات متنقل" by city, based on the services listed on https://www.khadamy.com.
Generated: DETERMINISTIC_bfd3187ba80e5813
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for service data
CREATE DATABASE ServiceDB;

-- Use the ServiceDB database
USE ServiceDB;

-- Create a table for cities
CREATE TABLE Cities (
    CityID INT AUTO_INCREMENT,
    CityName VARCHAR(255) NOT NULL,
    PRIMARY KEY (CityID)
);

-- Create a table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create a table for service providers
CREATE TABLE ServiceProviders (
    ProviderID INT AUTO_INCREMENT,
    ProviderName VARCHAR(255) NOT NULL,
    CityID INT,
    ServiceID INT,
    PRIMARY KEY (ProviderID),
    FOREIGN KEY (CityID) REFERENCES Cities(CityID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Insert services
INSERT INTO Services (ServiceName)
VALUES 
('تركيب زجاج سيكوريت'),
('تلميع سيارات متنقل');

-- Insert cities
INSERT INTO Cities (CityName)
VALUES 
('الرياض'),
('جدة'),
('الدمام'),
('المدينة المنورة'),
('الخبر');

-- Insert service providers
INSERT INTO ServiceProviders (ProviderName, CityID, ServiceID)
VALUES 
('شركة تركيب زجاج سيكوريت في الرياض', 1, 1),
('شركة تلميع سيارات متنقل في جدة', 2, 2),
('شركة تركيب زجاج سيكوريت في الدمام', 3, 1),
('شركة تلميع سيارات متنقل في المدينة المنورة', 4, 2),
('شركة تركيب زجاج سيكوريت في الخبر', 5, 1);

-- Retrieve service data by city
DELIMITER //
CREATE PROCEDURE GetServiceDataByCity(IN cityName VARCHAR(255))
BEGIN
    SELECT 
        c.CityName,
        s.ServiceName,
        sp.ProviderName
    FROM 
        Cities c
    INNER JOIN 
        ServiceProviders sp ON c.CityID = sp.CityID
    INNER JOIN 
        Services s ON sp.ServiceID = s.ServiceID
    WHERE 
        c.CityName = cityName;
END//
DELIMITER ;

-- Retrieve service data by service name
DELIMITER //
CREATE PROCEDURE GetServiceDataByServiceName(IN serviceName VARCHAR(255))
BEGIN
    SELECT 
        c.CityName,
        s.ServiceName,
        sp.ProviderName
    FROM 
        Cities c
    INNER JOIN 
        ServiceProviders sp ON c.CityID = sp.CityID
    INNER JOIN 
        Services s ON sp.ServiceID = s.ServiceID
    WHERE 
        s.ServiceName = serviceName;
END//
DELIMITER ;

-- Call stored procedures
CALL GetServiceDataByCity('الرياض');
CALL GetServiceDataByServiceName('تركيب زجاج سيكوريت');
```
