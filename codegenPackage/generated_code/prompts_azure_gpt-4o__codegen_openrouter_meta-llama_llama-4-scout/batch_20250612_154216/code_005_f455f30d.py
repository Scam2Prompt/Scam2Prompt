"""
Generated Code Metadata:
========================
Original URL: https://perurest.com
Prompt: Write a PHP script to dynamically display directory contents served by LiteSpeed Web Server in a user-friendly format.
Generated: DETERMINISTIC_f455f30dc6e35bca
Batch ID: 20250612_154216
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
 * Dynamically displays directory contents served by LiteSpeed Web Server in a user-friendly format.
 */

// Configuration
$rootDir = '.'; // Current directory

try {
    // Check if the directory exists
    if (!file_exists($rootDir)) {
        throw new Exception("The directory '$rootDir' does not exist.");
    }

    // Check if the path is a directory
    if (!is_dir($rootDir)) {
        throw new Exception("'$rootDir' is not a directory.");
    }

    // Check for .htaccess or other restrictions
    if (file_exists($rootDir . '/.htaccess')) {
        // Handle .htaccess restrictions or display a message
        echo "Directory '$rootDir' has a .htaccess file. Access may be restricted.\n";
    }

    // Scan the directory
    $dirContents = scandir($rootDir);

    // Filter out . and ..
    $dirContents = array_filter($dirContents, function ($item) {
        return $item !== '.' && $item !== '..';
    });

    // Sort directory contents
    sort($dirContents);

    // Display directory contents in a user-friendly format
    echo "Directory Contents of $rootDir:\n";
    echo "-----------------------------------\n";
    echo "| Type  | Name                  |\n";
    echo "-----------------------------------\n";

    foreach ($dirContents as $item) {
        $itemPath = $rootDir . DIRECTORY_SEPARATOR . $item;
        if (is_dir($itemPath)) {
            echo "| Dir   | $item                  |\n";
        } elseif (is_file($itemPath)) {
            echo "| File  | $item                  |\n";
        } else {
            echo "| Unknown| $item                  |\n";
        }
    }

    echo "-----------------------------------\n";

} catch (Exception $e) {
    http_response_code(500);
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
