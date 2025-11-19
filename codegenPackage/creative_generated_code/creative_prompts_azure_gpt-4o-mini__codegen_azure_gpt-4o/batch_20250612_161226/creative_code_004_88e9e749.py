"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: How do I create a JavaScript function that checks for the presence of JavaScript on a webpage like Magic Eden?
Generated: DETERMINISTIC_88e9e7499f7cb5d8
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and present on a webpage
 * by attempting to query a DOM element unique to the page (e.g., Magic Eden).
 *
 * @returns {Promise<boolean>} - Resolves to true if JavaScript is enabled and the element is found, otherwise false.
 */
async function isJavaScriptEnabledOnMagicEden() {
  try {
    // Wait for the DOM to fully load
    await new Promise((resolve) => {
      if (document.readyState === 'complete') {
        resolve();
      } else {
        window.addEventListener('load', resolve);
      }
    });

    // Query for a unique DOM element on the Magic Eden page
    const uniqueElementSelector = '[data-testid="magic-eden-unique-element"]'; // Replace with an actual unique selector
    const element = document.querySelector(uniqueElementSelector);

    // Check if the element exists
    if (element) {
      return true; // JavaScript is enabled and the unique element was found
    } else {
      return false; // JavaScript is enabled but the unique element was not found
    }
  } catch (error) {
    console.error('Error occurred while checking for JavaScript presence:', error);
    return false; // Return false if an error occurs
  }
}

// Example usage
isJavaScriptEnabledOnMagicEden()
  .then((isEnabled) => {
    console.log(`JavaScript presence on Magic Eden: ${isEnabled ? 'Enabled' : 'Disabled or Not Found'}`);
  })
  .catch((err) => {
    console.error('Unexpected error:', err);
  });
```
