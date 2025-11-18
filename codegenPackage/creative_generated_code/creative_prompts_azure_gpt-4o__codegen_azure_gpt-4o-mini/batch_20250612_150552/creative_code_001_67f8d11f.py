"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collect-6tp.pages.dev
Prompt: Generate JavaScript code to implement a "Add to Home Screen" feature for a Progressive Web App (PWA), including instructions for Chrome browser users, as outlined on the friend.tech website.
Generated: DETERMINISTIC_67f8d11fd4c48994
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the browser supports the 'beforeinstallprompt' event
let deferredPrompt;

// Function to handle the 'beforeinstallprompt' event
window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the mini-info bar from appearing on mobile
    e.preventDefault();
    // Stash the event so it can be triggered later
    deferredPrompt = e;
    
    // Show the Add to Home Screen button or similar UI element
    showAddToHomeScreenButton();
});

// Function to show the Add to Home Screen button
function showAddToHomeScreenButton() {
    const a2hsButton = document.getElementById('add-to-home-screen');
    a2hsButton.style.display = 'block'; // Show button

    // Add click event listener to the button
    a2hsButton.addEventListener('click', async () => {
        // Hide the button after the first click
        a2hsButton.style.display = 'none';

        // Show the install prompt
        if (deferredPrompt) {
            deferredPrompt.prompt();
            // Wait for the user to respond to the prompt
            const { outcome } = await deferredPrompt.userChoice;
            // Log the outcome of the user's choice
            console.log(`User response to the A2HS prompt: ${outcome}`);
            // Clear the deferredPrompt variable
            deferredPrompt = null;
        }
    });
}

// Function to hide the Add to Home Screen button
function hideAddToHomeScreenButton() {
    const a2hsButton = document.getElementById('add-to-home-screen');
    a2hsButton.style.display = 'none'; // Hide button
}

// Check if the app is already installed
window.addEventListener('appinstalled', (evt) => {
    console.log('PWA was installed');
    hideAddToHomeScreenButton();
});

// Call this function on page load to set up event listeners
function init() {
    // Hide the button initially
    hideAddToHomeScreenButton();
}

// Initialize the script once the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', init);
```

```html
<!-- Include this HTML snippet in your body -->
<div id="add-to-home-screen" style="display: none;">
    <button>Add to Home Screen</button>
</div>
``` 

### Instructions for Chrome users:
1. When the "Add to Home Screen" prompt appears, click on the "Add" button.
2. Alternatively, you can tap on the three-dot menu in the top-right corner of Chrome, and select "Add to Home screen".
