"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xpet-tech.pages.dev
Prompt: Explain how to implement a "Clear Cache" button in a web application, similar to the functionality provided on xPet.tech.
Generated: DETERMINISTIC_e9f89ddb26b18067
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML: Clear Cache Button -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clear Cache Example</title>
  <style>
    /* Basic styling for the button */
    #clear-cache-btn {
      padding: 10px 20px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 1rem;
    }

    #clear-cache-btn:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Clear Cache Example</h1>
  <button id="clear-cache-btn">Clear Cache</button>

  <script>
    // JavaScript: Clear Cache Functionality
    document.getElementById('clear-cache-btn').addEventListener('click', async () => {
      try {
        // Check if the browser supports Cache Storage API
        if ('caches' in window) {
          // Open all cache keys and delete each one
          const cacheKeys = await caches.keys();
          await Promise.all(cacheKeys.map(cache => caches.delete(cache)));

          // Notify the user of success
          alert('Cache cleared successfully!');
        } else {
          // Fallback in case Cache Storage API is not supported
          alert('Cache clearing is not supported in this browser.');
        }
      } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while clearing the cache:', error);
        alert('Failed to clear cache. Please try again.');
      }
    });
  </script>
</body>
</html>
```
