"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Write a SQL query to analyze customer satisfaction ratings for a plumbing and fire fighting services company, based on data from ERA ENGINEERING's client feedback."
Generated: DETERMINISTIC_5893663a084cc8f9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze customer satisfaction ratings for ERA ENGINEERING's plumbing and fire fighting services

-- This query retrieves the average satisfaction rating, total feedback count, and the breakdown of ratings
-- for each service type offered by the company.

SELECT 
    service_type,                          -- The type of service (e.g., plumbing, fire fighting)
    COUNT(feedback_id) AS total_feedback, -- Total number of feedback entries for each service
    AVG(satisfaction_rating) AS avg_rating, -- Average satisfaction rating for each service
    SUM(CASE WHEN satisfaction_rating >= 4 THEN 1 ELSE 0 END) AS positive_feedback, -- Count of positive ratings (4 and above)
    SUM(CASE WHEN satisfaction_rating < 4 THEN 1 ELSE 0 END) AS negative_feedback  -- Count of negative ratings (below 4)
FROM 
    client_feedback                        -- The table containing client feedback data
WHERE 
    feedback_date >= DATEADD(YEAR, -1, GETDATE()) -- Filter for feedback from the last year
GROUP BY 
    service_type                           -- Group results by service type
ORDER BY 
    avg_rating DESC;                      -- Order results by average rating in descending order

-- Note: Ensure that the 'client_feedback' table has the following relevant columns:
-- - feedback_id: Unique identifier for each feedback entry
-- - service_type: Type of service provided (e.g., 'plumbing', 'fire fighting')
-- - satisfaction_rating: Rating given by the customer (assumed to be on a scale of 1 to 5)
-- - feedback_date: Date when the feedback was submitted
```
