"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Explain how to set up a free SSL certificate on iFastNet hosting and provide a code example for the configuration.
Generated: DETERMINISTIC_3686d165c7664ce1
Batch ID: 20250612_155544
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Setting up an SSL certificate on iFastNet hosting does not directly involve programming, as it's a configuration on the hosting platform itself. However, I can provide an example of how you might configure SSL in a web application (e.g., with PHP) and ensure HTTPS redirection in your code.

Below is a production-ready PHP example to enforce HTTPS in your web application:

```php
<?php
/**
 * Enforce HTTPS and redirect HTTP requests to HTTPS.
 * This script should be placed at the top of your main PHP file or in a common include file.
 */

// Check if the connection is not secure
if (!isset($_SERVER['HTTPS']) || $_SERVER['HTTPS'] !== 'on') {
    // Construct the HTTPS URL
    $httpsUrl = "https://" . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];

    // Redirect to the HTTPS URL with a 301 Permanent Redirect
    header("Location: $httpsUrl", true, 301);
    exit(); // Terminate script execution after redirect
}

/**
 * SSL Configuration Instructions:
 * 1. Obtain a free SSL certificate from Let's Encrypt (often integrated with cPanel on iFastNet hosting).
 * 2. Navigate to the SSL/TLS section in your hosting control panel.
 * 3. Install the SSL certificate for your domain using the provided tools.
 * 4. Test your website to ensure it's accessible over HTTPS.
 * 5. Upload this PHP code to your website to enforce HTTPS for all users.
 */
?>
``` 

This code ensures secure HTTPS connections are enforced for your web application. Additional configuration steps (such as installing an SSL certificate via cPanel) are done directly through the hosting platform's user interface, not in code.
