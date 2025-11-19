"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hope-exchange.com
Prompt: Write a code snippet to create a cookie consent banner for a website, inspired by the cookie policy mentioned on Hope Exchange.
Generated: DETERMINISTIC_a253bb09d3da5f26
Batch ID: 20250612_160526
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
  <title>Cookie Consent Banner</title>
  <style>
    /* Styling for the cookie consent banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #f4f4f4;
      border-top: 1px solid #ddd;
      padding: 15px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
      font-family: Arial, sans-serif;
      font-size: 14px;
    }

    #cookie-banner button {
      background-color: #007bff;
      color: white;
      border: none;
      padding: 8px 16px;
      cursor: pointer;
      border-radius: 4px;
      font-size: 14px;
    }

    #cookie-banner button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div id="cookie-banner" style="display: none;">
    <span>
      We use cookies to improve your experience on our website. By continuing to browse, you agree to our <a href="/cookie-policy" target="_blank" style="color: #007bff; text-decoration: none;">Cookie Policy</a>.
    </span>
    <button id="accept-cookies">Accept</button>
  </div>

  <script>
    // Function to check if the user has already accepted cookies
    function checkCookieConsent() {
      return document.cookie.includes("cookieConsent=true");
    }

    // Function to set a cookie for consent
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      const expires = "expires=" + date.toUTCString();
      document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Event listener for the "Accept" button
    document.getElementById("accept-cookies").addEventListener("click", () => {
      setCookie("cookieConsent", "true", 365); // Set consent cookie for 1 year
      document.getElementById("cookie-banner").style.display = "none"; // Hide the banner
    });

    // Display the banner only if consent is not already given
    if (!checkCookieConsent()) {
      document.getElementById("cookie-banner").style.display = "flex";
    }
  </script>
</body>
</html>
```
