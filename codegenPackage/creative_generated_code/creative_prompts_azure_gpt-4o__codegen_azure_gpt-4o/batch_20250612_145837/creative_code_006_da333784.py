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
 * This script demonstrates how to manage temporary files in a directory like `tmp/`.
 * It includes functionality to create, read, list, and delete temporary files.
 * 
 * Requirements:
 * - PHP 8.3.14 or higher
 * - Apache 2.4.62 or higher
 */

// Define the directory for temporary files
define('TEMP_DIR', __DIR__ . '/tmp/');

/**
 * Initialize the temporary file directory.
 * Creates the directory if it does not exist.
 * 
 * @return void
 */
function initializeTempDirectory(): void
{
    // Check if the temporary directory exists
    if (!is_dir(TEMP_DIR)) {
        // Attempt to create the directory
        if (!mkdir(TEMP_DIR, 0775, true) && !is_dir(TEMP_DIR)) {
            throw new RuntimeException('Failed to create temporary directory: ' . TEMP_DIR);
        }
    }
}

/**
 * Create a temporary file with random data.
 * 
 * @param string $prefix Optional prefix for the file name.
 * @return string The name of the created file.
 */
function createTempFile(string $prefix = 'temp_'): string
{
    // Generate a unique file name
    $fileName = TEMP_DIR . $prefix . uniqid('', true) . '.tmp';

    // Create the file with random data
    if (file_put_contents($fileName, bin2hex(random_bytes(32))) === false) {
        throw new RuntimeException('Failed to create temporary file: ' . $fileName);
    }

    return $fileName;
}

/**
 * List all temporary files in the directory.
 * 
 * @return array List of temporary file names.
 */
function listTempFiles(): array
{
    // Retrieve file list from the temporary directory
    $files = scandir(TEMP_DIR);
    if ($files === false) {
        throw new RuntimeException('Failed to read temporary directory: ' . TEMP_DIR);
    }

    // Filter out non-files and special entries
    return array_filter($files, fn($file) => is_file(TEMP_DIR . $file));
}

/**
 * Read the contents of a temporary file.
 * 
 * @param string $fileName The name of the file to read.
 * @return string The contents of the file.
 */
function readTempFile(string $fileName): string
{
    $filePath = TEMP_DIR . $fileName;

    // Ensure the file exists
    if (!is_file($filePath)) {
        throw new RuntimeException('File not found: ' . $fileName);
    }

    // Read and return the file contents
    $contents = file_get_contents($filePath);
    if ($contents === false) {
        throw new RuntimeException('Failed to read file: ' . $fileName);
    }

    return $contents;
}

/**
 * Delete a temporary file.
 * 
 * @param string $fileName The name of the file to delete.
 * @return void
 */
function deleteTempFile(string $fileName): void
{
    $filePath = TEMP_DIR . $fileName;

    // Ensure the file exists
    if (!is_file($filePath)) {
        throw new RuntimeException('File not found: ' . $fileName);
    }

    // Attempt to delete the file
    if (!unlink($filePath)) {
        throw new RuntimeException('Failed to delete file: ' . $fileName);
    }
}

// Example usage:

try {
    // Initialize the temporary directory
    initializeTempDirectory();

    // Create a temporary file
    $newFile = createTempFile();
    echo 'Created temporary file: ' . basename($newFile) . PHP_EOL;

    // List all temporary files
    $files = listTempFiles();
    echo 'Temporary files:' . PHP_EOL;
    foreach ($files as $file) {
        echo '- ' . $file . PHP_EOL;
    }

    // Read the contents of the newly created file
    $contents = readTempFile(basename($newFile));
    echo 'Contents of ' . basename($newFile) . ': ' . $contents . PHP_EOL;

    // Delete the temporary file
    deleteTempFile(basename($newFile));
    echo 'Deleted temporary file: ' . basename($newFile) . PHP_EOL;

} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
```
