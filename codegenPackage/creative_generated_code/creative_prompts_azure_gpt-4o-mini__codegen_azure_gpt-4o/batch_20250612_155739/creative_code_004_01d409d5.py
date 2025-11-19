"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upaerc.com
Prompt: How do I create a fallback message for users with JavaScript disabled on my website?
Generated: DETERMINISTIC_01d409d5bf04bd4c
Batch ID: 20250612_155739
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
  <title>JavaScript Disabled Fallback</title>
  <style>
    /* Style the fallback message */
    #no-js-message {
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 15px;
      margin: 20px 0;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- Fallback message displayed if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      It seems your browser has JavaScript disabled. To experience the full functionality of this site, please enable JavaScript in your browser.
    </div>
  </noscript>

  <!-- Example content that depends on JavaScript -->
  <div id="main-content">
    <h1>Welcome to My Website</h1>
    <p>This content is enhanced with JavaScript functionality.</p>
  </div>

  <script>
    // Example JavaScript functionality
    // This script will hide the fallback message since JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Handle any initialization logic here
      console.log('JavaScript is enabled and running!');
    });
  </script>
</body>
</html>
```
