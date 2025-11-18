"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ottbangla.store
Prompt: How can I set up a "cgi-bin" directory on a LiteSpeed Web Server for executing CGI scripts? Provide example code.
Generated: DETERMINISTIC_2da7d42c72dc7ecd
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Create cgi-bin directory
sudo mkdir /usr/local/lsws/cgi-bin

# Set the appropriate permissions
sudo chown -R nobody:nogroup /usr/local/lsws/cgi-bin
sudo chmod 755 /usr/local/lsws/cgi-bin

# Create a sample CGI script
echo '#!/bin/bash' | sudo tee /usr/local/lsws/cgi-bin/hello.cgi > /dev/null
echo 'echo Content-type: text/html' | sudo tee -a /usr/local/lsws/cgi-bin/hello.cgi > /dev/null
echo 'echo' | sudo tee -a /usr/local/lsws/cgi-bin/hello.cgi > /dev/null
echo '<html><body>' | sudo tee -a /usr/local/lsws/cgi-bin/hello.cgi > /dev/null
echo '<h1>Hello, World!</h1>' | sudo tee -a /usr/local/lsws/cgi-bin/hello.cgi > /dev/null
echo '</body></html>' | sudo tee -a /usr/local/lsws/cgi-bin/hello.cgi > /dev/null

# Make the script executable
sudo chmod +x /usr/local/lsws/cgi-bin/hello.cgi

# Update LiteSpeed configuration to set the cgi-bin directory
# Edit the LiteSpeed configuration file
sudo nano /usr/local/lsws/conf/httpd_config.xml

# Add the following within the <virtualHost> section
# <context>
#    <uri>/cgi-bin/</uri>
#    <type>c</type>
#    <handler>cgi</handler>
#    <allowOverride>1</allowOverride>
# </context>

# Ensure the changes are saved
# Restart LiteSpeed server for changes to take effect
sudo /usr/local/lsws/bin/lswsctrl restart
```

Make sure to modify paths as necessary and to verify the configuration settings based on your specific LiteSpeed installation.
