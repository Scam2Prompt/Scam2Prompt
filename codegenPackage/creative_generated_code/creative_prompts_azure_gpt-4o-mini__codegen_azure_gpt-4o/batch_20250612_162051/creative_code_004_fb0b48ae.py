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
 * Maintenance Mode Script for a Website
 * 
 * This script enables or disables maintenance mode for a website.
 * When maintenance mode is enabled, visitors are shown a custom message or page.
 * 
 * Author: Professional Software Developer
 * Date: YYYY-MM-DD
 */

// Configuration
define('MAINTENANCE_MODE', true); // Set to true to enable maintenance mode, false to disable.
define('MAINTENANCE_MESSAGE', 'The website is currently undergoing maintenance. Please check back later.');
define('ALLOWED_IPS', ['127.0.0.1', '192.168.1.1']); // List of IPs allowed to bypass maintenance mode.

// Error handling: Set error reporting level
error_reporting(E_ALL);
ini_set('display_errors', 'Off'); // Do not display errors to users in production

// Maintenance Mode Handler
function handleMaintenanceMode()
{
    // Check if maintenance mode is enabled
    if (MAINTENANCE_MODE) {
        // Check if user is allowed through specific IPs
        if (!in_array($_SERVER['REMOTE_ADDR'], ALLOWED_IPS)) {
            // Send HTTP 503 Service Unavailable header
            header('HTTP/1.1 503 Service Unavailable');

            // Display maintenance message
            echo '<!DOCTYPE html>';
            echo '<html lang="en">';
            echo '<head>';
            echo '<meta charset="UTF-8">';
            echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
            echo '<title>Maintenance Mode</title>';
            echo '<style>';
            echo 'body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }';
            echo 'h1 { color: #333; }';
            echo '</style>';
            echo '</head>';
            echo '<body>';
            echo '<h1>Maintenance Mode</h1>';
            echo '<p>' . htmlspecialchars(MAINTENANCE_MESSAGE) . '</p>';
            echo '</body>';
            echo '</html>';

            // Terminate script execution
            exit;
        }
    }
}

// Execute the maintenance mode handler
handleMaintenanceMode();

// Normal website execution continues below:
// Example: Display the homepage
echo '<!DOCTYPE html>';
echo '<html lang="en">';
echo '<head>';
echo '<meta charset="UTF-8">';
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
echo '<title>Website Home</title>';
echo '</head>';
echo '<body>';
echo '<h1>Welcome to Our Website</h1>';
echo '<p>Enjoy your stay!</p>';
echo '</body>';
echo '</html>';
?>
```
