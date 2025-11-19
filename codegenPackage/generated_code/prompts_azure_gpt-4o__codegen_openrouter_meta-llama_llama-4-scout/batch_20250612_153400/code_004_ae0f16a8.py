"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Generate a JavaScript snippet that detects browser type and provides tailored instructions for installing a PWA like friend.tech on both Chrome and Safari.
Generated: DETERMINISTIC_ae0f16a80b4aecf7
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BrowserDetector.js

/**
 * Detects the browser type and provides instructions for installing a PWA.
 */

// Define a function to detect the browser type
function detectBrowser() {
  // Use the navigator.userAgent property to detect the browser type
  const userAgent = navigator.userAgent.toLowerCase();

  // Check if the browser is Chrome
  if (userAgent.includes('chrome')) {
    return 'chrome';
  }
  // Check if the browser is Safari
  else if (userAgent.includes('safari') && !userAgent.includes('chrome')) {
    return 'safari';
  }
  // If the browser is not supported, return null
  else {
    return null;
  }
}

// Define a function to provide installation instructions
function provideInstallationInstructions(browserType) {
  // Define the installation instructions for each browser type
  const instructions = {
    chrome: `
      <h2>Install on Chrome:</h2>
      <ol>
        <li>Open Chrome and navigate to friend.tech</li>
        <li>Click the three vertical dots in the top right corner</li>
        <li>Select "Install friend.tech"</li>
        <li>Click "Install" to confirm</li>
      </ol>
    `,
    safari: `
      <h2>Install on Safari:</h2>
      <ol>
        <li>Open Safari and navigate to friend.tech</li>
        <li>Tap the share icon in the bottom toolbar</li>
        <li>Select "Add to Home Screen"</li>
        <li>Enter a name for the app and tap "Add"</li>
      </ol>
    `,
  };

  // Return the installation instructions for the detected browser type
  return instructions[browserType] || `
    <h2>Unsupported Browser:</h2>
    <p>Sorry, your browser is not supported. Please try using Chrome or Safari.</p>
  `;
}

// Define a function to display the installation instructions
function displayInstallationInstructions() {
  try {
    // Detect the browser type
    const browserType = detectBrowser();

    // Check if the browser type is supported
    if (browserType) {
      // Provide and display the installation instructions
      const instructions = provideInstallationInstructions(browserType);
      document.getElementById('installation-instructions').innerHTML = instructions;
    } else {
      // Display an error message if the browser type is not supported
      document.getElementById('installation-instructions').innerHTML = `
        <h2>Unsupported Browser:</h2>
        <p>Sorry, your browser is not supported. Please try using Chrome or Safari.</p>
      `;
    }
  } catch (error) {
    // Log any errors that occur
    console.error('Error displaying installation instructions:', error);
  }
}

// Call the function to display the installation instructions
document.addEventListener('DOMContentLoaded', displayInstallationInstructions);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Install PWA</title>
</head>
<body>
  <div id="installation-instructions"></div>
  <script src="BrowserDetector.js"></script>
</body>
</html>
```
