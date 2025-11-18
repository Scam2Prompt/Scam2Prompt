"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testsite.104zero.com
Prompt: Write a JavaScript function to test the performance of RAM usage in a web application.
Generated: DETERMINISTIC_c46ab6890260617c
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Measures and logs the RAM usage of the web application.
 * This function utilizes the Performance API to capture memory usage.
 * It runs a memory usage test and logs the initial and final memory used.
 * 
 * Note: This is a simplified function, and it may not be able to accurately 
 * determine RAM usage in all environments or browsers.
 */
function testRamUsage() {
    if (typeof performance.memory === 'undefined') {
        console.error('Memory usage API is not supported in this browser.');
        return;
    }

    // Capture initial memory usage
    const initialMemoryUsage = performance.memory.usedJSHeapSize;
    console.log(`Initial Memory Usage: ${formatBytes(initialMemoryUsage)}`);

    // Perform a memory-intensive operation (example)
    try {
        const largeArray = new Array(1e6).fill('Test String'); // Allocating memory
        console.log('Memory-intensive operation completed.');
        
        // Capture final memory usage
        const finalMemoryUsage = performance.memory.usedJSHeapSize;
        console.log(`Final Memory Usage: ${formatBytes(finalMemoryUsage)}`);
        
        // Free up the large array reference
        largeArray.length = 0;
        console.log('Memory reference cleared.');
        
        // Log memory usage difference
        console.log(`Memory Increase: ${formatBytes(finalMemoryUsage - initialMemoryUsage)}`);
    } catch (error) {
        console.error('An error occurred during memory test:', error);
    }
}

/**
 * Converts bytes to a human-readable format (e.g., KB, MB).
 * 
 * @param {number} bytes - The number of bytes to convert.
 * @returns {string} - The formatted string representing the memory size.
 */
function formatBytes(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes === 0) return '0 Byte';
    
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    return `${parseFloat((bytes / Math.pow(1024, i)).toFixed(2))} ${sizes[i]}`;
}

// Example usage
testRamUsage();
```
