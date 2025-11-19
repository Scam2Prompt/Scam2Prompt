"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Design a simple database schema to store information about electric vehicles, including their mileage on a single charge, traction battery capacity, and price, inspired by the car models listed on eControl SA's website."
Generated: DETERMINISTIC_90ab361378e6b8b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing electric vehicle information

-- Create a table to store electric vehicle details
CREATE TABLE ElectricVehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    ModelName VARCHAR(100) NOT NULL,          -- Name of the vehicle model
    Manufacturer VARCHAR(100) NOT NULL,       -- Name of the manufacturer
    MileagePerCharge FLOAT NOT NULL,          -- Mileage on a single charge (in kilometers)
    BatteryCapacity FLOAT NOT NULL,           -- Traction battery capacity (in kWh)
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the vehicle (in USD)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Add an index to optimize queries on Manufacturer
CREATE INDEX idx_manufacturer ON ElectricVehicles (Manufacturer);

-- Add an index to optimize queries on Price
CREATE INDEX idx_price ON ElectricVehicles (Price);

-- Example of inserting data into the table
-- INSERT INTO ElectricVehicles (ModelName, Manufacturer, MileagePerCharge, BatteryCapacity, Price)
-- VALUES ('Model S', 'Tesla', 652.0, 100.0, 79999.99);

-- Example of querying data
-- SELECT * FROM ElectricVehicles WHERE Manufacturer = 'Tesla';

-- Example of updating data
-- UPDATE ElectricVehicles SET Price = 75999.99 WHERE VehicleID = 1;

-- Example of deleting data
-- DELETE FROM ElectricVehicles WHERE VehicleID = 1;
```
