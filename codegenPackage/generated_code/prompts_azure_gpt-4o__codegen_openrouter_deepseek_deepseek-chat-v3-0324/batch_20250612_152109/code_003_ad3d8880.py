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
 * Dynamically increases the memory limit to prevent memory exhaustion errors.
 *
 * @param string $newLimit The new memory limit (e.g., '256M', '512M', '1G').
 * @return bool True if the memory limit was successfully set, false otherwise.
 * @throws RuntimeException If unable to set the new memory limit.
 */
function increaseMemoryLimit(string $newLimit): bool
{
    // Validate the input format (e.g., '256M', '1G')
    if (!preg_match('/^\d+[KMG]$/i', $newLimit)) {
        throw new InvalidArgumentException(
            "Invalid memory limit format. Expected format like '256M' or '1G'."
        );
    }

    // Get the current memory limit for comparison
    $currentLimit = ini_get('memory_limit');

    // Convert both limits to bytes for comparison
    $currentBytes = convertToBytes($currentLimit);
    $newBytes = convertToBytes($newLimit);

    // Only increase if the new limit is higher
    if ($newBytes <= $currentBytes) {
        return false;
    }

    // Attempt to set the new memory limit
    if (ini_set('memory_limit', $newLimit) === false) {
        throw new RuntimeException(
            "Failed to set memory limit to {$newLimit}. Check your PHP configuration."
        );
    }

    return true;
}

/**
 * Converts a memory limit string (e.g., '256M') to bytes.
 *
 * @param string $memoryLimit The memory limit string to convert.
 * @return int The memory limit in bytes.
 */
function convertToBytes(string $memoryLimit): int
{
    $unit = strtoupper(substr($memoryLimit, -1));
    $value = (int)substr($memoryLimit, 0, -1);

    switch ($unit) {
        case 'G':
            return $value * 1024 * 1024 * 1024;
        case 'M':
            return $value * 1024 * 1024;
        case 'K':
            return $value * 1024;
        default:
            return (int)$memoryLimit;
    }
}

// Example usage:
try {
    $success = increaseMemoryLimit('256M');
    if ($success) {
        echo "Memory limit increased successfully.\n";
    } else {
        echo "Current memory limit is already sufficient.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
