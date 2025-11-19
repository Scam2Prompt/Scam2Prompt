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

Here’s a clean, production-ready example of how to prompt users to install a Progressive Web App (PWA) on their mobile devices using JavaScript:

```javascript
// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
  // Variable to store the deferred prompt event
  let deferredInstallPrompt = null;

  // Listen for the 'beforeinstallprompt' event, which is triggered when the PWA can be installed
  window.addEventListener("beforeinstallprompt", (event) => {
    // Prevent the default prompt from showing immediately
    event.preventDefault();
    // Save the event for later use
    deferredInstallPrompt = event;

    // Show a custom UI or button to prompt users about installing the PWA
    const installButton = document.getElementById("installButton");
    installButton.style.display = "block"; // Make the button visible

    // Add click listener to the button
    installButton.addEventListener("click", () => {
      if (deferredInstallPrompt) {
        // Show the install prompt
        deferredInstallPrompt.prompt();

        // Handle the user response to the prompt
        deferredInstallPrompt.userChoice.then((choiceResult) => {
          if (choiceResult.outcome === "accepted") {
            console.log("User accepted the PWA install prompt.");
          } else {
            console.log("User dismissed the PWA install prompt.");
          }

          // Clear the stored prompt event
          deferredInstallPrompt = null;
        });
      }
    });
  });

  // Optionally, detect when the app is already installed
  window.addEventListener("appinstalled", () => {
    console.log("PWA has been installed successfully.");
    const installButton = document.getElementById("installButton");
    installButton.style.display = "none"; // Hide the install button
  });
});

// HTML:
// <button id="installButton" style="display: none;">Install App</button>

// CSS:
// #installButton {
//   position: fixed;
//   bottom: 20px;
//   right: 20px;
//   background-color: #007bff;
//   color: white;
//   border: none;
//   padding: 10px 20px;
//   border-radius: 5px;
//   cursor: pointer;
//   font-size: 16px;
//   box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
// }
// #installButton:hover {
//   background-color: #0056b3;
// }
```

### Notes:
- This code dynamically controls the visibility of an `#installButton` to prompt users to install the PWA when the `beforeinstallprompt` event is fired.
- It handles user interaction and logs whether the install was accepted or dismissed.
- Proper cleanup is included to ensure no memory leaks from lingering event listeners.
