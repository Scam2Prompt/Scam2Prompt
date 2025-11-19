"""
Generated Code Metadata:
========================
Original URL: https://abubit.com
Prompt: Generate a JavaScript snippet that handles cookie consent, similar to the functionality implied on the abubit.com website.
Generated: DETERMINISTIC_4103a40f2ac200c7
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Consent Handler
// This script displays a cookie consent banner and manages user consent for cookies.

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Check if the user has already given consent
  const userConsent = getCookie("cookieConsent");
  if (!userConsent) {
    // If no consent, display the cookie consent banner
    displayCookieBanner();
  }
});

/**
 * Displays the cookie consent banner.
 */
function displayCookieBanner() {
  // Create the banner element
  const banner = document.createElement("div");
  banner.id = "cookie-banner";
  banner.style.position = "fixed";
  banner.style.bottom = "0";
  banner.style.left = "0";
  banner.style.width = "100%";
  banner.style.backgroundColor = "#333";
  banner.style.color = "#fff";
  banner.style.padding = "15px";
  banner.style.textAlign = "center";
  banner.style.zIndex = "1000";

  // Banner content
  banner.innerHTML = `
    <p style="margin: 0; font-size: 14px;">
      We use cookies to improve your experience. By using our site, you consent to cookies.
      <button id="accept-cookies" style="margin-left: 10px; padding: 5px 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer;">Accept</button>
      <button id="decline-cookies" style="margin-left: 10px; padding: 5px 10px; background-color: #f44336; color: white; border: none; cursor: pointer;">Decline</button>
    </p>
  `;

  // Append the banner to the body
  document.body.appendChild(banner);

  // Add event listeners for buttons
  document.getElementById("accept-cookies").addEventListener("click", () => {
    setCookie("cookieConsent", "accepted", 365); // Set consent cookie for 1 year
    removeCookieBanner();
  });

  document.getElementById("decline-cookies").addEventListener("click", () => {
    setCookie("cookieConsent", "declined", 365); // Set declined cookie for 1 year
    removeCookieBanner();
  });
}

/**
 * Removes the cookie consent banner from the DOM.
 */
function removeCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  if (banner) {
    banner.remove();
  }
}

/**
 * Sets a cookie.
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
 * Gets a cookie value by name.
 * @param {string} name - The name of the cookie.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
  const nameEQ = name + "=";
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.indexOf(nameEQ) === 0) {
      return cookie.substring(nameEQ.length, cookie.length);
    }
  }
  return null;
}

/**
 * Deletes a cookie by name.
 * @param {string} name - The name of the cookie.
 */
function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
}
```
