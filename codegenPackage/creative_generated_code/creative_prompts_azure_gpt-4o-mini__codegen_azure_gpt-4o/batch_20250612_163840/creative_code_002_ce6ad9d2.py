"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkyyj.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a mobile device for a web application?
Generated: DETERMINISTIC_ce6ad9d20882ea62
Batch ID: 20250612_163840
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
  <title>JavaScript Enabled Check</title>
</head>
<body>
  <!-- Default message for users if JavaScript is disabled -->
  <noscript>
    <div style="text-align: center; margin-top: 20px;">
      <p style="color: red; font-size: 18px;">JavaScript is disabled on your device. Please enable JavaScript to use this web application.</p>
    </div>
  </noscript>

  <!-- Content to be shown when JavaScript is enabled -->
  <div id="js-enabled-content" style="text-align: center; margin-top: 20px;">
    <!-- This will be hidden by default and shown only if JavaScript is enabled -->
    <p style="color: green; font-size: 18px;">JavaScript is enabled on your device. Welcome to the application!</p>
  </div>

  <script>
    // Ensure the content for JavaScript-enabled users is visible
    try {
      const jsEnabledContent = document.getElementById('js-enabled-content');
      if (jsEnabledContent) {
        jsEnabledContent.style.display = 'block'; // Show content for JavaScript-enabled users
      }
    } catch (error) {
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
the message to the body
        document.body.appendChild(messageElement);
      } catch (error) {
        // Handle any unexpected errors
        console.error('An error occurred while checking JavaScript:', error);
      }
    }

    // Call the function to run the check
    checkJavaScriptEnabled();
  </script>
</body>
</html>
```
