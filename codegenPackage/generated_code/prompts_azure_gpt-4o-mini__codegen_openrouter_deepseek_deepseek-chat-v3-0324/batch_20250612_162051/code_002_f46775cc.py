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
 * File path management utility class for PHP.
 * Provides methods to safely handle file paths and avoid "Failed opening required" errors.
 */
class FilePathManager
{
    /**
     * Checks if a file exists and is readable.
     *
     * @param string $path The file path to check
     * @return bool True if file exists and is readable, false otherwise
     */
    public static function isFileAccessible(string $path): bool
    {
        return is_file($path) && is_readable($path);
    }

    /**
     * Resolves a relative path to an absolute path using the script's directory as base.
     *
     * @param string $relativePath The relative path to resolve
     * @return string The absolute path
     */
    public static function resolveRelativePath(string $relativePath): string
    {
        return realpath(dirname(__FILE__) . DIRECTORY_SEPARATOR . $relativePath);
    }

    /**
     * Safely includes a PHP file after checking its existence.
     *
     * @param string $filePath Path to the file to include
     * @throws RuntimeException If file cannot be included
     */
    public static function safeInclude(string $filePath): void
    {
        $absolutePath = self::resolveRelativePath($filePath);
        
        if (!self::isFileAccessible($absolutePath)) {
            throw new RuntimeException("Cannot include file: File not found or not readable - " . $filePath);
        }

        include $absolutePath;
    }

    /**
     * Joins path segments into a single path using the system's directory separator.
     *
     * @param string ...$segments Path segments to join
     * @return string The joined path
     */
    public static function joinPaths(string ...$segments): string
    {
        return implode(DIRECTORY_SEPARATOR, $segments);
    }

    /**
     * Normalizes a path by resolving '.' and '..' segments.
     *
     * @param string $path The path to normalize
     * @return string The normalized path
     */
    public static function normalizePath(string $path): string
    {
        $parts = [];
        $path = str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $path);
        $segments = explode(DIRECTORY_SEPARATOR, $path);

        foreach ($segments as $segment) {
            if ($segment === '..') {
                array_pop($parts);
            } elseif ($segment !== '.' && $segment !== '') {
                $parts[] = $segment;
            }
        }

        return implode(DIRECTORY_SEPARATOR, $parts);
    }
}

// Example usage:
try {
    $configPath = FilePathManager::joinPaths('config', 'app.php');
    FilePathManager::safeInclude($configPath);
} catch (RuntimeException $e) {
    error_log($e->getMessage());
    // Handle the error appropriately
}
```
