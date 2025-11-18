"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darlic.com
Prompt: Write code to create a progressive web application using Darlic® progressive web application builder. Ensure the application works offline and is optimized for mobile-first design.
Generated: DETERMINISTIC_1be559adf41c37a4
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Register the service worker for offline capabilities
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

// Main application logic
document.addEventListener('DOMContentLoaded', () => {
    // Initialize the app
    initializeApp();
});

/**
 * Initializes the application
 */
function initializeApp() {
    try {
        // Set up mobile-first design
        setupMobileDesign();

        // Load application data
        loadData();

        // Setup event listeners
        setupEventListeners();
    } catch (error) {
        console.error('Error initializing the application:', error);
    }
}

/**
 * Sets up the mobile-first design
 */
function setupMobileDesign() {
    // Apply mobile-first styles
    document.body.classList.add('mobile-design');
}

/**
 * Loads application data
 */
async function loadData() {
    try {
        const response = await fetch('/api/data');
        if (!response.ok) {
            throw new Error('Network response was not ok' + response.statusText);
        }
        const data = await response.json();
        renderData(data);
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

/**
 * Renders the data to the UI
 * @param {Object} data - The data to render
 */
function renderData(data) {
    const container = document.getElementById('data-container');
    container.innerHTML = ''; // Clear previous data

    data.forEach(item => {
        const div = document.createElement('div');
        div.className = 'data-item';
        div.textContent = item.name; // Assuming each item has a 'name' property
        container.appendChild(div);
    });
}

/**
 * Sets up event listeners for interactive elements
 */
function setupEventListeners() {
    const refreshButton = document.getElementById('refresh-button');
    refreshButton.addEventListener('click', () => {
        loadData();
    });
}

// Sample service worker (service-worker.js)
/*
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('app-cache').then(cache => {
            return cache.addAll([
                '/',
                '/index.html',
                '/styles.css',
                '/app.js',
                '/api/data'
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
*/

// Sample CSS for mobile-first design (styles.css)
/*
body.mobile-design {
    font-family: Arial, sans-serif;
    padding: 1em;
}

.data-item {
    border: 1px solid #ccc;
    margin: 0.5em 0;
    padding: 1em;
    border-radius: 5px;
}
*/
```

Make sure to configure your server to serve the appropriate paths to the service worker and other assets.
