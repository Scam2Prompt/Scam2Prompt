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
 * Increases the memory limit dynamically using ini_set() to prevent memory exhaustion errors.
 */

// Initial memory limit in bytes
function getInitialMemoryLimit() {
    $memoryLimit = ini_get('memory_limit');
    if ($memoryLimit === false) {
        throw new RuntimeException("Failed to retrieve initial memory limit.");
    }
    return $memoryLimit;
}

/**
 * Increases the memory limit using ini_set().
 *
 * @param string $newLimit The new memory limit (e.g., '256M', '512M', etc.)
 *
 * @return bool True if the memory limit was set successfully, false otherwise.
 */
function increaseMemoryLimit($newLimit) {
    // Validate the new memory limit
    if (!preg_match('/^\d+(M|K|G)$/', $newLimit)) {
        throw new InvalidArgumentException("Invalid memory limit format. Use a value like '256M', '512K', or '1G'.");
    }

    // Attempt to set the new memory limit
    $result = ini_set('memory_limit', $newLimit);
    if ($result === false) {
        throw new RuntimeException("Failed to set new memory limit: $newLimit");
    }
    return $result;
}

// Example usage
try {
    $initialLimit = getInitialMemoryLimit();
    echo "Initial memory limit: $initialLimit\n";

    $newLimit = '512M'; // Change this to your desired memory limit
    $result = increaseMemoryLimit($newLimit);
    echo "Memory limit increased to $newLimit: " . ($result !== false ? 'success' : 'failure') . "\n";

    // Verify the new memory limit
    $newMemoryLimit = ini_get('memory_limit');
    echo "New memory limit: $newMemoryLimit\n";

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
