"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robilliardag.com
Prompt: Create a PHP function that sorts files by their last modified date, similar to the listing on robilliardag.com.
Generated: DETERMINISTIC_1c2c7166d0ada330
Batch ID: 20250612_161209
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
 * Sorts files in a specified directory by their last modified date.
 * 
 * @param string $directoryPath The path to the directory containing the files.
 * @return array Sorted array of file paths by last modified date (newest first).
 * @throws Exception If the directory cannot be opened or is invalid.
 */
function sortFilesByModifiedDate($directoryPath) {
    // Ensure the directory exists and is readable
    if (!is_dir($directoryPath) || !is_readable($directoryPath)) {
        throw new Exception("Invalid or unreadable directory: $directoryPath");
    }

    // Open the directory
    $dirHandle = opendir($directoryPath);
    if ($dirHandle === false) {
        throw new Exception("Failed to open directory: $directoryPath");
    }

    $files = [];
    
    // Read files from the directory
    while (($file = readdir($dirHandle)) !== false) {
        $filePath = $directoryPath . DIRECTORY_SEPARATOR . $file;

        // Skip directories and hidden files
        if (is_file($filePath) && substr($file, 0, 1) !== '.') {
            $files[$filePath] = filemtime($filePath); // Store filepath and last modified timestamp
        }
    }

    // Close the directory handle
    closedir($dirHandle);

    // Sort files by last modified date, newest first
    arsort($files);

    // Return sorted file paths
    return array_keys($files);
}

// Example Usage:
// $sortedFiles = sortFilesByModifiedDate('/path/to/directory');
// print_r($sortedFiles);
?>
```
