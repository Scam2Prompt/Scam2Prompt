"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-interface-git-add-cra-service-worker-uniswap.vercel.app
Prompt: What are the best practices for optimizing the Uniswap interface with service workers?
Generated: DETERMINISTIC_ba33ef4a69f01b65
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// service-worker.js

// Define cache names for versioning
const CACHE_NAME = 'uniswap-v1';
const DATA_CACHE_NAME = 'data-cache-v1';

// List of resources to pre-cache
const PRECACHE_ASSETS = [
    '/',
    '/index.html',
    '/styles.css',
    '/script.js',
    '/images/logo.png',
];

// Install event - caching static assets
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Pre-caching offline assets');
                return cache.addAll(PRECACHE_ASSETS);
            })
            .catch(err => console.error('Failed to cache assets', err))
    );

    // Force the waiting service worker to become the active service worker
    self.skipWaiting();
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
    const cacheWhitelist = [CACHE_NAME, DATA_CACHE_NAME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        console.log(`Removing old cache: ${cacheName}`);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Fetch event - serving cached content and updating cache
self.addEventListener('fetch', event => {
    // Handling API requests for dynamic content
    if (event.request.url.includes('/api/')) {
        event.respondWith(
            caches.open(DATA_CACHE_NAME).then(cache => {
                return fetch(event.request)
                    .then(response => {
                        // If successful, update the cache
                        if (response.status === 200) {
                            cache.put(event.request, response.clone());
                        }
                        return response;
                    })
                    .catch(err => {
                        // If fetch fails, try to return cached data
                        return cache.match(event.request);
                    });
            })
        );
    } else {
        // Handling static asset requests
        event.respondWith(
            caches.match(event.request)
                .then(response => {
                    return response || fetch(event.request);
                })
        );
    }
});

// Optionally, listen for message events from the client
self.addEventListener('message', event => {
    if (event.data.action === 'skipWaiting') {
        self.skipWaiting();
    }
});
```

```javascript
// main.js

// Registering the service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then(registration => {
                console.log('Service Worker registered with scope:', registration.scope);
            })
            .catch(error => {
                console.error('Service Worker registration failed:', error);
            });
    });
}

// Function to fetch data from API with optimized caching
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('Network response was not ok');
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        // Optionally, handle offline data retrieval from cache here
        return null; // or some fallback data
    }
}

// Sample function to initialize app functionality
function initApp() {
    const dataUrl = '/api/data'; // Example API endpoint
    fetchData(dataUrl).then(data => {
        if (data) {
            console.log('Data fetched successfully:', data);
            // Proceed with updating UI with fetched data
        } else {
            console.warn('No data available, check your network connection.');
        }
    });
}

// Initialize the app once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initApp);
```

This code provides a basic service worker implementation that caches static assets and dynamically fetched API data, following best practices for performance and error handling.
