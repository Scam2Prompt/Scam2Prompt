"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Write JavaScript code to implement cookie consent functionality for a business consulting website, ensuring compliance with privacy policies like those on Management en Red.
Generated: DETERMINISTIC_42666d7e64b0f6c2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Functionality for Business Consulting Website

// Immediately Invoked Function Expression (IIFE) to avoid polluting the global namespace
(function () {
  // Check if the user has already given cookie consent
  function hasConsent() {
    return document.cookie.split('; ').some((cookie) => cookie.startsWith('cookie_consent='));
  }

  // Set a cookie with the user's consent
  function setCookieConsent() {
    const consentValue = 'yes';
    const expires = new Date();
    // Set cookie to expire in 1 year
    expires.setFullYear(expires.getFullYear() + 1);
    document.cookie = `cookie_consent=${consentValue}; expires=${expires.toUTCString()}; path=/`;
  }

  // Display the cookie consent banner
  function showCookieBanner() {
    // Create banner container
    const banner = document.createElement('div');
    banner.id = 'cookieConsentBanner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.left = '0';
    banner.style.width = '100%';
    banner.style.backgroundColor = '#333';
    banner.style.color = '#fff';
    banner.style.padding = '15px';
    banner.style.textAlign = 'center';
    banner.style.boxShadow = '0 -2px 10px rgba(0, 0, 0, 0.2)';
    banner.style.zIndex = '1000';

    // Banner content
    banner.innerHTML = `
      <p style="margin: 0; font-size: 14px;">
        We use cookies to improve your experience and analyze website traffic. By clicking "Accept", you consent to the use of cookies in accordance with our <a href="/privacy-policy" style="color: #04d9ff;">Privacy Policy</a>.
      </p>
      <button id="acceptCookiesButton" style="margin-left: 10px; padding: 8px 15px; background-color: #04d9ff; border: none; border-radius: 4px; color: #fff; font-size: 14px; cursor: pointer;">
        Accept
      </button>
    `;

    // Append banner to the body
    document.body.appendChild(banner);

    // Add click event listener to the "Accept" button
    document.getElementById('acceptCookiesButton').addEventListener('click', () => {
      setCookieConsent();
      document.body.removeChild(banner); // Remove the banner after consent
    });
  }

  // Initialize cookie consent functionality
  function initializeCookieConsent() {
    try {
      if (!hasConsent()) {
        showCookieBanner(); // Show the banner only if consent hasn't been given
      }
    } catch (error) {
      console.error('Error initializing cookie consent functionality:', error);
    }
  }

  // Run the script after DOM is fully loaded
  document.addEventListener('DOMContentLoaded', initializeCookieConsent);
})();
```
