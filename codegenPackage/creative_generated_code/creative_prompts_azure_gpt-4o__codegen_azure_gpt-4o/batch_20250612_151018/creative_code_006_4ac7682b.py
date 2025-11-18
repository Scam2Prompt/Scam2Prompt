"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Implement a dark mode toggle in JavaScript for a personal website, similar to the one on Joe Previte's site. Include a smooth transition effect.
Generated: DETERMINISTIC_4ac7682b4b8257f2
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
  <title>Dark Mode Toggle</title>
  <style>
    /* Default light mode styles */
    body {
      background-color: #ffffff;
      color: #000000;
      font-family: Arial, sans-serif;
      transition: background-color 0.3s, color 0.3s; /* Smooth transition effect */
    }

    /* Dark mode styles */
    body.dark-mode {
      background-color: #121212;
      color: #ffffff;
    }

    .dark-mode-toggle {
      position: fixed;
      top: 10px;
      right: 10px;
      padding: 10px 15px;
      background-color: #f0f0f0;
      border: 1px solid #ccc;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
      transition: background-color 0.3s, color 0.3s;
    }

    .dark-mode-toggle.dark-mode {
      background-color: #333333;
      color: #ffffff;
      border: 1px solid #666666;
    }
  </style>
</head>
<body>
  <button id="darkModeToggle" class="dark-mode-toggle">Toggle Dark Mode</button>

  <script>
    // Select the toggle button
    const toggleButton = document.getElementById('darkModeToggle');

    // Add event listener to toggle button for dark mode toggle
    toggleButton.addEventListener('click', () => {
      try {
        // Toggle the 'dark-mode' class on the body element
        document.body.classList.toggle('dark-mode');

        // Update button styles and text based on current mode
        const isDarkMode = document.body.classList.contains('dark-mode');
        toggleButton.classList.toggle('dark-mode', isDarkMode);
        toggleButton.textContent = isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode';

        // Store user preference in localStorage
        localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
      } catch (error) {
        console.error('An error occurred while toggling dark mode:', error);
      }
    });

    // Check localStorage for saved preference and apply it
    (function initializeDarkMode() {
      try {
        const savedPreference = localStorage.getItem('darkMode');
        if (savedPreference === 'enabled') {
          document.body.classList.add('dark-mode');
          toggleButton.classList.add('dark-mode');
          toggleButton.textContent = 'Switch to Light Mode';
        }
      } catch (error) {
        console.error('An error occurred while initializing dark mode:', error);
      }
    })();
  </script>
</body>
</html>
```
