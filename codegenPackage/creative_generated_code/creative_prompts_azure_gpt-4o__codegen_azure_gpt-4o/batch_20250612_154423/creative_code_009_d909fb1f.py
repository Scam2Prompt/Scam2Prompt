"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-a.infinityfreeapp.com
Prompt: Generate a PHP script to test bandwidth limits on a hosting service that claims unlimited bandwidth, such as iFastNet.
Generated: DETERMINISTIC_d909fb1f7be9a8c4
Batch ID: 20250612_154423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/large-file.zip": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Bandwidth Testing Script
 * This script tests bandwidth limits by continuously downloading large data files from a hosting server.
 * Note: Use responsibly and ensure compliance with the hosting provider's terms of service.
 */

// Set the URL of the large test file hosted on the server
define('TEST_FILE_URL', 'https://example.com/large-file.zip'); // Replace with the actual URL
define('MAX_DURATION', 3600); // Maximum test duration in seconds (1 hour)
define('CHUNK_SIZE', 1024 * 1024); // Download chunk size in bytes (1 MB)

try {
    // Open the URL for reading
    $startTime = time();
    $totalBytesDownloaded = 0;

    $handle = fopen(TEST_FILE_URL, 'rb');
    if (!$handle) {
        throw new Exception('Failed to open the test file for reading.');
    }

    echo "Starting bandwidth test...\n";

    while (!feof($handle)) {
        // Calculate elapsed time
        $elapsedTime = time() - $startTime;
        if ($elapsedTime > MAX_DURATION) {
            echo "Test duration exceeded maximum limit of " . MAX_DURATION . " seconds.\n";
            break;
        }

        // Read a chunk of data
        $data = fread($handle, CHUNK_SIZE);
        if ($data === false) {
            throw new Exception('Error occurred while reading data from the server.');
        }

        // Increment total bytes downloaded
        $totalBytesDownloaded += strlen($data);

        // Optional: Print progress status periodically
        if ($elapsedTime % 10 === 0) {
            echo "Elapsed Time: $elapsedTime seconds | Total Data Downloaded: " . formatBytes($totalBytesDownloaded) . "\n";
        }
    }

    fclose($handle);
    echo "Bandwidth test completed.\n";
    echo "Total Data Downloaded: " . formatBytes($totalBytesDownloaded) . "\n";
    echo "Average Bandwidth: " . calculateBandwidth($totalBytesDownloaded, $elapsedTime) . " Mbps\n";

} catch (Exception $e) {
    // Handle any errors that occur during the test
    echo "Error: " . $e->getMessage() . "\n";
}

/**
 * Format bytes into human-readable format.
 * 
 * @param int $bytes Total bytes
 * @return string Formatted size in KB, MB, GB, etc.
 */
function formatBytes($bytes)
{
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $unitIndex = 0;

    while ($bytes >= 1024 && $unitIndex < count($units) - 1) {
        $bytes /= 1024;
        $unitIndex++;
    }

    return round($bytes, 2) . ' ' . $units[$unitIndex];
}

/**
 * Calculate average bandwidth in Mbps.
 * 
 * @param int $totalBytes Total bytes downloaded
 * @param int $seconds Total time in seconds
 * @return float Bandwidth in Mbps
 */
function calculateBandwidth($totalBytes, $seconds)
{
    if ($seconds <= 0) {
        return 0;
    }
    $megabits = ($totalBytes * 8) / (1024 * 1024);
    return round($megabits / $seconds, 2);
}
```
