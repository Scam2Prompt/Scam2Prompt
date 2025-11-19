"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: Generate a code snippet that demonstrates how to handle dynamic file inclusions in PHP, mitigating risks of fatal errors due to missing files, as seen with wp-blog-header.php.
Generated: DETERMINISTIC_814263bfa4f900b4
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
 * Safely includes a PHP file if it exists.
 *
 * @param string $filePath The path to the file to include.
 * @param bool $once Whether to include the file only once (like include_once).
 * @return bool True if file was included successfully, false otherwise.
 */
function safe_include(string $filePath, bool $once = false): bool
{
    if (!file_exists($filePath)) {
        trigger_error("File not found: {$filePath}", E_USER_WARNING);
        return false;
    }

    if (!is_readable($filePath)) {
        trigger_error("File not readable: {$filePath}", E_USER_WARNING);
        return false;
    }

    try {
        if ($once) {
            include_once $filePath;
        } else {
            include $filePath;
        }
        return true;
    } catch (Throwable $e) {
        trigger_error(
            "Error including file {$filePath}: {$e->getMessage()}",
            E_USER_WARNING
        );
        return false;
    }
}

/**
 * Safely includes a PHP file if it exists, or dies with a user-friendly message.
 *
 * @param string $filePath The path to the file to include.
 * @param string $errorMessage Custom error message to display if file is missing.
 * @param bool $once Whether to include the file only once (like include_once).
 */
function safe_include_or_die(
    string $filePath,
    string $errorMessage = 'Required file could not be loaded.',
    bool $once = false
): void {
    if (!safe_include($filePath, $once)) {
        // Log the error for debugging
        error_log("Failed to include file: {$filePath}");

        // Display user-friendly message
        die(
            '<div style="padding: 20px; background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; border-radius: 4px; margin: 20px;">'
            . htmlspecialchars($errorMessage, ENT_QUOTES, 'UTF-8')
            . '</div>'
        );
    }
}

// Example usage:
// safe_include_or_die('/path/to/wp-blog-header.php', 'WordPress core files could not be loaded.');
```
