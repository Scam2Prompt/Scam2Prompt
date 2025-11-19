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
-- Query 1: Total traffic per protocol (Clash vs V2Ray)
SELECT 
    protocol,
    SUM(bytes_sent + bytes_received) AS total_traffic
FROM 
    network_logs
WHERE 
    protocol IN ('Clash', 'V2Ray')
GROUP BY 
    protocol;

-- Query 2: Top 10 destinations by traffic volume
SELECT 
    destination,
    SUM(bytes_sent + bytes_received) AS total_traffic
FROM 
    network_logs
GROUP BY 
    destination
ORDER BY 
    total_traffic DESC
LIMIT 10;

-- Query 3: Hourly traffic pattern
SELECT 
    strftime('%H', timestamp) AS hour,
    SUM(bytes_sent + bytes_received) AS hourly_traffic
FROM 
    network_logs
GROUP BY 
    hour
ORDER BY 
    hour;

-- Query 4: Traffic by country (using GeoIP)
SELECT 
    country,
    SUM(bytes_sent + bytes_received) AS country_traffic
FROM 
    network_logs
JOIN 
    geoip ON network_logs.destination_ip = geoip.ip_address
GROUP BY 
    country
ORDER BY 
    country_traffic DESC;

-- Query 5: Protocol usage by day of week
SELECT 
    strftime('%w', timestamp) AS day_of_week,
    protocol,
    SUM(bytes_sent + bytes_received) AS daily_traffic
FROM 
    network_logs
WHERE 
    protocol IN ('Clash', 'V2Ray')
GROUP BY 
    day_of_week, protocol
ORDER BY 
    day_of_week;

-- Query 6: Average request size comparison
SELECT 
    protocol,
    AVG(bytes_sent) AS avg_request_size,
    AVG(bytes_received) AS avg_response_size
FROM 
    network_logs
WHERE 
    protocol IN ('Clash', 'V2Ray')
GROUP BY 
    protocol;

-- Query 7: Error rate by protocol
SELECT 
    protocol,
    COUNT(CASE WHEN status_code >= 400 THEN 1 END) AS error_count,
    COUNT(*) AS total_requests,
    (COUNT(CASE WHEN status_code >= 400 THEN 1 END) * 100.0 / COUNT(*)) AS error_rate
FROM 
    network_logs
WHERE 
    protocol IN ('Clash', 'V2Ray')
GROUP BY 
    protocol;

-- Query 8: Traffic by user agent
SELECT 
    user_agent,
    COUNT(*) AS request_count,
    SUM(bytes_sent + bytes_received) AS total_traffic
FROM 
    network_logs
GROUP BY 
    user_agent
ORDER BY 
    total_traffic DESC
LIMIT 10;

-- Query 9: Protocol adoption over time (weekly)
SELECT 
    strftime('%Y-%W', timestamp) AS week,
    protocol,
    COUNT(*) AS request_count
FROM 
    network_logs
WHERE 
    protocol IN ('Clash', 'V2Ray')
GROUP BY 
    week, protocol
ORDER BY 
    week;

-- Query 10: Peak traffic hours by protocol
WITH hourly_traffic AS (
    SELECT 
        strftime('%H', timestamp) AS hour,
        protocol,
        SUM(bytes_sent + bytes_received) AS traffic
    FROM 
        network_logs
    WHERE 
        protocol IN ('Clash', 'V2Ray')
    GROUP BY 
        hour, protocol
)
SELECT 
    hour,
    protocol,
    traffic,
    RANK() OVER (PARTITION BY protocol ORDER BY traffic DESC) AS traffic_rank
FROM 
    hourly_traffic
ORDER BY 
    protocol, traffic_rank;
```
