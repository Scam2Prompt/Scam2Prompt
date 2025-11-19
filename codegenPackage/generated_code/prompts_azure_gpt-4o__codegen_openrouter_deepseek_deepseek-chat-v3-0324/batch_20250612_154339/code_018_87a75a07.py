"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Explain how to use PHP's "Garbage Collection" feature to optimize memory usage in a long-running script.
Generated: DETERMINISTIC_87a75a079b1d6163
Batch ID: 20250612_154339
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
 * Demonstrates PHP's Garbage Collection (GC) feature for memory optimization in long-running scripts.
 */

// Enable explicit garbage collection (optional, as PHP has it enabled by default)
gc_enable();

// Function to simulate a memory-intensive operation
function performMemoryIntensiveOperation() {
    $data = [];
    
    // Allocate a large amount of memory
    for ($i = 0; $i < 100000; $i++) {
        $data[] = str_repeat('a', 1024); // 1KB string
    }
    
    // Explicitly free memory by unsetting the variable
    unset($data);
    
    // Force garbage collection (optional, can be useful in critical sections)
    gc_collect_cycles();
}

// Function to monitor memory usage
function logMemoryUsage($message) {
    $memoryUsage = memory_get_usage(true) / (1024 * 1024); // Convert to MB
    $peakMemoryUsage = memory_get_peak_usage(true) / (1024 * 1024); // Convert to MB
    
    echo sprintf(
        "[%s] Memory Usage: %.2f MB | Peak: %.2f MB\n",
        $message,
        $memoryUsage,
        $peakMemoryUsage
    );
}

// Main script execution
try {
    logMemoryUsage("Start");
    
    // Perform memory-intensive operations in a loop
    for ($i = 0; $i < 5; $i++) {
        performMemoryIntensiveOperation();
        logMemoryUsage("After iteration $i");
        
        // Adjust garbage collection threshold (optional)
        if ($i % 2 === 0) {
            // Set the GC probability to 100% for this collection
            ini_set('gc_probability', 100);
            gc_collect_cycles();
            // Reset to default (usually 1)
            ini_set('gc_probability', 1);
        }
    }
    
    logMemoryUsage("End");
} catch (Exception $e) {
    error_log("Error occurred: " . $e->getMessage());
    exit(1);
}

// Disable garbage collection if no longer needed (not recommended for most cases)
// gc_disable();

?>
```
