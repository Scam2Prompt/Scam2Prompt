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
/**
 * Toggles dark mode on the webpage by adding/removing a 'dark' class on the document element.
 * Persists the user's preference in localStorage for consistency across sessions.
 */
function toggleDarkMode() {
    try {
        const htmlElement = document.documentElement;
        const isDarkMode = htmlElement.classList.contains('dark');
        
        // Toggle the 'dark' class
        if (isDarkMode) {
            htmlElement.classList.remove('dark');
            localStorage.setItem('darkMode', 'false');
        } else {
            htmlElement.classList.add('dark');
            localStorage.setItem('darkMode', 'true');
        }
    } catch (error) {
        console.error('Error toggling dark mode:', error);
    }
}

/**
 * Initializes dark mode based on user preference stored in localStorage or system preference.
 * Should be called when the page loads.
 */
function initializeDarkMode() {
    try {
        const htmlElement = document.documentElement;
        const storedPreference = localStorage.getItem('darkMode');
        const systemPreference = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        if (storedPreference === 'true' || (storedPreference === null && systemPreference)) {
            htmlElement.classList.add('dark');
        }
    } catch (error) {
        console.error('Error initializing dark mode:', error);
    }
}

// Initialize dark mode when the script loads
initializeDarkMode();

// Example event listener for a dark mode toggle button (uncomment to use)
// document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);
```
