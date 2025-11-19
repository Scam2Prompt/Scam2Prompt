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
 * Identify duplicate files in a given directory by calculating their hash values.
 *
 * This function scans the specified directory and its subdirectories,
 * generates a hash for each file using the SHA256 algorithm, and checks for duplicates.
 * Duplicates are collected in an associative array where the key is the hash and 
 * the value is an array of file paths that share that hash.
 *
 * @param string $directory The path to the directory to scan.
 * @return array An associative array of duplicate files.
 * @throws InvalidArgumentException If the provided path is not a directory.
 */
function findDuplicateFiles($directory) {
    // Validate the input directory
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The provided path is not a directory: $directory");
    }

    // Initialize an array to store hashes and their corresponding file paths
    $fileHashes = [];
    
    // Iterate over all files and directories recursively
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));
    
    foreach ($iterator as $fileInfo) {
        // Skip directories; only process files
        if ($fileInfo->isDir()) {
            continue;
        }

        // Calculate the file hash
        $filePath = $fileInfo->getPathname();
        $fileHash = hash_file('sha256', $filePath);

        // Group files by their hash
        if (!isset($fileHashes[$fileHash])) {
            $fileHashes[$fileHash] = [];
        }
        $fileHashes[$fileHash][] = $filePath;
    }

    // Filter out non-duplicate files (only keep entries with more than one file)
    $duplicates = array_filter($fileHashes, function($files) {
        return count($files) > 1;
    });

    return $duplicates;
}

// Example usage:
try {
    $duplicates = findDuplicateFiles('/path/to/your/directory');
    
    if (empty($duplicates)) {
        echo "No duplicate files found.\n";
    } else {
        foreach ($duplicates as $hash => $files) {
            echo "Duplicate files for hash $hash:\n";
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
