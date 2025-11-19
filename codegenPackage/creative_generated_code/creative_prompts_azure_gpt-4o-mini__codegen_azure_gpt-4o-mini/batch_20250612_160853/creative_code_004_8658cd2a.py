"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxdx7dvv77chf5hp3hxaflijsphox6jetahbbsqma5roloogvtey.ipfs.dweb.link
Prompt: What are the best practices for prompting users to install a PWA on their mobile devices, as seen in friend.tech?
Generated: DETERMINISTIC_8658cd2a340103f9
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PWA Installation Prompt Example

// Check if the browser supports PWA installation
if ('serviceWorker' in navigator && 'Notification' in window) {
    let deferredPrompt; // Variable to hold the prompt event

    // Listen for the 'beforeinstallprompt' event
    window.addEventListener('beforeinstallprompt', (event) => {
        // Prevent the mini-info bar from appearing on mobile
        event.preventDefault();
        // Stash the event so it can be triggered later
        deferredPrompt = event;

        // Show the custom install button
        showInstallButton();
    });

    // Function to show the install button
    function showInstallButton() {
        const installButton = document.getElementById('install-button');
        installButton.style.display = 'block';

        installButton.addEventListener('click', () => {
            // Hide the button after click
            installButton.style.display = 'none';

            // Show the install prompt
            deferredPrompt.prompt();

            // Wait for the user to respond to the prompt
            deferredPrompt.userChoice.then((choiceResult) => {
                if (choiceResult.outcome === 'accepted') {
                    console.log('User accepted the A2HS prompt');
                } else {
                    console.log('User dismissed the A2HS prompt');
                }
                deferredPrompt = null; // Clear the prompt
            }).catch((error) => {
                console.error('Error during A2HS prompt:', error);
            });
        });
    }
} else {
    console.warn('This browser does not support PWA installation prompts.');
}

// Function to handle service worker registration
async function registerServiceWorker() {
    try {
        const registration = await navigator.serviceWorker.register('/sw.js');
        console.log('Service Worker registered successfully:', registration);
    } catch (error) {
        console.error('Service Worker registration failed:', error);
    }
}

// Call the function to register the service worker
registerServiceWorker();

// HTML Element for Install Button (must be included in your HTML)
// <button id="install-button" style="display: none;">Install App</button>
```

**Note:** Make sure to include a proper service worker file (`sw.js`) for the PWA to work correctly.
