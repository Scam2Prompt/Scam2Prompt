"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Write a PHP script to implement HTTP authentication using PHP's built-in features, as described in the documentation.
Generated: DETERMINISTIC_184eba2779fa1ad4
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

// Define the username and password for authentication
define('USERNAME', 'admin');
define('PASSWORD', 'password123');

// Check if the user is already authenticated
if (isset($_SESSION['authenticated']) && $_SESSION['authenticated'] === true) {
    // User is authenticated, display a welcome message
    echo "Welcome, " . htmlspecialchars(USERNAME) . "!";
    exit;
}

// Function to send the authentication headers
function sendAuthHeaders() {
    header('HTTP/1.0 401 Unauthorized');
    header('WWW-Authenticate: Basic realm="Protected Area"');
    echo 'You must provide valid credentials to access this resource.';
    exit;
}

// Check if credentials are sent via HTTP Basic Authentication
if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    sendAuthHeaders();
}

// Validate the credentials
if ($_SERVER['PHP_AUTH_USER'] === USERNAME && $_SERVER['PHP_AUTH_PW'] === PASSWORD) {
    // Credentials are valid, set the session variable to indicate authentication
    $_SESSION['authenticated'] = true;
    echo "Welcome, " . htmlspecialchars(USERNAME) . "!";
} else {
    // Invalid credentials, send authentication headers again
    sendAuthHeaders();
}
```
