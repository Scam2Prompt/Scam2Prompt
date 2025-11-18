"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Write a function in JavaScript to toggle between light and dark themes on the Ten Gateway interface.
Generated: DETERMINISTIC_8f17253b87d363fd
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to toggle between light and dark themes
function toggleTheme() {
    try {
        // Get the current theme from local storage or default to light
        const currentTheme = localStorage.getItem('theme') || 'light';
        
        // Determine the new theme
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';

        // Update the body class to reflect the new theme
        document.body.classList.remove(currentTheme);
        document.body.classList.add(newTheme);

        // Store the new theme in local storage for persistence
        localStorage.setItem('theme', newTheme);
        
        // Optional: Update any other elements or styles if necessary
        updateThemeStyles(newTheme);
        
        console.log(`Theme changed to ${newTheme}`);
    } catch (error) {
        console.error('Error toggling theme:', error);
    }
}

// Optional function to update additional styles based on theme
function updateThemeStyles(theme) {
    // Implementation for updating any other styles can go here
    // For example, updating text colors, background colors, etc.
}

// Event listener to toggle theme on button click
document.getElementById('theme-toggle-button').addEventListener('click', toggleTheme);

// Immediately apply the stored theme on page load
(function applyStoredTheme() {
    const storedTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.add(storedTheme);
})();
```
