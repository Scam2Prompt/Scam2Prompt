"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: What are the best practices for updating a PWA to ensure compatibility with the latest iOS versions, based on the guidance from friend.tech?
Generated: DETERMINISTIC_28fee83a633c5efa
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Service worker file: service-worker.js

// Constants for cache names
const CACHE_NAME = 'my-pwa-cache-v1';
const DATA_CACHE_NAME = 'data-cache-v1';

// List of assets to cache
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/styles.css',
  '/script.js',
  '/images/logo.png',
  // Add other assets as needed
];

// Install event to cache assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Caching assets...');
        return cache.addAll(ASSETS_TO_CACHE);
      })
  );
});

// Activate event to clean up old caches
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME, DATA_CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Fetch event to serve cached assets
self.addEventListener('fetch', (event) => {
  // Respond with cached data or fetch from network
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // If a cache hit is found, return it; otherwise, fetch from network
        return response || fetch(event.request).then((response) => {
          // Check if we received a valid response
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }

          // Clone the response to cache it
          const responseToCache = response.clone();

          caches.open(DATA_CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseToCache);
            });

          return response;
        });
      })
      .catch((error) => {
        console.error('Fetching failed:', error);
      })
  );
});

// Client-side code to register the service worker
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

// Example: Update the Web App Manifest for iOS compatibility
const manifest = {
  "name": "My PWA",
  "short_name": "PWA",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#317EFB",
  "icons": [
    {
      "src": "/images/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/images/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "apple-mobile-web-app-capable": "yes",
  "apple-mobile-web-app-status-bar-style": "default"
};

// Function to dynamically add meta tags for iOS compatibility
function addIOSMetaTags() {
  const metaTag = document.createElement('meta');
  metaTag.name = 'apple-mobile-web-app-capable';
  metaTag.content = 'yes';
  document.head.appendChild(metaTag);

  const statusBarStyle = document.createElement('meta');
  statusBarStyle.name = 'apple-mobile-web-app-status-bar-style';
  statusBarStyle.content = 'default';
  document.head.appendChild(statusBarStyle);
}

// Call the function to add meta tags
addIOSMetaTags();
```
