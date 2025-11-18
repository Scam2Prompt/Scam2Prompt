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
 * Class FileDuplicationDetector
 * This class provides a method to detect duplicate files in a specified directory using file hashing.
 */
class FileDuplicationDetector
{
    /**
     * Detects duplicate files in the given directory.
     *
     * @param string $directory The directory to scan for duplicate files.
     * @return array An associative array with hash values as keys and arrays of file paths as values.
     * @throws InvalidArgumentException If the directory is not valid.
     */
    public function detectDuplicates(string $directory): array
    {
        // Validate the directory
        if (!is_dir($directory)) {
            throw new InvalidArgumentException("The provided path is not a valid directory: $directory");
        }

        // Initialize an array to hold file hashes and duplicate files
        $fileHashes = [];
        $duplicates = [];

        // Recursively iterate through the directory
        $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));
        foreach ($iterator as $file) {
            // Skip if it's not a file
            if (!$file->isFile()) {
                continue;
            }

            // Calculate the hash of the file
            $hash = md5_file($file->getPathname());

            // Store the file path under the computed hash
            if (!isset($fileHashes[$hash])) {
                $fileHashes[$hash] = [];
            }
            $fileHashes[$hash][] = $file->getPathname();
        }

        // Filter out non-duplicate entries
        foreach ($fileHashes as $hash => $files) {
            if (count($files) > 1) {
                $duplicates[$hash] = $files;
            }
        }

        return $duplicates;
    }
}

// Example usage
try {
    $detector = new FileDuplicationDetector();
    $duplicates = $detector->detectDuplicates('/path/to/your/directory');

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
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
