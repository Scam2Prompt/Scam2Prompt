"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Write a script to integrate cookie consent management into an e-commerce website, referencing the detailed cookie policy implementation on ActiveSport.cz.
Generated: DETERMINISTIC_3ca24325c04bead3
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// cookieConsent.js
// This script integrates cookie consent management into an e-commerce website.
// It follows best practices for readability, modularity, and compliance with cookie policies.
// Please replace the example URLs and policy details with those specific to your implementation.

/**
 * Initializes cookie consent management for the website.
 */
document.addEventListener('DOMContentLoaded', function () {
  // Check if cookie consent has already been given
  if (getCookie('cookieConsent') !== 'true') {
    showCookieConsentBanner();
  }
});

/**
 * Displays the cookie consent banner to the user.
 */
function showCookieConsentBanner() {
  // Create the banner container
  const banner = document.createElement('div');
  banner.id = 'cookieConsentBanner';
  banner.style.cssText = `
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    color: white;
    padding: 20px;
    text-align: center;
    font-family: Arial, sans-serif;
    z-index: 1000;
  `;

  // Message content inside the banner
  const message = document.createElement('p');
  message.textContent = 'We use cookies to improve your experience on our website and provide personalized services. By clicking "Accept", you agree to our cookie policy. Learn more in our ';
  message.style.cssText = 'display: inline;';

  // Link to the cookie policy
  const policyLink = document.createElement('a');
  policyLink.href = '/cookie-policy'; // Replace with your actual URL
  policyLink.textContent = 'Cookie Policy';
  policyLink.style.cssText = 'color: #00f; text-decoration: underline; cursor: pointer;';
  message.appendChild(policyLink);

  banner.appendChild(message);

  // Add accept button
  const acceptButton = document.createElement('button');
  acceptButton.textContent = 'Accept';
  acceptButton.style.cssText = `
    margin-left: 20px;
    padding: 10px 20px;
    background-color: #00f;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  `;
  acceptButton.onclick = function () {
    handleConsent();
  };
  banner.appendChild(acceptButton);

  // Add banner to the DOM
  document.body.appendChild(banner);
}

/**
 * Handles user consent for cookies.
 * Sets the cookie and removes the banner.
 */
function handleConsent() {
  try {
    setCookie('cookieConsent', 'true', 365); // Set cookie for 1 year
    const banner = document.getElementById('cookieConsentBanner');
    if (banner) {
      banner.remove(); // Remove the banner after consent
    }
  } catch (error) {
    console.error('Error while handling cookie consent:', error);
  }
}

/**
 * Sets a cookie in the browser.
 * @param {string} name - Name of the cookie.
 * @param {string} value - Value of the cookie.
 * @param {number} days - Expiry in days.
 */
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Calculate expiry date
  const expires = 'expires=' + date.toUTCString();
  document.cookie = `${name}=${value}; ${expires}; path=/; Secure; SameSite=Strict`;
}

/**
 * Gets a cookie value by name.
 * @param {string} name - Name of the cookie.
 * @returns {string|null} - The value of the cookie or null if not found.
 */
function getCookie(name) {
  const cookieString = document.cookie;
  const cookies = cookieString.split(';');
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(name + '=')) {
      return cookie.split('=')[1];
    }
  }
  return null;
}
```

Save this script as `cookieConsent.js` and include it in your website's HTML file with the following line in the `<head>` section:

```html
<script src="cookieConsent.js" defer></script>
```

Replace the `/cookie-policy` link with the actual URL of your website's cookie policy page.
