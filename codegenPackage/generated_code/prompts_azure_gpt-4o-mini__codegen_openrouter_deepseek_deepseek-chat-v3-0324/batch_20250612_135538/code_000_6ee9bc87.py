"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Generate code to implement a cookie consent feature for a website, similar to the one described on celestia.solutions.
Generated: DETERMINISTIC_6ee9bc874d99672c
Batch ID: 20250612_135538
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
            display: none;
        }
        
        .cookie-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }
        
        .cookie-text {
            flex: 1;
            min-width: 300px;
            margin-bottom: 10px;
        }
        
        .cookie-buttons {
            display: flex;
            gap: 10px;
        }
        
        .cookie-btn {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
        }
        
        .cookie-btn-accept {
            background: #007bff;
            color: white;
        }
        
        .cookie-btn-reject {
            background: #6c757d;
            color: white;
        }
        
        .cookie-btn-settings {
            background: transparent;
            border: 1px solid #6c757d;
            color: #6c757d;
        }
        
        #cookie-settings-modal {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
            z-index: 10000;
            max-width: 600px;
            width: 90%;
        }
        
        .cookie-settings-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .cookie-settings-title {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .cookie-settings-close {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
        }
        
        .cookie-settings-group {
            margin-bottom: 15px;
        }
        
        .cookie-settings-label {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .cookie-settings-description {
            color: #6c757d;
            font-size: 0.9rem;
            margin-bottom: 15px;
        }
        
        .cookie-settings-footer {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-top: 20px;
        }
        
        .switch {
            position: relative;
            display: inline-block;
            width: 60px;
            height: 34px;
        }
        
        .switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        
        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            transition: .4s;
            border-radius: 34px;
        }
        
        .slider:before {
            position: absolute;
            content: "";
            height: 26px;
            width: 26px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        
        input:checked + .slider {
            background-color: #007bff;
        }
        
        input:checked + .slider:before {
            transform: translateX(26px);
        }
    </style>
</head>
<body>
    <!-- Cookie Consent Banner -->
    <div id="cookie-consent-banner">
        <div class="cookie-content">
            <div class="cookie-text">
                We use cookies to enhance your browsing experience, serve personalized content, and analyze our traffic. 
                By clicking "Accept All", you consent to our use of cookies.
            </div>
            <div class="cookie-buttons">
                <button class="cookie-btn cookie-btn-settings" id="cookie-settings-btn">Settings</button>
                <button class="cookie-btn cookie-btn-reject" id="cookie-reject-btn">Reject All</button>
                <button class="cookie-btn cookie-btn-accept" id="cookie-accept-btn">Accept All</button>
            </div>
        </div>
    </div>

    <!-- Cookie Settings Modal -->
    <div id="cookie-settings-modal">
        <div class="cookie-settings-header">
            <div class="cookie-settings-title">Cookie Settings</div>
            <button class="cookie-settings-close" id="cookie-settings-close">&times;</button>
        </div>
        
        <div class="cookie-settings-description">
            You can set your preferences for how this website uses cookies below.
        </div>
        
        <div class="cookie-settings-group">
            <div class="cookie-settings-label">
                <span>Necessary Cookies</span>
                <label class="switch">
                    <input type="checkbox" id="necessary-cookies" checked disabled>
                    <span class="slider"></span>
                </label>
            </div>
            <div class="cookie-settings-description">
                These cookies are essential for the website to function properly and cannot be switched off.
            </div>
        </div>
        
        <div class="cookie-settings-group">
            <div class="cookie-settings-label">
                <span>Analytics Cookies</span>
                <label class="switch">
                    <input type="checkbox" id="analytics-cookies">
                    <span class="slider"></span>
                </label>
            </div>
            <div class="cookie-settings-description">
                These cookies help us understand how visitors interact with our website by collecting and reporting information anonymously.
            </div>
        </div>
        
        <div class="cookie-settings-group">
            <div class="cookie-settings-label">
                <span>Marketing Cookies</span>
                <label class="switch">
                    <input type="checkbox" id="marketing-cookies">
                    <span class="slider"></span>
                </label>
            </div>
            <div class="cookie-settings-description">
                These cookies are used to track visitors across websites to display more relevant ads.
            </div>
        </div>
        
        <div class="cookie-settings-footer">
            <button class="cookie-btn cookie-btn-reject" id="cookie-save-reject">Reject All</button>
            <button class="cookie-btn cookie-btn-accept" id="cookie-save-accept">Accept All</button>
            <button class="cookie-btn cookie-btn-accept" id="cookie-save-settings">Save Settings</button>
        </div>
    </div>

    <script>
        // Check if cookie consent has been given
        function checkCookieConsent() {
            const consent = localStorage.getItem('cookieConsent');
            if (consent === null) {
                // Show banner if no consent has been given
                document.getElementById('cookie-consent-banner').style.display = 'block';
            }
            return consent;
        }

        // Set cookie consent
        function setCookieConsent(necessary, analytics, marketing) {
            const consent = {
                necessary: necessary,
                analytics: analytics,
                marketing: marketing,
                date: new Date().toISOString()
            };
            localStorage.setItem('cookieConsent', JSON.stringify(consent));
            
            // Apply consent settings (e.g., load analytics scripts if consented)
            applyConsentSettings(consent);
            
            // Hide the banner
            document.getElementById('cookie-consent-banner').style.display = 'none';
        }

        // Apply consent settings (e.g., load scripts)
        function applyConsentSettings(consent) {
            if (consent.analytics) {
                // Load analytics scripts
                console.log('Loading analytics scripts');
            }
            
            if (consent.marketing) {
                // Load marketing scripts
                console.log('Loading marketing scripts');
            }
        }

        // Initialize cookie consent
        function initCookieConsent() {
            // Check for existing consent
            const existingConsent = checkCookieConsent();
            
            if (existingConsent) {
                // Apply existing consent settings
                applyConsentSettings(JSON.parse(existingConsent));
            }
            
            // Set up event listeners
            document.getElementById('cookie-accept-btn').addEventListener('click', function() {
                setCookieCons
