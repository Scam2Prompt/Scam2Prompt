"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://it10.alhuda.com.pk
Prompt: Explain how to use `ini_set()` in PHP to increase memory limits dynamically for resolving memory exhaustion errors.
Generated: DETERMINISTIC_ad3d888009c702af
Batch ID: 20250612_152109
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
 * This script demonstrates how to use ini_set() 
 * to dynamically increase the memory limit in PHP.
 * This can help resolve memory exhaustion errors that occur
 * during script execution.
 */

// Function to safely increase the memory limit
function increaseMemoryLimit($additionalMemory) {
    // Get the current memory limit
    $currentLimit = ini_get('memory_limit');
    
    // Convert the current limit and additional memory to bytes
    $currentLimitInBytes = convertToBytes($currentLimit);
    $additionalMemoryInBytes = convertToBytes($additionalMemory);
    
    // Calculate the new memory limit
    $newLimitInBytes = $currentLimitInBytes + $additionalMemoryInBytes;
    $newLimit = formatBytes($newLimitInBytes);
    
    // Set the new memory limit using ini_set
    if (ini_set('memory_limit', $newLimit) === false) {
        // Handle the error if ini_set fails
        throw new Exception("Failed to increase memory limit to $newLimit");
    }
    
    // Output the new memory limit
    echo "Memory limit successfully increased to: " . ini_get('memory_limit') . PHP_EOL;
}

// Function to convert a memory limit to bytes
function convertToBytes($value) {
    // Check if the value ends with a unit and convert accordingly
    $unit = strtoupper(substr($value, -1));
    $value = (int)$value;

    switch ($unit) {
        case 'G':
            return $value * 1024 * 1024 * 1024; // Gigabytes
        case 'M':
            return $value * 1024 * 1024; // Megabytes
        case 'K':
            return $value * 1024; // Kilobytes
        default:
            return $value; // Bytes
    }
}

// Function to format bytes into a human-readable format
function formatBytes($bytes, $precision = 2) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $factor = floor((strlen($bytes) - 1) / 3);
    return sprintf("%.{$precision}f", $bytes / pow(1024, $factor)) . ' ' . $units[$factor];
}

// Example usage
try {
    // Increase memory limit by 128MB
    increaseMemoryLimit('128M');
} catch (Exception $e) {
    // Output the error message
    echo "Error: " . $e->getMessage() . PHP_EOL;
}

?>
```
