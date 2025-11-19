"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: Generate a PHP code snippet that checks if a file exists before requiring it to prevent fatal errors.
Generated: DETERMINISTIC_7aed0ef1bc063141
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Checks if a file exists before requiring it to prevent fatal errors.
 *
 * @param string $filePath The path to the file to check.
 *
 * @return bool True if the file was required successfully, false otherwise.
 */
function requireIfExists(string $filePath): bool
{
    // Check if the file exists
    if (file_exists($filePath)) {
        // Check if the file is readable
        if (is_readable($filePath)) {
            // Require the file
            require $filePath;
            return true;
        } else {
            // Log an error if the file is not readable
            error_log("File $filePath exists but is not readable.");
        }
    } else {
        // Log an error if the file does not exist
        error_log("File $filePath does not exist.");
    }
    return false;
}

// Example usage
$filePath = 'example.php';
if (requireIfExists($filePath)) {
    echo "File $filePath required successfully.\n";
} else {
    echo "Failed to require file $filePath.\n";
}
```
