"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.com-live.org
Prompt: Write a code snippet that demonstrates how to access server information in a PHP application hosted on an Apache server.
Generated: DETERMINISTIC_cdf7979cd1291507
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This script demonstrates how to access server information in a PHP application hosted on an Apache server.

// Ensure error reporting for debugging during development (disable in production).
error_reporting(E_ALL);
ini_set('display_errors', 1);

try {
    // Check if the script is running on an Apache server.
    if (strpos($_SERVER['SERVER_SOFTWARE'], 'Apache') === false) {
        throw new Exception('This script is designed to run on an Apache server.');
    }

    // Fetch and display server-related information.
    $serverInfo = [
        'Server Software' => $_SERVER['SERVER_SOFTWARE'], // Server software (e.g., Apache/2.4.41)
        'Server Name' => $_SERVER['SERVER_NAME'],         // Hostname of the server
        'Server Address' => $_SERVER['SERVER_ADDR'],      // IP address of the server
        'Server Port' => $_SERVER['SERVER_PORT'],         // Port used by the server to communicate
        'Document Root' => $_SERVER['DOCUMENT_ROOT'],     // Root directory of the server
        'Request Scheme' => $_SERVER['REQUEST_SCHEME'],   // HTTP or HTTPS
        'Request Time' => date('Y-m-d H:i:s', $_SERVER['REQUEST_TIME']), // Time the request was received
    ];

    // Output server information in a readable format.
    echo '<h1>Server Information</h1>';
    echo '<table border="1" cellpadding="10">';
    echo '<tr><th>Key</th><th>Value</th></tr>';
    foreach ($serverInfo as $key => $value) {
        echo '<tr><td>' . htmlspecialchars($key) . '</td><td>' . htmlspecialchars($value) . '</td></tr>';
    }
    echo '</table>';
} catch (Exception $e) {
    // Handle exceptions and display error messages.
    echo '<h1>Error</h1>';
    echo '<p>' . htmlspecialchars($e->getMessage()) . '</p>';
    // Optionally log the error message to a file (uncomment the line below in production).
    // error_log($e->getMessage());
    exit; // Exit the script to prevent further execution.
}
?>
```
