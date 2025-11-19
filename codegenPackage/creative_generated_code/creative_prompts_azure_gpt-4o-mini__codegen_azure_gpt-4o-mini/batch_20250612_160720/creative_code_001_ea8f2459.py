"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xpet-tech.pages.dev
Prompt: Write a code snippet to clear cache in a web application using JavaScript.
Generated: DETERMINISTIC_ea8f2459e3ebad94
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Clears the cache in a web application.
 * This function attempts to clear both the local storage and session storage,
 * as well as service worker caches if they are available.
 */
async function clearCache() {
    try {
        // Clear local storage
        localStorage.clear();
        console.log("Local storage cleared.");

        // Clear session storage
        sessionStorage.clear();
        console.log("Session storage cleared.");

        // Check if service workers are supported
        if ('caches' in window) {
            // Clear all caches
            const cacheNames = await caches.keys();
            await Promise.all(cacheNames.map(async (cacheName) => {
                await caches.delete(cacheName);
                console.log(`Cache ${cacheName} cleared.`);
            }));
        } else {
            console.warn("Service workers are not supported in this browser.");
        }
    } catch (error) {
        // Log the error for troubleshooting
        console.error("Error clearing cache:", error);
    }
}

// Usage: Call clearCache() when appropriate, such as during a logout process or when clearing user data.
// clearCache();
```
