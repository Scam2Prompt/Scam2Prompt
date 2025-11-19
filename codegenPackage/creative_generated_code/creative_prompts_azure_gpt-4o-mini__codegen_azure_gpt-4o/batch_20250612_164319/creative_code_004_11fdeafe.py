"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-application5.pages.dev
Prompt: How can I create a fallback message for users who have disabled JavaScript in their browsers?
Generated: DETERMINISTIC_11fdeafe85e5f65e
Batch ID: 20250612_164319
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
  <title>JavaScript Fallback Message</title>
  <style>
    /* Styling for the fallback message */
    .no-js-message {
      display: none; /* Hide the message by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 10px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      margin: 20px 0;
    }
  </style>
</head>
<body>

  <!-- Fallback message for users who have disabled JavaScript -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable it for an improved experience.
  </div>

  <!-- Main content of the page -->
  <h1>Welcome to Our Website</h1>
  <p>This page works best with JavaScript enabled.</p>

  <script>
    // JavaScript code to hide the fallback message when JS is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Select the fallback message element
      const noJsMessage = document.querySelector('.no-js-message');
      
      // Hide the fallback message
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });
  </script>

  <!-- NoScript tag for users who have completely disabled JS -->
  <noscript>
    <style>
      /* Show the fallback message if JavaScript is disabled */
      .no-js-message {
        display: block;
      }
    </style>
  </noscript>

</body>
</html>
```
