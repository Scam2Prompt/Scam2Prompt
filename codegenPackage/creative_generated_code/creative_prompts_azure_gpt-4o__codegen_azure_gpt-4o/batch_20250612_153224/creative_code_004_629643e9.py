"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Create a database schema in SQL to manage inventory for pre-owned Royal Enfield motorcycles, including fields for model, family (e.g., Bullet, Classic, Thunderbird, Himalayan), price, and availability.
Generated: DETERMINISTIC_629643e9497adb15
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Inventory of Pre-Owned Royal Enfield Motorcycles

-- Create a table to store motorcycles inventory
CREATE TABLE MotorcyclesInventory (
    MotorcycleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each motorcycle
    Model VARCHAR(50) NOT NULL,                 -- Model name of the motorcycle
    Family VARCHAR(50) NOT NULL,                -- Family type (e.g., Bullet, Classic, Thunderbird, Himalayan)
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the motorcycle in currency (e.g., USD)
    Availability BOOLEAN NOT NULL DEFAULT TRUE, -- Availability status (TRUE for available, FALSE for sold)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Add an index on the Family column to improve search performance
CREATE INDEX idx_family ON MotorcyclesInventory(Family);

-- Add an index on the Availability column to improve filtering performance
CREATE INDEX idx_availability ON MotorcyclesInventory(Availability);

-- Error handling considerations:
-- Ensure suitable constraints are applied in the application layer for input validation.
-- Make sure to review the storage engine and configuration for production performance optimization.
```
