"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Write a PHP function to identify duplicate files using file hashing as described on Omidtak's website.
Generated: DETERMINISTIC_bfc7bdf8ba5f26f5
Batch ID: 20250612_163625
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
 * Identify duplicate files in a given directory using file hashing.
 * 
 * This function scans a directory and its subdirectories for duplicate files
 * by comparing their hash values. It returns an array detailing the duplicates.
 * 
 * @param string $directory Path to the directory to scan for duplicate files.
 * @param string $hashAlgorithm Hashing algorithm to use (default: sha256).
 * @return array An associative array where the keys are hash values and the values are arrays of duplicate file paths.
 * @throws InvalidArgumentException If the provided directory path is invalid.
 */
function findDuplicateFiles(string $directory, string $hashAlgorithm = 'sha256'): array
{
    // Validate the directory path
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The provided directory path '$directory' is invalid.");
    }

    $fileHashes = []; // Array to store file hashes and their corresponding paths
    $duplicates = []; // Array to store duplicate files

    /**
     * Recursively scans a directory and hashes its files.
     * 
     * @param string $dir Current directory being scanned.
     */
    $scanDirectory = function (string $dir) use (&$fileHashes, $hashAlgorithm) {
        $items = scandir($dir);
        if ($items === false) {
            throw new RuntimeException("Failed to read directory '$dir'.");
        }

        foreach ($items as $item) {
            // Skip special directories "." and ".."
            if ($item === '.' || $item === '..') {
                continue;
            }

            $path = $dir . DIRECTORY_SEPARATOR . $item;

            if (is_dir($path)) {
                // Recursively scan subdirectories
                ($this)($path);
            } elseif (is_file($path)) {
                // Compute hash of the file
                $hash = hash_file($hashAlgorithm, $path);
                if ($hash === false) {
                    throw new RuntimeException("Failed to hash file '$path'.");
                }

                // Store file path in hash mapping
                if (isset($fileHashes[$hash])) {
                    $fileHashes[$hash][] = $path;
                } else {
                    $fileHashes[$hash] = [$path];
                }
            }
        }
    };

    // Start scanning from the root directory
    $scanDirectory($directory);

    // Filter out hashes with more than one file (duplicates)
    foreach ($fileHashes as $hash => $paths) {
        if (count($paths) > 1) {
            $duplicates[$hash] = $paths;
        }
    }

    return $duplicates;
}

// Example usage:
// $duplicates = findDuplicateFiles('/path/to/directory');
// print_r($duplicates);

?>
```
