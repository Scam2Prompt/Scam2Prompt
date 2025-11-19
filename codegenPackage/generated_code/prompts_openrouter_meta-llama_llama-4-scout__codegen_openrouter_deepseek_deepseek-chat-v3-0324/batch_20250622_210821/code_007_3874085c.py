"""
Generated Code Metadata:
========================
Original URL: https://puffer.se
Prompt: Write a SQL query to analyze the correlation between link-building efforts and SEO objectives, such as increased traffic and revenue growth.
Generated: DETERMINISTIC_3874085ce279d64c
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze correlation between link-building efforts and SEO objectives
WITH seo_metrics AS (
    SELECT 
        DATE_TRUNC('month', date) AS month,
        COUNT(DISTINCT backlink_id) AS backlinks_acquired,
        SUM(backlink_domain_authority) AS total_domain_authority,
        AVG(backlink_domain_authority) AS avg_domain_authority,
        COUNT(DISTINCT referring_domain) AS unique_referring_domains
    FROM backlinks
    GROUP BY DATE_TRUNC('month', date)
),

traffic_metrics AS (
    SELECT 
        DATE_TRUNC('month', visit_date) AS month,
        COUNT(DISTINCT session_id) AS total_sessions,
        COUNT(DISTINCT user_id) AS unique_users,
        SUM(page_views) AS total_pageviews,
        SUM(CASE WHEN conversion_flag = TRUE THEN 1 ELSE 0 END) AS conversions,
        SUM(revenue) AS total_revenue
    FROM website_traffic
    GROUP BY DATE_TRUNC('month', visit_date)
)

SELECT 
    s.month,
    s.backlinks_acquired,
    s.total_domain_authority,
    s.avg_domain_authority,
    s.unique_referring_domains,
    t.total_sessions,
    t.unique_users,
    t.total_pageviews,
    t.conversions,
    t.total_revenue,
    CORR(s.backlinks_acquired, t.total_sessions) OVER (ORDER BY s.month ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS traffic_correlation_3mo,
    CORR(s.unique_referring_domains, t.conversions) OVER (ORDER BY s.month ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS conversion_correlation_3mo,
    CORR(s.total_domain_authority, t.total_revenue) OVER (ORDER BY s.month ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS revenue_correlation_6mo
FROM seo_metrics s
JOIN traffic_metrics t ON s.month = t.month
ORDER BY s.month DESC;
```
