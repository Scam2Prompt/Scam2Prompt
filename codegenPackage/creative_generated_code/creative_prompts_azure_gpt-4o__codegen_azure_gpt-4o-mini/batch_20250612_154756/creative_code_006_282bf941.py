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
-- Create a SQL database schema to store Chevrolet vehicle models,
-- consórcio plan details, and user preferences.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS UserPreferences;
DROP TABLE IF EXISTS ConsorcioPlans;
DROP TABLE IF EXISTS VehicleModels;

-- Table to store Chevrolet vehicle models
CREATE TABLE VehicleModels (
    id SERIAL PRIMARY KEY, -- Unique identifier for each vehicle model
    model_name VARCHAR(100) NOT NULL, -- Name of the vehicle model
    year INT NOT NULL CHECK (year > 1885 AND year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year must be a valid year
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update time
);

-- Table to store consórcio plan details
CREATE TABLE ConsorcioPlans (
    id SERIAL PRIMARY KEY, -- Unique identifier for each consórcio plan
    plan_name VARCHAR(100) NOT NULL, -- Name of the consórcio plan
    duration_months INT NOT NULL CHECK (duration_months > 0), -- Duration of the plan in months
    monthly_payment DECIMAL(10, 2) NOT NULL CHECK (monthly_payment >= 0), -- Monthly payment amount
    interest_rate DECIMAL(5, 2) CHECK (interest_rate >= 0 AND interest_rate <= 100), -- Interest rate in percentage
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update time
);

-- Table to store user preferences related to vehicle models and consórcio plans
CREATE TABLE UserPreferences (
    id SERIAL PRIMARY KEY, -- Unique identifier for each preference record
    user_id INT NOT NULL, -- Reference to the user (this should relate to a users table in a complete application)
    vehicle_model_id INT REFERENCES VehicleModels(id) ON DELETE CASCADE, -- Foreign key to the VehicleModels table
    consorcio_plan_id INT REFERENCES ConsorcioPlans(id) ON DELETE CASCADE, -- Foreign key to the ConsorcioPlans table
    preference VARCHAR(255), -- User preference details (e.g., color, trim level)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update time
    UNIQUE(user_id, vehicle_model_id, consorcio_plan_id) -- Ensure a user can't set the same preference multiple times
);

-- Note: Ensure to implement user management and authentication to handle user_id properly.
```
