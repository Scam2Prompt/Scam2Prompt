"""
Generated Code Metadata:
========================
Original URL: https://xpet-tech.pages.dev
Prompt: Explain how to implement a "Clear Cache" button in a web application, similar to the functionality provided on xPet.tech.
Generated: DETERMINISTIC_e9f89ddb26b18067
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clear Cache Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        button {
            background-color: #f44336;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #d32f2f;
        }
        #status {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        .success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        .error {
            background-color: #f2dede;
            color: #a94442;
        }
    </style>
</head>
<body>
    <h1>Clear Cache</h1>
    <button id="clearCacheBtn">Clear Cache</button>
    <div id="status"></div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const clearCacheBtn = document.getElementById('clearCacheBtn');
            const statusElement = document.getElementById('status');

            /**
             * Clear the browser cache by making a request to the server
             * with cache-busting headers and clearing local storage
             */
            clearCacheBtn.addEventListener('click', async function() {
                try {
                    // Show loading state
                    clearCacheBtn.disabled = true;
                    clearCacheBtn.textContent = 'Clearing...';

                    // Clear localStorage (optional)
                    localStorage.clear();

                    // Clear sessionStorage (optional)
                    sessionStorage.clear();

                    // Make a request to the server with cache-busting headers
                    const response = await fetch('/clear-cache', {
                        method: 'POST',
                        headers: {
                            'Cache-Control': 'no-cache, no-store, must-revalidate',
                            'Pragma': 'no-cache',
                            'Expires': '0'
                        },
                        credentials: 'include' // Include cookies if needed
                    });

                    if (!response.ok) {
                        throw new Error('Failed to clear cache');
                    }

                    // Force reload the page to ensure fresh content
                    window.location.reload(true);

                } catch (error) {
                    // Show error message
                    statusElement.textContent = `Error: ${error.message}`;
                    statusElement.className = 'error';
                    statusElement.style.display = 'block';

                    // Reset button state
                    clearCacheBtn.disabled = false;
                    clearCacheBtn.textContent = 'Clear Cache';
                }
            });
        });
    </script>
</body>
</html>
```

```javascript
// Server-side example (Node.js with Express)
const express = require('express');
const app = express();

// Middleware to prevent caching for certain routes
app.use((req, res, next) => {
    res.header('Cache-Control', 'no-cache, private, no-store, must-revalidate');
    res.header('Expires', '-1');
    res.header('Pragma', 'no-cache');
    next();
});

// Clear cache endpoint
app.post('/clear-cache', (req, res) => {
    try {
        // Here you would implement your server-side cache clearing logic
        // For example:
        // - Clear server-side caches (Redis, Memcached, etc.)
        // - Clear CDN caches if applicable
        // - Clear any other application-specific caches
        
        res.status(200).json({ success: true, message: 'Cache cleared successfully' });
    } catch (error) {
        console.error('Error clearing cache:', error);
        res.status(500).json({ success: false, message: 'Failed to clear cache' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
