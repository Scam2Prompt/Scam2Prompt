"""
Generated Code Metadata:
========================
Original URL: https://connectwallet.digital
Prompt: Write a PHP script that interacts with a server running Apache/2.4.62 and PHP/8.3.14, as seen on connectwallet.digital, to manage temporary files in a `tmp/` directory.
Generated: DETERMINISTIC_a62a059d7552a454
Batch ID: 20250612_145208
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
 * Temporary File Manager
 * 
 * This script manages temporary files in a specified 'tmp/' directory.
 * It allows for creating, listing, and deleting temporary files.
 * 
 * PHP Version: 8.3.14
 * Server: Apache/2.4.62
 */

// Define the path to the temporary directory
define('TMP_DIR', __DIR__ . '/tmp/');

// Ensure the temporary directory exists
if (!is_dir(TMP_DIR)) {
    if (!mkdir(TMP_DIR, 0755, true)) {
        die('Failed to create temporary directory: ' . TMP_DIR);
    }
}

/**
 * Create a temporary file with a unique name
 * 
 * @return string The path to the created temporary file
 * @throws Exception If the file cannot be created
 */
function createTempFile(): string {
    $tempFile = TMP_DIR . uniqid('temp_', true) . '.tmp';
    if (file_put_contents($tempFile, '') === false) {
        throw new Exception('Unable to create temporary file: ' . $tempFile);
    }
    return $tempFile;
}

/**
 * List all temporary files in the directory
 * 
 * @return array An array of temporary file names
 */
function listTempFiles(): array {
    return array_values(array_filter(scandir(TMP_DIR), function($file) {
        return preg_match('/^temp_.*\.tmp$/', $file);
    }));
}

/**
 * Delete a specified temporary file
 * 
 * @param string $filename The name of the file to delete
 * @throws Exception If the file cannot be deleted
 */
function deleteTempFile(string $filename): void {
    $filePath = TMP_DIR . $filename;
    if (!file_exists($filePath)) {
        throw new Exception('File not found: ' . $filePath);
    }
    if (!unlink($filePath)) {
        throw new Exception('Unable to delete temporary file: ' . $filePath);
    }
}

// Example usage
try {
    // Create a temporary file
    $newFile = createTempFile();
    echo "Created temporary file: $newFile\n";

    // List temporary files
    $files = listTempFiles();
    echo "Temporary files:\n" . implode("\n", $files) . "\n";

    // Delete the created temporary file
    deleteTempFile(basename($newFile));
    echo "Deleted temporary file: " . basename($newFile) . "\n";

} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo 'Error: ' . $e->getMessage() . "\n";
}
?>
```
