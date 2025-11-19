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
 * This class provides a method to identify duplicate files in a given directory.
 */
class DuplicateFileFinder {

    /**
     * @var array $hashes A dictionary to store file hashes and their corresponding paths.
     */
    private $hashes = [];

    /**
     * @var string $rootDir The root directory to start searching for duplicate files.
     */
    private $rootDir;

    /**
     * Constructor to initialize the root directory.
     *
     * @param string $rootDir The root directory to start searching for duplicate files.
     */
    public function __construct($rootDir) {
        $this->rootDir = $rootDir;
    }

    /**
     * Method to find duplicate files in the given directory.
     *
     * @return array A dictionary with file hashes as keys and arrays of their corresponding paths as values.
     */
    public function findDuplicates() {
        $this->scanDirectory($this->rootDir);
        return $this->getDuplicates();
    }

    /**
     * Recursive method to scan a directory and its subdirectories for files.
     *
     * @param string $dir The current directory being scanned.
     */
    private function scanDirectory($dir) {
        try {
            $files = scandir($dir);
            foreach ($files as $file) {
                if ($file == '.' || $file == '..') {
                    continue;
                }
                $filePath = $dir . DIRECTORY_SEPARATOR . $file;
                if (is_file($filePath)) {
                    $this->addFileHash($filePath);
                } elseif (is_dir($filePath)) {
                    $this->scanDirectory($filePath);
                }
            }
        } catch (Exception $e) {
            echo "Error scanning directory $dir: " . $e->getMessage() . PHP_EOL;
        }
    }

    /**
     * Method to calculate the hash of a file and store it in the $hashes dictionary.
     *
     * @param string $filePath The path of the file to calculate the hash for.
     */
    private function addFileHash($filePath) {
        try {
            $hash = md5_file($filePath);
            if (isset($this->hashes[$hash])) {
                $this->hashes[$hash][] = $filePath;
            } else {
                $this->hashes[$hash] = [$filePath];
            }
        } catch (Exception $e) {
            echo "Error processing file $filePath: " . $e->getMessage() . PHP_EOL;
        }
    }

    /**
     * Method to get an array of file hashes that have duplicates.
     *
     * @return array A dictionary with file hashes as keys and arrays of their corresponding paths as values, filtered for duplicates.
     */
    private function getDuplicates() {
        $duplicates = [];
        foreach ($this->hashes as $hash => $paths) {
            if (count($paths) > 1) {
                $duplicates[$hash] = $paths;
            }
        }
        return $duplicates;
    }
}

// Example usage
if __name__ == "__main__" {
    $rootDir = '/path/to/your/directory';
    $finder = new DuplicateFileFinder($rootDir);
    $duplicates = $finder->findDuplicates();
    if (!empty($duplicates)) {
        echo "Found the following duplicate files:" . PHP_EOL;
        foreach ($duplicates as $hash => $paths) {
            echo "Hash: $hash" . PHP_EOL;
            foreach ($paths as $path) {
                echo "- $path" . PHP_EOL;
            }
        }
    } else {
        echo "No duplicate files found." . PHP_EOL;
    }
}
```
