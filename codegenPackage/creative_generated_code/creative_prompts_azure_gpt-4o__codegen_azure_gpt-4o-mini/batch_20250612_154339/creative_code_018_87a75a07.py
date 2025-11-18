"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Explain how to use PHP's "Garbage Collection" feature to optimize memory usage in a long-running script.
Generated: DETERMINISTIC_87a75a079b1d6163
Batch ID: 20250612_154339
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
 * This script demonstrates how to use PHP's Garbage Collection (GC) feature
 * to optimize memory usage in a long-running script.
 * 
 * Garbage Collection helps to free up memory by removing objects that are no 
 * longer in use. This is particularly useful in long-running scripts where 
 * memory consumption may increase over time.
 */

// Enable Garbage Collection
gc_enable();

/**
 * Function that simulates a long-running process.
 */
function longRunningProcess() {
    // Create a large number of objects for demonstration
    $objects = [];

    for ($i = 0; $i < 10000; $i++) {
        // Each iteration creates a new object
        $objects[] = new stdClass();
    }

    // At this point, we have allocated memory for a lot of objects

    // Manually trigger Garbage Collection
    $collected = gc_collect_cycles();
    
    // Log the number of collected cycles
    echo "Garbage Collection performed, collected $collected cycles.\n";

    // Simulate some processing time
    sleep(2);
}

// Run the long-running process multiple times to demonstrate memory usage
for ($run = 0; $run < 5; $run++) {
    echo "Run " . ($run + 1) . ":\n";
    longRunningProcess();
}

// Final Garbage Collection before script ends
$finalCollected = gc_collect_cycles();
echo "Final Garbage Collection performed, collected $finalCollected cycles.\n";

// Disable Garbage Collection after use (optional)
gc_disable();
?>
```
