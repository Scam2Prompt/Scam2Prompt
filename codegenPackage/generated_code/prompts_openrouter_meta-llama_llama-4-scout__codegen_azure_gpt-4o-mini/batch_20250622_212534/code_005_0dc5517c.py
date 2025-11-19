"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Write a SQL query to analyze customer data and cleaning service usage for an industrial ultrasonic cleaning company, identifying trends and areas for improvement."
Generated: DETERMINISTIC_0dc5517c1ac1b4c4
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze customer data and cleaning service usage
-- for an industrial ultrasonic cleaning company

-- This query retrieves customer usage trends and identifies areas for improvement
-- by aggregating data on service usage, customer feedback, and service frequency.

WITH CustomerUsage AS (
    SELECT 
        c.customer_id,
        c.customer_name,
        COUNT(s.service_id) AS total_services_used,
        SUM(s.service_duration) AS total_service_duration,
        AVG(f.feedback_score) AS average_feedback_score
    FROM 
        customers c
    LEFT JOIN 
        services s ON c.customer_id = s.customer_id
    LEFT JOIN 
        feedback f ON s.service_id = f.service_id
    GROUP BY 
        c.customer_id, c.customer_name
),

UsageTrends AS (
    SELECT 
        customer_id,
        total_services_used,
        total_service_duration,
        average_feedback_score,
        CASE 
            WHEN total_services_used > 10 THEN 'High Usage'
            WHEN total_services_used BETWEEN 5 AND 10 THEN 'Moderate Usage'
            ELSE 'Low Usage'
        END AS usage_category
    FROM 
        CustomerUsage
)

-- Final selection of data to analyze trends and areas for improvement
SELECT 
    ut.customer_id,
    ut.total_services_used,
    ut.total_service_duration,
    ut.average_feedback_score,
    ut.usage_category,
    CASE 
        WHEN ut.average_feedback_score < 3 THEN 'Needs Improvement'
        WHEN ut.average_feedback_score BETWEEN 3 AND 4 THEN 'Satisfactory'
        ELSE 'Excellent'
    END AS feedback_category
FROM 
    UsageTrends ut
ORDER BY 
    ut.total_services_used DESC;

-- Note: Ensure that the tables 'customers', 'services', and 'feedback' exist
-- and contain the appropriate columns as referenced in the query.
-- Adjust the feedback score thresholds and usage categories as necessary based on business requirements.
```
