"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imotokaen.com
Prompt: How do I create a fallback for users who have JavaScript disabled on mobile devices?
Generated: DETERMINISTIC_238fcd8257933432
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
  <title>Fallback Example</title>
  <style>
    /* Style for the fallback message */
    .no-js-message {
      display: none; /* Hidden by default */
      text-align: center;
      padding: 20px;
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      margin: 20px;
      border-radius: 5px;
    }
    /* Show the message if JavaScript is disabled */
    .no-js .no-js-message {
      display: block;
    }
  </style>
  <script>
    // Add a class to the <html> element if JavaScript is enabled
    document.documentElement.classList.add('js');
  </script>
</head>
<body>
  <noscript>
    <!-- Fallback content for users with JavaScript disabled -->
    <div class="no-js-message">
      JavaScript is disabled on your browser. Please enable JavaScript for the best experience.
    </div>
  </noscript>
  
  <main>
    <!-- Main application content here -->
    <h1>Welcome to our website</h1>
    <p>If you see this content, JavaScript is enabled.</p>
  </main>
</body>
</html>
```
