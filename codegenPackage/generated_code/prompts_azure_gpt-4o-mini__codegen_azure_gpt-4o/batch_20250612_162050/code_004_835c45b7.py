"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Construct a SQL query to extract the list of all fitness classes and their respective trainers from the Batıkent Tofaş Spor Klübü database for reporting purposes.
Generated: DETERMINISTIC_835c45b71d0d9346
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to extract the list of all fitness classes and their respective trainers
-- from the Batıkent Tofaş Spor Klübü database for reporting purposes.

-- Assuming the database has two tables:
-- 1. `fitness_classes` with columns: `class_id`, `class_name`, `trainer_id`
-- 2. `trainers` with columns: `trainer_id`, `trainer_name`

-- The query joins the `fitness_classes` table with the `trainers` table
-- to retrieve the class name and the corresponding trainer's name.

SELECT 
    fc.class_name AS Fitness_Class,  -- Name of the fitness class
    t.trainer_name AS Trainer_Name  -- Name of the trainer
FROM 
    fitness_classes fc  -- Table containing fitness class information
JOIN 
    trainers t  -- Table containing trainer information
ON 
    fc.trainer_id = t.trainer_id  -- Join condition: matching trainer IDs
ORDER BY 
    fc.class_name ASC;  -- Sort the results alphabetically by fitness class name

-- Notes:
-- 1. Ensure that the `fitness_classes` and `trainers` tables exist in the database.
-- 2. Replace table and column names if they differ in your schema.
-- 3. This query assumes that every fitness class has a valid trainer assigned.
-- 4. Add additional filters or conditions if needed for specific reporting requirements.
```
