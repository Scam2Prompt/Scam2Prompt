"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: Recommend a method to secure directories like `cgi-bin` on a LiteSpeed Web Server, as seen on https://abelltodoit.com.au.
Generated: DETERMINISTIC_55851e2f871561bd
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**LiteSpeed Web Server Directory Security Configuration**
===========================================================

### .htaccess Configuration for LiteSpeed Web Server

```bash
# Enable LiteSpeed's mod_security
<IfModule mod_security2.c>
    # Enable mod_security for the cgi-bin directory
    <Directory /path/to/cgi-bin>
        # Enable mod_security
        SecEnabled On

        # Define the security policy
        SecRuleEngine On

        # Set the paranoia level (higher is more secure)
        SecParanoiaLevel 1

        # Set the rule IDs to include/exclude
        SecIncludeRuleIDs 900000-999999
        SecExcludeRuleIDs 200000-299999

        # Set the audit log location
        SecAuditLog /var/log/litespeed/modsec_audit.log
        SecAuditLogType Serial

        # Set the debug log location
        SecDebugLog /var/log/litespeed/modsec_debug.log
        SecDebugLogLevel 1

        # Block requests with suspicious headers
        SecRequestBodyAccess On
        SecRequestBodyLimit 131072
        SecRequestBodyNoFilesLimit 131072

        # Block common web attacks
        SecRuleRemoveById 200000
        SecRuleRemoveById 200001
    </Directory>
</IfModule>

# Enable directory listing protection
<Directory /path/to/cgi-bin>
    Options -Indexes
</Directory>

# Restrict access to cgi-bin directory
<Directory /path/to/cgi-bin>
    <Files *.*>
        Order allow,deny
        Deny from all
    </Files>
</Directory>
```

### LiteSpeed Web Server Configuration File (lsws.conf)

```bash
<VirtualHost *:80>
    # ... existing configuration ...

    # Enable directory security
    <Directory /path/to/cgi-bin>
        # Set the handler for cgi-bin
        AddHandler cgi-script .cgi .pl .plx .plp .perl

        # Set the cgi-bin directory security
        CGI nokeepalive
    </Directory>
</VirtualHost>
```

### LiteSpeed Web Server mod_security Rules

Create a file named `modsec_rules.conf` in the `/usr/local/lsws/etc/` directory:

```bash
# Load the OWASP ModSecurity Core Rule Set
Include /usr/local/lsws/etc/owasp-modsecurity-crs/crs-setup.conf
Include /usr/local/lsws/etc/owasp-modsecurity-crs/rules/*.conf

# Load custom mod_security rules
Include /usr/local/lsws/etc/modsec_rules/*.conf
```

### Custom mod_security Rule Example

Create a file named `900001.conf` in the `/usr/local/lsws/etc/modsec_rules/` directory:

```bash
SecRuleEngine On
SecRule ARGS|ARGS_NAMES|QUERY_STRING|BODY "@streq 'union'" "id:'900001',phase:2,deny,status:403,msg:'SQL Injection Attack Detected'"
```
