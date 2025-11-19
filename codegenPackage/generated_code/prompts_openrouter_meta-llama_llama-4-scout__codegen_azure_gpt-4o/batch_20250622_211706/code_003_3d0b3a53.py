"""
Generated Code Metadata:
========================
Original URL: https://11tesorosibericos.com
Prompt: "Create a JavaScript function to implement a cookie consent banner for an e-commerce website, similar to the one on 11tesorosibericos.com."
Generated: DETERMINISTIC_3d0b3a53fccc00d1
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Banner Implementation
 * This script creates a cookie consent banner for an e-commerce website.
 * The banner allows users to accept or reject cookies and stores their preferences.
 */

// Function to initialize the cookie consent banner
function initializeCookieConsentBanner() {
  // Check if the user has already made a cookie preference decision
  const userConsent = getCookie('cookieConsent');
  if (userConsent) {
    // If consent is already given or rejected, do not show the banner
    return;
  }

  // Create the banner element
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

  // Banner content
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
    setCookie('cookieConsent', 'accepted', 365); // Store consent for 365 days
    removeBanner();
  });

  document.getElementById('reject-cookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'rejected', 365); // Store rejection for 365 days
    removeBanner();
  });

  // Function to remove the banner
  function removeBanner() {
    banner.remove();
  }
}

// Function to set a cookie
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${value};${expires};path=/`;
}

// Function to get a cookie value
function getCookie(name) {
  const nameEQ = `${name}=`;
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.indexOf(nameEQ) === 0) {
      return cookie.substring(nameEQ.length, cookie.length);
    }
  }
  return null;
}

// Initialize the cookie consent banner when the page loads
window.addEventListener('load', initializeCookieConsentBanner);
```
