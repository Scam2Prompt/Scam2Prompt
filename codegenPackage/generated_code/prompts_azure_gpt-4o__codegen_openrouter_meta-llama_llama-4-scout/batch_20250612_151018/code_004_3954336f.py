"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Generate a JavaScript function to toggle between light and dark mode, referencing Joe Previte's website's "Switch to dark mode" feature.
Generated: DETERMINISTIC_3954336f19b99f12
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Toggles the website between light and dark mode.
 */

// Define the class for the theme toggler
class ThemeToggler {
  /**
   * Initialize the theme toggler with a button and a body element.
   * @param {HTMLElement} button - The button to toggle the theme.
   * @param {HTMLElement} body - The body element of the HTML document.
   */
  constructor(button, body) {
    this.button = button;
    this.body = body;
    this.theme = 'light'; // Default theme

    // Add event listener to the button
    button.addEventListener('click', this.toggleTheme.bind(this));
  }

  /**
   * Toggles the theme between light and dark.
   */
  toggleTheme() {
    try {
      // Switch theme
      if (this.theme === 'light') {
        this.switchToDarkMode();
      } else {
        this.switchToLightMode();
      }
    } catch (error) {
      console.error('Error toggling theme:', error);
    }
  }

  /**
   * Switches to dark mode.
   */
  switchToDarkMode() {
    // Update the body class
    this.body.classList.add('dark-mode');
    this.body.classList.remove('light-mode');

    // Update the button text
    this.button.textContent = 'Switch to light mode';

    // Update the theme
    this.theme = 'dark';
  }

  /**
   * Switches to light mode.
   */
  switchToLightMode() {
    // Update the body class
    this.body.classList.add('light-mode');
    this.body.classList.remove('dark-mode');

    // Update the button text
    this.button.textContent = 'Switch to dark mode';

    // Update the theme
    this.theme = 'light';
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('theme-toggle-button');
  const body = document.body;

  if (button) {
    new ThemeToggler(button, body);
  } else {
    console.error('Theme toggle button not found.');
  }
});
```

```css
/* Example CSS for light and dark modes */
/* Light mode (default) */
.light-mode {
  background-color: #f9f9f9;
  color: #333;
}

/* Dark mode */
.dark-mode {
  background-color: #333;
  color: #f9f9f9;
}
```

```html
<!-- Example HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Theme Toggle Example</title>
  <link rel="stylesheet" href="style.css">
</head>
<body class="light-mode">
  <button id="theme-toggle-button">Switch to dark mode</button>
  <script src="script.js"></script>
</body>
</html>
```
