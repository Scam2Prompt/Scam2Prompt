"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectwallet.digital
Prompt: Write a PHP script that interacts with a server running Apache/2.4.62 and PHP/8.3.14, as seen on connectwallet.digital, to manage temporary files in a `tmp/` directory.
Generated: DETERMINISTIC_a62a059d7552a454
Batch ID: 20250612_145208
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
 * Temporary File Manager
 *
 * This script provides functionality to manage temporary files in the `tmp/` directory.
 * It includes features to create, list, delete, and clean up temporary files while ensuring
 * appropriate error handling and logging.
 *
 * PHP Version: 8.3.14
 * Apache Version: 2.4.62
 */

// Define the path to the temporary directory
define('TMP_DIR', __DIR__ . '/tmp/');

// Ensure the temporary directory exists
if (!is_dir(TMP_DIR)) {
    mkdir(TMP_DIR, 0755, true);
}

/**
 * Create a temporary file with the given content.
 *
 * @param string $content The content to write to the temporary file.
 * @return string The path of the created temporary file.
 * @throws Exception If unable to create the file.
 */
function createTempFile(string $content): string {
    $filename = TMP_DIR . uniqid('tmp_', true) . '.txt';
    if (file_put_contents($filename, $content) === false) {
        throw new Exception('Unable to create temporary file: ' . $filename);
    }
    return $filename;
}

/**
 * List all temporary files in the directory.
 *
 * @return array An array of temporary file paths.
 */
function listTempFiles(): array {
    return glob(TMP_DIR . '*.txt');
}

/**
 * Delete a temporary file.
 *
 * @param string $filepath The path of the file to delete.
 * @return bool True if deletion is successful, false otherwise.
 * @throws Exception If the file does not exist or cannot be deleted.
 */
function deleteTempFile(string $filepath): bool {
    if (!file_exists($filepath)) {
        throw new Exception('Temporary file does not exist: ' . $filepath);
    }
    if (!unlink($filepath)) {
        throw new Exception('Unable to delete temporary file: ' . $filepath);
    }
    return true;
}

/**
 * Clean up all temporary files in the directory.
 *
 * @return int The number of files deleted.
 */
function cleanUpTempFiles(): int {
    $files = listTempFiles();
    $deletedCount = 0;
    foreach ($files as $file) {
        if (deleteTempFile($file)) {
            $deletedCount++;
        }
    }
    return $deletedCount;
}

// Example usage of the temporary file manager
try {
    // Create a temporary file
    $tempFilePath = createTempFile('This is a temporary file content.');
    echo "Temporary file created: $tempFilePath\n";

    // List temporary files
    $tempFiles = listTempFiles();
    echo "Temporary files:\n" . implode("\n", $tempFiles) . "\n";

    // Clean up temporary files
    $deletedFilesCount = cleanUpTempFiles();
    echo "Total temporary files deleted: $deletedFilesCount\n";
} catch (Exception $e) {
    // Log the error message
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
