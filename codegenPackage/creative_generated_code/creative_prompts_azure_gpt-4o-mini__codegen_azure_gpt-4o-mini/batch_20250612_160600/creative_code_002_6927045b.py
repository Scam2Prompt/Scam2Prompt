"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abubit.com
Prompt: How can I implement a cookie policy notification in my web application like the one on abubit.com?
Generated: DETERMINISTIC_6927045b0b17567a
Batch ID: 20250612_160600
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
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Policy Notification</title>
    <style>
        /* Basic styling for the notification bar */
        #cookie-notification {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
            display: none; /* Hidden by default */
            z-index: 1000;
        }
        #cookie-notification button {
            background-color: #ffcc00; /* Button color */
            border: none;
            color: #333;
            padding: 10px 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div id="cookie-notification">
        This website uses cookies to ensure you get the best experience. 
        <button id="accept-cookies">Accept</button>
    </div>

    <script>
        // Function to check if cookies have been accepted
        function checkCookieConsent() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
        }

        // Function to set a cookie for consent
        function setCookie(name, value, days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiration time
            const expires = "expires=" + date.toUTCString();
            document.cookie = name + "=" + value + ";" + expires + ";path=/"; // Set the cookie
        }

        // Function to show the cookie notification if consent isn't given
        function showCookieNotification() {
            const notification = document.getElementById('cookie-notification');
            if (!checkCookieConsent()) {
                notification.style.display = 'block'; // Show notification
            }
        }

        // Event listener for the accept button
        document.getElementById('accept-cookies').addEventListener('click', function() {
            setCookie('cookieConsent', 'accepted', 30); // Set a cookie for 30 days
            document.getElementById('cookie-notification').style.display = 'none'; // Hide notification
        });

        // Show the cookie notification on page load if consent has not been given
        window.onload = function() {
            showCookieNotification();
        };
    </script>
</body>
</html>
```
