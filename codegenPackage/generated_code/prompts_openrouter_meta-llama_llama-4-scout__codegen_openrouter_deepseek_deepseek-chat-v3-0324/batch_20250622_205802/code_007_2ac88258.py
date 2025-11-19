"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Generate a SQL query to retrieve customer information and service history for a plumbing company, based on the data stored on a website like Deep Book Online.
Generated: DETERMINISTIC_2ac88258c274a6c2
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve customer information and service history for a plumbing company
-- Assumes the following tables exist in the database:
--   - customers: Contains customer information
--   - service_history: Contains service records linked to customers
--   - service_types: Contains types of services offered
--   - technicians: Contains technician information

SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    c.phone,
    c.address,
    c.city,
    c.state,
    c.zip_code,
    sh.service_id,
    st.service_name,
    sh.service_date,
    sh.description AS service_description,
    sh.cost,
    t.technician_id,
    t.first_name AS tech_first_name,
    t.last_name AS tech_last_name,
    sh.completed,
    sh.payment_status
FROM 
    customers c
LEFT JOIN 
    service_history sh ON c.customer_id = sh.customer_id
LEFT JOIN 
    service_types st ON sh.service_type_id = st.service_type_id
LEFT JOIN 
    technicians t ON sh.technician_id = t.technician_id
WHERE 
    c.customer_id = :customer_id_param  -- Parameter for specific customer
    OR (:customer_id_param IS NULL AND c.active = TRUE)  -- All active customers if no param
ORDER BY 
    c.last_name ASC,
    c.first_name ASC,
    sh.service_date DESC;
```
