"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Build a SQL database schema to store Chevrolet vehicle models, consórcio plan details, and user preferences, referencing the data structure described on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_282bf941c9b84412
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Chevrolet Vehicle Models, Consórcio Plan Details, and User Preferences

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS UserPreferences;
DROP TABLE IF EXISTS ConsorcioPlans;
DROP TABLE IF EXISTS VehicleModels;

-- Table to store Chevrolet vehicle models
CREATE TABLE VehicleModels (
    id SERIAL PRIMARY KEY, -- Unique identifier for each vehicle model
    model_name VARCHAR(100) NOT NULL, -- Name of the vehicle model
    year INT NOT NULL CHECK (year > 1885), -- Year of manufacture, must be greater than 1885
    price DECIMAL(10, 2) NOT NULL, -- Price of the vehicle model
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store Consórcio plan details
CREATE TABLE ConsorcioPlans (
    id SERIAL PRIMARY KEY, -- Unique identifier for each consórcio plan
    plan_name VARCHAR(100) NOT NULL, -- Name of the consórcio plan
    duration_months INT NOT NULL CHECK (duration_months > 0), -- Duration of the plan in months
    monthly_payment DECIMAL(10, 2) NOT NULL, -- Monthly payment amount
    vehicle_model_id INT NOT NULL, -- Foreign key referencing VehicleModels
    FOREIGN KEY (vehicle_model_id) REFERENCES VehicleModels(id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store user preferences
CREATE TABLE UserPreferences (
    id SERIAL PRIMARY KEY, -- Unique identifier for each user preference
    user_id INT NOT NULL, -- Identifier for the user (could reference a Users table if it exists)
    vehicle_model_id INT NOT NULL, -- Foreign key referencing VehicleModels
    consorcio_plan_id INT NOT NULL, -- Foreign key referencing ConsorcioPlans
    preference_notes TEXT, -- Additional notes or preferences from the user
    FOREIGN KEY (vehicle_model_id) REFERENCES VehicleModels(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (consorcio_plan_id) REFERENCES ConsorcioPlans(id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for performance optimization
CREATE INDEX idx_vehicle_model_name ON VehicleModels(model_name);
CREATE INDEX idx_plan_name ON ConsorcioPlans(plan_name);
CREATE INDEX idx_user_preferences ON UserPreferences(user_id);
```
