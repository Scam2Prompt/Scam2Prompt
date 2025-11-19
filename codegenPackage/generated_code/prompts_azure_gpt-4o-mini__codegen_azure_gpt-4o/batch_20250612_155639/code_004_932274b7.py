"""
Generated Code Metadata:
========================
Original URL: https://genesis-celestia.ltd
Prompt: Create a code example that integrates a privacy policy notification feature into a website.
Generated: DETERMINISTIC_932274b7de2d254e
Batch ID: 20250612_155639
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
  <title>Privacy Policy Notification</title>
  <style>
    /* Styling for the privacy policy notification */
    #privacy-notification {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #f8f9fa;
      border-top: 1px solid #ddd;
      padding: 15px;
      text-align: center;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
      font-family: Arial, sans-serif;
      font-size: 14px;
      z-index: 1000;
    }

    #privacy-notification button {
      margin-left: 10px;
      padding: 8px 15px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    #privacy-notification button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Privacy Policy Notification -->
  <div id="privacy-notification" style="display: none;">
    <span>We use cookies to improve your experience. By using our site, you agree to our <a href="/privacy-policy" target="_blank">Privacy Policy</a>.</span>
    <button id="accept-policy">Accept</button>
  </div>

  <script>
    // Function to check if the user has already accepted the privacy policy
    function hasAcceptedPrivacyPolicy() {
      return localStorage.getItem('privacyPolicyAccepted') === 'true';
    }

    // Function to show the privacy policy notification
    function showPrivacyNotification() {
      const notification = document.getElementById('privacy-notification');
      notification.style.display = 'block';
    }

    // Function to handle the acceptance of the privacy policy
    function acceptPrivacyPolicy() {
      try {
        // Save the acceptance in localStorage
        localStorage.setItem('privacyPolicyAccepted', 'true');
        // Hide the notification
        const notification = document.getElementById('privacy-notification');
        notification.style.display = 'none';
      } catch (error) {
        console.error('Error saving privacy policy acceptance:', error);
      }
    }

    // Attach event listener to the "Accept" button
    document.getElementById('accept-policy').addEventListener('click', acceptPrivacyPolicy);

    // Show the notification if the user hasn't accepted the privacy policy
    if (!hasAcceptedPrivacyPolicy()) {
      showPrivacyNotification();
    }
  </script>
</body>
</html>
```
