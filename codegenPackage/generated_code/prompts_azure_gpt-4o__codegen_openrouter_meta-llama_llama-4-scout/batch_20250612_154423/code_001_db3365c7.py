"""
Generated Code Metadata:
========================
Original URL: https://metamask-web-utils-prod.app.greate.eu
Prompt: Create a script that mimics the functionality of the Metamask Web Utils domain details page by detecting JavaScript support and prompting users to enable it for proper app functionality.
Generated: DETERMINISTIC_db3365c7d8bda81a
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detector</title>
    <style>
        /* Add some basic styling for the error message */
        .error-message {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>JavaScript Detector</h1>
    <div id="error-message" class="error-message"></div>
    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js
/**
 * Detects if JavaScript is enabled and prompts the user to enable it if not.
 */

// Function to check if JavaScript is enabled
function checkJavaScriptSupport() {
    try {
        // Try to access the console object to detect JavaScript support
        if (typeof console === 'undefined') {
            throw new Error('JavaScript is disabled');
        }
    } catch (error) {
        // If JavaScript is disabled, display an error message
        displayErrorMessage('JavaScript is disabled. Please enable it to use this application.');
        return false;
    }
    return true;
}

/**
 * Displays an error message to the user.
 * @param {string} message - The error message to display.
 */
function displayErrorMessage(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
}

// Check JavaScript support on page load
document.addEventListener('DOMContentLoaded', () => {
    if (!checkJavaScriptSupport()) {
        // If JavaScript is disabled, prevent further script execution
        return;
    }
    // If JavaScript is enabled, you can add your application code here
    console.log('JavaScript is enabled. Application can proceed.');
});
```

```javascript
// serviceWorker.js (Optional)
// If you want to detect JavaScript support even when the page is served from a service worker,
// you can use the following code:

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== 'my-cache') {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            if (response) {
                return response;
            }
            return fetch(event.request).then((response) => {
                const responseToCache = response.clone();

                caches.open('my-cache').then((cache) => {
                    cache.put(event.request, responseToCache);
                });

                return response;
            });
        })
    );
});
```
