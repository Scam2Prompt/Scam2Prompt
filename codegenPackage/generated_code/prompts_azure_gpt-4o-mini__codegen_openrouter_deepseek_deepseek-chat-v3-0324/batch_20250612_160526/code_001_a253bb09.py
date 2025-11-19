"""
Generated Code Metadata:
========================
Original URL: https://hope-exchange.com
Prompt: Write a code snippet to create a cookie consent banner for a website, inspired by the cookie policy mentioned on Hope Exchange.
Generated: DETERMINISTIC_a253bb09d3da5f26
Batch ID: 20250612_160526
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
    <title>Cookie Consent</title>
    <style>
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #f8f9fa;
            padding: 15px;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
            z-index: 9999;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }
        
        #cookie-consent-banner p {
            margin: 0;
            flex: 1;
            min-width: 250px;
            padding-right: 15px;
            color: #333;
            font-size: 14px;
        }
        
        .cookie-buttons {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .cookie-btn {
            padding: 8px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            white-space: nowrap;
        }
        
        #accept-cookies {
            background-color: #28a745;
            color: white;
        }
        
        #reject-cookies {
            background-color: #dc3545;
            color: white;
        }
        
        #customize-cookies {
            background-color: #007bff;
            color: white;
        }
        
        #cookie-settings {
            display: none;
            margin-top: 15px;
            width: 100%;
            padding: 15px;
            background: #e9ecef;
            border-radius: 4px;
        }
        
        .cookie-setting {
            margin-bottom: 10px;
        }
        
        .cookie-setting label {
            display: flex;
            align-items: center;
            cursor: pointer;
        }
        
        .cookie-setting input {
            margin-right: 10px;
        }
        
        #save-settings {
            background-color: #6c757d;
            color: white;
        }
    </style>
</head>
<body>
    <!-- Main content would go here -->
    
    <!-- Cookie Consent Banner -->
    <div id="cookie-consent-banner">
        <p>
            We use cookies to enhance your experience on our website. By continuing to browse, you agree to our use of cookies. 
            <a href="/cookie-policy" style="color: #007bff;">Learn more</a>
        </p>
        <div class="cookie-buttons">
            <button id="accept-cookies" class="cookie-btn">Accept All</button>
            <button id="reject-cookies" class="cookie-btn">Reject All</button>
            <button id="customize-cookies" class="cookie-btn">Customize</button>
        </div>
        <div id="cookie-settings">
            <h3>Cookie Preferences</h3>
            <div class="cookie-setting">
                <label>
                    <input type="checkbox" name="necessary" checked disabled>
                    Necessary Cookies (Required)
                </label>
                <p>These cookies are essential for the website to function properly.</p>
            </div>
            <div class="cookie-setting">
                <label>
                    <input type="checkbox" name="analytics" checked>
                    Analytics Cookies
                </label>
                <p>These cookies help us understand how visitors interact with our website.</p>
            </div>
            <div class="cookie-setting">
                <label>
                    <input type="checkbox" name="marketing">
                    Marketing Cookies
                </label>
                <p>These cookies are used to track visitors across websites for marketing purposes.</p>
            </div>
            <button id="save-settings" class="cookie-btn">Save Preferences</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Check if cookie consent has already been given
            if (document.cookie.includes('cookie_consent=')) {
                document.getElementById('cookie-consent-banner').style.display = 'none';
                return;
            }

            // Get DOM elements
            const acceptBtn = document.getElementById('accept-cookies');
            const rejectBtn = document.getElementById('reject-cookies');
            const customizeBtn = document.getElementById('customize-cookies');
            const cookieSettings = document.getElementById('cookie-settings');
            const saveSettingsBtn = document.getElementById('save-settings');

            // Set cookie with expiration (30 days)
            function setCookie(name, value, days) {
                const date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                const expires = "expires=" + date.toUTCString();
                document.cookie = name + "=" + value + ";" + expires + ";path=/";
            }

            // Handle accept all cookies
            acceptBtn.addEventListener('click', function() {
                setCookie('cookie_consent', 'all', 30);
                document.getElementById('cookie-consent-banner').style.display = 'none';
                // You would typically load all cookies here
            });

            // Handle reject all cookies
            rejectBtn.addEventListener('click', function() {
                setCookie('cookie_consent', 'necessary', 30);
                document.getElementById('cookie-consent-banner').style.display = 'none';
                // You would typically block all non-essential cookies here
            });

            // Toggle cookie settings panel
            customizeBtn.addEventListener('click', function() {
                cookieSettings.style.display = cookieSettings.style.display === 'block' ? 'none' : 'block';
            });

            // Handle save settings
            saveSettingsBtn.addEventListener('click', function() {
                const analyticsChecked = document.querySelector('input[name="analytics"]').checked;
                const marketingChecked = document.querySelector('input[name="marketing"]').checked;
                
                let consentValue = 'necessary';
                if (analyticsChecked) consentValue += ',analytics';
                if (marketingChecked) consentValue += ',marketing';
                
                setCookie('cookie_consent', consentValue, 30);
                document.getElementById('cookie-consent-banner').style.display = 'none';
                
                // You would typically load cookies based on preferences here
            });
        });
    </script>
</body>
</html>
```
