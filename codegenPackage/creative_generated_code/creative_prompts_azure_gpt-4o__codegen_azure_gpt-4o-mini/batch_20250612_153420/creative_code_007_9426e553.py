"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dggieecoins.pages.dev
Prompt: Create a JavaScript code snippet to enable users to install the Ord.io PWA directly from a webpage, emphasizing its use for accessing snapshots like "Dog Runestone Snapshot."
Generated: DETERMINISTIC_9426e553fced0712
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the service worker is supported in the browser
if ('serviceWorker' in navigator && 'BeforeInstallPromptEvent' in window) {
    // Register the service worker
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then(registration => {
                console.log('Service Worker registered with scope:', registration.scope);
            })
            .catch(error => {
                console.error('Service Worker registration failed:', error);
            });
    });

    let deferredPrompt; // Variable to hold the deferred prompt event

    // Listen for the 'beforeinstallprompt' event
    window.addEventListener('beforeinstallprompt', (e) => {
        // Prevent the mini-info bar from appearing on mobile
        e.preventDefault();
        // Stash the event so it can be triggered later
        deferredPrompt = e;
        
        // Show a custom install button (make sure this is included in your HTML)
        const installButton = document.getElementById('installButton');
        installButton.style.display = 'block'; // Show the button

        // Handle the install button click
        installButton.addEventListener('click', async () => {
            installButton.style.display = 'none'; // Hide the button
            // Show the install prompt
            deferredPrompt.prompt();
            // Wait for the user to respond to the prompt
            const { outcome } = await deferredPrompt.userChoice;
            // Handle the user's choice
            if (outcome === 'accepted') {
                console.log('User accepted the A2HS prompt');
            } else {
                console.log('User dismissed the A2HS prompt');
            }
            deferredPrompt = null; // Clear the prompt variable
        });
    });
    
    // Optional: Handle the app being installed
    window.addEventListener('appinstalled', (e) => {
        console.log('PWA was installed');
        // Optionally inform the user of the successful installation
    });
} else {
    console.warn('PWA installation is not supported in this browser.');
}
```

```html
<!-- Include this button in your HTML to trigger the install prompt -->
<button id="installButton" style="display: none;">Install Ord.io PWA</button>
```

```javascript
// Ensure you have a service worker file at the specified path
// Example service-worker.js content is required for full functionality
```
