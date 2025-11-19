"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Implement a dark mode toggle in JavaScript for a personal website, similar to the one on Joe Previte's site. Include a smooth transition effect.
Generated: DETERMINISTIC_4ac7682b4b8257f2
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// dark-mode-toggle.js

// Get the body element
const body = document.body;

// Define the dark mode class
const DARK_MODE_CLASS = 'dark-mode';

// Get the toggle button
const toggleButton = document.getElementById('dark-mode-toggle');

// Check if the user has a preferred theme
const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

// Initialize dark mode based on user preference and local storage
const isDarkMode = prefersDarkMode || localStorage.getItem('darkMode') === 'true';

// Toggle dark mode on page load
if (isDarkMode) {
  enableDarkMode();
}

// Add event listener to the toggle button
toggleButton.addEventListener('click', toggleDarkMode);

// Function to enable dark mode
function enableDarkMode() {
  // Add the dark mode class to the body
  body.classList.add(DARK_MODE_CLASS);

  // Update local storage
  localStorage.setItem('darkMode', 'true');

  // Update the toggle button text
  toggleButton.textContent = 'Light Mode';
}

// Function to disable dark mode
function disableDarkMode() {
  // Remove the dark mode class from the body
  body.classList.remove(DARK_MODE_CLASS);

  // Update local storage
  localStorage.setItem('darkMode', 'false');

  // Update the toggle button text
  toggleButton.textContent = 'Dark Mode';
}

// Function to toggle dark mode
function toggleDarkMode() {
  // Check if dark mode is enabled
  if (body.classList.contains(DARK_MODE_CLASS)) {
    // Disable dark mode
    disableDarkMode();
  } else {
    // Enable dark mode
    enableDarkMode();
  }
}

// Add a transition effect
body.classList.add('transition');

// Remove the transition class after the transition duration
setTimeout(() => {
  body.classList.remove('transition');
}, 500);
```

```css
/* dark-mode-styles.css */

body {
  transition: background-color 0.5s, color 0.5s;
}

body.dark-mode {
  background-color: #333;
  color: #fff;
}

body.transition {
  transition: background-color 0.5s, color 0.5s;
}

#dark-mode-toggle {
  position: fixed;
  top: 10px;
  right: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

#dark-mode-toggle:hover {
  background-color: #ccc;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dark Mode Toggle</title>
  <link rel="stylesheet" href="dark-mode-styles.css">
</head>
<body>
  <button id="dark-mode-toggle">Dark Mode</button>
  <script src="dark-mode-toggle.js"></script>
</body>
</html>
```
