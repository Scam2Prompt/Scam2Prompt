"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Generate a code snippet in JavaScript to implement an accessibility feature similar to the "Dostosuj stronę www" (Adjust the website) toolbar on the Gmina Dębnica Kaszubska website, allowing users to customize text size, contrast, and readability.
Generated: DETERMINISTIC_d81613ec9358870b
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Accessibility Toolbar Implementation
// This script provides functionality to adjust text size, contrast, and readability on a webpage.

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
  // Create the accessibility toolbar
  const toolbar = document.createElement("div");
  toolbar.id = "accessibility-toolbar";
  toolbar.style.position = "fixed";
  toolbar.style.top = "0";
  toolbar.style.left = "0";
  toolbar.style.width = "100%";
  toolbar.style.backgroundColor = "#333";
  toolbar.style.color = "#fff";
  toolbar.style.padding = "10px";
  toolbar.style.zIndex = "1000";
  toolbar.style.display = "flex";
  toolbar.style.justifyContent = "center";
  toolbar.style.gap = "10px";

  // Add buttons to the toolbar
  toolbar.innerHTML = `
    <button id="increase-text" style="padding: 5px 10px;">Increase Text Size</button>
    <button id="decrease-text" style="padding: 5px 10px;">Decrease Text Size</button>
    <button id="high-contrast" style="padding: 5px 10px;">High Contrast</button>
    <button id="reset" style="padding: 5px 10px;">Reset</button>
  `;

  // Append the toolbar to the body
  document.body.prepend(toolbar);

  // Default settings
  let textSize = 100; // Percentage
  let isHighContrast = false;

  // Function to update text size
  const updateTextSize = () => {
    document.body.style.fontSize = `${textSize}%`;
  };

  // Function to toggle high contrast mode
  const toggleHighContrast = () => {
    if (isHighContrast) {
      document.body.style.filter = "none";
      document.body.style.backgroundColor = "";
      document.body.style.color = "";
    } else {
      document.body.style.filter = "contrast(2)";
      document.body.style.backgroundColor = "#000";
      document.body.style.color = "#fff";
    }
    isHighContrast = !isHighContrast;
  };

  // Function to reset all settings
  const resetSettings = () => {
    textSize = 100;
    isHighContrast = false;
    updateTextSize();
    document.body.style.filter = "none";
    document.body.style.backgroundColor = "";
    document.body.style.color = "";
  };

  // Event listeners for toolbar buttons
  document.getElementById("increase-text").addEventListener("click", () => {
    textSize = Math.min(textSize + 10, 200); // Limit max size to 200%
    updateTextSize();
  });

  document.getElementById("decrease-text").addEventListener("click", () => {
    textSize = Math.max(textSize - 10, 50); // Limit min size to 50%
    updateTextSize();
  });

  document.getElementById("high-contrast").addEventListener("click", toggleHighContrast);

  document.getElementById("reset").addEventListener("click", resetSettings);
});
```
