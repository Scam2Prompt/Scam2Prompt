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
        /* Basic styles for light and dark mode */
        body {
            transition: background-color 0.5s ease, color 0.5s ease; /* Smooth transition effect */
            background-color: #ffffff; /* Light mode background */
            color: #000000; /* Light mode text color */
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        /* Dark mode styles */
        body.dark-mode {
            background-color: #000000; /* Dark mode background */
            color: #ffffff; /* Dark mode text color */
        }

        /* Toggle button styles */
        #darkModeToggle {
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            margin-top: 20px;
            transition: background-color 0.3s ease;
        }

        /* Button styles for dark mode */
        body.dark-mode #darkModeToggle {
            background-color: #ffffff;
            color: #000000;
        }

        /* Button styles for light mode */
        body #darkModeToggle {
            background-color: #000000;
            color: #ffffff;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Personal Website</h1>
    <p>This is an example of a dark mode toggle implementation.</p>
    <button id="darkModeToggle">Toggle Dark Mode</button>

    <script>
        // Function to toggle dark mode
        function toggleDarkMode() {
            // Toggle the 'dark-mode' class on the body element
            document.body.classList.toggle('dark-mode');

            // Update local storage based on the current mode
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        }

        // Function to apply the saved theme on page load
        function applySavedTheme() {
            const savedTheme = localStorage.getItem('theme');

            // If a theme is saved, apply it
            if (savedTheme === 'dark') {
                document.body.classList.add('dark-mode');
            }
        }

        // Add event listener to the toggle button
        document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);

        // Apply saved theme when the page loads
        applySavedTheme();
    </script>
</body>
</html>
```
