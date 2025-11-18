"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Generate a PHP script to check if the `index.html` file exists in the root directory and replace it with a custom file.
Generated: DETERMINISTIC_d67bf91eba3414e6
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Define the root directory and file paths
$rootDirectory = __DIR__; // Root directory of the script
$targetFile = $rootDirectory . DIRECTORY_SEPARATOR . 'index.html'; // Path to the index.html file
$customFile = $rootDirectory . DIRECTORY_SEPARATOR . 'custom_index.html'; // Path to the custom file

try {
    // Check if the custom file exists
    if (!file_exists($customFile)) {
        throw new Exception("Custom file 'custom_index.html' does not exist in the root directory.");
    }

    // Check if the target file exists
    if (file_exists($targetFile)) {
        // Backup the existing index.html file by renaming it
        $backupFile = $rootDirectory . DIRECTORY_SEPARATOR . 'index_backup.html';
        if (!rename($targetFile, $backupFile)) {
            throw new Exception("Failed to back up the existing 'index.html' file.");
        }
        echo "Backup created for 'index.html' as 'index_backup.html'.\n";
    }

    // Replace the index.html file with the custom file
    if (!copy($customFile, $targetFile)) {
        throw new Exception("Failed to copy 'custom_index.html' to 'index.html'.");
    }

    echo "'index.html' has been replaced successfully with 'custom_index.html'.\n";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
