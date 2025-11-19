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
-- SQL Query to analyze data from electrical audits in industrial plants
-- This query identifies areas of energy inefficiency and recommends improvements.

-- Assumptions:
-- 1. The table `electrical_audits` contains data from audits with the following columns:
--    - `plant_id`: Unique identifier for the industrial plant
--    - `audit_date`: Date of the audit
--    - `energy_consumption`: Total energy consumption (kWh)
--    - `energy_efficiency`: Efficiency rating (percentage)
--    - `recommended_action`: Suggested improvement action
-- 2. The table `plants` contains plant details with the following columns:
--    - `plant_id`: Unique identifier for the industrial plant
--    - `plant_name`: Name of the plant
--    - `location`: Location of the plant

-- Query starts here
WITH InefficientPlants AS (
    -- Identify plants with energy efficiency below 80%
    SELECT
        ea.plant_id,
        p.plant_name,
        p.location,
        ea.audit_date,
        ea.energy_consumption,
        ea.energy_efficiency,
        ea.recommended_action
    FROM
        electrical_audits ea
    INNER JOIN
        plants p ON ea.plant_id = p.plant_id
    WHERE
        ea.energy_efficiency < 80 -- Threshold for inefficiency
),
RecommendationsSummary AS (
    -- Summarize recommended actions for inefficient plants
    SELECT
        plant_id,
        COUNT(recommended_action) AS total_recommendations,
        STRING_AGG(recommended_action, '; ') AS all_recommendations -- Combine all recommendations into a single string
    FROM
        InefficientPlants
    GROUP BY
        plant_id
)
-- Final output: Combine inefficient plant details with summarized recommendations
SELECT
    ip.plant_id,
    ip.plant_name,
    ip.location,
    ip.audit_date,
    ip.energy_consumption,
    ip.energy_efficiency,
    rs.total_recommendations,
    rs.all_recommendations
FROM
    InefficientPlants ip
LEFT JOIN
    RecommendationsSummary rs ON ip.plant_id = rs.plant_id
ORDER BY
    ip.energy_efficiency ASC; -- Sort by efficiency to prioritize the least efficient plants
```
