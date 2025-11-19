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
-- Query 1: Total number of requests logged
SELECT COUNT(*) AS total_requests
FROM network_logs;

-- Query 2: Total data transferred (in bytes)
SELECT SUM(data_transferred) AS total_data_transferred
FROM network_logs;

-- Query 3: Top 10 most visited domains
SELECT domain, COUNT(*) AS visit_count
FROM network_logs
GROUP BY domain
ORDER BY visit_count DESC
LIMIT 10;

-- Query 4: Average data transferred per request
SELECT AVG(data_transferred) AS avg_data_per_request
FROM network_logs;

-- Query 5: Requests grouped by protocol (e.g., HTTP, HTTPS)
SELECT protocol, COUNT(*) AS request_count
FROM network_logs
GROUP BY protocol
ORDER BY request_count DESC;

-- Query 6: Hourly traffic analysis (requests per hour)
SELECT DATE_FORMAT(timestamp, '%Y-%m-%d %H:00:00') AS hour, COUNT(*) AS request_count
FROM network_logs
GROUP BY hour
ORDER BY hour;

-- Query 7: Top 10 IP addresses generating the most traffic
SELECT source_ip, SUM(data_transferred) AS total_data
FROM network_logs
GROUP BY source_ip
ORDER BY total_data DESC
LIMIT 10;

-- Query 8: Percentage of traffic by protocol
SELECT protocol, 
       (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM network_logs)) AS percentage
FROM network_logs
GROUP BY protocol;

-- Query 9: Requests grouped by country (assuming GeoIP data is available)
SELECT country, COUNT(*) AS request_count
FROM network_logs
GROUP BY country
ORDER BY request_count DESC;

-- Query 10: Peak traffic hour (hour with the most requests)
SELECT DATE_FORMAT(timestamp, '%Y-%m-%d %H:00:00') AS peak_hour, COUNT(*) AS request_count
FROM network_logs
GROUP BY peak_hour
ORDER BY request_count DESC
LIMIT 1;
```

Note: Replace `network_logs` with the actual table name containing Clash and V2Ray logs. Ensure the table has columns like `timestamp`, `domain`, `protocol`, `source_ip`, `data_transferred`, and `country` (if GeoIP data is integrated).
