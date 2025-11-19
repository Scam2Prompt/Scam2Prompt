"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Write a function in JavaScript that simulates a loading state for a web page, inspired by the loading message on the KSA Academy site.
Generated: DETERMINISTIC_a635c37c62aad796
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates a loading state for a web page.
 * This function displays a loading message inspired by the KSA Academy site
 * and removes it after a specified duration.
 *
 * @param {string} message - The loading message to display.
 * @param {number} duration - The duration (in milliseconds) to show the loading message.
 */
function simulateLoadingState(message = "Loading, please wait...", duration = 3000) {
  try {
    // Create a container for the loading message
    const loadingContainer = document.createElement("div");
    loadingContainer.id = "loading-container";
    loadingContainer.style.position = "fixed";
    loadingContainer.style.top = "0";
    loadingContainer.style.left = "0";
    loadingContainer.style.width = "100%";
    loadingContainer.style.height = "100%";
    loadingContainer.style.display = "flex";
    loadingContainer.style.justifyContent = "center";
    loadingContainer.style.alignItems = "center";
    loadingContainer.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
    loadingContainer.style.color = "#fff";
    loadingContainer.style.fontSize = "1.5rem";
    loadingContainer.style.zIndex = "9999";

    // Add the loading message to the container
    loadingContainer.textContent = message;

    // Append the container to the body
    document.body.appendChild(loadingContainer);

    // Remove the loading message after the specified duration
    setTimeout(() => {
      document.body.removeChild(loadingContainer);
    }, duration);
  } catch (error) {
    console.error("An error occurred while simulating the loading state:", error);
  }
}

// Example usage:
// simulateLoadingState("Loading, please wait...", 5000);
```
