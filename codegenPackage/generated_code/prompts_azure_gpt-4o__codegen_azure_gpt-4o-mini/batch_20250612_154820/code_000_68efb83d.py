"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement cookie consent management similar to the GDPR Cookie Consent plugin described on the Health Insurance Shop website, including categories like "Analytics," "Functional," and "Necessary."
Generated: DETERMINISTIC_68efb83d4aeed834
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent Management</title>
    <style>
        /* Basic styles for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: white;
            padding: 15px;
            display: none; /* Hidden by default */
            z-index: 1000;
        }
        #cookie-consent-banner button {
            margin-left: 10px;
        }
    </style>
</head>
<body>

<div id="cookie-consent-banner">
    <p>This website uses cookies to enhance the user experience. 
        <strong>Necessary</strong> cookies are required for the website to function. 
        <strong>Functional</strong> cookies help us remember your preferences. 
        <strong>Analytics</strong> cookies help us understand how you use the site.
    </p>
    <button id="accept-all">Accept All</button>
    <button id="manage-preferences">Manage Preferences</button>
</div>

<!-- Preferences Modal -->
<div id="preferences-modal" style="display:none;">
    <h2>Cookie Preferences</h2>
    <form id="cookie-preferences-form">
        <label>
            <input type="checkbox" name="necessary" checked disabled>
            Necessary Cookies (Always Active)
        </label><br>
        <label>
            <input type="checkbox" name="functional">
            Functional Cookies
        </label><br>
        <label>
            <input type="checkbox" name="analytics">
            Analytics Cookies
        </label><br>
        <button type="submit">Save Preferences</button>
        <button type="button" id="close-modal">Close</button>
    </form>
</div>

<script>
    // Function to show the cookie consent banner
    function showCookieConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        banner.style.display = 'block';
    }

    // Function to hide the cookie consent banner
    function hideCookieConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        banner.style.display = 'none';
    }

    // Function to handle the acceptance of all cookies
    function acceptAllCookies() {
        setCookie('cookieConsent', 'all', 30);
        hideCookieConsentBanner();
    }

    // Function to manage cookie preferences
    function managePreferences(event) {
        event.preventDefault();
        const modal = document.getElementById('preferences-modal');
        modal.style.display = 'block';
    }

    // Function to save cookie preferences
    function savePreferences(event) {
        event.preventDefault();
        const form = event.target;
        const preferences = {
            necessary: true, // Always true
            functional: form.functional.checked,
            analytics: form.analytics.checked
        };
        setCookie('cookieConsent', JSON.stringify(preferences), 30);
        hideCookieConsentBanner();
        document.getElementById('preferences-modal').style.display = 'none';
    }

    // Function to set a cookie
    function setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
    }

    // Function to check if cookie consent has been given
    function checkCookieConsent() {
        const cookieConsent = document.cookie.split('; ').find(row => row.startsWith('cookieConsent='));
        return cookieConsent ? JSON.parse(decodeURIComponent(cookieConsent.split('=')[1])) : null;
    }

    // Event listeners
    document.getElementById('accept-all').addEventListener('click', acceptAllCookies);
    document.getElementById('manage-preferences').addEventListener('click', managePreferences);
    document.getElementById('cookie-preferences-form').addEventListener('submit', savePreferences);
    document.getElementById('close-modal').addEventListener('click', () => {
        document.getElementById('preferences-modal').style.display = 'none';
    });

    // Initialize cookie consent management
    window.onload = function() {
        const consent = checkCookieConsent();
        if (!consent) {
            showCookieConsentBanner();
        }
    };
</script>

</body>
</html>
```
