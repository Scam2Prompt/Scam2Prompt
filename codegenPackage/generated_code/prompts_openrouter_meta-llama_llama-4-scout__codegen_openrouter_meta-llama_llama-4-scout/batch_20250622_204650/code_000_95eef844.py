"""
Generated Code Metadata:
========================
Original URL: https://leonidas-dogme.pages.dev
Prompt: "Write a JavaScript code snippet to implement a PWA for Ord.io, enabling offline access and push notifications."
Generated: DETERMINISTIC_95eef844666ec74f
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// sw.js (Service Worker script)

// Set cache name and version
const CACHE_NAME = 'ord-io-cache';
const CACHE_VERSION = '1.0.0';

// Files to cache
const FILES_TO_CACHE = [
  '/',
  '/index.html',
  '/styles.css',
  '/script.js',
  '/manifest.json',
  '/icons/icon-192x192.png',
  '/icons/icon-256x256.png',
  '/icons/icon-384x384.png',
  '/icons/icon-512x512.png',
];

// Install event handler
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(FILES_TO_CACHE);
    })
  );
});

// Activate event handler
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Fetch event handler
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

// Push event handler
self.addEventListener('push', (event) => {
  const { title, message } = event.data.json();
  event.waitUntil(
    self.registration.showNotification(title, {
      body: message,
      icon: '/icons/icon-192x192.png',
    })
  );
});

// Notification click event handler
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll().then((clients) => {
      if (clients.length) {
        clients[0].focus();
      } else {
        self.clients.openWindow('/');
      }
    })
  );
});

// Register service worker
// script.js
if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('sw.js')
    .then((registration) => {
      console.log('Service worker registered:', registration);
    })
    .catch((error) => {
      console.error('Service worker registration failed:', error);
    });
}

// Request permission for push notifications
// script.js
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistration().then((registration) => {
    registration.pushManager
      .getSubscription()
      .then((subscription) => {
        if (!subscription) {
          registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: 'YOUR_PUBLIC_KEY',
          })
            .then((subscription) => {
            console.log('Push subscription:', subscription);
          })
          .catch((error) => {
            console.error('Push subscription failed:', error);
          });
        }
      });
  });
}

// manifest.json
{
  "short_name": "Ord.io",
  "name": "Ord.io Progressive Web App",
  "icons": [
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-256x256.png",
      "sizes": "256x256",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "start_url": "/",
  "background_color": "#f7f0eb",
  "display": "standalone",
  "theme_color": "#a29bfe",
  "description": "Ord.io Progressive Web App",
  "screenshots": [],
  "categories": [],
  "share_target": {
    "url": "/"
  }
}
```
