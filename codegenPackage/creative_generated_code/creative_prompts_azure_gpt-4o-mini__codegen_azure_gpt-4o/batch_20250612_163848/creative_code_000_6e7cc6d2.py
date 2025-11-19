"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-interface-git-add-cra-service-worker-uniswap.vercel.app
Prompt: How can I implement a service worker for the Uniswap interface using JavaScript?
Generated: DETERMINISTIC_6e7cc6d2c35d7297
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: service-worker.js

// Version of the cache to force updates when changes occur
const CACHE_VERSION = 'v1';
const CACHE_NAME = `uniswap-cache-${CACHE_VERSION}`;

// List of resources to cache
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/favicon.ico',
  '/static/js/main.js',
  '/static/css/main.css',
  '/logo192.png'
];

// Event: Install Service Worker
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installing...');
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('Service Worker: Caching assets...');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

// Event: Activate Service Worker
self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activating...');
  event.waitUntil(
    // Cleanup old caches that are not the current version
    caches.keys().then((cacheNames) =>
      Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log(`Service Worker: Removing old cache: ${cacheName}`);
            return caches.delete(cacheName);
          }
        })
      )
    )
  );
});

// Event: Fetch requests
self.addEventListener('fetch', (event) => {
  // Check if the request is for navigation or static assets
  if (event.request.method === 'GET') {
    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        // Serve cached response if available, otherwise fetch from the network
        if (cachedResponse) {
          console.log(`Service Worker: Serving from cache: ${event.request.url}`);
          return cachedResponse;
        }
        console.log(`Service Worker: Fetching from network: ${event.request.url}`);
        return fetch(event.request)
          .then((networkResponse) => {
            // Cache the new response for future use
            return caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, networkResponse.clone());
              return networkResponse;
            });
          })
          .catch((error) => {
            console.error(`Service Worker: Fetch failed: ${error.message}`);
            // You can handle errors by returning fallback content or a custom error page
            return new Response('Network error occurred.', {
              status: 500,
              statusText: 'Service Worker error'
            });
          });
      })
    );
  }
});

// Optional: Listen for 'message' events to handle client interactions
self.addEventListener('message', (event) => {
  console.log('Service Worker: Received message:', event.data);
  if (event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
});

// Note: To register this service worker, include the following code in your main JavaScript file:
// if ('serviceWorker' in navigator) {
//   window.addEventListener('load', () => {
//     navigator.serviceWorker.register('/service-worker.js').then(
//       (registration) => {
//         console.log('Service Worker registered with scope:', registration.scope);
//       },
//       (error) => {
//         console.error('Service Worker registration failed:', error);
//       }
//     );
//   });
// }
```
