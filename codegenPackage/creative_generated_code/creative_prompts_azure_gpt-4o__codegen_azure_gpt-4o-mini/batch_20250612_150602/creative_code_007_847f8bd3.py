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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="cookie-consent-banner" class="cookie-banner">
        <p>We use cookies to enhance your browsing experience. By continuing to use our site, you consent to our use of cookies.</p>
        <button id="accept-cookies" class="cookie-button">Accept All</button>
        <button id="customize-cookies" class="cookie-button">Customize</button>
    </div>

    <div id="cookie-settings-modal" class="modal hidden">
        <div class="modal-content">
            <span id="close-modal" class="close">&times;</span>
            <h2>Cookie Settings</h2>
            <form id="cookie-settings-form">
                <label>
                    <input type="checkbox" name="analytics" checked>
                    Allow Analytics Cookies
                </label>
                <label>
                    <input type="checkbox" name="advertising">
                    Allow Advertising Cookies
                </label>
                <button type="submit" class="modal-button">Save Preferences</button>
            </form>
        </div>
    </div>

    <script>
        // Wait until the DOM is fully loaded before executing script
        document.addEventListener("DOMContentLoaded", function () {
            const cookieBanner = document.getElementById("cookie-consent-banner");
            const acceptCookiesButton = document.getElementById("accept-cookies");
            const customizeCookiesButton = document.getElementById("customize-cookies");
            const cookieSettingsModal = document.getElementById("cookie-settings-modal");
            const closeModalButton = document.getElementById("close-modal");
            const cookieSettingsForm = document.getElementById("cookie-settings-form");

            // Check if cookies have already been accepted
            if (!getCookie("cookiesAccepted")) {
                cookieBanner.classList.remove("hidden");
            }

            // Accept all cookies and hide the banner
            acceptCookiesButton.addEventListener("click", function () {
                setCookie("cookiesAccepted", true, 365);
                cookieBanner.classList.add("hidden");
            });

            // Open the cookie settings modal
            customizeCookiesButton.addEventListener("click", function () {
                cookieSettingsModal.classList.remove("hidden");
            });

            // Close the cookie settings modal
            closeModalButton.addEventListener("click", function () {
                cookieSettingsModal.classList.add("hidden");
            });

            // Handle the cookie settings form submission
            cookieSettingsForm.addEventListener("submit", function (event) {
                event.preventDefault();
                const formData = new FormData(cookieSettingsForm);
                const analyticsConsent = formData.get("analytics") ? true : false;
                const advertisingConsent = formData.get("advertising") ? true : false;

                // Save user's cookie preferences in browser cookies
                setCookie("analyticsConsent", analyticsConsent, 365);
                setCookie("advertisingConsent", advertisingConsent, 365);

                cookieSettingsModal.classList.add("hidden");
                alert("Your preferences have been saved.");
            });

            // Utility function to set a cookie
            function setCookie(name, value, days) {
                var expires = "";
                if (days) {
                    const date = new Date();
                    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                    expires = "; expires=" + date.toUTCString();
                }
                document.cookie = name + "=" + (value || "") + expires + "; path=/";
            }

            // Utility function to get a cookie value by name
            function getCookie(name) {
                const nameEQ = name + "=";
                const ca = document.cookie.split(';');
                for (let i = 0; i < ca.length; i++) {
                    let c = ca[i];
                    while (c.charAt(0) === ' ') c = c.substring(1, c.length);
                    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
                }
                return null;
            }
        });
    </script>
    <style>
        /* Basic styling for cookie banner and modal */
        .cookie-banner {
            background-color: #f9f9f9;
            padding: 15px;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            text-align: center;
            border-top: 1px solid #ccc;
        }

        .cookie-button {
            margin: 5px;
            padding: 10px 15px;
            cursor: pointer;
        }

        .modal {
            display: flex;
            justify-content: center;
            align-items: center;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.5);
        }

        .modal-content {
            background-color: white;
            padding: 20px;
            border-radius: 4px;
            width: 300px;
            position: relative;
        }

        .close {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
        }

        .hidden {
            display: none;
        }
    </style>
</body>
</html>
```
