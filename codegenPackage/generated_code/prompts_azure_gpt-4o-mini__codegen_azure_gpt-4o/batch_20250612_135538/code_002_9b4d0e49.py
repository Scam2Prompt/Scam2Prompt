"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Write a JavaScript function that tracks user consent for cookies, inspired by the cookie policy on celestia.solutions.
Generated: DETERMINISTIC_9b4d0e49e36b00e5
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Tracker
 * This function manages user consent for cookies, inspired by the cookie policy on celestia.solutions.
 * It provides functionality to display a consent banner, store user preferences, and retrieve consent status.
 */

// Immediately Invoked Function Expression (IIFE) to avoid polluting the global scope
(function () {
  // Constants
  const COOKIE_NAME = "user_cookie_consent";
  const COOKIE_EXPIRATION_DAYS = 365; // 1 year
  const CONSENT_BANNER_ID = "cookie-consent-banner";

  /**
   * Sets a cookie with the given name, value, and expiration days.
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value of the cookie.
   * @param {number} days - The number of days until the cookie expires.
   */
  function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value};${expires};path=/`;
  }

  /**
   * Retrieves the value of a cookie by name.
   * @param {string} name - The name of the cookie.
   * @returns {string|null} - The value of the cookie, or null if not found.
   */
  function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split("; ");
    for (let i = 0; i < cookies.length; i++) {
      if (cookies[i].indexOf(nameEQ) === 0) {
        return cookies[i].substring(nameEQ.length);
      }
    }
    return null;
  }

  /**
   * Checks if the user has already provided cookie consent.
   * @returns {boolean} - True if consent is given, false otherwise.
   */
  function hasConsent() {
    const consent = getCookie(COOKIE_NAME);
    return consent === "true";
  }

  /**
   * Displays the cookie consent banner if consent has not been provided.
   */
  function displayConsentBanner() {
    if (hasConsent()) return;

    // Create banner element
    const banner = document.createElement("div");
    banner.id = CONSENT_BANNER_ID;
    banner.style.position = "fixed";
    banner.style.bottom = "0";
    banner.style.left = "0";
    banner.style.width = "100%";
    banner.style.backgroundColor = "#333";
    banner.style.color = "#fff";
    banner.style.padding = "10px";
    banner.style.textAlign = "center";
    banner.style.zIndex = "1000";

    // Banner content
    banner.innerHTML = `
      <p>
        We use cookies to improve your experience. By continuing to use our site, you consent to our cookie policy.
        <button id="accept-cookies" style="margin-left: 10px; padding: 5px 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer;">
          Accept
        </button>
      </p>
    `;

    // Append banner to the body
    document.body.appendChild(banner);

    // Add event listener for the "Accept" button
    document.getElementById("accept-cookies").addEventListener("click", () => {
      setCookie(COOKIE_NAME, "true", COOKIE_EXPIRATION_DAYS);
      document.getElementById(CONSENT_BANNER_ID).remove();
    });
  }

  // Initialize the cookie consent tracker
  document.addEventListener("DOMContentLoaded", displayConsentBanner);
})();
```
