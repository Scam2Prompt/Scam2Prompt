"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Write a PHP function to detect duplicate files on a server using file hashing, similar to the method described on Omidtak.ir for identifying duplicate files with hash values.
Generated: DETERMINISTIC_9dc910e50d60b83f
Batch ID: 20250612_142628
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
 * Detect duplicate files on a server using file hashing.
 * 
 * This function scans the specified directory recursively,
 * calculates hash values for each file, and identifies duplicates.
 * 
 * @param string $directory The root directory to scan for duplicate files.
 * @param string $hashAlgorithm The hashing algorithm to use (e.g., 'md5', 'sha256').
 * 
 * @return array Returns an associative array where keys are hash values
 *               and values are arrays of file paths with identical content.
 * 
 * @throws InvalidArgumentException If the directory does not exist or is not readable.
 */
function detectDuplicateFiles(string $directory, string $hashAlgorithm = 'md5'): array
{
    // Validate directory
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new InvalidArgumentException("The specified directory is invalid or not readable: $directory");
    }

    // Array to store files grouped by hash values
    $hashToFileMap = [];

    /**
     * Recursive function to scan files in a directory.
     * 
     * @param string $dirPath The directory path to scan.
     */
    function scanDirectory(string $dirPath) use (&$hashToFileMap, $hashAlgorithm)
    {
        // Get all files and directories inside the current directory
        $items = scandir($dirPath);

        foreach ($items as $item) {
            if ($item === '.' || $item === '..') {
                continue; // Skip special directory entries
            }

            $itemPath = $dirPath . DIRECTORY_SEPARATOR . $item;

            if (is_dir($itemPath)) {
                // Recursively scan subdirectories
                scanDirectory($itemPath);
            } elseif (is_file($itemPath) && is_readable($itemPath)) {
                // Calculate the hash of the file content
                $hash = hash_file($hashAlgorithm, $itemPath);

                // Group files by their hash value
                if (!isset($hashToFileMap[$hash])) {
                    $hashToFileMap[$hash] = [];
                }
                $hashToFileMap[$hash][] = $itemPath;
            }
        }
    }

    // Begin scanning the directory
    scanDirectory($directory);

    // Filter out hash groups with only one file (no duplicates)
    $duplicates = array_filter($hashToFileMap, fn($files) => count($files) > 1);

    return $duplicates;
}

// Example usage:
try {
    $directory = '/path/to/your/directory';
    $duplicates = detectDuplicateFiles($directory, 'sha256');
    
    // Output duplicate files
    foreach ($duplicates as $hash => $files) {
        echo "Duplicate files (Hash: $hash):\n";
        foreach ($files as $file) {
            echo " - $file\n";
        }
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}

?>
```
