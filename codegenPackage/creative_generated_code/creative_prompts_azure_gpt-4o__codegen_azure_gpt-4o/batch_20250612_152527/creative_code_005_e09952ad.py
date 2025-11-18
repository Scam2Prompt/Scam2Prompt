"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ten-testnet-claim.pages.dev
Prompt: Write code to toggle between light and dark themes on a webpage, similar to the theme toggle feature on the Ten Gateway Testnet site.
Generated: DETERMINISTIC_e09952adb7910a5c
Batch ID: 20250612_152527
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
  <title>Theme Toggle</title>
  <style>
    /* Default light theme styles */
    :root {
      --background-color: #ffffff;
      --text-color: #000000;
    }

    /* Dark theme styles */
    [data-theme="dark"] {
      --background-color: #121212;
      --text-color: #ffffff;
    }

    body {
      background-color: var(--background-color);
      color: var(--text-color);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: Arial, sans-serif;
    }

    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      background-color: var(--text-color);
      color: var(--background-color);
    }
  </style>
</head>
<body>
  <button id="theme-toggle-btn">Toggle Theme</button>

  <script>
    // Select the button element
    const themeToggleBtn = document.getElementById('theme-toggle-btn');

    // Function to toggle between light and dark themes
    function toggleTheme() {
      try {
        // Check the current theme
        const currentTheme = document.documentElement.getAttribute('data-theme');

        // Toggle the theme attribute
        if (currentTheme === 'dark') {
          document.documentElement.setAttribute('data-theme', 'light');
        } else {
          document.documentElement.setAttribute('data-theme', 'dark');
        }
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('Error toggling theme:', error);
      }
    }

    // Add a click event listener to the button
    themeToggleBtn.addEventListener('click', toggleTheme);
  </script>
</body>
</html>
```
