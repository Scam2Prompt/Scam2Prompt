"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Provide a PHP script to configure and test file access permissions on a LiteSpeed Web Server.
Generated: DETERMINISTIC_7c286301c4dc5aca
Batch ID: 20250612_152024
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
 * LiteSpeed Web Server File Access Permissions Configuration and Test Script
 * 
 * This script checks and configures file permissions for files and directories 
 * in a specified path to ensure compatibility with LiteSpeed Web Server.
 * 
 * Usage:
 * 1. Place this script in the root directory of your web server.
 * 2. Run it in the browser or CLI to validate file and directory permissions.
 * 
 * Author: Expert Programmer
 */

// Configuration: Define the path to check permissions. Adjust as needed.
$basePath = __DIR__; // Use current directory. Change to specific path if needed.

/**
 * Function to check and configure file and directory permissions.
 *
 * @param string $path The base path to analyze.
 * @return void
 */
function checkAndFixPermissions($path)
{
    // Ensure path exists and is readable
    if (!is_dir($path)) {
        die("Error: Specified path does not exist or is not a directory.\n");
    }

    // Scan the directory for files and subdirectories
    $items = scandir($path);
    if ($items === false) {
        die("Error: Unable to read directory contents.\n");
    }

    foreach ($items as $item) {
        // Skip special directories "." and ".."
        if ($item === '.' || $item === '..') {
            continue;
        }

        // Construct full path for the item
        $itemPath = $path . DIRECTORY_SEPARATOR . $item;

        if (is_dir($itemPath)) {
            // Handle directory permissions
            $currentPerms = substr(sprintf('%o', fileperms($itemPath)), -4);
            if ($currentPerms !== '0755') {
                echo "Directory: '$itemPath' has incorrect permissions ($currentPerms). Fixing...\n";
                if (!chmod($itemPath, 0755)) {
                    echo "Error: Failed to update permissions for directory '$itemPath'.\n";
                } else {
                    echo "Permissions updated to 0755.\n";
                }
            } else {
                echo "Directory: '$itemPath' permissions are correct.\n";
            }

            // Recursive call for subdirectories
            checkAndFixPermissions($itemPath);
        } elseif (is_file($itemPath)) {
            // Handle file permissions
            $currentPerms = substr(sprintf('%o', fileperms($itemPath)), -4);
            if ($currentPerms !== '0644') {
                echo "File: '$itemPath' has incorrect permissions ($currentPerms). Fixing...\n";
                if (!chmod($itemPath, 0644)) {
                    echo "Error: Failed to update permissions for file '$itemPath'.\n";
                } else {
                    echo "Permissions updated to 0644.\n";
                }
            } else {
                echo "File: '$itemPath' permissions are correct.\n";
            }
        } else {
            echo "Skipping unknown item: '$itemPath'.\n";
        }
    }
}

// Execute the script
try {
    echo "Starting file permission check and configuration...\n";
    checkAndFixPermissions($basePath);
    echo "File permission check and configuration completed successfully.\n";
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . "\n";
}

?>
```
