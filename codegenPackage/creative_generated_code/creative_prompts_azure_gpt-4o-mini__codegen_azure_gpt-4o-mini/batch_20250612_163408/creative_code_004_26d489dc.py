"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a JavaScript function that toggles dark mode on a webpage, similar to the functionality mentioned on Joe Previte's site.
Generated: DETERMINISTIC_26d489dcea919fc5
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to toggle dark mode on the webpage
function toggleDarkMode() {
    // Get the current theme from localStorage or set default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Determine the new theme based on the current theme
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    // Apply the new theme to the body element
    document.body.classList.remove(currentTheme);
    document.body.classList.add(newTheme);
    
    // Update the theme in localStorage for persistence
    localStorage.setItem('theme', newTheme);
}

// Function to initialize the theme on page load
function initializeTheme() {
    // Get the stored theme from localStorage
    const savedTheme = localStorage.getItem('theme') || 'light';
    
    // Apply the saved theme to the body element
    document.body.classList.add(savedTheme);
}

// Add event listener to a button for toggling dark mode
document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);

// Initialize the theme on page load
document.addEventListener('DOMContentLoaded', initializeTheme);
```

```html
<!-- HTML structure for the toggle button -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Mode Toggle Example</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS -->
</head>
<body>
    <button id="darkModeToggle">Toggle Dark Mode</button> <!-- Button for toggling dark mode -->
    <script src="script.js"></script> <!-- Link to JavaScript file -->
</body>
</html>
```

```css
/* styles.css */

/* Default light theme styles */
body {
    background-color: white;
    color: black;
    transition: background-color 0.3s, color 0.3s; /* Smooth transition */
}

/* Dark theme styles */
body.dark {
    background-color: black;
    color: white;
}
```
