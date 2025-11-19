"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imptp.com
Prompt: Can you provide a code snippet that checks if JavaScript is enabled on a mobile browser?
Generated: DETERMINISTIC_3f60bf985f7c9875
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
  <title>JavaScript Check</title>
</head>
<body>
  <!-- Fallback message for browsers with JavaScript disabled -->
  <noscript>
    <p style="color: red;">JavaScript is disabled on your mobile browser. Please enable it to proceed.</p>
  </noscript>

  <!-- Container to display result dynamically if JavaScript is enabled -->
  <div id="js-check-result"></div>

  <script>
    // Function to check if JavaScript is enabled and display a message
    (function() {
      try {
        const resultContainer = document.getElementById("js-check-result");

        // Ensure the container exists in the DOM
        if (resultContainer) {
          resultContainer.textContent = "JavaScript is enabled on your mobile browser.";
          resultContainer.style.color = "green"; // Style the message appropriately
        }
      } catch (error) {
        // Fallback error handling (not likely needed for this simple check)
        console.error("An error occurred while checking JavaScript:", error);
      }
    })();
  </script>
</body>
</html>
```
