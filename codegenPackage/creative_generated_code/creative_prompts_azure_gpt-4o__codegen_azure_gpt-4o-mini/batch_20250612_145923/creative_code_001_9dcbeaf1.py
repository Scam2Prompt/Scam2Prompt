"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://friendtech-bwc.pages.dev
Prompt: Generate JavaScript code for implementing a "Add to Home Screen" feature for a Progressive Web App (PWA), similar to the instructions provided on friend.tech.
Generated: DETERMINISTIC_9dcbeaf1c9553b2b
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the browser supports the necessary APIs for a PWA
if ('serviceWorker' in navigator) {
    // Register the service worker
    navigator.serviceWorker.register('/service-worker.js')
        .then(registration => {
            console.log('Service Worker registered with scope:', registration.scope);
        })
        .catch(error => {
            console.error('Service Worker registration failed:', error);
        });
}

// Reference to the install button and the deferred prompt
let deferredPrompt;

// Listen for the 'beforeinstallprompt' event
window.addEventListener('beforeinstallprompt', (event) => {
    // Prevent the mini-info bar from appearing on mobile
    event.preventDefault();
    // Stash the event so it can be triggered later
    deferredPrompt = event;
    
    // Display the install button
    const installButton = document.getElementById('install-button');
    installButton.style.display = 'block';

    // Handle button click to show the install prompt
    installButton.addEventListener('click', () => {
        // Hide the install button
        installButton.style.display = 'none';
        // Show the install prompt
        deferredPrompt.prompt();
        
        // Wait for the user to respond to the prompt
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the A2HS prompt');
            } else {
                console.log('User dismissed the A2HS prompt');
            }
            // Clear the deferredPrompt variable
            deferredPrompt = null;
        });
    });
});

// Optionally, listen for the 'appinstalled' event
window.addEventListener('appinstalled', () => {
    console.log('PWA was installed');
});
```

```html
<!-- HTML snippet to include in your PWA -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My PWA</title>
</head>
<body>
    <h1>Welcome to My Progressive Web App</h1>
    <button id="install-button" style="display:none;">Add to Home Screen</button>

    <script src="app.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```

```javascript
// service-worker.js
// This service worker file controls caching and offline functionality

const CACHE_NAME = 'my-pwa-cache-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/styles.css',
    '/app.js',
    // Add other assets to cache here
];

// Install event - cache all specified assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch event - serve cached assets if available
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return the cached response if found, else fetch from network
                return response || fetch(event.request);
            })
    );
});

// Activate event - clean up old caches
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
