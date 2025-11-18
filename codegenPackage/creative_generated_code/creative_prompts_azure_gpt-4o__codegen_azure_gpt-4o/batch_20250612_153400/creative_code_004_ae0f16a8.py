"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Generate a JavaScript snippet that detects browser type and provides tailored instructions for installing a PWA like friend.tech on both Chrome and Safari.
Generated: DETERMINISTIC_ae0f16a80b4aecf7
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Detect the browser type and provide tailored instructions
 * for installing a Progressive Web App (PWA).
 */

// Function to detect the browser type
function detectBrowser() {
  const userAgent = navigator.userAgent.toLowerCase();

  if (userAgent.includes("chrome") && !userAgent.includes("edge") && !userAgent.includes("opera")) {
    return "Chrome";
  } else if (userAgent.includes("safari") && !userAgent.includes("chrome")) {
    return "Safari";
  } else {
    return "Other";
  }
}

// Function to display installation instructions for PWA
function showPWAInstructions() {
  const browser = detectBrowser();

  switch (browser) {
    case "Chrome":
      alert(
        `[Chrome Instructions]\n\n1. Open the website in Chrome.\n` +
        `2. Tap the three-dot menu (⋮) in the top-right corner.\n` +
        `3. Select "Install App" or "Add to Home Screen".\n` +
        `4. Follow the prompts to complete the installation.`
      );
      break;

    case "Safari":
      alert(
        `[Safari Instructions]\n\n1. Open the website in Safari.\n` +
        `2. Tap the "Share" icon (box with an arrow pointing up).\n` +
        `3. Scroll down and select "Add to Home Screen".\n` +
        `4. Name the app as desired and tap "Add".`
      );
      break;

    default:
      alert(
        `[General Instructions]\n\n1. Open the website in your browser.\n` +
        `2. Look for an "Install" or "Add to Home Screen" option.\n` +
        `3. Follow the browser-specific prompts to complete installation.`
      );
      break;
  }
}

// Call the function to show PWA instructions
try {
  showPWAInstructions();
} catch (error) {
  console.error("An error occurred while detecting the browser or showing instructions:", error);
  alert("Unable to detect browser or show instructions. Please try again.");
}
```
