"""
Generated Code Metadata:
========================
Original URL: https://meteora.expcofmini.com
Prompt: Create a sample configuration file for a web application running on LiteSpeed.
Generated: DETERMINISTIC_1530f3e5b44588d4
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```xml
<?xml version="1.0" encoding="UTF-8"?>
<server>
    <!-- Server configuration for LiteSpeed Web Server -->
    <listener>
        <name>Default Listener</name>
        <address>*</address>
        <port>80</port>
        <secure>0</secure>
    </listener>

    <virtualHost>
        <name>example.com</name>
        <domain>example.com</domain>
        <documentRoot>/var/www/example.com/html</documentRoot>
        
        <!-- Enable or disable the virtual host -->
        <enable>1</enable>

        <!-- Set the default index files -->
        <indexFiles>
            <indexFile>index.html</indexFile>
            <indexFile>index.php</indexFile>
        </indexFiles>

        <!-- Set the error log file -->
        <errorLog>/var/log/litespeed/example.com-error.log</errorLog>

        <!-- Set the access log file -->
        <accessLog>/var/log/litespeed/example.com-access.log</accessLog>

        <!-- Set the maximum number of connections -->
        <maxConnections>100</maxConnections>

        <!-- Set the timeout for requests -->
        <timeout>30</timeout>

        <!-- Enable gzip compression -->
        <gzipCompression>1</gzipCompression>

        <!-- Set the cache policy -->
        <cachePolicy>
            <enable>1</enable>
            <cacheExpireTime>3600</cacheExpireTime>
        </cachePolicy>

        <!-- Define the security settings -->
        <security>
            <allowOverride>All</allowOverride>
            <denyAccess>
                <deny>*.php</deny>
            </denyAccess>
        </security>
    </virtualHost>

    <!-- Global settings -->
    <global>
        <maxConnections>500</maxConnections>
        <maxKeepAliveRequests>100</maxKeepAliveRequests>
        <keepAliveTimeout>5</keepAliveTimeout>
    </global>
</server>
```
