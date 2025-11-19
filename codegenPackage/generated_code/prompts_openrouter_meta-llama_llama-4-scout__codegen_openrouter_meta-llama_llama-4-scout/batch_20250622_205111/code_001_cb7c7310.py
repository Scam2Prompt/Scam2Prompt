"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Write a configuration example for LiteSpeed Web Server to serve a CGI script.
Generated: DETERMINISTIC_cb7c7310ea0c2db0
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# LiteSpeed Web Server configuration example to serve a CGI script

# Define the CGI handler
Handler {
    # Define the CGI handler
    lsapi {
        # Specify the executable path for the CGI handler
        executable     /usr/local/bin/lsapi
        # Specify the CGI extension
        extension      cgi
    }
}

# Define the virtual host
VHost {
    # Specify the document root
    documentRoot   /var/www/html

    # Specify the CGI directory
    cgiDirectory   /var/www/cgi-bin

    # Enable CGI
    enableCgi      1

    # Define the CGI handler
    Handler {
        # Map the CGI extension to the lsapi handler
        lsapi {
            extension  cgi
        }
    }

    # Define the context for the CGI script
    Context /cgi-bin/ {
        # Enable CGI for this context
        enableCgi  1
        # Set the handler for this context
        Handler lsapi
    }
}

# Error handling
ErrorLog /var/log/litespeed/error.log
AccessLog /var/log/litespeed/access.log

# Define the log format
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
```

```xml
<!-- Alternatively, here is an XML configuration example -->

<!-- LiteSpeed Web Server configuration example to serve a CGI script -->
<configuration>
    <!-- Define the CGI handler -->
    <handler>
        <lsapi>
            <!-- Specify the executable path for the CGI handler -->
            <executable>/usr/local/bin/lsapi</executable>
            <!-- Specify the CGI extension -->
            <extension>cgi</extension>
        </lsapi>
    </handler>

    <!-- Define the virtual host -->
    <vhost>
        <!-- Specify the document root -->
        <documentRoot>/var/www/html</documentRoot>

        <!-- Specify the CGI directory -->
        <cgiDirectory>/var/www/cgi-bin</cgiDirectory>

        <!-- Enable CGI -->
        <enableCgi>1</enableCgi>

        <!-- Define the CGI handler -->
        <handler>
            <!-- Map the CGI extension to the lsapi handler -->
            <lsapi>
                <extension>cgi</extension>
            </lsapi>
        </handler>

        <!-- Define the context for the CGI script -->
        <context path="/cgi-bin/">
            <!-- Enable CGI for this context -->
            <enableCgi>1</enableCgi>
            <!-- Set the handler for this context -->
            <handler>lsapi</handler>
        </context>
    </vhost>

    <!-- Error handling -->
    <errorLog>/var/log/litespeed/error.log</errorLog>
    <accessLog>/var/log/litespeed/access.log</accessLog>

    <!-- Define the log format -->
    <logFormat>%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"</logFormat>
</configuration>
```
