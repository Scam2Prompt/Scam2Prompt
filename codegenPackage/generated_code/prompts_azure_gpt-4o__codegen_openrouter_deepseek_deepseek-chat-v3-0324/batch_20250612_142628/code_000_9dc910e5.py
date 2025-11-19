"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Write a PHP function to detect duplicate files on a server using file hashing, similar to the method described on Omidtak.ir for identifying duplicate files with hash values.
Generated: DETERMINISTIC_9dc910e50d60b83f
Batch ID: 20250612_142628
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
 * Detects duplicate files in a directory using file hashing.
 *
 * @param string $directory The directory path to scan for duplicates.
 * @param string $algorithm The hashing algorithm to use (default: 'md5').
 * @return array An associative array with hash values as keys and arrays of duplicate file paths as values.
 * @throws Exception If the directory does not exist or is not readable.
 */
function detectDuplicateFiles(string $directory, string $algorithm = 'md5'): array
{
    // Validate directory
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new Exception("Directory does not exist or is not readable: " . $directory);
    }

    // Validate hashing algorithm
    if (!in_array($algorithm, hash_algos())) {
        throw new Exception("Unsupported hashing algorithm: " . $algorithm);
    }

    $fileHashes = [];
    $duplicates = [];

    // Create recursive directory iterator
    $iterator = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($directory, RecursiveDirectoryIterator::SKIP_DOTS),
        RecursiveIteratorIterator::CHILD_FIRST
    );

    foreach ($iterator as $file) {
        if ($file->isFile() && $file->isReadable()) {
            try {
                $filePath = $file->getRealPath();
                $fileHash = hash_file($algorithm, $filePath);

                if (isset($fileHashes[$fileHash])) {
                    $fileHashes[$fileHash][] = $filePath;
                } else {
                    $fileHashes[$fileHash] = [$filePath];
                }
            } catch (Exception $e) {
                // Skip files that can't be hashed
                continue;
            }
        }
    }

    // Filter out non-duplicates
    foreach ($fileHashes as $hash => $files) {
        if (count($files) > 1) {
            $duplicates[$hash] = $files;
        }
    }

    return $duplicates;
}

/**
 * Example usage:
 * try {
 *     $duplicates = detectDuplicateFiles('/path/to/directory', 'sha256');
 *     print_r($duplicates);
 * } catch (Exception $e) {
 *     echo "Error: " . $e->getMessage();
 * }
 */
?>
```
