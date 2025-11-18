"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xpet-tech.pages.dev
Prompt: Generate a script to clear browser cache programmatically for a web application like xPet.tech.
Generated: DETERMINISTIC_5f2de2a59f06ead2
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to clear the browser cache and storage for a web application
async function clearBrowserCache() {
    try {
        // Clear the cache
        if ('caches' in window) {
            const cacheNames = await caches.keys();
            await Promise.all(cacheNames.map(cacheName => caches.delete(cacheName)));
            console.log('Cache cleared successfully.');
        } else {
            console.warn('Cache API is not supported in this browser.');
        }

        // Clear local storage
        localStorage.clear();
        console.log('Local storage cleared successfully.');

        // Clear session storage
        sessionStorage.clear();
        console.log('Session storage cleared successfully.');

        // Optional: Reload the page to reflect changes
        window.location.reload();
    } catch (error) {
        console.error('Error clearing browser cache:', error);
        // Optionally, you can inform the user about the error
        alert('An error occurred while clearing the browser cache. Please try again.');
    }
}

// Usage: Call this function to clear the cache
// clearBrowserCache();
```

This script defines a function `clearBrowserCache` that, when invoked, will clear the browser's cache, local storage, and session storage. The function includes error handling to catch any issues that arise during the cache clearing process.
