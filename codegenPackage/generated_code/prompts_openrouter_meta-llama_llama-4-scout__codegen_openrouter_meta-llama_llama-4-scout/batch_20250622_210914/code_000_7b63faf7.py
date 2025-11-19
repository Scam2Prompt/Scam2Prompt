"""
Generated Code Metadata:
========================
Original URL: https://claim-doggotothemoon.pages.dev
Prompt: Write a JavaScript snippet to implement a PWA feature similar to what is described on Ord.io, focusing on snapshot functionality.
Generated: DETERMINISTIC_7b63faf735d978e2
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Service Worker Registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js')
    .then(registration => {
      console.log('Service Worker registered:', registration);
    })
    .catch(registrationError => {
      console.error('Service Worker registration failed:', registrationError);
    });
} else {
  console.error('Service Workers are not supported.');
}

// sw.js (Service Worker Script)

// Cache Name and Files
const CACHE_NAME = 'ord-io-snapshot-cache';
const urlsToCache = [
  '/',
  '/styles.css',
  '/script.js',
  '/images/icon.png',
];

// Install Event Handler
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Cache opened');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activate Event Handler
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('Cache removed:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Fetch Event Handler
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Clone response to use in both .then and .catch
        return response.clone().then(r2 => {
          // Check if response is valid
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          // Update cache with new response
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, r2);
          });

          return response;
        }).catch(error => {
          console.error('Error fetching or caching:', error);
          return caches.match(event.request).then(cachedResponse => {
            return cachedResponse || fetch(event.request);
          });
        });
      })
  );
});

// Snapshot Functionality
self.addEventListener('message', event => {
  if (event.data.action === 'snapshot') {
    // Take a snapshot of the current page
    takeSnapshot()
      .then(blob => {
        // Send the snapshot back to the client
        event.source.postMessage({ action: 'snapshot', blob });
      })
      .catch(error => {
        console.error('Error taking snapshot:', error);
      });
  }
});

// Helper function to take a snapshot
function takeSnapshot() {
  return new Promise((resolve, reject) => {
    // Get the current client's scroll position and dimensions
    const scrollX = window.scrollX;
    const scrollY = window.scrollY;
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Create a canvas to draw the snapshot on
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    const ctx = canvas.getContext('2d');

    // Draw the current page on the canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, width, height);
    ctx.drawImage(document.body, 0, 0, width, height);

    // Convert the canvas to a blob
    canvas.toBlob(blob => {
      resolve(blob);
    }, 'image/png');
  });
}
```
