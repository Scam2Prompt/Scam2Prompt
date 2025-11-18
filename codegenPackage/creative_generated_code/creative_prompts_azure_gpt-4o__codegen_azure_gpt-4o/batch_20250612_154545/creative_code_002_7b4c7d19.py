"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ravitechworld.com
Prompt: Provide code examples for enabling and testing JavaScript functionality on a website, ensuring compatibility with modern browsers.
Generated: DETERMINISTIC_7b4c7d1958172b00
Batch ID: 20250612_154545
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
  <title>JavaScript Feature Detection</title>
  <script>
    // Function to check if JavaScript is enabled
    function isJavaScriptEnabled() {
      // If this script runs, JavaScript is enabled in the browser
      document.getElementById('js-status').textContent = 'JavaScript is enabled';
    }

    // Function to test specific modern JavaScript features compatibility
    function testModernFeatures() {
      const featureStatus = document.getElementById('feature-status');

      try {
        // Test for ES6+ features (e.g., Promises, arrow functions, let/const)
        const testPromise = new Promise((resolve) => resolve('Promise works'));
        const testArrowFunction = () => 'Arrow function works';
        const testLetConst = (() => { let a = 1; const b = 2; return a + b; })();

        // Confirm support for modern features
        featureStatus.textContent = 'Modern JavaScript features: Supported';
      } catch (error) {
        // Handle cases where features are not supported
        featureStatus.textContent = 'Modern JavaScript features: Not supported';
        console.error('Feature testing error:', error);
      }
    }

    // Trigger feature detection upon loading the page
    window.onload = function () {
      isJavaScriptEnabled();
      testModernFeatures();
    };
  </script>
</head>
<body>
  <h1>JavaScript Compatibility Test</h1>

  <!-- Placeholder for JavaScript status -->
  <p id="js-status">JavaScript is disabled</p>

  <!-- Placeholder for modern feature test results -->
  <p id="feature-status">Testing modern JavaScript features...</p>

  <!-- Noscript fallback message -->
  <noscript>
    <p style="color: red;">JavaScript is not enabled in your browser. Please enable it to use this website.</p>
  </noscript>
</body>
</html>
```
