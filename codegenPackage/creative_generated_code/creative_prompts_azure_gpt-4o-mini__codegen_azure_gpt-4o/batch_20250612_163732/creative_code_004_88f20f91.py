"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hgdsjhgdjhsgff.pages.dev
Prompt: How can I create a notification for users to enable JavaScript on my website?
Generated: DETERMINISTIC_88f20f9158f201ac
Batch ID: 20250612_163732
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
  <title>Enable JavaScript Notification</title>
  <style>
    /* Style for the notification displayed when JavaScript is disabled */
    .no-js-notification {
      display: none; /* Hide the notification by default */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #ffcc00;
      color: #000;
      text-align: center;
      padding: 10px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
      z-index: 1000;
    }
    /* Display notification when JavaScript is disabled */
    .no-js {
      display: block; /* Show the notification if JavaScript is disabled */
    }
  </style>
</head>
<body>
  <!-- Notification that appears when JavaScript is disabled -->
  <div id="js-notification" class="no-js-notification no-js">
    JavaScript is disabled in your browser. Please enable JavaScript to use this website.
  </div>

  <script>
    /**
     * Remove the "no-js" class from the notification element if JavaScript is enabled.
     * This ensures the notification is only visible when JavaScript is disabled.
     */
    document.addEventListener("DOMContentLoaded", () => {
      try {
        const notificationElement = document.getElementById("js-notification");
        if (notificationElement) {
          // Remove the "no-js" class to hide the notification
          notificationElement.classList.remove("no-js");
        }
      } catch (error) {
        console.error("Error handling JavaScript notification:", error);
      }
    });
  </script>
</body>
</html>
```
