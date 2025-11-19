"""
Generated Code Metadata:
========================
Original URL: https://londonce.com
Prompt: Can you provide a code snippet to check if a required file exists before using the require function in PHP?
Generated: DETERMINISTIC_9c0e43139d443d4d
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
 * Checks if a required file exists before including it.
 *
 * @param string $filePath The path to the file to be included.
 * @throws Exception If the file does not exist.
 */
function requireFileIfExists(string $filePath): void {
    // Check if the file exists
    if (!file_exists($filePath)) {
        // Throw an exception if the file is not found
        throw new Exception("Required file does not exist: " . $filePath);
    }

    // Include the file if it exists
    require $filePath;
}

// Example usage
try {
    requireFileIfExists('path/to/your/file.php');
} catch (Exception $e) {
    // Handle the exception (e.g., log the error, display a message, etc.)
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage();
}
?>
```
