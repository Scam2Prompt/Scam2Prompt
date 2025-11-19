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
/**
 * Checks if a required file exists before using the require function in PHP.
 *
 * @param string $filePath The path to the file to check.
 *
 * @return bool True if the file exists, false otherwise.
 */
function checkFileExists(string $filePath): bool
{
    // Check if the file path is not empty
    if (empty($filePath)) {
        throw new InvalidArgumentException('File path cannot be empty');
    }

    // Use file_exists to check if the file exists
    return file_exists($filePath);
}

/**
 * Requires a file if it exists.
 *
 * @param string $filePath The path to the file to require.
 *
 * @return void
 */
function requireIfExists(string $filePath): void
{
    try {
        // Check if the file exists
        if (checkFileExists($filePath)) {
            // If the file exists, require it
            require $filePath;
        } else {
            // If the file does not exist, throw a RuntimeException
            throw new RuntimeException("The file $filePath does not exist.");
        }
    } catch (Exception $e) {
        // Catch and log any exceptions
        error_log("Error requiring file $filePath: " . $e->getMessage());
        throw $e;
    }
}

// Example usage:
$filePath = 'path/to/your/file.php';
requireIfExists($filePath);
```
