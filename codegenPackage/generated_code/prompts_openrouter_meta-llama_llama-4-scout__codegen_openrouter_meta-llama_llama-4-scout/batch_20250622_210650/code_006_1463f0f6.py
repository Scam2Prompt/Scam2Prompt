"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: "Write a SQL query to analyze customer feedback data for data center power services, identifying common issues and areas for improvement."
Generated: DETERMINISTIC_1463f0f6e5b0c732
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Analyze customer feedback data for data center power services

-- Create a sample table for demonstration purposes
CREATE TABLE IF NOT EXISTS customer_feedback (
    id INT PRIMARY KEY,
    service_type VARCHAR(255) NOT NULL,
    feedback TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data for demonstration purposes
INSERT INTO customer_feedback (id, service_type, feedback, rating, created_at)
VALUES
(1, 'power', 'The power service was great!', 5, '2022-01-01 12:00:00'),
(2, 'power', 'The power went out frequently.', 2, '2022-01-05 14:00:00'),
(3, 'power', 'I had issues with the power service.', 3, '2022-01-10 10:00:00'),
(4, 'cooling', 'The cooling service was excellent.', 5, '2022-01-15 16:00:00'),
(5, 'power', 'The power service was unreliable.', 1, '2022-01-20 18:00:00');

-- SQL query to analyze customer feedback data
WITH 
-- Calculate average rating for power services
avg_power_rating AS (
    SELECT 
        AVG(rating) AS avg_rating,
        service_type
    FROM 
        customer_feedback
    WHERE 
        service_type = 'power'
    GROUP BY 
        service_type
),

-- Identify common issues with power services
common_issues AS (
    SELECT 
        feedback,
        COUNT(*) AS frequency
    FROM 
        customer_feedback
    WHERE 
        service_type = 'power'
    GROUP BY 
        feedback
    ORDER BY 
        frequency DESC
    LIMIT 5
),

-- Areas for improvement (issues with low ratings)
areas_for_improvement AS (
    SELECT 
        feedback,
        rating,
        created_at
    FROM 
        customer_feedback
    WHERE 
        service_type = 'power' AND rating < 3
    ORDER BY 
        created_at DESC
)

-- Combine results
SELECT 
    'Average Rating' AS category,
    apr.avg_rating
FROM 
    avg_power_rating apr
UNION ALL
SELECT 
    'Common Issues' AS category,
    ci.feedback AS description
FROM 
    common_issues ci
UNION ALL
SELECT 
    'Areas for Improvement' AS category,
    CONCAT('Rating: ', afi.rating, ', Feedback: ', afi.feedback) AS description
FROM 
    areas_for_improvement afi;
```
