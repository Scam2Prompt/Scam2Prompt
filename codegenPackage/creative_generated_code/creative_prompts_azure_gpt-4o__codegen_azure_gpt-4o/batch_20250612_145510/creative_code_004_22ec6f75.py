"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powertools.reviewsrelay.com
Prompt: Write a script to display a custom notification on a webpage when an affiliate store powered by FreshStore is suspended, including contact information for support.
Generated: DETERMINISTIC_22ec6f75d5418983
Batch ID: 20250612_145510
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
  <title>Store Suspended</title>
  <style>
    /* Basic styling for the suspended notice */
    .notification-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #f8d7da;
      color: #721c24;
      padding: 20px;
      text-align: center;
      font-family: Arial, sans-serif;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      z-index: 9999;
    }
    .notification-container a {
      color: #0056b3;
      text-decoration: none;
      font-weight: bold;
    }
    .notification-container a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <!-- The custom notification container -->
  <div class="notification-container" id="suspended-notification">
    This store has been suspended. If you have questions, please contact our support team at 
    <a href="mailto:support@example.com">support@example.com</a> or call us at (123) 456-7890.
  </div>

  <script>
    // JavaScript to handle display logic for the notification
    (function () {
      try {
        // Check if the store is suspended (simulated condition for this example)
        const isStoreSuspended = true; // Replace with actual condition or API call

        if (isStoreSuspended) {
          // If suspended, display the notification
          const notification = document.getElementById('suspended-notification');
          if (notification) {
            notification.style.display = 'block';
          } else {
            console.error('Notification element not found in the DOM.');
          }
        } else {
          // If not suspended, hide/remove the notification
          const notification = document.getElementById('suspended-notification');
          if (notification) {
            notification.style.display = 'none';
          }
        }
      } catch (error) {
        // Log unexpected errors for debugging
        console.error('An error occurred while handling the store suspension notification:', error);
      }
    })();
  </script>
</body>
</html>
```
