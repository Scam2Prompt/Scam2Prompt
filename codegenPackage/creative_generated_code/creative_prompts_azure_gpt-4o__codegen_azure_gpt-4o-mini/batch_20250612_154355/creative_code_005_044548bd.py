"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-interface-git-add-cra-service-worker-uniswap.vercel.app
Prompt: Create a service worker script for a React application that ensures offline support for the Uniswap interface.
Generated: DETERMINISTIC_044548bd756daa0d
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Service Worker for Offline Support in a React Application
// This service worker is designed to cache assets for the Uniswap interface,
// allowing the application to function even when offline.

const CACHE_NAME = 'uniswap-cache-v1';
const CACHE_ASSETS = [
    // Add the URLs of the assets you want to cache
    '/',
    '/index.html',
    '/static/js/bundle.js',
    '/static/css/main.css',
    // Add other assets as needed
];

// Install event - Cache assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Caching assets');
                return cache.addAll(CACHE_ASSETS);
            })
            .catch((error) => {
                console.error('Failed to cache assets during installation:', error);
            })
    );
});

// Activate event - Cleanup old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Fetch event - Serve cached content or fetch from network
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return cached response if found, otherwise fetch from network
                return response || fetch(event.request);
            })
            .catch((error) => {
                console.error('Fetch failed; returning offline page instead.', error);
            })
    );
});

// Listen for the 'message' event (to handle updates)
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});
```

Make sure to register the service worker in your React application, typically in the `index.js` file:

```javascript
// Registering the service worker in the React app
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then((registration) => {
                console.log('Service Worker registered with scope:', registration.scope);
            })
            .catch((error) => {
                console.error('Service Worker registration failed:', error);
            });
    });
}
```
