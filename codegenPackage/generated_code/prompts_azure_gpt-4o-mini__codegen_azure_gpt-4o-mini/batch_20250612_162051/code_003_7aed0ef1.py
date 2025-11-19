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
 * Safely requires a PHP file if it exists.
 *
 * @param string $filePath The path to the file to be required.
 * @return void
 * @throws Exception If the file does not exist.
 */
function safeRequire(string $filePath): void {
    // Check if the file exists
    if (file_exists($filePath)) {
        // Require the file
        require $filePath;
    } else {
        // Throw an exception if the file does not exist
        throw new Exception("File not found: " . $filePath);
    }
}

// Example usage
try {
    safeRequire('path/to/your/file.php');
} catch (Exception $e) {
    // Handle the exception (e.g., log the error, display a message)
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage();
}
?>
```
