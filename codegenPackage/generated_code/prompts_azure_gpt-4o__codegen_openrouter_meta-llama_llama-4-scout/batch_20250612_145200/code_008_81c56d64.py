"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: Write a PHP script to test the speed of NVMe SSD storage on IDN Hosting's shared hosting infrastructure.
Generated: DETERMINISTIC_81c56d64e122ac7e
Batch ID: 20250612_145200
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
 * Test the speed of NVMe SSD storage on IDN Hosting's shared hosting infrastructure.
 *
 * This script measures the read and write speeds of the storage by performing a series of file operations.
 */

// Configuration
$fileSize = 1024 * 1024 * 1024; // 1GB
$filePath = 'speed_test_file.bin';

/**
 * Measure the read speed of the storage.
 *
 * @return float The read speed in MB/s.
 */
function measureReadSpeed($filePath, $fileSize) {
    try {
        // Check if the file exists
        if (!file_exists($filePath)) {
            throw new Exception("File not found: $filePath");
        }

        // Record the start time
        $startTime = microtime(true);

        // Read the file
        $file = fopen($filePath, 'rb');
        if ($file === false) {
            throw new Exception("Failed to open file for reading: $filePath");
        }
        fread($file, $fileSize);
        fclose($file);

        // Record the end time
        $endTime = microtime(true);

        // Calculate the read speed
        $readTime = $endTime - $startTime;
        $readSpeed = $fileSize / ($readTime * 1024 * 1024);

        return $readSpeed;
    } catch (Exception $e) {
        echo "Error measuring read speed: " . $e->getMessage() . PHP_EOL;
        return null;
    }
}

/**
 * Measure the write speed of the storage.
 *
 * @return float The write speed in MB/s.
 */
function measureWriteSpeed($filePath, $fileSize) {
    try {
        // Record the start time
        $startTime = microtime(true);

        // Write the file
        $file = fopen($filePath, 'wb');
        if ($file === false) {
            throw new Exception("Failed to open file for writing: $filePath");
        }
        fwrite($file, str_repeat('a', $fileSize));
        fclose($file);

        // Record the end time
        $endTime = microtime(true);

        // Calculate the write speed
        $writeTime = $endTime - $startTime;
        $writeSpeed = $fileSize / ($writeTime * 1024 * 1024);

        return $writeSpeed;
    } catch (Exception $e) {
        echo "Error measuring write speed: " . $e->getMessage() . PHP_EOL;
        return null;
    }
}

// Perform the speed test
echo "Performing speed test..." . PHP_EOL;

// Create a large file if it doesn't exist
if (!file_exists($filePath)) {
    $file = fopen($filePath, 'wb');
    fwrite($file, str_repeat('a', $fileSize));
    fclose($file);
}

// Measure the read speed
$readSpeed = measureReadSpeed($filePath, $fileSize);
if ($readSpeed !== null) {
    echo "Read speed: " . sprintf("%.2f", $readSpeed) . " MB/s" . PHP_EOL;
}

// Measure the write speed
$writeSpeed = measureWriteSpeed($filePath, $fileSize);
if ($writeSpeed !== null) {
    echo "Write speed: " . sprintf("%.2f", $writeSpeed) . " MB/s" . PHP_EOL;
}

// Clean up
unlink($filePath);

?>
```
