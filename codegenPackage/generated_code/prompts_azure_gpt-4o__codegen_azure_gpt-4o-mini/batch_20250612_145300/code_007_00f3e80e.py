"""
Generated Code Metadata:
========================
Original URL: https://siemensgamesare.great-site.net
Prompt: Develop a PHP-based tool to monitor disk space usage on a hosting platform that offers unlimited disk space and modern cPanel, as highlighted by iFastNet.
Generated: DETERMINISTIC_00f3e80eebf47aac
Batch ID: 20250612_145300
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
 * Disk Space Monitor Tool
 * This script monitors disk space usage on a hosting platform with unlimited disk space.
 * It retrieves the disk usage information from the server and displays it in a user-friendly format.
 * 
 * PHP Version: 7.4 or higher
 * 
 * @package DiskSpaceMonitor
 * @author Your Name
 * @license MIT
 */

// Set the timezone to UTC
date_default_timezone_set('UTC');

/**
 * Function to get disk space usage
 *
 * @return array|false Returns an associative array with total and free disk space, or false on failure
 */
function getDiskSpaceUsage() {
    // Check if the function is available
    if (!function_exists('disk_total_space') || !function_exists('disk_free_space')) {
        error_log("Required disk functions are not available.");
        return false;
    }

    // Get the total and free disk space
    $totalSpace = disk_total_space("/");
    $freeSpace = disk_free_space("/");

    // Check for errors in retrieving disk space
    if ($totalSpace === false || $freeSpace === false) {
        error_log("Failed to retrieve disk space information.");
        return false;
    }

    // Calculate used space
    $usedSpace = $totalSpace - $freeSpace;

    // Return the disk space usage as an associative array
    return [
        'total' => $totalSpace,
        'used' => $usedSpace,
        'free' => $freeSpace,
        'percentage_used' => ($usedSpace / $totalSpace) * 100,
    ];
}

/**
 * Function to format bytes into a human-readable format
 *
 * @param int $bytes The number of bytes
 * @param int $decimals The number of decimal points to display
 * @return string Human-readable format of bytes
 */
function formatBytes($bytes, $decimals = 2) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $factor = floor((strlen($bytes) - 1) / 3);
    return sprintf("%.{$decimals}f", $bytes / pow(1024, $factor)) . ' ' . @$units[$factor];
}

// Main execution
try {
    $diskUsage = getDiskSpaceUsage();

    if ($diskUsage === false) {
        throw new Exception("Unable to retrieve disk space usage.");
    }

    // Display the disk space usage
    echo "<h1>Disk Space Usage</h1>";
    echo "<p>Total Disk Space: " . formatBytes($diskUsage['total']) . "</p>";
    echo "<p>Used Disk Space: " . formatBytes($diskUsage['used']) . "</p>";
    echo "<p>Free Disk Space: " . formatBytes($diskUsage['free']) . "</p>";
    echo "<p>Percentage Used: " . round($diskUsage['percentage_used'], 2) . "%</p>";

} catch (Exception $e) {
    // Log the error message
    error_log($e->getMessage());
    echo "<p>Error: Unable to retrieve disk space information. Please try again later.</p>";
}
?>
```
