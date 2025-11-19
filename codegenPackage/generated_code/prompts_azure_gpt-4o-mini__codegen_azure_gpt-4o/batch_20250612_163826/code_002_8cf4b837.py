"""
Generated Code Metadata:
========================
Original URL: https://hitchwallet.com
Prompt: Create a JavaScript code example that implements cookie consent management for a business website, inspired by the practices outlined on Hitch Wallet.
Generated: DETERMINISTIC_8cf4b83774b38a22
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Management Script
 * This script handles cookie consent for a business website.
 * It displays a consent banner, allows users to accept or reject cookies,
 * and manages cookie preferences accordingly.
 */

// Utility function to set a cookie
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = "expires=" + date.toUTCString();
  document.cookie = `${name}=${value};${expires};path=/`;
}

// Utility function to get a cookie value
function getCookie(name) {
  const nameEQ = name + "=";
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.indexOf(nameEQ) === 0) {
      return cookie.substring(nameEQ.length, cookie.length);
    }
  }
  return null;
}

// Utility function to delete a cookie
function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
}

// Function to display the cookie consent banner
function displayCookieBanner() {
  // Check if consent has already been given
  const consent = getCookie('cookieConsent');
  if (consent) return;

  // Create banner elements
  const banner = document.createElement('div');
  banner.id = 'cookie-banner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.left = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#333';
  banner.style.color = '#fff';
  banner.style.padding = '15px';
  banner.style.textAlign = 'center';
  banner.style.zIndex = '1000';

  const message = document.createElement('span');
  message.textContent = 'We use cookies to improve your experience. By using our site, you consent to cookies.';

  const acceptButton = document.createElement('button');
  acceptButton.textContent = 'Accept';
  acceptButton.style.marginLeft = '10px';
  acceptButton.style.padding = '5px 10px';
  acceptButton.style.backgroundColor = '#4CAF50';
  acceptButton.style.color = '#fff';
  acceptButton.style.border = 'none';
  acceptButton.style.cursor = 'pointer';

  const rejectButton = document.createElement('button');
  rejectButton.textContent = 'Reject';
  rejectButton.style.marginLeft = '10px';
  rejectButton.style.padding = '5px 10px';
  rejectButton.style.backgroundColor = '#f44336';
  rejectButton.style.color = '#fff';
  rejectButton.style.border = 'none';
  rejectButton.style.cursor = 'pointer';

  // Append elements to the banner
  banner.appendChild(message);
  banner.appendChild(acceptButton);
  banner.appendChild(rejectButton);
  document.body.appendChild(banner);

  // Event listeners for buttons
  acceptButton.addEventListener('click', () => {
    setCookie('cookieConsent', 'accepted', 365); // Store consent for 1 year
    document.body.removeChild(banner);
  });

  rejectButton.addEventListener('click', () => {
    setCookie('cookieConsent', 'rejected', 365); // Store rejection for 1 year
    document.body.removeChild(banner);
  });
}

// Function to initialize cookie consent management
function initCookieConsent() {
  try {
    displayCookieBanner();
  } catch (error) {
    console.error('Error initializing cookie consent management:', error);
  }
}

// Initialize cookie consent management on page load
window.addEventListener('load', initCookieConsent);
```
