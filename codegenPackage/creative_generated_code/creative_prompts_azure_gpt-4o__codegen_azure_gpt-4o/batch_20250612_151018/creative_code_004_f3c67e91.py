"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Create a script to toggle between light and dark modes on a website, inspired by Joe Previte's site design.
Generated: DETERMINISTIC_f3c67e915172bd13
Batch ID: 20250612_151018
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
  <title>Light/Dark Mode Toggle</title>
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

    /* Applying theme styles */
    body {
      background-color: var(--background-color);
      color: var(--text-color);
      margin: 0;
      font-family: Arial, sans-serif;
      transition: background-color 0.3s, color 0.3s;
    }

    .toggle-button {
      position: absolute;
      top: 1rem;
      right: 1rem;
      padding: 0.5rem 1rem;
      font-size: 1rem;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      background-color: var(--text-color);
      color: var(--background-color);
      transition: background-color 0.3s, color 0.3s;
    }
  </style>
</head>
<body>
  <button class="toggle-button" id="themeToggleBtn">Toggle Theme</button>

  <script>
    // Select the theme toggle button
    const themeToggleBtn = document.getElementById('themeToggleBtn');

    // Function to toggle between light and dark themes
    function toggleTheme() {
      // Check the current theme
      const currentTheme = document.documentElement.getAttribute('data-theme');

      // Toggle the theme
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);

      // Update the button text based on the theme
      themeToggleBtn.textContent = newTheme === 'dark' ? 'Light Mode' : 'Dark Mode';

      // Save the selected theme to localStorage for persistence
      localStorage.setItem('theme', newTheme);
    }

    // Event listener for the theme toggle button
    themeToggleBtn.addEventListener('click', toggleTheme);

    // Load the saved theme from localStorage on page load
    window.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
      themeToggleBtn.textContent = savedTheme === 'dark' ? 'Light Mode' : 'Dark Mode';
    });
  </script>
</body>
</html>
```
