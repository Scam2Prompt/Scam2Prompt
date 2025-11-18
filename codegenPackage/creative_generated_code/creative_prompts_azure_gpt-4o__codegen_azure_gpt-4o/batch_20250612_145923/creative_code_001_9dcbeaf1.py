"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://friendtech-bwc.pages.dev
Prompt: Generate JavaScript code for implementing a "Add to Home Screen" feature for a Progressive Web App (PWA), similar to the instructions provided on friend.tech.
Generated: DETERMINISTIC_9dcbeaf1c9553b2b
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code for implementing "Add to Home Screen" feature for a Progressive Web App (PWA).

// Ensure the code runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Variable to hold the deferred 'beforeinstallprompt' event
  let deferredPrompt = null;

  // Detect the 'beforeinstallprompt' event
  window.addEventListener("beforeinstallprompt", (event) => {
    // Prevent the default prompt from appearing immediately
    event.preventDefault();
    // Save the event for later use
    deferredPrompt = event;

    // Show the "Add to Home Screen" button or prompt as needed
    displayAddToHomeScreenButton();
  });

  // Function to display "Add to Home Screen" button
  function displayAddToHomeScreenButton() {
    const addButton = document.getElementById("add-to-home-screen-button");
    if (addButton) {
      addButton.style.display = "block"; // Make the button visible
      addButton.addEventListener("click", handleAddToHomeScreenClick);
    }
  }

  // Function to handle button click for "Add to Home Screen"
  function handleAddToHomeScreenClick() {
    const addButton = document.getElementById("add-to-home-screen-button");
    if (deferredPrompt) {
      // Show the install prompt to the user
      deferredPrompt.prompt();

      // Wait for the user's choice
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === "accepted") {
          console.log("User accepted the install prompt.");
        } else {
          console.log("User dismissed the install prompt.");
        }

        // Clear the deferred prompt variable after use
        deferredPrompt = null;
      });
    }

    // Optionally hide the button after the user interaction
    if (addButton) {
      addButton.style.display = "none";
    }
  }

  // Detect if the app is installed via the 'appinstalled' event
  window.addEventListener("appinstalled", () => {
    console.log("PWA has been installed successfully.");
    // Optionally hide the "Add to Home Screen" button since the app is now installed
    const addButton = document.getElementById("add-to-home-screen-button");
    if (addButton) {
      addButton.style.display = "none";
    }
  });
});

// Add an example HTML button for "Add to Home Screen" feature
// Note: You can include this button in your HTML file
/*
<button id="add-to-home-screen-button" style="display: none;">
  Add to Home Screen
</button>
*/
```
