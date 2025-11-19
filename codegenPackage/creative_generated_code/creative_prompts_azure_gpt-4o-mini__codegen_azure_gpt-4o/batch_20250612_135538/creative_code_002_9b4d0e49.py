"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: Write a JavaScript function that tracks user consent for cookies, inspired by the cookie policy on celestia.solutions.
Generated: DETERMINISTIC_9b4d0e49e36b00e5
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Tracks user consent for cookies.
 * This function manages the user consent status based on their interaction
 * with a cookie consent banner and stores the status in localStorage.
 * Inspired by the cookie policy on celestia.solutions.
 */

// Function to initialize and manage cookie consent
function manageCookieConsent() {
  const CONSENT_KEY = 'user_cookie_consent';
  const consentBannerId = 'cookie-consent-banner';
  const acceptButtonId = 'accept-cookies';
  const rejectButtonId = 'reject-cookies';

  /**
   * Checks if user consent exists in localStorage.
   * @returns {string|null} Consent status ('accepted', 'rejected', or null if not set)
   */
  function getUserConsent() {
    return localStorage.getItem(CONSENT_KEY);
  }

  /**
   * Saves user consent in localStorage.
   * @param {string} consentStatus - The user's consent status ('accepted' or 'rejected').
   */
  function saveUserConsent(consentStatus) {
    try {
      localStorage.setItem(CONSENT_KEY, consentStatus);
    } catch (error) {
      console.error('Error saving user consent to localStorage:', error);
    }
  }

  /**
   * Displays the cookie consent banner if no consent is found.
   */
  function displayConsentBanner() {
    const consentBanner = document.getElementById(consentBannerId);
    if (consentBanner) {
      consentBanner.style.display = 'block'; // Show the banner
    }
  }

  /**
   * Hides the cookie consent banner.
   */
  function hideConsentBanner() {
    const consentBanner = document.getElementById(consentBannerId);
    if (consentBanner) {
      consentBanner.style.display = 'none'; // Hide the banner
    }
  }

  /**
   * Handles user consent action (accept or reject).
   * @param {string} action - The consent action ('accepted' or 'rejected').
   */
  function handleUserConsent(action) {
    saveUserConsent(action);
    hideConsentBanner();
  }

  // Initialize consent banner
  document.addEventListener('DOMContentLoaded', () => {
    const existingConsent = getUserConsent();

    // If consent is not set, show the banner
    if (!existingConsent) {
      displayConsentBanner();

      // Attach event listeners to the accept and reject buttons
      const acceptButton = document.getElementById(acceptButtonId);
      const rejectButton = document.getElementById(rejectButtonId);

      if (acceptButton) {
        acceptButton.addEventListener('click', () => handleUserConsent('accepted'));
      }

      if (rejectButton) {
        rejectButton.addEventListener('click', () => handleUserConsent('rejected'));
      }
    }
  });
}

// Call the function to manage cookie consent
manageCookieConsent();
```

### HTML Example for Reference:
```html
<div id="cookie-consent-banner" style="display: none; position: fixed; bottom: 0; width: 100%; background: #333; color: #fff; padding: 10px; text-align: center;">
  <p>We use cookies to ensure you get the best experience on our website. Do you accept cookies?</p>
  <button id="accept-cookies" style="margin-right: 10px;">Accept</button>
  <button id="reject-cookies">Reject</button>
</div>
```

### Notes:
- Ensure the `cookie-consent-banner`, `accept-cookies`, and `reject-cookies` elements exist in your HTML for the script to work properly.
- This code follows best practices such as modularity, error handling, and separation of concerns.
