"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Write a SQL query to extract data on MG car models with specific engine features, such as turbocharged or electric engines, and calculate their average fuel efficiency.
Generated: DETERMINISTIC_c998f67d8d673030
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to extract data on MG car models with specific engine features and calculate their average fuel efficiency

-- Define a query to extract relevant data
SELECT 
    cm.model_name,
    cm.engine_type,
    cm.fuel_efficiency,
    et.engine_feature
FROM 
    mg_car_models cm
INNER JOIN 
    engine_types et ON cm.engine_type_id = et.engine_type_id
WHERE 
    et.engine_feature IN ('Turbocharged', 'Electric');

-- Create a view to calculate average fuel efficiency for each engine feature
CREATE VIEW avg_fuel_efficiency AS
SELECT 
    et.engine_feature,
    AVG(cm.fuel_efficiency) AS avg_fuel_efficiency
FROM 
    mg_car_models cm
INNER JOIN 
    engine_types et ON cm.engine_type_id = et.engine_type_id
GROUP BY 
    et.engine_feature;

-- Query to retrieve the average fuel efficiency for each engine feature
SELECT 
    engine_feature,
    avg_fuel_efficiency
FROM 
    avg_fuel_efficiency
ORDER BY 
    avg_fuel_efficiency DESC;

-- Stored procedure to encapsulate the queries
DELIMITER //
CREATE PROCEDURE get_mg_car_models_with_avg_fuel_efficiency()
BEGIN
    -- Check if the required tables exist
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'mg_car_models') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'mg_car_models table does not exist';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'engine_types') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'engine_types table does not exist';
    END IF;

    -- Execute the queries
    SELECT 
        cm.model_name,
        cm.engine_type,
        cm.fuel_efficiency,
        et.engine_feature
    FROM 
        mg_car_models cm
    INNER JOIN 
        engine_types et ON cm.engine_type_id = et.engine_type_id
    WHERE 
        et.engine_feature IN ('Turbocharged', 'Electric');

    SELECT 
        engine_feature,
        avg_fuel_efficiency
    FROM 
        avg_fuel_efficiency
    ORDER BY 
        avg_fuel_efficiency DESC;
END//
DELIMITER ;

-- Call the stored procedure
CALL get_mg_car_models_with_avg_fuel_efficiency();
```

```sql
-- Sample table schema for demonstration purposes
CREATE TABLE mg_car_models (
    model_id INT AUTO_INCREMENT,
    model_name VARCHAR(255) NOT NULL,
    engine_type_id INT NOT NULL,
    fuel_efficiency DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (model_id)
);

CREATE TABLE engine_types (
    engine_type_id INT AUTO_INCREMENT,
    engine_type VARCHAR(255) NOT NULL,
    engine_feature VARCHAR(255) NOT NULL,
    PRIMARY KEY (engine_type_id)
);

-- Sample data for demonstration purposes
INSERT INTO engine_types (engine_type_id, engine_type, engine_feature)
VALUES 
(1, '2.0L Turbocharged', 'Turbocharged'),
(2, '1.5L Electric', 'Electric'),
(3, '1.0L Naturally Aspirated', 'Naturally Aspirated');

INSERT INTO mg_car_models (model_id, model_name, engine_type_id, fuel_efficiency)
VALUES 
(1, 'MG ZS Turbo', 1, 25.5),
(2, 'MG e-ZS', 2, 120.0),
(3, 'MG 3', 3, 30.2),
(4, 'MG HS Turbo', 1, 24.8),
(5, 'MG e-HS', 2, 110.0);
```
