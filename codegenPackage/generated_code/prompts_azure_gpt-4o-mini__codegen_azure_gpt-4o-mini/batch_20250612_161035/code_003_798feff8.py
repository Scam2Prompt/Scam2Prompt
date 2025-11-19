"""
Generated Code Metadata:
========================
Original URL: https://dorgbglgn.pages.dev
Prompt: Provide an example of how to implement the PWA for the Dog Runestone Snapshot on a website.
Generated: DETERMINISTIC_798feff855b90008
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dog Runestone Snapshot PWA</title>
    <link rel="manifest" href="/manifest.json">
    <link rel="stylesheet" href="styles.css">
    <script src="app.js" defer></script>
</head>
<body>
    <header>
        <h1>Dog Runestone Snapshot</h1>
    </header>
    <main>
        <section id="snapshot">
            <h2>Take a Snapshot</h2>
            <button id="snapshotButton">Capture Snapshot</button>
            <canvas id="canvas" width="600" height="400"></canvas>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Dog Runestone</p>
    </footer>
</body>
</html>
```

```json
// manifest.json
{
    "name": "Dog Runestone Snapshot",
    "short_name": "Dog Snapshot",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#4CAF50",
    "icons": [
        {
            "src": "icon-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "icon-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #4CAF50;
    color: white;
    padding: 10px 0;
    text-align: center;
}

main {
    padding: 20px;
}

#snapshot {
    text-align: center;
}

canvas {
    border: 1px solid #ccc;
    margin-top: 10px;
}
```

```javascript
// app.js

// Check if the service worker can be registered
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

// Function to capture a snapshot from the canvas
function captureSnapshot() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');

    // Clear the canvas before drawing
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Draw a simple representation of a dog (for demonstration)
    context.fillStyle = 'brown';
    context.fillRect(50, 50, 100, 100); // Dog body
    context.fillStyle = 'black';
    context.fillRect(70, 70, 20, 20); // Dog head

    // Log the snapshot action
    console.log('Snapshot captured!');
}

// Event listener for the snapshot button
document.getElementById('snapshotButton').addEventListener('click', captureSnapshot);
```

```javascript
// service-worker.js

// Cache version
const CACHE_NAME = 'dog-runestone-cache-v1';

// Files to cache
const CACHE_ASSETS = [
    '/',
    '/index.html',
    '/styles.css',
    '/app.js',
    '/manifest.json',
    '/icon-192x192.png',
    '/icon-512x512.png'
];

// Install event
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Caching files');
                return cache.addAll(CACHE_ASSETS);
            })
    );
});

// Fetch event
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Return cached response or fetch from network
                return response || fetch(event.request);
            })
    );
});

// Activate event
self.addEventListener('activate', event => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
```
