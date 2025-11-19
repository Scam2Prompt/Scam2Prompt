"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-virtuswap.pages.dev
Prompt: Provide an example of how to enable a light theme in a web app like Virtuswap.
Generated: DETERMINISTIC_ac7e128e68bc7dd0
Batch ID: 20250612_140309
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
    <title>Virtuswap Light Theme Example</title>
    <style>
        /* Default dark theme styles */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
        }

        .theme-button {
            padding: 10px 20px;
            margin: 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        /* Light theme styles */
        body.light-theme {
            background-color: #f5f5f5;
            color: #000000;
        }

        .theme-button.light {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #ccc;
        }

        .theme-button.dark {
            background-color: #333333;
            color: #ffffff;
        }
    </style>
</head>
<body>
    <button id="themeToggleButton" class="theme-button dark">Enable Light Theme</button>

    <script>
        // Error-safe theme toggling function
        document.addEventListener("DOMContentLoaded", () => {
            const themeButton = document.getElementById("themeToggleButton");

            // Verify the button exists
            if (!themeButton) {
                console.error("Error: Theme toggle button not found.");
                return;
            }

            // Event listener to toggle between themes
            themeButton.addEventListener("click", () => {
                try {
                    const isLightTheme = document.body.classList.contains("light-theme");

                    if (isLightTheme) {
                        // Switch to dark theme
                        document.body.classList.remove("light-theme");
                        themeButton.classList.remove("light");
                        themeButton.classList.add("dark");
                        themeButton.textContent = "Enable Light Theme";
                    } else {
                        // Switch to light theme
                        document.body.classList.add("light-theme");
                        themeButton.classList.remove("dark");
                        themeButton.classList.add("light");
                        themeButton.textContent = "Enable Dark Theme";
                    }
                } catch (error) {
                    console.error("Error toggling theme:", error);
                }
            });
        });
    </script>
</body>
</html>
```
