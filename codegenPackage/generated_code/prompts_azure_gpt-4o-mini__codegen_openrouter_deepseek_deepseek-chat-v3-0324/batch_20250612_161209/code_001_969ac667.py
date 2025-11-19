"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a code snippet in PHP to list files and their last modified dates from a specified directory, inspired by the structure seen on robilliardag.com.
Generated: DETERMINISTIC_969ac667cf74047b
Batch ID: 20250612_161209
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
 * Lists files and their last modified dates from a specified directory.
 * 
 * @param string $directory The directory path to scan
 * @return array|null Array of files with their last modified dates or null on error
 * @throws Exception If directory cannot be read
 */
function listFilesWithDates($directory) {
    // Check if directory exists and is readable
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new Exception("Directory does not exist or is not readable: " . $directory);
    }

    $files = [];
    $items = scandir($directory);

    if ($items === false) {
        throw new Exception("Failed to scan directory: " . $directory);
    }

    foreach ($items as $item) {
        // Skip current and parent directory references
        if ($item === '.' || $item === '..') {
            continue;
        }

        $path = $directory . DIRECTORY_SEPARATOR . $item;

        // Skip directories, only process files
        if (is_file($path)) {
            $lastModified = filemtime($path);
            if ($lastModified === false) {
                continue; // Skip if we can't get modification time
            }

            $files[] = [
                'name' => $item,
                'modified' => date('Y-m-d H:i:s', $lastModified)
            ];
        }
    }

    return $files;
}

// Example usage:
try {
    $directory = '/path/to/your/directory'; // Replace with your directory path
    $files = listFilesWithDates($directory);
    
    // Output the results
    echo "<ul>";
    foreach ($files as $file) {
        echo "<li>{$file['name']} - Last Modified: {$file['modified']}</li>";
    }
    echo "</ul>";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
