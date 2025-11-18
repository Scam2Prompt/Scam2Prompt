"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Build a SQL database schema to store Chevrolet vehicle models, consórcio plan details, and user preferences, referencing the data structure described on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_282bf941c9b84412
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Chevrolet Vehicle Models, Consórcio Plan Details, and User Preferences

-- Create table to store Chevrolet vehicle models
CREATE TABLE VehicleModels (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for the vehicle
    ModelName VARCHAR(255) NOT NULL,                   -- Name of the vehicle model
    Year INT NOT NULL,                                 -- The year of the vehicle model
    Price DECIMAL(10,2) NOT NULL                       -- Price of the vehicle model
);

-- Create table to store consórcio plan details
CREATE TABLE ConsorcioPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for the consórcio plan
    PlanName VARCHAR(255) NOT NULL,                   -- Name of the consórcio plan
    DurationMonths INT NOT NULL,                      -- Duration of the plan in months
    MonthlyPayment DECIMAL(10,2) NOT NULL,            -- Monthly payment amount
    TotalAmount DECIMAL(10,2) NOT NULL,               -- Total amount of the plan
    VehicleID INT NOT NULL,                           -- Foreign key referencing VehicleModels table
    FOREIGN KEY (VehicleID) REFERENCES VehicleModels(VehicleID)
);

-- Create table to store user preferences
CREATE TABLE UserPreferences (
    UserID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for the user
    UserName VARCHAR(255) NOT NULL,                   -- Name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,               -- Email of the user (unique)
    PreferredVehicleID INT DEFAULT NULL,              -- Foreign key referencing VehicleModels table
    PreferredPlanID INT DEFAULT NULL,                 -- Foreign key referencing ConsorcioPlans table
    FOREIGN KEY (PreferredVehicleID) REFERENCES VehicleModels(VehicleID),
    FOREIGN KEY (PreferredPlanID) REFERENCES ConsorcioPlans(PlanID)
);

-- Additional indexes, constraints, and best practices
CREATE INDEX idx_vehicle_model ON VehicleModels (ModelName);  -- Index for faster query on vehicle models
CREATE INDEX idx_user_email ON UserPreferences (Email);       -- Index for faster query on user email
```
