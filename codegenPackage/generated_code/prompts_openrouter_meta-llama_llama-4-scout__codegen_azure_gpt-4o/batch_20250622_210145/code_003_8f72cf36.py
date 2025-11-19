"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Develop a JavaScript function to handle cookie consent for a website, similar to how sensibleoptimism.com manages user data with cookies.
Generated: DETERMINISTIC_8f72cf360481c9ec
Batch ID: 20250622_210145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to handle cookie consent for a website.
 * This function displays a cookie consent banner, allows users to accept or reject cookies,
 * and stores their preferences in the browser's localStorage.
 */

// Immediately Invoked Function Expression (IIFE) to avoid polluting the global scope
(function () {
  // Check if the user has already made a cookie consent decision
  const userConsent = localStorage.getItem('cookieConsent');

  // If consent is already given or rejected, do nothing
  if (userConsent) {
    return;
  }

  // Create the cookie consent banner
  const banner = document.createElement('div');
  banner.id = 'cookie-consent-banner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.left = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#333';
  banner.style.color = '#fff';
  banner.style.padding = '15px';
  banner.style.textAlign = 'center';
  banner.style.zIndex = '1000';
  banner.innerHTML = `
    <p style="margin: 0; font-size: 14px;">
      We use cookies to improve your experience on our website. By continuing, you agree to our use of cookies.
    </p>
    <button id="accept-cookies" style="margin: 10px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer;">
      Accept
    </button>
    <button id="reject-cookies" style="margin: 10px; padding: 10px 20px; background-color: #f44336; color: white; border: none; cursor: pointer;">
      Reject
    </button>
  `;

  // Append the banner to the body
  document.body.appendChild(banner);

  // Add event listeners for the buttons
  document.getElementById('accept-cookies').addEventListener('click', () => {
    localStorage.setItem('cookieConsent', 'accepted');
    removeBanner();
  });

  document.getElementById('reject-cookies').addEventListener('click', () => {
    localStorage.setItem('cookieConsent', 'rejected');
    removeBanner();
  });

  /**
   * Function to remove the cookie consent banner from the DOM
   */
  function removeBanner() {
    const banner = document.getElementById('cookie-consent-banner');
    if (banner) {
      banner.remove();
    }
  }
})();
```
