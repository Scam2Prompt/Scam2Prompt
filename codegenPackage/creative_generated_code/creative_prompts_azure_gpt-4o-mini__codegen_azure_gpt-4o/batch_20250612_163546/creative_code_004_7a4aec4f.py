"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoclaim.rf.gd
Prompt: Provide a code example for implementing SSL on a website hosted with iFastNet, considering their free SSL feature.
Generated: DETERMINISTIC_7a4aec4f629e4501
Batch ID: 20250612_163546
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

Below is an example of PHP code for enabling and verifying SSL on a website hosted with iFastNet using their free SSL feature. This code focuses on redirecting HTTP traffic to HTTPS and verifying SSL functionality.

```php
<?php
// Enable error reporting for debugging in development mode (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if SSL is enabled
function isSSLEnabled() {
    // Check the HTTPS server variable
    if (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') {
        return true;
    }
    // Check for SSL in forwarded headers (useful for proxies/load balancers)
    if (!empty($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {
        return true;
    }
    return false;
}

// Force redirect to HTTPS if SSL is not enabled
function forceHTTPS() {
    if (!isSSLEnabled()) {
        // Build the HTTPS URL
        $httpsURL = 'https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
        // Perform a 301 redirect to HTTPS
        header('Location: ' . $httpsURL, true, 301);
        exit;
    }
}

// Call the function to enforce HTTPS
forceHTTPS();

// Example functionality: Display a confirmation message
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSL Enabled Website</title>
</head>
<body>
    <h1>Welcome to My Secure Website</h1>
    <p>Your connection is secure with SSL enabled.</p>
</body>
</html>
```

### Notes:
- This code should be placed in the entry point of your website, typically in the `index.php` file.
- Ensure the free SSL certificate provided by iFastNet is installed and active for your domain.
- Test the functionality after deployment to confirm HTTPS redirection and SSL functionality.
