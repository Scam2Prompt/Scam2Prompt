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
 * Function to identify duplicate files in a given directory using file hashing.
 *
 * @param string $directory The path to the directory to scan for duplicate files.
 * @return array An associative array where keys are file hashes and values are arrays of file paths that share the same hash.
 * @throws InvalidArgumentException If the provided directory is not valid or not a directory.
 */
function findDuplicateFiles($directory) {
    // Validate the provided directory
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The provided path is not a valid directory: $directory");
    }

    // Initialize an array to hold file hashes and their corresponding file paths
    $fileHashes = [];
    $duplicates = [];

    // Create a recursive directory iterator to scan through files
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));

    // Iterate through each file in the directory
    foreach ($iterator as $file) {
        // Skip directories
        if ($file->isDir()) {
            continue;
        }

        // Get the file path
        $filePath = $file->getPathname();

        // Calculate the file hash using SHA256
        $fileHash = hash_file('sha256', $filePath);

        // Store the file path in the array under its hash
        if (isset($fileHashes[$fileHash])) {
            $fileHashes[$fileHash][] = $filePath;
        } else {
            $fileHashes[$fileHash] = [$filePath];
        }
    }

    // Filter out hashes that have only one file (no duplicates)
    foreach ($fileHashes as $hash => $paths) {
        if (count($paths) > 1) {
            $duplicates[$hash] = $paths;
        }
    }

    return $duplicates;
}

// Example usage
try {
    $directoryPath = '/path/to/your/directory'; // Change this to your target directory
    $duplicates = findDuplicateFiles($directoryPath);

    if (empty($duplicates)) {
        echo "No duplicate files found.\n";
    } else {
        echo "Duplicate files found:\n";
        foreach ($duplicates as $hash => $files) {
            echo "Hash: $hash\n";
            foreach ($files as $file) {
                echo " - $file\n";
            }
        }
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
