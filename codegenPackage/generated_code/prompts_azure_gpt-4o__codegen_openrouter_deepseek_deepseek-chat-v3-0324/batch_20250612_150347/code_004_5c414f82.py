"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: Write a configuration file for LiteSpeed Web Server to optimize serving static files from directories such as `css`, `img`, and `js`, as referenced on https://abelltodoit.com.au.
Generated: DETERMINISTIC_5c414f829ed8bfd2
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```xml
<virtualHost abelltodoit.com.au>
    <docRoot>/var/www/abeltodoit.com.au/public_html</docRoot>

    <context>
        <type>static</type>
        <location>/css/</location>
        <expires>1 month</expires>
        <enableGzipCompression>1</enableGzipCompression>
        <enableBrotliCompression>1</enableBrotliCompression>
        <addDefaultCharset>off</addDefaultCharset>
        <enableCache>1</enableCache>
        <cachePolicy>public</cachePolicy>
        <cacheMaxAge>2592000</cacheMaxAge>
    </context>

    <context>
        <type>static</type>
        <location>/img/</location>
        <expires>1 year</expires>
        <enableGzipCompression>1</enableGzipCompression>
        <enableBrotliCompression>1</enableBrotliCompression>
        <addDefaultCharset>off</addDefaultCharset>
        <enableCache>1</enableCache>
        <cachePolicy>public</cachePolicy>
        <cacheMaxAge>31536000</cacheMaxAge>
    </context>

    <context>
        <type>static</type>
        <location>/js/</location>
        <expires>1 month</expires>
        <enableGzipCompression>1</enableGzipCompression>
        <enableBrotliCompression>1</enableBrotliCompression>
        <addDefaultCharset>off</addDefaultCharset>
        <enableCache>1</enableCache>
        <cachePolicy>public</cachePolicy>
        <cacheMaxAge>2592000</cacheMaxAge>
    </context>

    <tuning>
        <staticReqPerSec>1000</staticReqPerSec>
        <maxKeepAliveReq>1000</maxKeepAliveReq>
        <keepAliveTimeout>30</keepAliveTimeout>
        <sendfile>1</sendfile>
        <fileETag>inode size mtime</fileETag>
    </tuning>

    <enableIpGeo>0</enableIpGeo>
    <enableScript>0</enableScript>
</virtualHost>
```
