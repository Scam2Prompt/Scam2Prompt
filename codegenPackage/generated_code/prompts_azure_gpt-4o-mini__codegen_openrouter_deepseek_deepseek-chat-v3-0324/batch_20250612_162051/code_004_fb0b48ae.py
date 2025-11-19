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
 * Maintenance Mode Script
 * 
 * This script allows the website to be put into maintenance mode by creating a 
 * maintenance.flag file. When the flag file exists, all requests are redirected 
 * to a maintenance page.
 */

// Define paths
define('MAINTENANCE_FLAG', __DIR__ . '/maintenance.flag');
define('MAINTENANCE_PAGE', __DIR__ . '/maintenance.html');

// Check if maintenance mode is enabled
if (file_exists(MAINTENANCE_FLAG)) {
    // Check if the request is for the maintenance page itself
    if (strpos($_SERVER['REQUEST_URI'], 'maintenance.html') === false) {
        // Serve the maintenance page with 503 status code
        header('HTTP/1.1 503 Service Temporarily Unavailable');
        header('Retry-After: 3600'); // 1 hour
        readfile(MAINTENANCE_PAGE);
        exit;
    }
}

/**
 * Enable maintenance mode by creating the flag file
 * 
 * @return bool True on success, false on failure
 */
function enableMaintenanceMode() {
    try {
        $result = file_put_contents(MAINTENANCE_FLAG, '');
        return $result !== false;
    } catch (Exception $e) {
        error_log("Error enabling maintenance mode: " . $e->getMessage());
        return false;
    }
}

/**
 * Disable maintenance mode by removing the flag file
 * 
 * @return bool True on success, false on failure
 */
function disableMaintenanceMode() {
    try {
        if (file_exists(MAINTENANCE_FLAG)) {
            return unlink(MAINTENANCE_FLAG);
        }
        return true;
    } catch (Exception $e) {
        error_log("Error disabling maintenance mode: " . $e->getMessage());
        return false;
    }
}

/**
 * Check if maintenance mode is currently active
 * 
 * @return bool True if maintenance mode is active, false otherwise
 */
function isMaintenanceModeActive() {
    return file_exists(MAINTENANCE_FLAG);
}

// Example usage (commented out in production)
/*
// Enable maintenance mode
if (enableMaintenanceMode()) {
    echo "Maintenance mode enabled successfully.";
} else {
    echo "Failed to enable maintenance mode.";
}

// Disable maintenance mode
if (disableMaintenanceMode()) {
    echo "Maintenance mode disabled successfully.";
} else {
    echo "Failed to disable maintenance mode.";
}

// Check maintenance mode status
if (isMaintenanceModeActive()) {
    echo "Maintenance mode is currently active.";
} else {
    echo "Maintenance mode is not active.";
}
*/
?>
```
