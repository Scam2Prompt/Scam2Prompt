"""
Generated Code Metadata:
========================
Original URL: https://optimism-app.lcfmedia.com
Prompt: Write a basic configuration example for LiteSpeed Web Server to serve a web application, referencing the "Proudly Served by LiteSpeed Web Server" header.
Generated: DETERMINISTIC_0cf88134855ea29c
Batch ID: 20250622_212422
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
        <!-- Define the listener for HTTP traffic -->
        <name>Default</name>
        <address>*</address>
        <port>80</port>
    </listener>

    <virtualHost>
        <!-- Define the virtual host for the web application -->
        <name>example.com</name>
        <domain>example.com</domain>
        <documentRoot>/var/www/example.com/public_html</documentRoot>
        
        <!-- Enable the Proudly Served by LiteSpeed header -->
        <header>
            <name>X-Powered-By</name>
            <value>Proudly Served by LiteSpeed Web Server</value>
        </header>

        <!-- Set up error handling -->
        <errorLog>
            <logLevel>warn</logLevel>
            <logFile>/var/log/litespeed/example.com_error.log</logFile>
        </errorLog>

        <accessLog>
            <logFile>/var/log/litespeed/example.com_access.log</logFile>
        </accessLog>

        <!-- Define the index files -->
        <indexFiles>
            <indexFile>index.html</indexFile>
            <indexFile>index.php</indexFile>
        </indexFiles>

        <!-- Set up document root permissions -->
        <allowOverride>All</allowOverride>
        <enableCache>1</enableCache>
        
        <!-- Define the PHP handler -->
        <php>
            <handler>
                <name>PHP</name>
                <type>php</type>
                <version>7.4</version>
                <maxRequests>100</maxRequests>
            </handler>
        </php>
    </virtualHost>
</server>
```
