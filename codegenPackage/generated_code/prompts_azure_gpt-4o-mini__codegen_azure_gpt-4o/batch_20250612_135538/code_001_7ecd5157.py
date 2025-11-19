"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: What are the best practices for optimizing user experience with cookie usage, as mentioned in the content from celestia.solutions?
Generated: DETERMINISTIC_7ecd5157856262e4
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
 * Best practices for optimizing user experience with cookie usage.
 * This script demonstrates how to handle cookies responsibly and improve user experience.
 * 
 * Key features:
 * - Transparent cookie usage
 * - Secure and efficient cookie handling
 * - Compliance with privacy regulations
 * - User-friendly cookie consent management
 */

// Function to set a cookie with best practices
function setCookie(name, value, days, secure = true) {
  try {
    // Calculate expiration date
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    const expires = `expires=${date.toUTCString()}`;

    // Construct cookie string
    let cookieString = `${name}=${encodeURIComponent(value)}; ${expires}; path=/`;
    if (secure) {
      cookieString += '; Secure; SameSite=Strict'; // Secure and SameSite attributes for better security
    }

    // Set the cookie
    document.cookie = cookieString;
  } catch (error) {
    console.error('Error setting cookie:', error);
  }
}

// Function to get a cookie value by name
function getCookie(name) {
  try {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) {
        return decodeURIComponent(value);
      }
    }
    return null; // Return null if cookie not found
  } catch (error) {
    console.error('Error getting cookie:', error);
    return null;
  }
}

// Function to delete a cookie by name
function deleteCookie(name) {
  try {
    // Set the cookie expiration date to the past
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
  } catch (error) {
    console.error('Error deleting cookie:', error);
  }
}

// Function to display a cookie consent banner
function displayCookieConsentBanner() {
  // Create banner element
  const banner = document.createElement('div');
  banner.id = 'cookie-consent-banner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#333';
  banner.style.color = '#fff';
  banner.style.padding = '10px';
  banner.style.textAlign = 'center';
  banner.style.zIndex = '1000';

  // Add banner content
  banner.innerHTML = `
    <p>We use cookies to improve your experience. By using our site, you agree to our cookie policy.</p>
    <button id="accept-cookies" style="margin-right: 10px;">Accept</button>
    <button id="decline-cookies">Decline</button>
  `;

  // Append banner to the body
  document.body.appendChild(banner);

  // Add event listeners for buttons
  document.getElementById('accept-cookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'accepted', 365); // Store consent in a cookie
    banner.remove(); // Remove banner
  });

  document.getElementById('decline-cookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'declined', 365); // Store consent in a cookie
    banner.remove(); // Remove banner
  });
}

// Function to check cookie consent status
function checkCookieConsent() {
  const consent = getCookie('cookieConsent');
  if (!consent) {
    displayCookieConsentBanner(); // Show banner if no consent is stored
  }
}

// Initialize cookie consent check on page load
document.addEventListener('DOMContentLoaded', () => {
  checkCookieConsent();
});
```
