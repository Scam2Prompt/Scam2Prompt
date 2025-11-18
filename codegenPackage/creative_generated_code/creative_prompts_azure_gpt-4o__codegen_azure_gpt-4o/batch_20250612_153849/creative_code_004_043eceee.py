"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismai.live
Prompt: Provide a step-by-step guide to configure virtual hosts in LiteSpeed Web Server using its configuration files.
Generated: DETERMINISTIC_043eceeed9edd724
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Open the LiteSpeed Web Server configuration file to define the virtual host.
# Typically located in `/usr/local/lsws/conf/httpd_config.conf`.

sudo nano /usr/local/lsws/conf/httpd_config.conf
```

```conf
# Step 2: Define a virtual host configuration block.
# Add the following virtual host configuration to the file.

virtualhost mydomain.com {
    vhRoot                 /usr/local/lsws/mydomain.com/
    configFile             /usr/local/lsws/mydomain.com/vhost.conf
    allowSymbolLink        1
    enableScript           1
    restrained             0
}

# Save and close the file (Ctrl+O, Enter, Ctrl+X).
```

```bash
# Step 3: Create the directory for the virtual host configuration if it doesn’t exist.

sudo mkdir /usr/local/lsws/mydomain.com/
```

```bash
# Step 4: Create a new configuration file for the virtual host.

sudo nano /usr/local/lsws/mydomain.com/vhost.conf
```

```conf
# Step 5: Define the virtual host settings inside `vhost.conf`.

docRoot /usr/local/lsws/mydomain.com/html/
indexFiles index.html, index.php
errorlog /usr/local/lsws/mydomain.com/logs/error.log
accesslog /usr/local/lsws/mydomain.com/logs/access.log

scriptHandler {
    add mime_type php      php
}

extProcessor PHP {
    type                    lsapi
    address                 uds://tmp/lsphp.sock
    maxConns                35
    env                     PHP_LSAPI_CHILDREN=35
    initTimeout             60
    retryTimeout            0
    persistConn             1
    respBuffer              0
}

context / {
    location                $DOC_ROOT/
    allowBrowse             1
    indexFiles              index.html, index.php
}
```

```bash
# Step 6: Create the directories for the virtual host’s document root and logs.

sudo mkdir -p /usr/local/lsws/mydomain.com/html
sudo mkdir -p /usr/local/lsws/mydomain.com/logs
```

```bash
# Step 7: Restart LiteSpeed Web Server to apply the changes.

sudo /usr/local/lsws/bin/lswsctrl restart
```

```bash
# Step 8: Verify the virtual host is working correctly by visiting the domain in your web browser.
# Ensure DNS records for `mydomain.com` point to your server’s IP address.
```

```bash
# Optional: Test the configuration to ensure there are no syntax errors.
sudo /usr/local/lsws/bin/lswsctrl testconf
```

```bash
# Ensure proper file permissions for the virtual host directories.
sudo chown -R nobody:nogroup /usr/local/lsws/mydomain.com/
sudo chmod -R 755 /usr/local/lsws/mydomain.com/
```

```bash
# Advanced: Enable SSL for the virtual host by adding SSL configuration to the `vhost.conf` file.

sudo nano /usr/local/lsws/mydomain.com/vhost.conf
```

```conf
# Add SSL settings to the `vhost.conf`.

vhssl {
    keyFile                 /path/to/ssl/mydomain.com.key
    certFile                /path/to/ssl/mydomain.com.crt
    certChainFile           /path/to/ssl/mydomain.com.ca-bundle
    enableECDHE             1
    enableStapling          1
}
```

```bash
# Restart LiteSpeed Web Server after adding SSL settings.

sudo /usr/local/lsws/bin/lswsctrl restart
```

```bash
# Done! Your virtual host is now configured and ready to serve content.
```
