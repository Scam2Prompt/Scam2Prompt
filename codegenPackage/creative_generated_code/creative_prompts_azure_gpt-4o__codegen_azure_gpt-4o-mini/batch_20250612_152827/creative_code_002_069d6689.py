"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-revenue.pages.dev
Prompt: Generate code to toggle between light and dark themes in a DeFi revenue tracking web application.
Generated: DETERMINISTIC_069d6689b4b8fdc8
Batch ID: 20250612_152827
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
    <title>DeFi Revenue Tracker</title>
    <link id="theme-stylesheet" rel="stylesheet" href="light-theme.css">
    <script>
        // Function to toggle between light and dark themes
        function toggleTheme() {
            const themeStylesheet = document.getElementById('theme-stylesheet');
            // Check current theme from the link element
            if (themeStylesheet.getAttribute('href') === 'light-theme.css') {
                themeStylesheet.setAttribute('href', 'dark-theme.css');
                localStorage.setItem('theme', 'dark'); // Store the user's preference
            } else {
                themeStylesheet.setAttribute('href', 'light-theme.css');
                localStorage.setItem('theme', 'light'); // Store the user's preference
            }
        }

        // Function to apply the saved theme on page load
        function applySavedTheme() {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme) {
                const themeStylesheet = document.getElementById('theme-stylesheet');
                themeStylesheet.setAttribute('href', savedTheme === 'dark' ? 'dark-theme.css' : 'light-theme.css');
            }
        }

        // Ensures the theme is applied on initial page load
        window.onload = applySavedTheme;
    </script>
    <style>
        /* Basic styles for the app */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            transition: background-color 0.3s, color 0.3s;
        }
        
        /* Light theme styles */
        .light-theme {
            background-color: #ffffff;
            color: #000000;
        }

        /* Dark theme styles */
        .dark-theme {
            background-color: #000000;
            color: #ffffff;
        }

        /* Button styles */
        #theme-toggle {
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
    </style>
</head>
<body class="light-theme">
    <h1>DeFi Revenue Tracker</h1>
    <button id="theme-toggle" onclick="toggleTheme()">Toggle Theme</button>
    <script>
        // Set initial class based on the theme
        const body = document.body;
        const themeStylesheet = document.getElementById('theme-stylesheet');
        if (themeStylesheet.getAttribute('href') === 'dark-theme.css') {
            body.classList.remove('light-theme');
            body.classList.add('dark-theme');
        } else {
            body.classList.remove('dark-theme');
            body.classList.add('light-theme');
        }
    </script>
</body>
</html>
```
### Note:
Make sure to create the respective CSS files (`light-theme.css` and `dark-theme.css`) with appropriate styling for each theme. The code above provides a basic functionality to toggle between themes and saves the user's preference in `localStorage`.
