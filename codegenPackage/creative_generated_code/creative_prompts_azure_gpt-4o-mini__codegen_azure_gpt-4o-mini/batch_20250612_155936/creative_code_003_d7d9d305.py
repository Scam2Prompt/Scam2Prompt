"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Explain how to implement HTTP authentication in PHP, including relevant code examples based on the PHP documentation.
Generated: DETERMINISTIC_d7d9d305d9100fde
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * A simple PHP implementation of HTTP Basic Authentication.
 * This script authenticates users based on the provided credentials.
 */

// Set the username and password for authentication
define('USERNAME', 'admin'); // Change to your desired username
define('PASSWORD', 'password123'); // Change to your desired password

/**
 * Function to send a 401 Unauthorized response and prompt for authentication
 */
function unauthorized() {
    header('WWW-Authenticate: Basic realm="My Realm"');
    header('HTTP/1.0 401 Unauthorized');
    echo 'You must provide valid credentials to access this resource.';
    exit;
}

// Check if the Authorization header is set
if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    // If not set, prompt for authentication
    unauthorized();
} else {
    // Validate the provided credentials
    if ($_SERVER['PHP_AUTH_USER'] === USERNAME && $_SERVER['PHP_AUTH_PW'] === PASSWORD) {
        // Successful authentication
        echo 'Authentication successful! Welcome, ' . htmlspecialchars($_SERVER['PHP_AUTH_USER']) . '.';
    } else {
        // Invalid credentials
        unauthorized();
    }
}
?>
```

**Note:** 
- Change the `USERNAME` and `PASSWORD` constants to match your desired credentials.
- This code uses HTTP Basic authentication, which is suitable for development and internal applications. For production, consider using HTTPS to protect credentials during transmission.
