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
 * This script handles the maintenance mode for a website.
 * It checks if the site is under maintenance and redirects to a maintenance page if so.
 */

// Configuration
$maintenanceFile = 'maintenance.txt';
$maintenancePage = 'maintenance.html';

/**
 * Check if the site is under maintenance
 *
 * @return bool
 */
function isUnderMaintenance($maintenanceFile) {
    try {
        return file_exists($maintenanceFile);
    } catch (Exception $e) {
        // Log the error
        error_log('Error checking maintenance file: ' . $e->getMessage());
        return false;
    }
}

/**
 * Redirect to maintenance page
 *
 * @param string $maintenancePage
 */
function redirectToMaintenancePage($maintenancePage) {
    try {
        header('Location: ' . $maintenancePage);
        exit;
    } catch (Exception $e) {
        // Log the error
        error_log('Error redirecting to maintenance page: ' . $e->getMessage());
    }
}

// Check if site is under maintenance
if (isUnderMaintenance($maintenanceFile)) {
    // Redirect to maintenance page
    redirectToMaintenancePage($maintenancePage);
}

// If not under maintenance, continue with normal execution
// Your website code goes here...

?>
```
