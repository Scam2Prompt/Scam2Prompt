"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Generate code to implement a cookie consent management system for an e-commerce site, similar to the cookie settings described on the PlusMedica Shop website.
Generated: DETERMINISTIC_847f8bd33219521c
Batch ID: 20250612_150602
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="cookie-consent-banner" class="cookie-banner">
        <p>This website uses cookies to ensure you get the best experience on our website. 
           <a href="/privacy-policy" target="_blank">Learn more</a>
        </p>
        <div class="cookie-buttons">
            <button id="accept-cookies" class="cookie-button">Accept All Cookies</button>
            <button id="customize-cookies" class="cookie-button">Customize Settings</button>
        </div>
    </div>

    <div id="cookie-settings-modal" class="cookie-modal hidden">
        <h2>Customize Cookie Settings</h2>
        <form id="cookie-settings-form">
            <label>
                <input type="checkbox" name="necessary" checked disabled>
                Necessary Cookies (required)
            </label>
            <label>
                <input type="checkbox" name="analytics">
                Analytics Cookies
            </label>
            <label>
                <input type="checkbox" name="marketing">
                Marketing Cookies
            </label>
            <button type="submit" class="cookie-button">Save Settings</button>
            <button type="button" id="close-modal" class="cookie-button">Close</button>
        </form>
    </div>

    <script>
        // Function to show the cookie consent banner
        function showCookieBanner() {
            const banner = document.getElementById('cookie-consent-banner');
            banner.style.display = 'block';
        }

        // Function to hide the cookie consent banner
        function hideCookieBanner() {
            const banner = document.getElementById('cookie-consent-banner');
            banner.style.display = 'none';
        }

        // Function to handle cookie acceptance
        function acceptCookies() {
            setCookie('cookieConsent', 'accepted', 30);
            hideCookieBanner();
        }

        // Function to handle cookie settings customization
        function customizeCookies() {
            const modal = document.getElementById('cookie-settings-modal');
            modal.classList.remove('hidden');
        }

        // Function to save cookie settings
        function saveCookieSettings(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const settings = {
                necessary: formData.get('necessary') === 'on',
                analytics: formData.get('analytics') === 'on',
                marketing: formData.get('marketing') === 'on'
            };
            setCookie('cookieSettings', JSON.stringify(settings), 30);
            hideCookieBanner();
            closeModal();
        }

        // Function to close the cookie settings modal
        function closeModal() {
            const modal = document.getElementById('cookie-settings-modal');
            modal.classList.add('hidden');
        }

        // Function to set a cookie
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
        }

        // Event listeners
        document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
        document.getElementById('customize-cookies').addEventListener('click', customizeCookies);
        document.getElementById('cookie-settings-form').addEventListener('submit', saveCookieSettings);
        document.getElementById('close-modal').addEventListener('click', closeModal);

        // Check for existing cookie consent
        window.onload = function() {
            if (!document.cookie.split('; ').find(row => row.startsWith('cookieConsent='))) {
                showCookieBanner();
            }
        };
    </script>
    <style>
        /* Basic styles for the cookie consent banner and modal */
        .cookie-banner, .cookie-modal {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f8f9fa;
            padding: 20px;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
            z-index: 1000;
        }
        .cookie-modal {
            top: 50%;
            transform: translateY(-50%);
            display: none;
        }
        .hidden {
            display: none;
        }
        .cookie-button {
            margin: 5px;
            padding: 10px 15px;
            border: none;
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }
        .cookie-button:hover {
            background-color: #0056b3;
        }
    </style>
</body>
</html>
```
