"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.com-live.org
Prompt: Write a PHP script to parse and display the directory structure served by Apache/2.4.52, including file names, sizes, and descriptions.
Generated: DETERMINISTIC_38be75e3ca78387a
Batch ID: 20250612_155006
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
 * Directory Structure Parser
 * 
 * This script scans the specified directory and displays its structure,
 * including file names, sizes, and descriptions. It is designed to be 
 * run in an Apache server environment.
 */

// Set the directory to be scanned
$directoryPath = __DIR__; // Current directory

/**
 * Function to format file size in human-readable format
 *
 * @param int $bytes - Size in bytes
 * @param int $decimals - Number of decimal points
 * @return string - Formatted file size
 */
function formatSize($bytes, $decimals = 2) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $factor = floor((strlen($bytes) - 1) / 3);
    return sprintf("%.{$decimals}f", $bytes / pow(1024, $factor)) . ' ' . $units[$factor];
}

/**
 * Function to scan and display the directory structure
 *
 * @param string $dir - The directory path
 */
function displayDirectoryStructure($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        echo "Error: The specified path is not a directory.";
        return;
    }

    // Scan the directory and filter out the current and parent directory references
    $files = array_diff(scandir($dir), ['..', '.']);
    
    if (empty($files)) {
        echo "No files found in the directory.";
        return;
    }

    echo "<h2>Directory Structure of: " . htmlspecialchars($dir) . "</h2>";
    echo "<ul>";
    
    foreach ($files as $file) {
        $filePath = $dir . DIRECTORY_SEPARATOR . $file;

        // Get file size and check if it's a directory
        if (is_file($filePath)) {
            $fileSize = formatSize(filesize($filePath));
            $description = 'File';
        } elseif (is_dir($filePath)) {
            $fileSize = '-';
            $description = 'Directory';
        } else {
            $fileSize = '-';
            $description = 'Unknown';
        }

        // Display file information
        echo "<li>";
        echo "<strong>" . htmlspecialchars($file) . "</strong> - Size: " . $fileSize . " - Description: " . $description;
        echo "</li>";
    }

    echo "</ul>";
}

// Call the function to display the directory structure
displayDirectoryStructure($directoryPath);

?>
```
