"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Create a script to toggle between light and dark modes on a website, inspired by Joe Previte's site design.
Generated: DETERMINISTIC_f3c67e915172bd13
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Light/Dark Mode Toggle</title>
    <link id="theme-stylesheet" rel="stylesheet" href="light-mode.css">
    <style>
        /* Basic styles for light and dark modes */
        body {
            transition: background-color 0.3s, color 0.3s;
        }
        .light-mode {
            background-color: #ffffff;
            color: #000000;
        }
        .dark-mode {
            background-color: #000000;
            color: #ffffff;
        }
        #toggle-button {
            padding: 10px 20px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body class="light-mode">
    <button id="toggle-button">Switch to Dark Mode</button>

    <script>
        // Function to toggle between light and dark modes
        function toggleTheme() {
            const body = document.body;
            const button = document.getElementById('toggle-button');

            // Check current theme and toggle
            if (body.classList.contains('light-mode')) {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                button.textContent = 'Switch to Light Mode';
            } else {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                button.textContent = 'Switch to Dark Mode';
            }

            // Save the current theme in localStorage
            try {
                localStorage.setItem('theme', body.className);
            } catch (error) {
                console.error('Error saving theme to localStorage:', error);
            }
        }

        // Function to load the saved theme from localStorage
        function loadTheme() {
            try {
                const savedTheme = localStorage.getItem('theme');
                if (savedTheme) {
                    document.body.className = savedTheme;
                    const button = document.getElementById('toggle-button');
                    button.textContent = savedTheme === 'dark-mode' ? 'Switch to Light Mode' : 'Switch to Dark Mode';
                }
            } catch (error) {
                console.error('Error loading theme from localStorage:', error);
            }
        }

        // Event listener for the toggle button
        document.getElementById('toggle-button').addEventListener('click', toggleTheme);

        // Load the theme on page load
        window.onload = loadTheme;
    </script>
</body>
</html>
```

**Note:** Ensure you create a `light-mode.css` file if you want to include additional styles for the light mode. The basic styles are included in the `<style>` tag for demonstration purposes.
