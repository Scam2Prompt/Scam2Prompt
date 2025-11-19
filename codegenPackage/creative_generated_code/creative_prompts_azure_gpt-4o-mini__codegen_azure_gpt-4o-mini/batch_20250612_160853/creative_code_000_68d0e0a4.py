"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxdx7dvv77chf5hp3hxaflijsphox6jetahbbsqma5roloogvtey.ipfs.dweb.link
Prompt: How can I implement a Progressive Web App (PWA) that allows users to add it to their home screen, similar to friend.tech?
Generated: DETERMINISTIC_68d0e0a4be724ead
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#ffffff">
    
    <title>My PWA</title>
    
    <!-- Link to the manifest file -->
    <link rel="manifest" href="/manifest.json">
    
    <!-- Link to stylesheets -->
    <link rel="stylesheet" href="styles.css">
    
    <!-- Service Worker Registration -->
    <script>
        // Check if service workers are supported
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('/service-worker.js')
                .then(function(registration) {
                    console.log('Service Worker registered with scope:', registration.scope);
                })
                .catch(function(error) {
                    console.error('Service Worker registration failed:', error);
                });
            });
        }
    </script>
</head>
<body>
    <h1>Welcome to My PWA</h1>
    <p>Use this app to manage your tasks effortlessly!</p>
    
    <button id="installButton" style="display: none;">Install App</button>

    <script>
        let deferredPrompt;

        // Listen for the 'beforeinstallprompt' event to show the install button
        window.addEventListener('beforeinstallprompt', (e) => {
            // Prevent the mini info bar from appearing on mobile
            e.preventDefault();
            // Stash the event so it can be triggered later
            deferredPrompt = e;
            // Show the install button
            document.getElementById('installButton').style.display = 'block';

            // Install button click event
            document.getElementById('installButton').addEventListener('click', () => {
                // Hide the button
                document.getElementById('installButton').style.display = 'none';
                // Show the install prompt
                deferredPrompt.prompt();
                // Wait for the user to respond to the prompt
                deferredPrompt.userChoice.then((choiceResult) => {
                    if (choiceResult.outcome === 'accepted') {
                        console.log('User accepted the A2HS prompt');
                    } else {
                        console.log('User dismissed the A2HS prompt');
                    }
                    deferredPrompt = null;
                });
            });
        });
    </script>
</body>
</html>
```

```json
// manifest.json
{
    "name": "My PWA",
    "short_name": "PWA",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#ffffff",
    "icons": [
        {
            "src": "icon-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "icon-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}
```

```javascript
// service-worker.js

// Cache name
const CACHE_NAME = 'v1';

// Files to cache
const CACHE_ASSETS = [
    '/',
    'index.html',
    'styles.css',
    'icon-192x192.png',
    'icon-512x512.png'
];

// Install event
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Caching files');
                return cache.addAll(CACHE_ASSETS);
            })
    );
});

// Fetch event
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return cache hit
                if (response) {
                    return response;
                }
                return fetch(event.request).catch(() => {
                    // Handle errors when the resource isn't available
                    console.error('Fetch failed; returning offline page instead.');
                });
            })
    );
});

// Activate event
self.addEventListener('activate', (event) => {
    const cacheWhitelist = [CACHE_NAME];
    
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
```
