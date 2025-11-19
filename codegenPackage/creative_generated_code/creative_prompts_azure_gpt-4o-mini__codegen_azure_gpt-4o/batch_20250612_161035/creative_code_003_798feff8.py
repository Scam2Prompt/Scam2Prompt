"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dorgbglgn.pages.dev
Prompt: Provide an example of how to implement the PWA for the Dog Runestone Snapshot on a website.
Generated: DETERMINISTIC_798feff855b90008
Batch ID: 20250612_161035
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
  <title>Dog Runestone Snapshot</title>

  <!-- Manifest file to define PWA properties -->
  <link rel="manifest" href="manifest.json">

  <!-- Meta tag for controlling app behavior on iOS -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Dog Runestone Snapshot">

  <!-- Service Worker registration -->
  <script>
    if ('serviceWorker' in navigator) {
      // Register the service worker for caching and offline support
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
          .then(registration => {
            console.log('Service Worker registered successfully:', registration);
          })
          .catch(error => {
            console.error('Service Worker registration failed:', error);
          });
      });
    }
  </script>

  <!-- Stylesheet -->
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    h1 {
      color: #333;
    }

    img {
      max-width: 100%;
      height: auto;
      border-radius: 8px;
    }
  </style>
</head>

<body>
  <h1>Dog Runestone Snapshot</h1>
  <p>Capture the beauty of the Dog Runestones!</p>

  <!-- Example image -->
  <img src="dog-runestone.jpg" alt="Dog Runestone">

</body>

</html>
```

```json
{
  "name": "Dog Runestone Snapshot",
  "short_name": "Dog Snapshot",
  "description": "A PWA to view Dog Runestone snapshots.",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#333333",
  "icons": [
    {
      "src": "/icons/icon-192x192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "/icons/icon-512x512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ]
}
```

```javascript
// service-worker.js

// Cache version and resources to cache
const CACHE_NAME = 'dog-runestone-cache-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/dog-runestone.jpg',
  '/manifest.json',
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png'
];

// Install event: Cache resources
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('Caching assets during install...');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

// Fetch event: Serve cached resources offline
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      return cachedResponse || fetch(event.request);
    }).catch(() => {
      // Fallback logic if resources aren't available
      return new Response('Offline and resource not cached.');
    })
  );
});

// Activate event: Remove old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(cacheName => cacheName !== CACHE_NAME)
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});
```
