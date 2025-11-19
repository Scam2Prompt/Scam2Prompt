"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Write a code snippet to list files in a directory using PHP, referencing the structure seen in the nkftransporte.com index page.
Generated: DETERMINISTIC_9ee4714d21d5ceb1
Batch ID: 20250612_155436
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
 * Lists files in a directory with error handling and security checks.
 * Mimics the structure seen in nkftransporte.com index page.
 *
 * @param string $directory The directory path to scan
 * @return array|false Array of files or false on error
 */
function listDirectoryFiles($directory) {
    // Validate input
    if (!is_string($directory) || trim($directory) === '') {
        trigger_error('Invalid directory path provided', E_USER_WARNING);
        return false;
    }

    // Sanitize directory path
    $directory = rtrim($directory, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;

    // Check if directory exists and is readable
    if (!is_dir($directory) || !is_readable($directory)) {
        trigger_error("Directory does not exist or is not readable: $directory", E_USER_WARNING);
        return false;
    }

    try {
        // Scan directory
        $files = scandir($directory);
        
        if ($files === false) {
            throw new RuntimeException("Failed to scan directory: $directory");
        }

        // Filter out . and .. entries
        $files = array_diff($files, ['.', '..']);

        // Sort files alphabetically
        sort($files);

        return $files;
    } catch (Exception $e) {
        trigger_error($e->getMessage(), E_USER_WARNING);
        return false;
    }
}

// Example usage:
$directory = __DIR__; // Current directory
$files = listDirectoryFiles($directory);

if ($files !== false) {
    echo "<h2>Files in directory:</h2>\n";
    echo "<ul>\n";
    foreach ($files as $file) {
        echo "    <li>$file</li>\n";
    }
    echo "</ul>\n";
} else {
    echo "<p>Error: Could not list directory contents.</p>\n";
}
?>
```
