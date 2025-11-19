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

```javascript
// toggle-theme.js

/**
 * Toggles the website's theme between light and dark modes.
 */

// Get the theme toggle button and body elements
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Define the available themes
const themes = {
  light: 'light',
  dark: 'dark',
};

// Get the current theme from local storage or default to light
const currentTheme = localStorage.getItem('theme') || themes.light;

// Set the initial theme
body.classList.add(currentTheme);

// Add event listener to the theme toggle button
themeToggle.addEventListener('click', () => {
  // Toggle the theme
  const newTheme = body.classList.contains(themes.light) ? themes.dark : themes.light;
  body.classList.remove(currentTheme);
  body.classList.add(newTheme);

  // Update local storage with the new theme
  localStorage.setItem('theme', newTheme);
});

// Check if the user's system prefers a dark theme
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  // If the current theme is light, offer to switch to dark
  if (currentTheme === themes.light) {
    const autoSwitch = confirm('Your system prefers dark mode. Would you like to switch?');
    if (autoSwitch) {
      body.classList.remove(currentTheme);
      body.classList.add(themes.dark);
      localStorage.setItem('theme', themes.dark);
    }
  }
}

// Handle theme toggle button's aria-label
themeToggle.setAttribute('aria-label', body.classList.contains(themes.light) ? 'Switch to dark mode' : 'Switch to light mode');

// Update aria-label on theme change
body.addEventListener('themechange', () => {
  themeToggle.setAttribute('aria-label', body.classList.contains(themes.light) ? 'Switch to dark mode' : 'Switch to light mode');
});
```

```css
/* toggle-theme.css */

/* Define light and dark themes */
body.light {
  background-color: #f9f9f9;
  color: #333;
}

body.dark {
  background-color: #333;
  color: #f9f9f9;
}

/* Optional: Add more styles for specific elements */
body.light h1,
body.light h2,
body.light h3 {
  color: #00698f;
}

body.dark h1,
body.dark h2,
body.dark h3 {
  color: #87ceeb;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Theme Toggle Example</title>
  <link rel="stylesheet" href="toggle-theme.css">
</head>
<body class="light">
  <button id="theme-toggle">Toggle theme</button>
  <h1>Welcome to my website!</h1>
  <p>This website has a toggleable theme.</p>
  <script src="toggle-theme.js"></script>
</body>
</html>
```
