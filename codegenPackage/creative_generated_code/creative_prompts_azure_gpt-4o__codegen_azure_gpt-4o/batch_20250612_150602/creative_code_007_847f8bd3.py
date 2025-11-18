"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Generate code to implement a cookie consent management system for an e-commerce site, similar to the cookie settings described on the PlusMedica Shop website.
Generated: DETERMINISTIC_847f8bd33219521c
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent Management</title>
    <style>
        /* Basic styling for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f1f1f1;
            padding: 1rem;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
            display: none; /* Hidden by default */
            z-index: 1000;
        }

        #cookie-consent-banner button {
            margin: 0 5px;
            padding: 0.5rem 1rem;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <!-- Cookie consent banner -->
    <div id="cookie-consent-banner">
        <p>We use cookies to enhance your browsing experience. You can manage your cookie preferences below.</p>
        <button id="accept-all-cookies">Accept All</button>
        <button id="decline-all-cookies">Decline All</button>
        <button id="manage-cookies">Manage Preferences</button>
    </div>

    <!-- Modal for managing cookie preferences -->
    <div id="cookie-settings-modal" style="display:none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: white; padding: 2rem; box-shadow: 0 4px 10px rgba(0,0,0,0.2); z-index: 1001;">
        <h2>Manage Cookie Preferences</h2>
        <form id="cookie-settings-form">
            <label>
                <input type="checkbox" name="essential" checked disabled>
                Essential Cookies (Required)
            </label>
            <br>
            <label>
                <input type="checkbox" name="analytics">
                Analytics Cookies
            </label>
            <br>
            <label>
                <input type="checkbox" name="marketing">
                Marketing Cookies
            </label>
            <br><br>
            <button type="button" id="save-cookie-settings">Save Preferences</button>
        </form>
    </div>

    <script>
        // Utility function to handle localStorage safely
        function setCookieConsent(consent) {
            try {
                localStorage.setItem('cookieConsent', JSON.stringify(consent));
            } catch (e) {
                console.error('Error saving cookie consent:', e);
            }
        }

        function getCookieConsent() {
            try {
                return JSON.parse(localStorage.getItem('cookieConsent')) || {};
            } catch (e) {
                console.error('Error fetching cookie consent:', e);
                return {};
            }
        }

        // Initialize cookie consent banner visibility
        document.addEventListener('DOMContentLoaded', () => {
            const consent = getCookieConsent();

            // Show banner only if consent not provided
            if (!consent.accepted) {
                document.getElementById('cookie-consent-banner').style.display = 'block';
            }
        });

        // Event listeners for banner buttons
        document.getElementById('accept-all-cookies').addEventListener('click', () => {
            setCookieConsent({ accepted: true, analytics: true, marketing: true });
            document.getElementById('cookie-consent-banner').style.display = 'none';
        });

        document.getElementById('decline-all-cookies').addEventListener('click', () => {
            setCookieConsent({ accepted: true, analytics: false, marketing: false });
            document.getElementById('cookie-consent-banner').style.display = 'none';
        });

        document.getElementById('manage-cookies').addEventListener('click', () => {
            document.getElementById('cookie-settings-modal').style.display = 'block';
        });

        // Event listener for saving cookie preferences
        document.getElementById('save-cookie-settings').addEventListener('click', () => {
            const form = document.getElementById('cookie-settings-form');
            const analytics = form.analytics.checked;
            const marketing = form.marketing.checked;

            setCookieConsent({ accepted: true, analytics, marketing });
            document.getElementById('cookie-settings-modal').style.display = 'none';
            document.getElementById('cookie-consent-banner').style.display = 'none';
        });
    </script>
</body>
</html>
```
