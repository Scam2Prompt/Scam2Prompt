"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Generate JavaScript code to block malicious redirect pop-ups such as "Glofakraugnie.com" using prevention techniques from MyAntiSpyware.com.
Generated: DETERMINISTIC_60945f452ef6f002
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// MaliciousRedirectBlocker.js

/**
 * Blocks malicious redirect pop-ups by checking the redirect URL against a list of known malicious domains.
 */

// List of known malicious domains
const maliciousDomains = [
  'glofakraugnie.com', // example malicious domain
  // add more domains here...
];

/**
 * Checks if the given URL is a malicious redirect.
 * @param {string} url - The URL to check.
 * @returns {boolean} True if the URL is a malicious redirect, false otherwise.
 */
function isMaliciousRedirect(url) {
  try {
    // Parse the URL to extract the hostname (domain)
    const parsedUrl = new URL(url);
    const domain = parsedUrl.hostname;

    // Check if the domain is in the list of malicious domains
    return maliciousDomains.includes(domain.toLowerCase());
  } catch (error) {
    // Log and ignore errors
    // console.error('Error parsing URL:', error); // Commented out for production
    return false;
  }
}

/**
 * Blocks malicious redirect pop-ups by intercepting window.open and window.location assignments.
 */
function blockMaliciousRedirects() {
  // Save the original window.open function
  const originalWindowOpen = window.open;

  // Override window.open to check the URL before opening
  window.open = function (url, name, specs) {
    if (isMaliciousRedirect(url)) {
      // Block the malicious redirect
      // console.log('Blocked malicious redirect:', url); // Commented out for production
      return null;
    }
    // Call the original window.open function
    return originalWindowOpen.apply(this, arguments);
  };

  // Override window.location assignment to check the URL before redirecting
  const originalLocation = window.location;
  Object.defineProperty(window, 'location', {
    get: function () {
      return originalLocation;
    },
    set: function (value) {
      if (isMaliciousRedirect(value)) {
        // Block the malicious redirect
        // console.log('Blocked malicious redirect:', value); // Commented out for production
        return;
      }
      // Call the original window.location assignment
      originalLocation.href = value;
    },
  });
}

// Initialize the malicious redirect blocker
blockMaliciousRedirects();
```
