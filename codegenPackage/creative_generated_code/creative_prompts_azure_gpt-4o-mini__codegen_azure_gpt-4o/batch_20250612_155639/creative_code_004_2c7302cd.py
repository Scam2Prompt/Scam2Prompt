"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: How do I implement a fallback message for users who have JavaScript disabled when they visit the Celestia domain details page?
Generated: DETERMINISTIC_2c7302cdea4cfbd2
Batch ID: 20250612_155639
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
  <title>Celestia Domain Details</title>
  <style>
    /* Style for fallback message */
    .no-js-message {
      color: #ff0000;
      font-size: 18px;
      text-align: center;
      margin-top: 50px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users without JavaScript enabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is required to view the Celestia domain details page. 
      Please enable JavaScript in your browser settings and try again.
    </div>
  </noscript>

  <!-- Main content that requires JavaScript -->
  <div id="app">
    <!-- Content dynamically loaded via JavaScript -->
  </div>

  <script>
    // Ensure JavaScript is enabled and functional
    document.getElementById('app').innerHTML = `
      <h1>Welcome to the Celestia Domain Details Page</h1>
      <p>Here you can find all the relevant details about your domain.</p>
    `;

    // Example fallback for potential JavaScript errors
    try {
      // Add your JavaScript logic here (e.g., fetch data, manipulate DOM)
      console.log('JavaScript is enabled and running!');
    } catch (error) {
      console.error('An error occurred while executing JavaScript:', error);
      alert('We encountered an issue. Please refresh the page or contact support.');
    }
  </script>
</body>
</html>
```
