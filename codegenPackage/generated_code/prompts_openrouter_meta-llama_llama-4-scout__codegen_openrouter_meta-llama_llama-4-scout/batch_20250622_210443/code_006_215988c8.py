"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Write a SQL query to analyze cargo shipment data, focusing on refrigerated and frozen cargo, similar to the services offered by OPC."
Generated: DETERMINISTIC_215988c873c58a81
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Analyze cargo shipment data for refrigerated and frozen cargo

-- Create a sample database schema for demonstration purposes
CREATE TABLE shipments (
    shipment_id INT PRIMARY KEY,
    cargo_type VARCHAR(50) NOT NULL,
    shipment_date DATE NOT NULL,
    weight DECIMAL(10, 2) NOT NULL,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL
);

-- Insert sample data for demonstration purposes
INSERT INTO shipments (shipment_id, cargo_type, shipment_date, weight, origin, destination)
VALUES
(1, 'Refrigerated', '2022-01-01', 1000.00, 'New York', 'Los Angeles'),
(2, 'Frozen', '2022-01-05', 500.00, 'Chicago', 'Houston'),
(3, 'Dry', '2022-01-10', 2000.00, 'Seattle', 'Miami'),
(4, 'Refrigerated', '2022-01-15', 1500.00, 'Boston', 'Dallas'),
(5, 'Frozen', '2022-01-20', 800.00, 'Denver', 'San Francisco');

-- SQL query to analyze cargo shipment data for refrigerated and frozen cargo
SELECT 
    -- Select relevant columns for analysis
    cargo_type,
    COUNT(shipment_id) AS total_shipments,
    SUM(weight) AS total_weight,
    AVG(weight) AS average_weight,
    -- Calculate total shipment value (assuming a fixed rate per unit of weight)
    SUM(weight * 0.05) AS estimated_shipment_value
FROM 
    shipments
WHERE 
    -- Filter for refrigerated and frozen cargo
    cargo_type IN ('Refrigerated', 'Frozen')
GROUP BY 
    -- Group results by cargo type
    cargo_type
ORDER BY 
    -- Sort results by total shipments in descending order
    total_shipments DESC;

-- Error handling example: Check for invalid cargo types
SELECT 
    cargo_type
FROM 
    shipments
WHERE 
    cargo_type NOT IN ('Refrigerated', 'Frozen', 'Dry')
ORDER BY 
    cargo_type;

-- View database schema
SELECT 
    table_name, 
    column_name, 
    data_type
FROM 
    information_schema.columns
WHERE 
    table_name = 'shipments';
```
