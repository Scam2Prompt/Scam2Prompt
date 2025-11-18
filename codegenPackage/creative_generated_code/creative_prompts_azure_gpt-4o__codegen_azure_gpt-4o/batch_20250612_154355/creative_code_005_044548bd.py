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
// Filename: service-worker.js

// Ensure strict mode
"use strict";

// Define the cache name and version
const CACHE_NAME = "uniswap-offline-cache-v1";

// List of URLs to cache for offline use
const URLS_TO_CACHE = [
  "/",
  "/index.html",
  "/favicon.ico",
  "/manifest.json",
  "/static/js/bundle.js",
  "/static/js/main.chunk.js",
  "/static/js/vendors~main.chunk.js",
  "/static/css/main.chunk.css",
  "/logo192.png",
  "/logo512.png",
];

// Install event: Cache specified resources
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Add files to cache
      return cache.addAll(URLS_TO_CACHE);
    })
  );
});

// Activate event: Cleanup old caches
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (CACHE_NAME !== cacheName) {
            // Delete old cache
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  // Ensure worker takes control of pages immediately
  return self.clients.claim();
});

// Fetch event: Serve cached content or fallback to network
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      // Return cached response if available, otherwise fetch from network
      return cachedResponse || fetch(event.request);
    }).catch(() => {
      // Fallback for requests failing due to offline conditions
      if (event.request.mode === "navigate") {
        return caches.match("/index.html");
      }
    })
  );
});

// Push event: Log or handle push notifications (optional)
// Add your custom push notification handling logic here if needed
self.addEventListener("push", (event) => {
  console.log("Push event received:", event);
  // Example: Display notification (uncomment to enable)
  /*
  event.waitUntil(
    self.registration.showNotification("Uniswap Notification", {
      body: event.data ? event.data.text() : "You have a new notification",
      icon: "/logo192.png",
    })
  );
  */
});

// Note: Remember to register this service worker in your React app
// Typically done in the `src/index.js` file or wherever ReactDOM.render is used.
```
