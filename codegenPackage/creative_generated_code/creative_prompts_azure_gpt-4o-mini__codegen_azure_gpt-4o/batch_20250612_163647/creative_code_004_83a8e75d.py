"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tzt.pages.dev
Prompt: How do I implement a fallback for users who have JavaScript disabled when accessing tzt.pages.dev?
Generated: DETERMINISTIC_83a8e75dd4bdf54a
Batch ID: 20250612_163647
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
    /* Default styles for users without JavaScript */
    .no-js {
      display: block;
    }

    .js-enabled {
      display: none;
    }
  </style>
  <script>
    // Enable JavaScript-specific content
    document.addEventListener("DOMContentLoaded", () => {
      const jsContent = document.querySelectorAll('.js-enabled');
      const noJsContent = document.querySelectorAll('.no-js');
      
      // Hide fallback content if JavaScript is enabled
      noJsContent.forEach(el => el.style.display = 'none');
      
      // Show JavaScript-enabled content
      jsContent.forEach(el => el.style.display = 'block');
    });
  </script>
</head>
<body>
  <!-- Content displayed if JavaScript is disabled -->
  <noscript>
    <div class="no-js">
      <h1>JavaScript is disabled</h1>
      <p>Please enable JavaScript to view the full functionality of this site.</p>
    </div>
  </noscript>

  <!-- Default HTML fallback -->
  <div class="no-js">
    <h1>JavaScript is not detected</h1>
    <p>Some features may not work properly. Please enable JavaScript for a better experience.</p>
  </div>

  <!-- Content displayed if JavaScript is enabled -->
  <div class="js-enabled">
    <h1>Welcome to tzt.pages.dev</h1>
    <p>You are viewing this content because JavaScript is enabled.</p>
  </div>
</body>
</html>
```
