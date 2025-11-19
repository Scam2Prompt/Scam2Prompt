"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a JavaScript function that toggles dark mode on a webpage, similar to the functionality mentioned on Joe Previte's site.
Generated: DETERMINISTIC_26d489dcea919fc5
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to toggle dark mode on the webpage
function toggleDarkMode() {
    // Select the body element
    const body = document.body;

    // Check if dark mode is currently enabled
    const isDarkMode = body.classList.toggle('dark-mode');

    // Update local storage to remember the user's preference
    try {
        localStorage.setItem('darkMode', isDarkMode);
    } catch (error) {
        console.error('Error saving dark mode preference:', error);
    }

    // Update the button text based on the current mode
    const toggleButton = document.getElementById('darkModeToggle');
    if (toggleButton) {
        toggleButton.textContent = isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode';
    }
}

// Function to initialize dark mode based on saved preference
function initializeDarkMode() {
    try {
        const darkModePreference = localStorage.getItem('darkMode') === 'true';
        if (darkModePreference) {
            document.body.classList.add('dark-mode');
        }
    } catch (error) {
        console.error('Error retrieving dark mode preference:', error);
    }
}

// Event listener for the toggle button
document.addEventListener('DOMContentLoaded', () => {
    // Initialize dark mode on page load
    initializeDarkMode();

    // Add event listener to the toggle button
    const toggleButton = document.getElementById('darkModeToggle');
    if (toggleButton) {
        toggleButton.addEventListener('click', toggleDarkMode);
    } else {
        console.warn('Toggle button not found. Ensure it has the ID "darkModeToggle".');
    }
});
```

```css
/* CSS for dark mode */
body.dark-mode {
    background-color: #121212; /* Dark background */
    color: #ffffff; /* Light text color */
}

/* Optional: Style for the toggle button */
#darkModeToggle {
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    font-size: 16px;
}
```

```html
<!-- HTML structure for the toggle button -->
<button id="darkModeToggle">Switch to Dark Mode</button>
```
