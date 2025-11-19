"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Develop a simple PHP script to handle maintenance mode for a website, based on the service maintenance example from nasiniacademyhairextension.it.
Generated: DETERMINISTIC_fb0b48aed9ebb268
Batch ID: 20250612_162051
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
 * Maintenance Mode Script
 * 
 * This script checks whether the website is in maintenance mode
 * and either serves the maintenance page or allows access to the site.
 */

// Define the path to the maintenance mode file
define('MAINTENANCE_MODE_FILE', __DIR__ . '/maintenance.flag');

/**
 * Function to check if the website is in maintenance mode
 *
 * @return bool True if in maintenance mode, false otherwise
 */
function isMaintenanceMode() {
    return file_exists(MAINTENANCE_MODE_FILE);
}

/**
 * Function to display the maintenance message
 */
function displayMaintenancePage() {
    // Set the HTTP response code to 503 Service Unavailable
    http_response_code(503);
    
    // Display a simple maintenance message
    echo '<html lang="en">';
    echo '<head><meta charset="UTF-8"><title>Maintenance Mode</title></head>';
    echo '<body>';
    echo '<h1>We are currently undergoing maintenance</h1>';
    echo '<p>Please check back later.</p>';
    echo '</body>';
    echo '</html>';
    exit; // Stop further execution
}

// Check if the website is in maintenance mode
if (isMaintenanceMode()) {
    displayMaintenancePage(); // Show maintenance page if true
}

// Normal website execution code goes here
// For example:
// require 'header.php';
// require 'content.php';
// require 'footer.php';
?>
```
