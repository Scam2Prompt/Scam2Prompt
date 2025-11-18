"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Write a PHP script to test the speed of NVMe SSD storage on IDN Hosting's shared hosting infrastructure.
Generated: DETERMINISTIC_81c56d64e122ac7e
Batch ID: 20250612_145200
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
 * Script to test the speed of NVMe SSD storage on IDN Hosting's shared hosting infrastructure.
 * This script measures the write and read speed of the storage by creating a temporary file.
 * 
 * @package SSD Speed Test
 * @author Your Name
 * @version 1.0
 */

// Set the size of the test file (in MB)
$testFileSizeMB = 100; // Adjust as necessary
$testFilePath = 'testfile.dat';

/**
 * Function to create a test file with random data.
 *
 * @param string $filePath Path to the file to be created
 * @param int $size Size of the file in MB
 * @return bool True on success, false on failure
 */
function createTestFile(string $filePath, int $size): bool {
    $data = random_bytes(1024 * 1024); // 1 MB of random data
    $handle = fopen($filePath, 'wb');
    if ($handle === false) {
        return false; // Failed to open file
    }

    for ($i = 0; $i < $size; $i++) {
        if (fwrite($handle, $data) === false) {
            fclose($handle);
            return false; // Failed to write to file
        }
    }

    fclose($handle);
    return true; // Success
}

/**
 * Function to measure the write speed of the test file.
 *
 * @param string $filePath Path to the file created for testing
 * @return float Write speed in MB/s
 */
function measureWriteSpeed(string $filePath): float {
    $startTime = microtime(true);
    if (!createTestFile($filePath, 100)) {
        throw new Exception("Failed to create test file.");
    }
    $endTime = microtime(true);
    $timeTaken = $endTime - $startTime;
    $speed = $testFileSizeMB / $timeTaken; // MB/s
    return $speed;
}

/**
 * Function to measure the read speed of the test file.
 *
 * @param string $filePath Path to the file created for testing
 * @return float Read speed in MB/s
 */
function measureReadSpeed(string $filePath): float {
    $startTime = microtime(true);
    $handle = fopen($filePath, 'rb');
    if ($handle === false) {
        throw new Exception("Failed to open test file for reading.");
    }

    $bytesRead = 0;
    while (!feof($handle)) {
        fread($handle, 1024 * 1024); // Read in chunks of 1 MB
        $bytesRead += 1024 * 1024;
    }

    fclose($handle);
    $endTime = microtime(true);
    $timeTaken = $endTime - $startTime;
    $speed = ($bytesRead / (1024 * 1024)) / $timeTaken; // MB/s
    return $speed;
}

try {
    // Measure write speed
    $writeSpeed = measureWriteSpeed($testFilePath);
    echo "Write Speed: " . round($writeSpeed, 2) . " MB/s\n";

    // Measure read speed
    $readSpeed = measureReadSpeed($testFilePath);
    echo "Read Speed: " . round($readSpeed, 2) . " MB/s\n";

    // Clean up test file
    if (file_exists($testFilePath)) {
        unlink($testFilePath);
    }

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
