"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiacelestiia.com
Prompt: Create a script to detect whether JavaScript is enabled in a browser and display a message prompting users to enable it for "Glow Node" to work properly.
Generated: DETERMINISTIC_2e56a28f55ca2a7a
Batch ID: 20250612_154115
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
  <title>JavaScript Detection - Glow Node</title>
  <style>
    /* Style for the message displayed if JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 15px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      margin: 20px 0;
      text-align: center;
      font-family: Arial, sans-serif;
    }
  </style>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block; /* Shown only if JavaScript is disabled */
      }
    </style>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable it for "Glow Node" to work properly.
    </div>
  </noscript>
</head>
<body>
  <div id="js-enabled-message" style="display:none;">
    <!-- This message is only shown if JavaScript is enabled -->
    <p>Welcome to Glow Node! JavaScript is enabled, and the application is ready to run.</p>
  </div>

  <script>
    // Detect if JavaScript is enabled and display the appropriate message
    document.addEventListener('DOMContentLoaded', function () {
      try {
        // Show the JavaScript-enabled message
        const jsEnabledMessage = document.getElementById('js-enabled-message');
        if (jsEnabledMessage) {
          jsEnabledMessage.style.display = 'block';
        }
      } catch (error) {
        // Log any unexpected errors for debugging
        console.error('An error occurred while detecting JavaScript:', error);
      }
    });
  </script>
</body>
</html>
```
