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
<?php
/**
 * Safely includes a PHP file if it exists.
 *
 * @param string $filePath The path to the file to be included.
 * @return bool Returns true if the file was included successfully, false otherwise.
 */
function safe_require($filePath) {
    if (file_exists($filePath) && is_file($filePath)) {
        require_once $filePath;
        return true;
    }
    return false;
}

/**
 * Safely includes a PHP file if it exists, with error handling.
 *
 * @param string $filePath The path to the file to be included.
 * @return bool Returns true if the file was included successfully, false otherwise.
 * @throws RuntimeException If the file exists but cannot be included.
 */
function safe_require_with_error_handling($filePath) {
    if (!file_exists($filePath)) {
        return false;
    }

    if (!is_file($filePath)) {
        throw new RuntimeException("Path is not a file: $filePath");
    }

    try {
        require_once $filePath;
        return true;
    } catch (Exception $e) {
        throw new RuntimeException("Failed to include file: $filePath", 0, $e);
    }
}
```
