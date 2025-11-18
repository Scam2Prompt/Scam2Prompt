"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Provide an example of a `robots.txt` file that allows only Googlebot to access the site while blocking all other crawlers.
Generated: DETERMINISTIC_9a5ab24d28266918
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```plaintext
# This is a robots.txt file for controlling web crawler access to the site

# User-agent specifies the web crawlers to which the following rules apply
User-agent: Googlebot
# Allow Googlebot to access all content on the site
Allow: /

# User-agent specifies all other crawlers
User-agent: *
# Block all other crawlers from accessing any content on the site
Disallow: /
```
