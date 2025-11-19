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
-- SQL Query to analyze customer feedback data for data center power services
-- This query identifies common issues and areas for improvement based on feedback data.

-- Assuming the table structure:
-- feedback_data (
--   id INT PRIMARY KEY, -- Unique identifier for each feedback entry
--   customer_id INT, -- Unique identifier for the customer
--   feedback_text TEXT, -- The text of the customer's feedback
--   rating INT, -- Customer rating (e.g., 1-5 scale)
--   created_at TIMESTAMP -- Timestamp of when the feedback was submitted
-- )

-- Step 1: Extract common issues from feedback text using keyword analysis
-- Step 2: Aggregate ratings to identify areas with low customer satisfaction

WITH keyword_analysis AS (
    SELECT
        id,
        customer_id,
        feedback_text,
        rating,
        created_at,
        -- Extract keywords or phrases related to common issues (example: 'outage', 'slow response')
        CASE
            WHEN feedback_text ILIKE '%outage%' THEN 'Power Outage'
            WHEN feedback_text ILIKE '%slow response%' THEN 'Slow Response'
            WHEN feedback_text ILIKE '%billing issue%' THEN 'Billing Issue'
            WHEN feedback_text ILIKE '%maintenance%' THEN 'Maintenance Problem'
            ELSE 'Other'
        END AS issue_category
    FROM feedback_data
),
issue_summary AS (
    SELECT
        issue_category,
        COUNT(*) AS issue_count, -- Count occurrences of each issue category
        AVG(rating) AS avg_rating -- Average rating for each issue category
    FROM keyword_analysis
    GROUP BY issue_category
    ORDER BY issue_count DESC -- Sort by most common issues
)
SELECT
    issue_category AS "Issue Category",
    issue_count AS "Number of Occurrences",
    avg_rating AS "Average Rating"
FROM issue_summary;
```
