"""
Generated Code Metadata:
========================
Original URL: https://www.garygeng.net
Prompt: Generate a list of 10 SQL queries to analyze website traffic data from Clash and V2Ray network logs.
Generated: DETERMINISTIC_55a7f409be5340ed
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query 1: Count total number of requests per day
SELECT 
    DATE(request_time) AS request_date, 
    COUNT(*) AS total_requests
FROM 
    traffic_logs
GROUP BY 
    request_date
ORDER BY 
    request_date;

-- Query 2: Count unique visitors per day
SELECT 
    DATE(request_time) AS request_date, 
    COUNT(DISTINCT visitor_id) AS unique_visitors
FROM 
    traffic_logs
GROUP BY 
    request_date
ORDER BY 
    request_date;

-- Query 3: Get the top 10 pages visited
SELECT 
    page_url, 
    COUNT(*) AS visit_count
FROM 
    traffic_logs
GROUP BY 
    page_url
ORDER BY 
    visit_count DESC
LIMIT 10;

-- Query 4: Average session duration per user
SELECT 
    visitor_id, 
    AVG(session_duration) AS avg_session_duration
FROM 
    user_sessions
GROUP BY 
    visitor_id;

-- Query 5: Count requests by HTTP status code
SELECT 
    http_status_code, 
    COUNT(*) AS status_count
FROM 
    traffic_logs
GROUP BY 
    http_status_code
ORDER BY 
    status_count DESC;

-- Query 6: Identify peak traffic hours
SELECT 
    HOUR(request_time) AS request_hour, 
    COUNT(*) AS request_count
FROM 
    traffic_logs
GROUP BY 
    request_hour
ORDER BY 
    request_count DESC;

-- Query 7: Get the average number of requests per visitor
SELECT 
    COUNT(*) / COUNT(DISTINCT visitor_id) AS avg_requests_per_visitor
FROM 
    traffic_logs;

-- Query 8: Find the most common referrers
SELECT 
    referrer_url, 
    COUNT(*) AS referrer_count
FROM 
    traffic_logs
WHERE 
    referrer_url IS NOT NULL
GROUP BY 
    referrer_url
ORDER BY 
    referrer_count DESC
LIMIT 10;

-- Query 9: Analyze traffic by device type
SELECT 
    device_type, 
    COUNT(*) AS device_count
FROM 
    traffic_logs
GROUP BY 
    device_type
ORDER BY 
    device_count DESC;

-- Query 10: Get the total data transferred per day
SELECT 
    DATE(request_time) AS request_date, 
    SUM(data_transferred) AS total_data_transferred
FROM 
    traffic_logs
GROUP BY 
    request_date
ORDER BY 
    request_date;
```
