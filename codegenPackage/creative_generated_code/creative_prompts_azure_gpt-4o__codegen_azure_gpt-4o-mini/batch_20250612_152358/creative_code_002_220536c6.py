"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dorgbglgn.pages.dev
Prompt: Generate JavaScript code to detect and install the Ord.io PWA for accessing Dog Runestone Snapshot functionality.
Generated: DETERMINISTIC_220536c6a3c7e470
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the service worker is supported by the browser
if ('serviceWorker' in navigator) {
    // Register the service worker
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

// Function to check if the PWA can be installed
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later
    deferredPrompt = e;
    // Show the install button or some UI to prompt the user
    showInstallButton();
});

// Function to show the install button
function showInstallButton() {
    const installButton = document.getElementById('installButton');
    installButton.style.display = 'block';
    
    installButton.addEventListener('click', () => {
        // Hide the button after clicking
        installButton.style.display = 'none';
        // Show the prompt
        deferredPrompt.prompt();
        // Wait for the user to respond to the prompt
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the A2HS prompt');
            } else {
                console.log('User dismissed the A2HS prompt');
            }
            deferredPrompt = null;
        });
    });
}

// Function to handle the PWA installation success
window.addEventListener('appinstalled', () => {
    console.log('PWA was installed');
});

// Add any additional UI management or functionality as needed
// For example, provide feedback to the user or handle specific app states
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ord.io PWA Installer</title>
</head>
<body>
    <h1>Install the Ord.io PWA</h1>
    <button id="installButton" style="display:none;">Install Ord.io</button>
    <script src="your-script.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```
