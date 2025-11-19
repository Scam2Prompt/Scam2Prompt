"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Write a SQL query to analyze data from electrical audits in industrial plants, identifying areas of energy inefficiency and recommending improvements, as per Marod Consultores' services for energy sector clients."
Generated: DETERMINISTIC_95002ab9a717b903
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to Analyze Energy Inefficiency in Industrial Plants

-- This query identifies areas of energy inefficiency based on electrical audit data
-- It calculates the average energy consumption per machine and compares it to the industry standard
-- Recommendations for improvements are provided based on the analysis

WITH EnergyConsumption AS (
    SELECT 
        plant_id,
        machine_id,
        SUM(energy_consumed) AS total_energy,
        COUNT(*) AS audit_count,
        AVG(energy_consumed) AS avg_energy_per_audit
    FROM 
        electrical_audits
    GROUP BY 
        plant_id, machine_id
),

IndustryStandards AS (
    SELECT 
        machine_type,
        AVG(standard_energy_consumption) AS avg_standard_energy
    FROM 
        industry_standards
    GROUP BY 
        machine_type
)

SELECT 
    ec.plant_id,
    ec.machine_id,
    ec.avg_energy_per_audit,
    is.avg_standard_energy,
    CASE 
        WHEN ec.avg_energy_per_audit > is.avg_standard_energy THEN 'Inefficient'
        ELSE 'Efficient'
    END AS efficiency_status,
    CASE 
        WHEN ec.avg_energy_per_audit > is.avg_standard_energy THEN 
            'Consider upgrading machinery or optimizing operational procedures.'
        ELSE 
            'No immediate action required.'
    END AS recommendations
FROM 
    EnergyConsumption ec
JOIN 
    machines m ON ec.machine_id = m.id
JOIN 
    IndustryStandards is ON m.machine_type = is.machine_type
ORDER BY 
    ec.plant_id, ec.machine_id;

-- Note: Ensure that the tables 'electrical_audits', 'industry_standards', and 'machines' exist
-- and contain the necessary data for this query to execute successfully.
```
