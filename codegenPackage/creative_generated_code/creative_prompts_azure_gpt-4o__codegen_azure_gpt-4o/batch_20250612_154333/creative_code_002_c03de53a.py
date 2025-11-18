"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fansliebe.com
Prompt: Create a frontend design for a social media platform with light/dark themes and RTL language support, inspired by Fansliebe's customizable themes.
Generated: DETERMINISTIC_c03de53afc32c13a
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Media Platform</title>
    <style>
        /* Base styles for light and dark themes */
        :root {
            --primary-color-light: #ffffff;
            --secondary-color-light: #f5f5f5;
            --text-color-light: #000000;

            --primary-color-dark: #181818;
            --secondary-color-dark: #242424;
            --text-color-dark: #ffffff;

            --transition-speed: 0.3s ease;
        }

        /* Light theme */
        body.light-theme {
            background-color: var(--primary-color-light);
            color: var(--text-color-light);
            transition: background-color var(--transition-speed), color var(--transition-speed);
        }

        /* Dark theme */
        body.dark-theme {
            background-color: var(--primary-color-dark);
            color: var(--text-color-dark);
            transition: background-color var(--transition-speed), color var(--transition-speed);
        }

        /* RTL-specific styles */
        [dir="rtl"] {
            direction: rtl;
            text-align: right;
        }

        /* General container styling */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Header */
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
        }

        .theme-toggle, .rtl-toggle {
            cursor: pointer;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            background-color: var(--secondary-color-light);
            transition: background-color var(--transition-speed);
        }

        body.dark-theme .theme-toggle,
        body.dark-theme .rtl-toggle {
            background-color: var(--secondary-color-dark);
        }

        /* Posts styling */
        .post {
            border: 1px solid var(--secondary-color-light);
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            background-color: var(--secondary-color-light);
        }

        body.dark-theme .post {
            background-color: var(--secondary-color-dark);
            border-color: var(--secondary-color-dark);
        }
    </style>
</head>
<body class="light-theme">
    <div class="container">
        <!-- Header section -->
        <header>
            <h1>Social Media Platform</h1>
            <div>
                <button class="theme-toggle" id="theme-toggle">Toggle Theme</button>
                <button class="rtl-toggle" id="rtl-toggle">Toggle RTL</button>
            </div>
        </header>

        <!-- Posts section -->
        <div class="post">
            <p>This is a post on the social media platform.</p>
        </div>
        <div class="post">
            <p>Another post with some text content.</p>
        </div>
    </div>

    <script>
        // Theme toggle functionality
        const themeToggle = document.getElementById('theme-toggle');
        const rtlToggle = document.getElementById('rtl-toggle');

        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-theme');
            document.body.classList.toggle('light-theme');
        });

        // RTL toggle functionality
        rtlToggle.addEventListener('click', () => {
            if (document.documentElement.getAttribute('dir') === 'ltr') {
                document.documentElement.setAttribute('dir', 'rtl');
            } else {
                document.documentElement.setAttribute('dir', 'ltr');
            }
        });
    </script>
</body>
</html>
```
