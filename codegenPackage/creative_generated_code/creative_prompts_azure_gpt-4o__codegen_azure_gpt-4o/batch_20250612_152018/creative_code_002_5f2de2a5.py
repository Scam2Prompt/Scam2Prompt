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

Below is a clean, production-ready JavaScript example for clearing browser cache programmatically for a web application like xPet.tech. It uses the Cache Storage API and also ensures sessionStorage and localStorage are cleared:

```javascript
/**
 * Clear browser cache programmatically for a web application.
 * This includes Cache Storage, sessionStorage, and localStorage.
 */
async function clearBrowserCache() {
  try {
    // Clear Cache Storage
    if ('caches' in window) {
      const cacheKeys = await caches.keys(); // Get all cache keys
      for (const key of cacheKeys) {
        await caches.delete(key); // Delete each cache
      }
      console.log("Cache Storage cleared successfully.");
    } else {
      console.warn("Cache Storage is not supported in this browser.");
    }

    // Clear sessionStorage
    sessionStorage.clear();
    console.log("Session storage cleared successfully.");

    // Clear localStorage
    localStorage.clear();
    console.log("Local storage cleared successfully.");

    console.log("Browser cache cleared successfully.");
  } catch (error) {
    // Log any errors encountered during cache clearing
    console.error("An error occurred while clearing browser cache:", error);
  }
}

// Trigger the cache clearing
clearBrowserCache();
```

This script can be embedded into the web application and triggered as needed. Always ensure that clearing cache does not result in unintended consequences for the end user's experience.
