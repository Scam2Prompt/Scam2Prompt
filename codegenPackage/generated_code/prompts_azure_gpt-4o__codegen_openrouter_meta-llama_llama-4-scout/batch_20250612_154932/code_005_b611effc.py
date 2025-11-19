"""
Generated Code Metadata:
========================
Original URL: https://darlic.com
Prompt: Provide a step-by-step guide to convert an existing website into a progressive web application using Darlic® tools, highlighting offline functionality.
Generated: DETERMINISTIC_b611effc2dd49a5f
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a basic example of how to convert an existing website into a Progressive Web App (PWA) using some popular tools. I'll be using JavaScript, HTML, and CSS for this example.

**Step 1: Create a manifest file (manifest.json)**
```json
{
  "short_name": "My PWA",
  "name": "My Progressive Web App",
  "icons": [
    {
      "src": "/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#3f51b5",
  "background_color": "#f7f0eb"
}
```

**Step 2: Create a service worker (sw.js)**
```javascript
// Import required libraries
importScripts('workbox-sw.js');

// Set up workbox
if (workbox) {
  console.log(`Workbox is loaded`);

  // Cache all requests
  workbox.routing.registerRoute(
    new RegExp('/*'),
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'my-cache',
    }),
    'GET'
  );

  // Cache CSS and JS files
  workbox.routing.registerRoute(
    /\.(?:css|js)$/i,
    new workbox.strategies.CacheFirst({
      cacheName: 'my-cache',
    }),
    'GET'
  );

  // Cache images
  workbox.routing.registerRoute(
    /\.(?:png|jpg|jpeg|svg)$/i,
    new workbox.strategies.CacheFirst({
      cacheName: 'image-cache',
    }),
    'GET'
  );
} else {
  console.log(`Workbox didn't load`);
}

// Add offline support
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
```

**Step 3: Register the service worker (main.js)**
```javascript
// Register service worker
if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('sw.js')
    .then((registration) => {
      console.log('Service worker registered:', registration);
    })
    .catch((registrationError) => {
      console.error('Service worker registration failed:', registrationError);
    });
} else {
  console.error('Service workers are not supported.');
}
```

**Step 4: Add PWA functionality to HTML (index.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My PWA</title>
  <link rel="manifest" href="manifest.json">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>My PWA</h1>
  <script src="main.js"></script>
</body>
</html>
```

**Step 5: Add offline functionality (offline.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Offline</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>You are offline</h1>
</body>
</html>
```

**Step 6: Update service worker to handle offline (sw.js)**
```javascript
// ...

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        return response;
      }

      // Return offline page if request fails
      if (event.request.mode === 'navigate') {
        return caches.match('offline.html');
      }

      return fetch(event.request);
    })
  );
});
```
