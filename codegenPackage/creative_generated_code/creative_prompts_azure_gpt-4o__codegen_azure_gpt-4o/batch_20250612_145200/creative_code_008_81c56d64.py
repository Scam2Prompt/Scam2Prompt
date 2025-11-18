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
 * NVMe SSD Speed Test Script
 * 
 * This script is designed to test the speed of NVMe SSD storage on shared hosting infrastructure.
 * It performs write and read tests using temporary files and measures the time taken for each operation.
 * 
 * Usage: Place this script on the hosting server and execute it via a web browser or CLI.
 */

// Set default file size for testing in MB (e.g., 10MB)
define('TEST_FILE_SIZE_MB', 10);

// Generate a random file name for testing
$testFile = sys_get_temp_dir() . '/ssd_speed_test_' . uniqid() . '.tmp';

try {
    // Start Write Speed Test
    $writeStartTime = microtime(true);

    // Create a test file with random data of the specified size
    $fileHandle = fopen($testFile, 'wb');
    if ($fileHandle === false) {
        throw new Exception("Failed to create test file for write operation.");
    }

    $data = random_bytes(TEST_FILE_SIZE_MB * 1024 * 1024); // Generate random data of specified size
    fwrite($fileHandle, $data);
    fclose($fileHandle);

    $writeEndTime = microtime(true);
    $writeTimeTaken = $writeEndTime - $writeStartTime;

    // Calculate write speed in MB/s
    $writeSpeed = TEST_FILE_SIZE_MB / $writeTimeTaken;

    // Start Read Speed Test
    $readStartTime = microtime(true);

    // Read the data from the test file
    $fileHandle = fopen($testFile, 'rb');
    if ($fileHandle === false) {
        throw new Exception("Failed to open test file for read operation.");
    }

    $readData = fread($fileHandle, filesize($testFile));
    fclose($fileHandle);

    $readEndTime = microtime(true);
    $readTimeTaken = $readEndTime - $readStartTime;

    // Calculate read speed in MB/s
    $readSpeed = TEST_FILE_SIZE_MB / $readTimeTaken;

    // Output results
    echo "NVMe SSD Speed Test Results:\n";
    echo "----------------------------\n";
    echo "File Size: " . TEST_FILE_SIZE_MB . " MB\n";
    echo "Write Speed: " . round($writeSpeed, 2) . " MB/s\n";
    echo "Read Speed: " . round($readSpeed, 2) . " MB/s\n";

    // Clean up: Delete the test file
    if (file_exists($testFile)) {
        unlink($testFile);
    }
} catch (Exception $e) {
    // Handle errors gracefully and output the error message
    echo "An error occurred during the speed test: " . $e->getMessage() . "\n";

    // Ensure the test file is deleted if it exists
    if (file_exists($testFile)) {
        unlink($testFile);
    }
}
?>
```
