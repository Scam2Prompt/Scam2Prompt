"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write JavaScript code to display a cookie consent banner on a website, with options to accept all cookies or manage consent for categories like "Performance" and "Advertisement," as described on the Health Insurance Shop site.
Generated: DETERMINISTIC_72ebfd385ce674f8
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Banner Script

// Ensure the script runs only when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Create the cookie consent banner
  const banner = document.createElement('div');
  banner.id = 'cookie-consent-banner';
  banner.style.cssText = `
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #f4f4f4;
    color: #333;
    padding: 20px;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
    z-index: 1000;
  `;
  banner.innerHTML = `
    <p style="margin: 0; font-size: 14px;">
      We use cookies to improve your experience. You can accept all cookies or manage your preferences.
    </p>
    <div style="margin-top: 10px;">
      <button id="accept-all-cookies" style="padding: 10px 15px; margin-right: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">
        Accept All Cookies
      </button>
      <button id="manage-cookies" style="padding: 10px 15px; background-color: #008CBA; color: white; border: none; border-radius: 4px; cursor: pointer;">
        Manage Preferences
      </button>
    </div>
  `;
  document.body.appendChild(banner);

  // Event listener for "Accept All Cookies"
  document.getElementById('accept-all-cookies').addEventListener('click', () => {
    try {
      setCookie('cookie-consent', JSON.stringify({ performance: true, advertisement: true }), 365);
      removeBanner();
    } catch (error) {
      console.error('Error accepting all cookies:', error);
    }
  });

  // Event listener for "Manage Preferences"
  document.getElementById('manage-cookies').addEventListener('click', () => {
    try {
      const preferencesModal = createPreferencesModal();
      document.body.appendChild(preferencesModal);
    } catch (error) {
      console.error('Error opening preferences modal:', error);
    }
  });

  // Helper function to remove the banner
  function removeBanner() {
    const bannerElement = document.getElementById('cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }

  // Helper function to create the preferences modal
  function createPreferencesModal() {
    const modal = document.createElement('div');
    modal.id = 'cookie-preferences-modal';
    modal.style.cssText = `
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
      z-index: 1001;
      width: 300px;
    `;
    modal.innerHTML = `
      <h3 style="margin-top: 0;">Manage Preferences</h3>
      <form id="cookie-preferences-form">
        <label style="display: block; margin-bottom: 10px;">
          <input type="checkbox" name="performance" checked />
          Performance Cookies
        </label>
        <label style="display: block; margin-bottom: 10px;">
          <input type="checkbox" name="advertisement" checked />
          Advertisement Cookies
        </label>
        <button type="submit" style="padding: 10px 15px; margin-top: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">
          Save Preferences
        </button>
        <button type="button" id="close-modal" style="padding: 10px 15px; margin-top: 10px; background-color: #f44336; color: white; border: none; border-radius: 4px; cursor: pointer;">
          Close
        </button>
      </form>
    `;

    // Handle form submission
    modal.querySelector('#cookie-preferences-form').addEventListener('submit', (event) => {
      event.preventDefault();
      const formData = new FormData(event.target);
      const preferences = {
        performance: formData.get('performance') === 'on',
        advertisement: formData.get('advertisement') === 'on',
      };
      setCookie('cookie-consent', JSON.stringify(preferences), 365);
      modal.remove();
      removeBanner();
    });

    // Handle modal close button
    modal.querySelector('#close-modal').addEventListener('click', () => {
      modal.remove();
    });

    return modal;
  }

  // Helper function to set a cookie
  function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;`;
  }

  // Helper function to get a cookie value
  function getCookie(name) {
    const cookies = document.cookie.split(';').map(cookie => cookie.trim());
    for (const cookie of cookies) {
      if (cookie.startsWith(`${name}=`)) {
        return cookie.split('=')[1];
      }
    }
    return null;
  }

  // Check if the cookie consent banner should be displayed
  const consentCookie = getCookie('cookie-consent');
  if (consentCookie) {
    try {
      const consent = JSON.parse(consentCookie);
      console.log('Cookie consent:', consent); // Log consent for debugging
    } catch (error) {
      console.error('Error parsing cookie consent:', error);
    }
  } else {
    banner.style.display = 'block'; // Show the banner
  }
});
```
