"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Develop a database schema for managing customer satisfaction metrics, rental plans, and delivery statistics for a refrigerated transport company, based on the features of RefrigeratorTransport.com.
Generated: DETERMINISTIC_884eeddcbde571ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for refrigerated transport company

CREATE DATABASE RefrigeratedTransport;

USE RefrigeratedTransport;

-- Table for customers
CREATE TABLE Customers (
  CustomerID INT AUTO_INCREMENT,
  CompanyName VARCHAR(255) NOT NULL,
  ContactName VARCHAR(255) NOT NULL,
  ContactTitle VARCHAR(255),
  Address VARCHAR(255),
  City VARCHAR(100),
  Region VARCHAR(100),
  PostalCode VARCHAR(20),
  Country VARCHAR(100),
  Phone VARCHAR(20),
  Email VARCHAR(100) UNIQUE,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (CustomerID)
);

-- Table for customer satisfaction metrics
CREATE TABLE CustomerSatisfaction (
  SatisfactionID INT AUTO_INCREMENT,
  CustomerID INT NOT NULL,
  Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
  Review TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (SatisfactionID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table for rental plans
CREATE TABLE RentalPlans (
  PlanID INT AUTO_INCREMENT,
  PlanName VARCHAR(255) NOT NULL,
  Description TEXT,
  DailyRate DECIMAL(10, 2) NOT NULL,
  WeeklyRate DECIMAL(10, 2) NOT NULL,
  MonthlyRate DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PlanID)
);

-- Table for rentals
CREATE TABLE Rentals (
  RentalID INT AUTO_INCREMENT,
  CustomerID INT NOT NULL,
  PlanID INT NOT NULL,
  RentalDate DATE NOT NULL,
  ReturnDate DATE,
  TotalCost DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (RentalID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
  FOREIGN KEY (PlanID) REFERENCES RentalPlans(PlanID) ON DELETE RESTRICT
);

-- Table for deliveries
CREATE TABLE Deliveries (
  DeliveryID INT AUTO_INCREMENT,
  RentalID INT NOT NULL,
  DeliveryDate DATE NOT NULL,
  DeliveryStatus ENUM('ON_TIME', 'LATE', 'FAILED') NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (DeliveryID),
  FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE CASCADE
);

-- Table for refrigerated transport statistics
CREATE TABLE TransportStatistics (
  StatisticID INT AUTO_INCREMENT,
  RentalID INT NOT NULL,
  TemperatureLog JSON,
  FuelConsumption DECIMAL(10, 2),
  DistanceTraveled DECIMAL(10, 2),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (StatisticID),
  FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_Customers_CompanyName ON Customers (CompanyName);
CREATE INDEX idx_Rentals_CustomerID ON Rentals (CustomerID);
CREATE INDEX idx_Deliveries_DeliveryDate ON Deliveries (DeliveryDate);
CREATE INDEX idx_TransportStatistics_RentalID ON TransportStatistics (RentalID);
```

```sql
-- Example stored procedure to insert a new customer satisfaction metric
DELIMITER //
CREATE PROCEDURE InsertCustomerSatisfaction(
  IN p_CustomerID INT,
  IN p_Rating TINYINT,
  IN p_Review TEXT
)
BEGIN
  INSERT INTO CustomerSatisfaction (CustomerID, Rating, Review)
  VALUES (p_CustomerID, p_Rating, p_Review);
END//
DELIMITER ;

-- Example stored procedure to get all customer satisfaction metrics for a customer
DELIMITER //
CREATE PROCEDURE GetCustomerSatisfactionMetrics(
  IN p_CustomerID INT
)
BEGIN
  SELECT * FROM CustomerSatisfaction
  WHERE CustomerID = p_CustomerID;
END//
DELIMITER ;
```
