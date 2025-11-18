"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-doggotothemoon.pages.dev
Prompt: Write code to implement a feature that installs a PWA for interacting with digital asset collections, as described on the Ord.io platform.
Generated: DETERMINISTIC_cb0297be85eee13f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useEffect } from 'react';
import { registerSW } from 'virtual:pwa-register';

// Main App component
const App = () => {
  // Register service worker for PWA functionality
  const { update, refetch } = registerSW({
    onNeedRefresh() {
      console.log('New content available, please refresh.');
    },
    onOfflineReady() {
      console.log('App is ready for offline use.');
    },
  });

  // Effect to handle updates to the service worker
  useEffect(() => {
    const handleUpdate = () => {
      if (confirm('New version available! Would you like to update?')) {
        update().catch(error => {
          console.error('Error updating the service worker:', error);
        });
      }
    };

    // Listen for updates
    window.addEventListener('update', handleUpdate);

    // Clean up listener on component unmount
    return () => {
      window.removeEventListener('update', handleUpdate);
    };
  }, [update]);

  return (
    <div className="App">
      <h1>Digital Asset Collection</h1>
      <p>Interact with your digital asset collections using this PWA.</p>
      <button onClick={refetch}>Refresh Data</button>
    </div>
  );
};

// Main render function
const rootElement = document.getElementById('root');
if (rootElement) {
  ReactDOM.render(<App />, rootElement);
} else {
  console.error('Root element not found. Ensure the HTML contains an element with id "root".');
}

// Service Worker Registration in `service-worker.js`

self.addEventListener('install', (event) => {
  console.log('Service Worker: Installing...');
  event.waitUntil(self.skipWaiting()); // Skips waiting state to activate immediately
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activating...');
  event.waitUntil(clients.claim()); // Claim control over all clients
});

self.addEventListener('fetch', (event) => {
  // Cache-first strategy
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        return response || fetch(event.request)
          .then((fetchResponse) => {
            return caches.open('dynamic-cache')
              .then((cache) => {
                cache.put(event.request, fetchResponse.clone());
                return fetchResponse;
              });
          });
      })
      .catch((error) => {
        console.error('Fetch failed; returning offline page instead.', error);
        return caches.match('/offline.html'); // Fallback to offline page
      })
  );
});

// Note: Make sure to create 'offline.html' and the required assets in your public folder for the PWA to work offline.
```
