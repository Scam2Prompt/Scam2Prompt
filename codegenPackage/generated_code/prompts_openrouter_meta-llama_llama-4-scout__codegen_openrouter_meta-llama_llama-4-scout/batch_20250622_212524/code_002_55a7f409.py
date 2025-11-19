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
-- Query 1: Get total number of connections
SELECT 
    COUNT(*) as total_connections
FROM 
    network_logs;

-- Query 2: Get top 5 countries by number of connections
SELECT 
    country, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    country
ORDER BY 
    num_connections DESC
LIMIT 5;

-- Query 3: Get number of connections per day
SELECT 
    DATE(timestamp) as date, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    date
ORDER BY 
    date;

-- Query 4: Get top 10 most active users
SELECT 
    user_id, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    user_id
ORDER BY 
    num_connections DESC
LIMIT 10;

-- Query 5: Get average traffic per user
SELECT 
    AVG(num_connections) as avg_traffic_per_user
FROM (
    SELECT 
        user_id, 
        COUNT(*) as num_connections
    FROM 
        network_logs
    GROUP BY 
        user_id
) as user_traffic;

-- Query 6: Get number of connections per protocol (Clash/V2Ray)
SELECT 
    protocol, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    protocol
ORDER BY 
    num_connections DESC;

-- Query 7: Get top 5 ports by number of connections
SELECT 
    port, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    port
ORDER BY 
    num_connections DESC
LIMIT 5;

-- Query 8: Get number of connections per hour of day
SELECT 
    EXTRACT(HOUR FROM timestamp) as hour, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    hour
ORDER BY 
    hour;

-- Query 9: Get number of connections from specific IP addresses
SELECT 
    ip_address, 
    COUNT(*) as num_connections
FROM 
    network_logs
WHERE 
    ip_address IN ('192.168.1.100', '192.168.1.200')
GROUP BY 
    ip_address
ORDER BY 
    num_connections DESC;

-- Query 10: Get traffic distribution by response status code
SELECT 
    response_status_code, 
    COUNT(*) as num_connections
FROM 
    network_logs
GROUP BY 
    response_status_code
ORDER BY 
    num_connections DESC;
```
