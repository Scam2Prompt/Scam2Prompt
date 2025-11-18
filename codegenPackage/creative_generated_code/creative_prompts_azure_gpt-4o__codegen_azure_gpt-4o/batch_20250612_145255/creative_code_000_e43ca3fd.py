"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimfriend.pages.dev
Prompt: Write JavaScript code to detect if a user is accessing a webpage on Chrome and display a prompt to "Add to Home Screen" using the browser's Install App feature, as described on friend.tech.
Generated: DETERMINISTIC_e43ca3fda1304e05
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the browser is Chrome and determine if the "Add to Home Screen" feature can be used
document.addEventListener('DOMContentLoaded', () => {
    // Detect if the browser is Chrome
    const isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);

    // Variable to store the deferred prompt event for later use
    let deferredPrompt;

    if (isChrome) {
        // Listen for the `beforeinstallprompt` event
        window.addEventListener('beforeinstallprompt', (event) => {
            // Prevent the default mini-infobar from appearing
            event.preventDefault();

            // Save the event for triggering later
            deferredPrompt = event;

            // Display a custom prompt to the user
            displayAddToHomeScreenPrompt();
        });

        // Function to display a custom "Add to Home Screen" prompt
        function displayAddToHomeScreenPrompt() {
            // Example: Display a custom message to the user
            const promptBanner = document.createElement('div');
            promptBanner.style.position = 'fixed';
            promptBanner.style.bottom = '20px';
            promptBanner.style.left = '50%';
            promptBanner.style.transform = 'translateX(-50%)';
            promptBanner.style.padding = '10px 20px';
            promptBanner.style.backgroundColor = '#fff';
            promptBanner.style.border = '1px solid #ccc';
            promptBanner.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.2)';
            promptBanner.style.zIndex = '1000';
            promptBanner.style.cursor = 'pointer';
            promptBanner.innerText = 'Add this app to your Home Screen! Click here.';
            document.body.appendChild(promptBanner);

            // Handle the click event on the custom prompt
            promptBanner.addEventListener('click', async () => {
                if (deferredPrompt) {
                    // Show the native prompt to the user
                    deferredPrompt.prompt();

                    // Wait for the user to respond to the prompt
                    const choiceResult = await deferredPrompt.userChoice;

                    // Log the user's choice
                    console.log(`User choice: ${choiceResult.outcome}`);

                    // Clear the deferred prompt to avoid reuse
                    deferredPrompt = null;

                    // Remove the custom prompt from the DOM
                    document.body.removeChild(promptBanner);
                }
            });
        }
    } else {
        console.log('The browser does not support the "Add to Home Screen" feature or is not Chrome.');
    }
});
```
