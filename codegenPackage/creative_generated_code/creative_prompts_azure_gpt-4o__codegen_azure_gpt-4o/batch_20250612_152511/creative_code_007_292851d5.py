"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ten-testnet.pages.dev
Prompt: Write a script to toggle between light and dark themes on a webpage, similar to the theme toggle feature on the Ten Gateway Testnet site.
Generated: DETERMINISTIC_292851d55cd1d39d
Batch ID: 20250612_152511
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
    /* Default Light Theme */
    body.light {
      background-color: #ffffff;
      color: #000000;
      font-family: Arial, sans-serif;
      transition: background-color 0.3s, color 0.3s;
    }

    /* Dark Theme */
    body.dark {
      background-color: #121212;
      color: #ffffff;
      transition: background-color 0.3s, color 0.3s;
    }

    .theme-toggle-btn {
      cursor: pointer;
      padding: 10px 20px;
      background-color: #007BFF;
      color: #ffffff;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      margin: 20px;
      transition: background-color 0.3s;
    }

    .theme-toggle-btn:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body class="light">
  <button id="themeToggleBtn" class="theme-toggle-btn">Switch to Dark Theme</button>

  <script>
    // Select the button element and the body element
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const body = document.body;

    // Load theme preference from localStorage (if set)
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      body.className = savedTheme; // Apply saved theme
      updateButtonText(savedTheme); // Update button text based on saved theme
    }

    // Add a click event listener to toggle themes
    themeToggleBtn.addEventListener('click', () => {
      try {
        // Determine the current theme and toggle it
        const currentTheme = body.className;
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';

        // Update the body class to the new theme
        body.className = newTheme;

        // Save the user's preference in localStorage
        localStorage.setItem('theme', newTheme);

        // Update button text to reflect the new theme
        updateButtonText(newTheme);
      } catch (error) {
        console.error('Error toggling theme:', error);
      }
    });

    /**
     * Updates the button text based on the selected theme.
     * @param {string} theme - The current theme ('light' or 'dark').
     */
    function updateButtonText(theme) {
      themeToggleBtn.textContent =
        theme === 'light' ? 'Switch to Dark Theme' : 'Switch to Light Theme';
    }
  </script>
</body>
</html>
```
