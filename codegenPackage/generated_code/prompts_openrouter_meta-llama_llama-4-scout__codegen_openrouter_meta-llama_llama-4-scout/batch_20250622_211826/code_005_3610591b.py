"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: "Create a SQL query to extract data on Omega Energy's contracts of exploration and production, including details on Bloque Buenavista, Campo Corrales, and Campo Bolívar."
Generated: DETERMINISTIC_3610591b58e6c31c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to extract data on Omega Energy's contracts of exploration and production

-- Define the database and tables
USE omega_energy_db;

-- Create a temporary table to store the contract details
CREATE TEMPORARY TABLE contract_details (
  contract_id INT,
  contract_name VARCHAR(255),
  contract_type VARCHAR(100),
  bloque VARCHAR(100),
  campo VARCHAR(100),
  exploration_date DATE,
  production_date DATE,
  expiration_date DATE
);

-- Insert data into the temporary table
INSERT INTO contract_details
SELECT 
  c.contract_id,
  c.contract_name,
  c.contract_type,
  c.bloque,
  c.campo,
  c.exploration_date,
  c.production_date,
  c.expiration_date
FROM 
  contracts c
WHERE 
  c.contract_type IN ('exploration', 'production')
  AND c.bloque IN ('Buenavista')
  AND c.campo IN ('Corrales', 'Bolívar');

-- Query to extract data on Omega Energy's contracts
SELECT 
  cd.contract_id,
  cd.contract_name,
  cd.contract_type,
  cd.bloque,
  cd.campo,
  cd.exploration_date,
  cd.production_date,
  cd.expiration_date
FROM 
  contract_details cd
ORDER BY 
  cd.contract_id;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS contract_details;
```

However, I realized I made an incorrect assumption on some details. A more accurate SQL query would likely involve joins with multiple tables. Here is a more complex query.

```sql
-- Query to extract data on Omega Energy's contracts of exploration and production

-- Define the database and tables
USE omega_energy_db;

-- Query to extract data on Omega Energy's contracts
SELECT 
  c.contract_id,
  c.contract_name,
  ct.contract_type_name,
  b.bloque_name,
  cp.campo_name,
  c.exploration_date,
  c.production_date,
  c.expiration_date
FROM 
  contracts c
  INNER JOIN contract_types ct ON c.contract_type_id = ct.contract_type_id
  INNER JOIN bloques b ON c.bloque_id = b.bloque_id
  INNER JOIN campos cp ON c.campo_id = cp.campo_id
WHERE 
  ct.contract_type_name IN ('exploration', 'production')
  AND b.bloque_name = 'Buenavista'
  AND cp.campo_name IN ('Corrales', 'Bolívar')
ORDER BY 
  c.contract_id;
```
