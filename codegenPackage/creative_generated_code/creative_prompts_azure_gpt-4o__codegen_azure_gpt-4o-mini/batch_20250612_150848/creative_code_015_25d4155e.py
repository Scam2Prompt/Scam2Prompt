"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Create PHP code to implement HTTP authentication, referencing the phpm.ru documentation.
Generated: DETERMINISTIC_25d4155effc7b8e8
Batch ID: 20250612_150848
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
 * Simple HTTP Authentication in PHP
 * This script checks for valid HTTP credentials and restricts access to protected content.
 */

// Define a username and password for authentication
define('USERNAME', 'admin');
define('PASSWORD', 'password123');

// Function to send a 401 Unauthorized response
function unauthorizedResponse() {
    header('WWW-Authenticate: Basic realm="Protected Area"');
    header('HTTP/1.0 401 Unauthorized');
    echo 'Unauthorized access. Please provide valid credentials.';
    exit;
}

// Check if the user is authenticated
if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    unauthorizedResponse(); // Prompt for authentication
} else {
    // Validate the provided credentials
    if ($_SERVER['PHP_AUTH_USER'] !== USERNAME || $_SERVER['PHP_AUTH_PW'] !== PASSWORD) {
        unauthorizedResponse(); // Invalid credentials
    }
}

// If authentication is successful, display protected content
echo '<h1>Welcome to the Protected Area!</h1>';
echo '<p>You have successfully authenticated.</p>';

// Add additional code for your application logic here

?>
```
