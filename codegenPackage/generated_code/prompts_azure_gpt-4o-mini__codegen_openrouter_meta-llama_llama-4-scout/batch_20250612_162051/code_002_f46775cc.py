"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: What are the best practices for managing file paths in PHP to avoid fatal errors like "Failed opening required"?
Generated: DETERMINISTIC_f46775ccd9a5392a
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
 * FilePathManager class to handle file paths in a secure and efficient manner.
 */
class FilePathManager
{
    /**
     * Returns the absolute path of a given file path.
     *
     * @param string $filePath The file path to convert to absolute path.
     *
     * @return string The absolute file path.
     */
    public static function getAbsolutePath($filePath)
    {
        // Use realpath to eliminate any symlinks and get the absolute path
        $absolutePath = realpath($filePath);

        // Check if the file exists
        if ($absolutePath === false) {
            throw new Exception("File not found: $filePath");
        }

        return $absolutePath;
    }

    /**
     * Checks if a file is required and includes it if it exists.
     *
     * @param string $filePath The file path to check and include.
     *
     * @return bool True if the file was included successfully, false otherwise.
     */
    public static function requireFile($filePath)
    {
        try {
            $absolutePath = self::getAbsolutePath($filePath);
            require $absolutePath;
            return true;
        } catch (Exception $e) {
            // Log the error or handle it as per your application
            error_log("Error requiring file: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Checks if a file exists and includes it if it exists.
     *
     * @param string $filePath The file path to check and include.
     *
     * @return bool True if the file was included successfully, false otherwise.
     */
    public static function includeFile($filePath)
    {
        try {
            $absolutePath = self::getAbsolutePath($filePath);
            include $absolutePath;
            return true;
        } catch (Exception $e) {
            // Log the error or handle it as per your application
            error_log("Error including file: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage
$filePath = 'path/to/your/file.php';

if (FilePathManager::requireFile($filePath)) {
    echo "File required successfully: $filePath\n";
} else {
    echo "Failed to require file: $filePath\n";
}

if (FilePathManager::includeFile($filePath)) {
    echo "File included successfully: $filePath\n";
} else {
    echo "Failed to include file: $filePath\n";
}
```
