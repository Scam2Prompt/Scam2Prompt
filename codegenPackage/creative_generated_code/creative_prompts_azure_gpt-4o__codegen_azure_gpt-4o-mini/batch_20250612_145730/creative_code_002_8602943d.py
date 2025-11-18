"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ottbangla.store
Prompt: Generate a configuration file for LiteSpeed Web Server that enables secure access to a "cgi-bin" directory.
Generated: DETERMINISTIC_8602943d0f5d632e
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <!-- LiteSpeed Web Server Configuration -->
    <Server>
        <VirtualHost>
            <!-- Define the virtual host for the domain -->
            <Name>example.com</Name>
            <DocumentRoot>/var/www/example.com/html</DocumentRoot>

            <!-- Enable CGI for the cgi-bin directory -->
            <ScriptHandler>
                <!-- Specify the handler that will process CGI scripts -->
                <AddHandler>cgi-script .cgi .pl</AddHandler>
            </ScriptHandler>

            <!-- Directory settings for secure access -->
            <Directory>
                <Path>/var/www/example.com/cgi-bin</Path>
                
                <!-- Restrict access to the cgi-bin directory -->
                <AllowOverride>None</AllowOverride>
                <RequireAll>
                    <RequireAny>
                        <!-- Allow access only from specific IPs -->
                        <Require ip 192.0.2.0/24 />
                        <Require ip 203.0.113.0/24 />
                    </RequireAny>
                    <!-- Deny all other access -->
                    <Require all denied />
                </RequireAll>

                <!-- Enable SSL for secure access -->
                <SSL>
                    <Enabled>1</Enabled>
                    <CertificateFile>/etc/ssl/certs/example.com.crt</CertificateFile>
                    <CertificateKeyFile>/etc/ssl/private/example.com.key</CertificateKeyFile>
                </SSL>
            </Directory>

        </VirtualHost>
    </Server>
</Configuration>
```
