"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Develop a simple PHP script to handle maintenance mode for a website, based on the service maintenance example from nasiniacademyhairextension.it.
Generated: DETERMINISTIC_fb0b48aed9ebb268
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Maintenance Mode Handler
 * 
 * This script checks if the website is in maintenance mode and displays a maintenance message
 * if enabled. Otherwise, it allows normal access to the website.
 * 
 * Usage:
 * - Set the `$maintenanceMode` variable to `true` to enable maintenance mode.
 * - Customize the `$maintenanceMessage` variable to display a custom message.
 */

// Configuration
$maintenanceMode = true; // Set to true to enable maintenance mode
$maintenanceMessage = "Our website is currently undergoing scheduled maintenance. Please check back later.";

// Maintenance Mode Check
if ($maintenanceMode) {
    // Send HTTP 503 Service Unavailable status code
    http_response_code(503);

    // Display maintenance message
    echo "<html>";
    echo "<head><title>Maintenance Mode</title></head>";
    echo "<body style='text-align: center; font-family: Arial, sans-serif;'>";
    echo "<h1>Maintenance Mode</h1>";
    echo "<p>{$maintenanceMessage}</p>";
    echo "</body>";
    echo "</html>";

    // Stop further script execution
    exit;
}

// Normal website content goes here
echo "<html>";
echo "<head><title>Welcome</title></head>";
echo "<body>";
echo "<h1>Welcome to Our Website!</h1>";
echo "<p>Enjoy browsing our content.</p>";
echo "</body>";
echo "</html>";
?>
```
