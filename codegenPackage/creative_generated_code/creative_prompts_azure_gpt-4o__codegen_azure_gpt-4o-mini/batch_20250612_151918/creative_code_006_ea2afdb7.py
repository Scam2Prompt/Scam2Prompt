"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet0732127-exodus-ssl48.shimi.com.au
Prompt: Suggest a method to secure directory listings on LiteSpeed Web Server to prevent unauthorized access, and provide an example configuration file.
Generated: DETERMINISTIC_ea2afdb75600bebf
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- LiteSpeed Web Server Configuration File -->
    <virtualHost>
        <name>example.com</name>
        
        <!-- Specify the document root for the virtual host -->
        <documentRoot>/var/www/html/example</documentRoot>

        <!-- Disable directory listings -->
        <enableDirectoryListing>0</enableDirectoryListing>

        <!-- Set access controls to secure sensitive directories -->
        <directory>
            <path>/var/www/html/example/private</path>
            <allow>none</allow>
            <deny>all</deny>
        </directory>

        <!-- Enable authentication for specific directories -->
        <directory>
            <path>/var/www/html/example/secure</path>
            <allow>authenticated</allow>
            <deny>all</deny>
            <authType>Basic</authType>
            <authName>Restricted Area</authName>
            <authUserFile>/var/www/.htpasswd</authUserFile>
        </directory>

        <!-- Custom error pages -->
        <errorPages>
            <errorPage>
                <status>403</status>
                <file>403.html</file>
            </errorPage>
            <errorPage>
                <status>404</status>
                <file>404.html</file>
            </errorPage>
        </errorPages>
    </virtualHost>
</configuration>
```

### Notes:
- Ensure that the paths referenced in the configuration file exist and have the appropriate permissions.
- The `.htpasswd` file must be created and populated with user credentials to access the secure directory.
- Adjust the `documentRoot`, `authUserFile`, and directory paths as per your directory structure.
- Error pages (e.g., `403.html`, `404.html`) should be created to provide a user-friendly response for forbidden and not found errors.
