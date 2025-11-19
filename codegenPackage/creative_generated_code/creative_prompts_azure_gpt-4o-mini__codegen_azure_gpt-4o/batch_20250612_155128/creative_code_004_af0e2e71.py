"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mymoneymgr.com
Prompt: Provide an example of a JavaScript function that handles cookie consent for a financial management platform.
Generated: DETERMINISTIC_af0e2e71603b7a90
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles cookie consent for a financial management platform.
 * This function displays a cookie consent banner, allows users to accept or reject cookies,
 * and stores their preferences in localStorage for future visits.
 */

// Function to initialize and handle cookie consent
function handleCookieConsent() {
  // Check if cookie consent has already been provided
  const consentStatus = localStorage.getItem('cookieConsent');
  if (consentStatus === 'accepted' || consentStatus === 'rejected') {
    return; // Consent already provided, no action needed
  }

  // Create the cookie consent banner
  const banner = document.createElement('div');
  banner.id = 'cookie-consent-banner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.left = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#f4f4f4';
  banner.style.padding = '15px';
  banner.style.boxShadow = '0 -2px 5px rgba(0,0,0,0.2)';
  banner.style.zIndex = '1000';
  banner.innerHTML = `
    <p style="margin: 0; font-size: 14px;">
      We use cookies to enhance your experience and analyze website performance. By continuing to use our site, you consent to our use of cookies.
    </p>
    <div style="margin-top: 10px;">
      <button id="accept-cookies" style="background-color: #4CAF50; color: white; border: none; padding: 10px 15px; cursor: pointer;">
        Accept
      </button>
      <button id="reject-cookies" style="background-color: #f44336; color: white; border: none; padding: 10px 15px; cursor: pointer;">
        Reject
      </button>
    </div>
  `;

  // Append the banner to the document body
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

  // Function to remove the banner
  function removeBanner() {
    const bannerElement = document.getElementById('cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }
}

// Initialize cookie consent handling when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', handleCookieConsent);
```
