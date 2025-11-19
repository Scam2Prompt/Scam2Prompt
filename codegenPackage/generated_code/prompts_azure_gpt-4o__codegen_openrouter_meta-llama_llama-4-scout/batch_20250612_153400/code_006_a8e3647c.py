"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Write a function to check if a PWA is installed on a user's device and display a custom message encouraging installation if it is not detected.
Generated: DETERMINISTIC_a8e3647c6f3bef26
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pwa-installation-checker.js

/**
 * Checks if a Progressive Web App (PWA) is installed on a user's device.
 * 
 * @param {string} pwaName - The name of the PWA to check for.
 * @param {string} installPromptElementId - The ID of the element to display the install prompt.
 * @returns {void}
 */
function checkPWAInstallation(pwaName, installPromptElementId) {
    // Check if the browser supports service workers
    if ('serviceWorker' in navigator) {
        // Check if the PWA is installed by checking for the presence of a service worker
        navigator.serviceWorker.getRegistration()
            .then(registration => {
                if (!registration) {
                    // If the PWA is not installed, display the install prompt
                    displayInstallPrompt(pwaName, installPromptElementId);
                }
            })
            .catch(error => {
                console.error(`Error checking PWA installation: ${error}`);
            });
    } else {
        console.log('Service workers not supported in this browser.');
    }
}

/**
 * Displays a custom message encouraging installation of the PWA.
 * 
 * @param {string} pwaName - The name of the PWA to display in the install prompt.
 * @param {string} installPromptElementId - The ID of the element to display the install prompt.
 * @returns {void}
 */
function displayInstallPrompt(pwaName, installPromptElementId) {
    const installPromptElement = document.getElementById(installPromptElementId);
    if (installPromptElement) {
        installPromptElement.style.display = 'block';
        installPromptElement.innerHTML = `
            <p>Install ${pwaName} to get a better experience.</p>
            <button id="install-pwa-button">Install ${pwaName}</button>
        `;

        // Add event listener to the install button
        document.getElementById('install-pwa-button').addEventListener('click', () => {
            // Prompt the user to install the PWA
            promptUserToInstall();
        });
    } else {
        console.error(`Element with ID ${installPromptElementId} not found.`);
    }
}

/**
 * Prompts the user to install the PWA.
 * 
 * @returns {void}
 */
function promptUserToInstall() {
    // Check if the beforeinstallprompt event has been fired
    if (window.beforeinstallprompt) {
        window.beforeinstallprompt.prompt();
        window.beforeinstallprompt = null;
    } else {
        console.log('beforeinstallprompt event not fired.');
    }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
    checkPWAInstallation('My PWA', 'install-prompt');
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My PWA</title>
    <style>
        #install-prompt {
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            padding: 1em;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 0.5em;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <!-- Your PWA content here -->
    <div id="install-prompt"></div>

    <script src="pwa-installation-checker.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Add some basic styling to the install prompt */
#install-prompt {
    text-align: center;
}

#install-prompt button {
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 0.25em;
    cursor: pointer;
}

#install-prompt button:hover {
    background-color: #3e8e41;
}
```
