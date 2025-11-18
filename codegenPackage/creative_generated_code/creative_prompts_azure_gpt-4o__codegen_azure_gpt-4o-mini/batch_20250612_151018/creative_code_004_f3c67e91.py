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
    <link id="theme-stylesheet" rel="stylesheet" href="light-theme.css">
    <style>
        /* Default body styles */
        body {
            transition: background-color 0.3s ease, color 0.3s ease;
            margin: 0;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        /* Light theme styles */
        .light-theme {
            background-color: #ffffff;
            color: #000000;
        }
        /* Dark theme styles */
        .dark-theme {
            background-color: #222222;
            color: #ffffff;
        }
        /* Button styles */
        .toggle-button {
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
        }
    </style>
</head>
<body class="light-theme">
    <h1>Toggle Light/Dark Mode</h1>
    <p>Click the button below to switch between light and dark modes.</p>
    <button class="toggle-button" id="theme-toggle">Toggle Dark Mode</button>

    <script>
        // Function to toggle between light and dark themes
        function toggleTheme() {
            // Get the current theme from the body class
            const body = document.body;
            const currentTheme = body.classList.contains('dark-theme');

            // Toggle class based on current theme
            if (currentTheme) {
                body.classList.remove('dark-theme');
                body.classList.add('light-theme');
                localStorage.setItem('theme', 'light'); // Save user's preference
            } else {
                body.classList.remove('light-theme');
                body.classList.add('dark-theme');
                localStorage.setItem('theme', 'dark'); // Save user's preference
            }
        }

        // Load the user's theme preference from localStorage
        function loadTheme() {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme) {
                document.body.classList.remove('light-theme', 'dark-theme');
                document.body.classList.add(savedTheme + '-theme');
            }
        }

        // Add event listener to the button
        document.getElementById('theme-toggle').addEventListener('click', toggleTheme);

        // Load the theme on initial page load
        loadTheme();
    </script>
</body>
</html>
```

This code provides a simple light/dark mode toggle for a website, using local storage to remember the user's preference. The transitions between themes are smooth, and best practices for HTML, CSS, and JavaScript are followed.
