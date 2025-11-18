"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Write code to detect if a user is accessing a Progressive Web App (PWA) like friend.tech and provide instructions for adding it to the home screen on Chrome browsers.
Generated: DETERMINISTIC_0f61277fcce3e40b
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PWA Home Screen Prompt</title>
    <link rel="manifest" href="/manifest.json">
    <style>
        #install-prompt {
            display: none; /* Hidden by default */
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 5px;
            z-index: 1000;
        }
    </style>
</head>

<body>
    <h1>Welcome to the PWA Example!</h1>
    <div id="install-prompt">
        <p>To add this app to your home screen:</p>
        <ul>
            <li>Tap the menu button (three dots) in the top right corner.</li>
            <li>Select "Add to Home screen".</li>
        </ul>
    </div>

    <script>
        // Check if the browser supports service workers and if this is a PWA
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/service-worker.js').then(() => {
                    console.log('Service Worker registered successfully.');
                }).catch((error) => {
                    console.error('Service Worker registration failed:', error);
                });
            });
        }

        // Variables to track the PWA installation prompt
        let deferredPrompt;

        // Listen for the 'beforeinstallprompt' event
        window.addEventListener('beforeinstallprompt', (e) => {
            // Prevent Chrome 67 and earlier from automatically showing the prompt
            e.preventDefault();
            // Stash the event so it can be triggered later
            deferredPrompt = e;

            // Show the install prompt
            document.getElementById('install-prompt').style.display = 'block';
        });

        // Optional: Handle the install button click (not shown in UI here)
        document.getElementById('install-prompt').addEventListener('click', () => {
            if (deferredPrompt) {
                // Show the install prompt
                deferredPrompt.prompt();
                // Wait for the user to respond to the prompt
                deferredPrompt.userChoice.then((choiceResult) => {
                    if (choiceResult.outcome === 'accepted') {
                        console.log('User accepted the A2HS prompt');
                    } else {
                        console.log('User dismissed the A2HS prompt');
                    }
                    // Clear the deferredPrompt variable, since it can only be used once
                    deferredPrompt = null;
                });
            }
        });

    </script>
</body>

</html>
```

This code implements a basic Progressive Web App (PWA) structure that detects if the user can add the app to their home screen on Chrome. It uses the `beforeinstallprompt` event to manage the installation prompt and provides clear instructions for the user. Proper error handling and comments are included for clarity and maintainability.
