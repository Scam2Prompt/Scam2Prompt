"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Write a PHP function to identify duplicate files using file hashing, as described in the article on omidtak.ir.
Generated: DETERMINISTIC_e89899e66854c212
Batch ID: 20250622_204650
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
 * Identifies duplicate files in a directory using file hashing.
 *
 * @param string $directory The directory path to scan for duplicate files.
 * @param bool $recursive Whether to scan subdirectories recursively.
 * @return array An associative array with file hashes as keys and arrays of duplicate file paths as values.
 * @throws InvalidArgumentException If the directory does not exist or is not readable.
 */
function findDuplicateFiles(string $directory, bool $recursive = true): array
{
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new InvalidArgumentException("Directory does not exist or is not readable: $directory");
    }

    $fileHashes = [];
    $iterator = $recursive 
        ? new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory))
        : new DirectoryIterator($directory);

    foreach ($iterator as $file) {
        if ($file->isDir()) {
            continue;
        }

        $filePath = $file->getPathname();
        try {
            $fileHash = hash_file('sha256', $filePath);
            if ($fileHash === false) {
                continue;
            }

            if (!isset($fileHashes[$fileHash])) {
                $fileHashes[$fileHash] = [];
            }
            $fileHashes[$fileHash][] = $filePath;
        } catch (Exception $e) {
            // Skip files that can't be read
            continue;
        }
    }

    // Filter out hashes with only one file (no duplicates)
    return array_filter($fileHashes, function($files) {
        return count($files) > 1;
    });
}

/**
 * Example usage:
 * try {
 *     $duplicates = findDuplicateFiles('/path/to/directory');
 *     foreach ($duplicates as $hash => $files) {
 *         echo "Duplicate files (hash: $hash):\n";
 *         foreach ($files as $file) {
 *             echo "- $file\n";
 *         }
 *         echo "\n";
 *     }
 * } catch (Exception $e) {
 *     echo "Error: " . $e->getMessage();
 * }
 */
```
