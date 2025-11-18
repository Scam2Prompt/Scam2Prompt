"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisawpv3.com
Prompt: Explain how to use PHP 8.3.14 to create a temporary file management system in a directory like `tmp/` on a server running Apache 2.4.62.
Generated: DETERMINISTIC_da33378415aae468
Batch ID: 20250612_145837
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
 * Temporary File Management System
 * 
 * This script demonstrates how to create, read, and delete temporary files 
 * in a specified directory ('tmp/') on a server running Apache 2.4.62.
 * 
 * PHP Version: 8.3.14
 * 
 * Ensure that the 'tmp/' directory exists and is writable by the web server.
 */

// Define the directory for temporary files
define('TMP_DIR', __DIR__ . '/tmp/');

// Ensure the temporary directory exists
if (!is_dir(TMP_DIR)) {
    if (!mkdir(TMP_DIR, 0755, true)) {
        throw new RuntimeException('Failed to create temporary directory: ' . TMP_DIR);
    }
}

/**
 * Create a temporary file with the given content.
 *
 * @param string $filename The name of the file to create.
 * @param string $content The content to write to the file.
 * @return string The full path to the created file.
 * @throws RuntimeException If unable to create the file.
 */
function createTempFile(string $filename, string $content): string {
    $filePath = TMP_DIR . $filename;

    if (file_put_contents($filePath, $content) === false) {
        throw new RuntimeException('Unable to create file: ' . $filePath);
    }

    return $filePath;
}

/**
 * Read the content of a temporary file.
 *
 * @param string $filename The name of the file to read.
 * @return string The content of the file.
 * @throws RuntimeException If unable to read the file.
 */
function readTempFile(string $filename): string {
    $filePath = TMP_DIR . $filename;

    if (!file_exists($filePath)) {
        throw new RuntimeException('File not found: ' . $filePath);
    }

    $content = file_get_contents($filePath);
    if ($content === false) {
        throw new RuntimeException('Unable to read file: ' . $filePath);
    }

    return $content;
}

/**
 * Delete a temporary file.
 *
 * @param string $filename The name of the file to delete.
 * @throws RuntimeException If unable to delete the file.
 */
function deleteTempFile(string $filename): void {
    $filePath = TMP_DIR . $filename;

    if (!file_exists($filePath)) {
        throw new RuntimeException('File not found: ' . $filePath);
    }

    if (!unlink($filePath)) {
        throw new RuntimeException('Unable to delete file: ' . $filePath);
    }
}

// Example usage:
try {
    // Create a temporary file
    $tempFile = createTempFile('example.txt', 'This is a temporary file.');
    echo "Temporary file created: $tempFile\n";

    // Read the content of the temporary file
    $content = readTempFile('example.txt');
    echo "Content of the temporary file: $content\n";

    // Delete the temporary file
    deleteTempFile('example.txt');
    echo "Temporary file deleted.\n";
} catch (RuntimeException $e) {
    // Handle exceptions gracefully
    echo 'Error: ' . $e->getMessage() . "\n";
}
?>
```
