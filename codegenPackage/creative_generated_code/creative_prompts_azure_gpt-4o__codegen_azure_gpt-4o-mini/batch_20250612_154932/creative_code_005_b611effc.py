"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darlic.com
Prompt: Provide a step-by-step guide to convert an existing website into a progressive web application using Darlic® tools, highlighting offline functionality.
Generated: DETERMINISTIC_b611effc2dd49a5f
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Darlic® tools package
import { Darlic, ServiceWorker, OfflineSupport } from 'darlic-tools';

// Initialize Darlic with website configuration
const darlic = new Darlic({
    name: 'My PWA',
    shortName: 'PWA',
    startUrl: '/',
    display: 'standalone',
    backgroundColor: '#ffffff',
    themeColor: '#000000',
    icons: [
        {
            src: 'icon-192x192.png',
            sizes: '192x192',
            type: 'image/png'
        },
        {
            src: 'icon-512x512.png',
            sizes: '512x512',
            type: 'image/png'
        }
    ]
});

// Register the service worker for offline functionality
const registerServiceWorker = async () => {
    try {
        const registration = await ServiceWorker.register('/service-worker.js');
        console.log('Service Worker registered successfully:', registration);
    } catch (error) {
        console.error('Service Worker registration failed:', error);
    }
};

// Create a service worker file for caching assets
const createServiceWorkerFile = () => {
    const serviceWorkerContent = `
    self.addEventListener('install', event => {
        event.waitUntil(
            caches.open('my-pwa-cache').then(cache => {
                return cache.addAll([
                    '/',
                    '/index.html',
                    '/styles.css',
                    '/script.js',
                    '/icon-192x192.png',
                    '/icon-512x512.png'
                ]);
            })
        );
    });

    self.addEventListener('fetch', event => {
        event.respondWith(
            caches.match(event.request)
                .then(response => {
                    // Return cached response if found, otherwise fetch from network
                    return response || fetch(event.request);
                })
        );
    });
    `;

    // Write the service worker content to a file
    require('fs').writeFileSync('service-worker.js', serviceWorkerContent);
};

// Handle offline functionality using Darlic's OfflineSupport
const setupOfflineSupport = () => {
    OfflineSupport.enable({
        strategy: 'cache-first', // Use cache-first strategy for better offline experience
        cacheName: 'my-pwa-cache'
    });
};

// Execute the functions to set up the PWA
const initializePWA = async () => {
    createServiceWorkerFile(); // Create the service worker file
    await registerServiceWorker(); // Register the service worker
    setupOfflineSupport(); // Enable offline support
};

// Start the PWA initialization
initializePWA().catch(error => {
    console.error('PWA initialization failed:', error);
});
```
