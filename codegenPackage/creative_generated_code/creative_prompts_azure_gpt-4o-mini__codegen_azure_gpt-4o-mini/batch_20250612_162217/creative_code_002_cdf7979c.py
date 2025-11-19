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
/**
 * Server Information Access Script
 *
 * This script demonstrates how to access and display
 * server information in a PHP application hosted on
 * an Apache server.
 *
 * PHP Version: 7.4+
 */

// Start output buffering to avoid issues with header information
ob_start();

// Function to display server information
function displayServerInfo() {
    // Check if server information is available
    if (empty($_SERVER)) {
        echo "<p>No server information available.</p>";
        return;
    }

    // Display server information in a structured format
    echo "<h1>Server Information</h1>";
    echo "<table border='1' cellpadding='5'>";
    echo "<tr><th>Variable</th><th>Value</th></tr>";

    // Iterate over server variables
    foreach ($_SERVER as $key => $value) {
        echo "<tr><td>" . htmlspecialchars($key) . "</td><td>" . htmlspecialchars($value) . "</td></tr>";
    }

    echo "</table>";
}

// Error handling
try {
    // Call the function to display server information
    displayServerInfo();
} catch (Exception $e) {
    // Log the error message to a log file
    error_log("Error occurred: " . $e->getMessage());

    // Display a generic error message to the user
    echo "<p>An error occurred while retrieving server information.</p>";
}

// Flush the output buffer and send output to the browser
ob_end_flush();
?>
```
