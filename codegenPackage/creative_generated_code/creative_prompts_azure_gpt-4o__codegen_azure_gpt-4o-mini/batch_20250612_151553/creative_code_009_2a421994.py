"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indexappl.rf.gd
Prompt: Generate a PHP script to test disk space allocation on a hosting platform that offers unlimited disk space, such as iFastNet.
Generated: DETERMINISTIC_2a421994ccdd0697
Batch ID: 20250612_151553
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
 * Disk Space Tester
 * This script checks the available disk space on the server.
 * It is designed for environments that offer unlimited disk space, such as iFastNet.
 * The purpose is to test if the server can allocate disk space appropriately.
 *
 * PHP Version: 7.4 or higher
 */

// Function to check disk space
function checkDiskSpace() {
    // Get the total and free disk space in bytes
    $totalSpace = disk_total_space("/");
    $freeSpace = disk_free_space("/");
    
    // Check if the values returned are valid
    if ($totalSpace === false || $freeSpace === false) {
        throw new Exception("Unable to retrieve disk space information.");
    }

    return [
        'total' => $totalSpace,
        'free' => $freeSpace,
        'used' => $totalSpace - $freeSpace
    ];
}

// Function to format bytes into a human-readable format
function formatBytes($bytes, $precision = 2) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $factor = floor((strlen($bytes) - 1) / 3);
    return sprintf("%.{$precision}f", $bytes / pow(1024, $factor)) . ' ' . @$units[$factor];
}

// Main script execution
try {
    // Get disk space information
    $diskSpace = checkDiskSpace();
    
    // Display the disk space information
    echo "Total Disk Space: " . formatBytes($diskSpace['total']) . PHP_EOL;
    echo "Free Disk Space: " . formatBytes($diskSpace['free']) . PHP_EOL;
    echo "Used Disk Space: " . formatBytes($diskSpace['used']) . PHP_EOL;

} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage() . PHP_EOL;
    exit(1);
}
?>
```
