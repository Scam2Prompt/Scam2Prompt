"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: How can I troubleshoot the "Failed to open stream: No such file or directory" error in PHP when including files?
Generated: DETERMINISTIC_58addea475f6203d
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
 * Safely includes a PHP file with proper error handling.
 *
 * @param string $filePath The path to the file to include
 * @return bool True if file was included successfully, false otherwise
 * @throws RuntimeException If file cannot be included
 */
function safeInclude($filePath) {
    // Check if file exists and is readable
    if (!file_exists($filePath)) {
        error_log("File not found: " . $filePath);
        return false;
    }

    if (!is_readable($filePath)) {
        error_log("File not readable: " . $filePath);
        return false;
    }

    // Include the file with error suppression and check for inclusion success
    $included = @include $filePath;
    if ($included === false) {
        $error = error_get_last();
        throw new RuntimeException("Failed to include file: " . $filePath . " - " . ($error['message'] ?? 'Unknown error'));
    }

    return true;
}

/**
 * Resolves a file path relative to a base directory.
 *
 * @param string $baseDir The base directory path
 * @param string $relativePath The relative file path
 * @return string The resolved absolute path
 * @throws InvalidArgumentException If paths are invalid
 */
function resolvePath($baseDir, $relativePath) {
    if (!is_dir($baseDir)) {
        throw new InvalidArgumentException("Base directory does not exist: " . $baseDir);
    }

    $resolvedPath = realpath($baseDir . DIRECTORY_SEPARATOR . $relativePath);
    if ($resolvedPath === false) {
        throw new InvalidArgumentException("Could not resolve path: " . $relativePath . " relative to " . $baseDir);
    }

    return $resolvedPath;
}

// Example usage:
try {
    $baseDir = __DIR__; // Current script directory
    $fileToInclude = 'config/settings.php';
    
    $absolutePath = resolvePath($baseDir, $fileToInclude);
    if (safeInclude($absolutePath)) {
        // File was included successfully
        echo "File included successfully: " . $absolutePath;
    }
} catch (Exception $e) {
    error_log("Error including file: " . $e->getMessage());
    // Handle the error appropriately (e.g., show user-friendly message)
    echo "An error occurred while loading required files. Please try again later.";
}
?>
```
