"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: What are the best practices for optimizing user experience with cookie usage, as mentioned in the content from celestia.solutions?
Generated: DETERMINISTIC_7ecd5157856262e4
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
 * Best Practices for Optimizing User Experience with Cookie Usage
 * This script demonstrates production-ready implementation of cookie handling
 * with a focus on user experience, privacy, and compliance with regulations.
 */

// Utility function to set a cookie
function setCookie(name, value, days) {
  try {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${encodeURIComponent(value)};expires=${date.toUTCString()};path=/;SameSite=Lax`;
  } catch (error) {
    console.error('Error setting cookie:', error);
  }
}

// Utility function to get a cookie by name
function getCookie(name) {
  try {
    const cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
      const [key, value] = cookie.split('=');
      if (key === name) {
        return decodeURIComponent(value);
      }
    }
    return null;
  } catch (error) {
    console.error('Error getting cookie:', error);
    return null;
  }
}

// Utility function to delete a cookie
function deleteCookie(name) {
  try {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;SameSite=Lax`;
  } catch (error) {
    console.error('Error deleting cookie:', error);
  }
}

// Function to show a cookie consent banner to users
function showCookieConsentBanner() {
  const banner = document.createElement('div');
  banner.id = 'cookie-consent-banner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#333';
  banner.style.color = '#fff';
  banner.style.padding = '10px';
  banner.style.textAlign = 'center';
  banner.innerHTML = `
    <p>This website uses cookies to enhance your experience. By continuing to use our site, you agree to our cookie policy.</p>
    <button id="accept-cookies" style="margin: 5px;">Accept</button>
    <button id="decline-cookies" style="margin: 5px;">Decline</button>
  `;
  document.body.appendChild(banner);

  document.getElementById('accept-cookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'true', 365); // Store user's consent in a cookie for one year
    document.body.removeChild(banner);
  });

  document.getElementById('decline-cookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'false', 365); // Store user's declination in a cookie for one year
    document.body.removeChild(banner);
  });
}

// Check if user has already interacted with the cookie consent banner
function checkCookieConsent() {
  const consent = getCookie('cookieConsent');
  if (!consent) {
    showCookieConsentBanner();
  }
}

// Execute on page load
document.addEventListener('DOMContentLoaded', () => {
  checkCookieConsent();
});
```
