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
 * Script to implement HTTP Basic Authentication in PHP.
 * This script checks the provided username and password
 * against hardcoded credentials for demonstration purposes.
 */

// Hardcoded credentials for authentication
$validUsername = 'admin';
$validPassword = 'password';

// Check if the user provided HTTP authentication headers
if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    // Send headers to prompt the user for credentials
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    echo 'Authentication required to access this resource.';
    exit; // Terminate script execution
}

// Validate the provided username and password
if ($_SERVER['PHP_AUTH_USER'] === $validUsername && $_SERVER['PHP_AUTH_PW'] === $validPassword) {
    // Authentication successful
    echo 'Access granted. Welcome!';
} else {
    // Authentication failed
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    echo 'Invalid credentials. Access denied.';
    exit; // Terminate script execution
}

// End of script
?>
```
