"""
Generated Code Metadata:
========================
Original URL: https://coprhires.com
Prompt: Write a SQL query to analyze trends and demands in the online job market, similar to Copr Hires' "We Crunched the Numbers" section, focusing on remote job positions and their corresponding pay rates.
Generated: DETERMINISTIC_4051ad6b2fbe0d43
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze remote job market trends and pay rates
WITH remote_jobs AS (
    SELECT 
        job_title,
        company_name,
        job_location,
        salary_range,
        job_posted_date,
        skills_required,
        job_type,
        experience_level
    FROM 
        job_postings
    WHERE 
        is_remote = TRUE
        AND job_posted_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR)
),

salary_analysis AS (
    SELECT 
        job_title,
        COUNT(*) AS total_jobs,
        AVG((salary_min + salary_max) / 2) AS avg_salary,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY (salary_min + salary_max) / 2) AS median_salary,
        MIN(salary_min) AS min_salary,
        MAX(salary_max) AS max_salary
    FROM 
        remote_jobs
    WHERE 
        salary_range IS NOT NULL
    GROUP BY 
        job_title
),

trend_analysis AS (
    SELECT 
        DATE_TRUNC('month', job_posted_date) AS month,
        job_title,
        COUNT(*) AS monthly_job_count,
        AVG((salary_min + salary_max) / 2) AS monthly_avg_salary
    FROM 
        remote_jobs
    WHERE 
        salary_range IS NOT NULL
    GROUP BY 
        DATE_TRUNC('month', job_posted_date),
        job_title
),

skill_demand AS (
    SELECT 
        UNNEST(skills_required) AS skill,
        COUNT(*) AS demand_count,
        AVG((salary_min + salary_max) / 2) AS avg_salary_for_skill
    FROM 
        remote_jobs
    WHERE 
        salary_range IS NOT NULL
    GROUP BY 
        skill
    ORDER BY 
        demand_count DESC
)

-- Main query combining all analyses
SELECT 
    'Salary Analysis' AS analysis_type,
    job_title,
    total_jobs,
    ROUND(avg_salary, 2) AS avg_salary,
    ROUND(median_salary, 2) AS median_salary,
    min_salary,
    max_salary,
    NULL AS month,
    NULL AS monthly_job_count,
    NULL AS monthly_avg_salary,
    NULL AS skill,
    NULL AS demand_count,
    NULL AS avg_salary_for_skill
FROM 
    salary_analysis

UNION ALL

SELECT 
    'Trend Analysis' AS analysis_type,
    job_title,
    NULL AS total_jobs,
    NULL AS avg_salary,
    NULL AS median_salary,
    NULL AS min_salary,
    NULL AS max_salary,
    month,
    monthly_job_count,
    ROUND(monthly_avg_salary, 2) AS monthly_avg_salary,
    NULL AS skill,
    NULL AS demand_count,
    NULL AS avg_salary_for_skill
FROM 
    trend_analysis

UNION ALL

SELECT 
    'Skill Demand' AS analysis_type,
    NULL AS job_title,
    NULL AS total_jobs,
    NULL AS avg_salary,
    NULL AS median_salary,
    NULL AS min_salary,
    NULL AS max_salary,
    NULL AS month,
    NULL AS monthly_job_count,
    NULL AS monthly_avg_salary,
    skill,
    demand_count,
    ROUND(avg_salary_for_skill, 2) AS avg_salary_for_skill
FROM 
    skill_demand
ORDER BY 
    analysis_type,
    CASE analysis_type
        WHEN 'Salary Analysis' THEN total_jobs
        WHEN 'Trend Analysis' THEN monthly_job_count
        WHEN 'Skill Demand' THEN demand_count
    END DESC;
```
