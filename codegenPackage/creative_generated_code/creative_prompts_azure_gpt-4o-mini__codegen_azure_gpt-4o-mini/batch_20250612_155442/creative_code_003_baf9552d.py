"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.au
Prompt: Can you provide a code example for redirecting a parked domain to another website using Clickhost?
Generated: DETERMINISTIC_baf9552d47eb323a
Batch ID: 20250612_155442
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.targetwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Redirect a parked domain to another website using Clickhost.
 * 
 * This script sets up a 301 (permanent) redirect from a parked domain 
 * to the specified target URL. Make sure to replace 'your_parked_domain.com' 
 * and 'http://www.targetwebsite.com' with your actual domain and target URL.
 */

// Define the parked domain and the target URL for redirection.
$parkedDomain = 'your_parked_domain.com';
$targetUrl = 'http://www.targetwebsite.com';

// Check if the current domain matches the parked domain.
if ($_SERVER['HTTP_HOST'] === $parkedDomain) {
    // Set the response code to 301 for permanent redirection.
    http_response_code(301);
    
    // Redirect to the target URL.
    header("Location: $targetUrl", true, 301);
    exit(); // Terminate the script after redirection.
}

// Optionally handle cases where the script is accessed without being the parked domain.
http_response_code(404); // Not Found
echo "This domain is not configured for redirection.";
?>
```
