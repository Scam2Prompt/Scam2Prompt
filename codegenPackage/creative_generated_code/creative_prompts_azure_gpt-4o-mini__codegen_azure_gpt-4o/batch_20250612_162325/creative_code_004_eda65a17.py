"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarityconnect.rf.gd
Prompt: How do I create a fallback message for users without JavaScript support on my website?
Generated: DETERMINISTIC_eda65a179c23d2f0
Batch ID: 20250612_162325
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
  <title>Fallback for No JavaScript Support</title>
  <style>
    /* Styling for the fallback message */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 15px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <!-- Content for JavaScript-enabled users -->
  <div id="main-content">
    <h1>Welcome to My Website</h1>
    <p>This content requires JavaScript to work properly.</p>
  </div>

  <!-- Fallback content for users without JavaScript -->
  <noscript>
    <div class="no-js-message">
      <strong>JavaScript is disabled!</strong> Please enable JavaScript in your browser to experience the full functionality of this website.
    </div>
  </noscript>

  <!-- Example JavaScript functionality -->
  <script>
    // Ensure the fallback message is hidden for browsers with JavaScript support
    document.addEventListener('DOMContentLoaded', () => {
      // If desired, you can add further JavaScript functionality here
      console.log("JavaScript is enabled!");
    });
  </script>
</body>
</html>
```
