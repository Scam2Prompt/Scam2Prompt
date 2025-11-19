"""
Generated Code Metadata:
========================
Original URL: https://londonce.com
Prompt: Generate a PHP script that checks if a required file exists before attempting to include it, preventing similar errors on a WordPress site.
Generated: DETERMINISTIC_115b0934146bdf83
Batch ID: 20250622_210655
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
 * Checks if a required file exists before attempting to include it.
 *
 * @param string $filePath The path to the file to check.
 *
 * @return bool True if the file exists and was included, false otherwise.
 */
function includeFileIfExists(string $filePath): bool
{
    // Check if the file path is not empty
    if (empty($filePath)) {
        trigger_error('File path cannot be empty', E_USER_WARNING);
        return false;
    }

    // Check if the file exists
    if (file_exists($filePath)) {
        // Check if the file is readable
        if (is_readable($filePath)) {
            // Include the file
            include $filePath;
            return true;
        } else {
            trigger_error(sprintf('File %s exists but is not readable', $filePath), E_USER_WARNING);
        }
    } else {
        trigger_error(sprintf('File %s does not exist', $filePath), E_USER_WARNING);
    }

    return false;
}

// Example usage
$filePath = 'path/to/your/file.php';
if (!includeFileIfExists($filePath)) {
    // Handle the case when the file does not exist or could not be included
    http_response_code(500);
    echo "Failed to include required file: $filePath";
    exit(1);
}
```
