"""
Generated Code Metadata:
========================
Original URL: https://it10.alhuda.com.pk
Prompt: Explain how to use `ini_set()` in PHP to increase memory limits dynamically for resolving memory exhaustion errors.
Generated: DETERMINISTIC_ad3d888009c702af
Batch ID: 20250612_152109
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
 * This script demonstrates how to use ini_set() in PHP
 * to dynamically increase the memory limit for resolving
 * memory exhaustion errors.
 */

// Function to increase memory limit
function increaseMemoryLimit($additionalMemory) {
    // Get the current memory limit
    $currentLimit = ini_get('memory_limit');

    // Convert the current limit to bytes for comparison
    $currentLimitBytes = convertToBytes($currentLimit);

    // Calculate the new memory limit
    $newLimitBytes = $currentLimitBytes + convertToBytes($additionalMemory);

    // Convert the new limit back to a human-readable format
    $newLimit = formatBytes($newLimitBytes);

    // Set the new memory limit
    if (ini_set('memory_limit', $newLimit) === false) {
        throw new RuntimeException("Failed to set memory limit to $newLimit");
    }

    return $newLimit;
}

/**
 * Convert a human-readable memory limit (e.g., '128M', '2G') to bytes.
 *
 * @param string $value The memory limit in human-readable format.
 * @return int The memory limit in bytes.
 */
function convertToBytes($value) {
    $value = trim($value);
    $unit = strtoupper(substr($value, -1));
    $bytes = (int)$value;

    switch ($unit) {
        case 'G':
            $bytes *= 1024;
        case 'M':
            $bytes *= 1024;
        case 'K':
            $bytes *= 1024;
            break;
    }

    return $bytes;
}

/**
 * Format bytes into a human-readable string.
 *
 * @param int $bytes The memory size in bytes.
 * @return string The formatted memory size.
 */
function formatBytes($bytes) {
    $units = ['B', 'K', 'M', 'G', 'T'];
    $factor = floor((strlen($bytes) - 1) / 3);
    return sprintf('%.2f %s', $bytes / pow(1024, $factor), $units[$factor]);
}

// Example usage
try {
    // Increase memory limit by 128M
    $newMemoryLimit = increaseMemoryLimit('128M');
    echo "Memory limit successfully increased to: $newMemoryLimit\n";
} catch (RuntimeException $e) {
    // Handle the error gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
