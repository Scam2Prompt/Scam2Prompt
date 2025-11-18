"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wpcontrol.be
Prompt: Generate JavaScript code to dynamically switch between WPControl themes on a WordPress site.
Generated: DETERMINISTIC_21a8eee7ea711da4
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * WPControl Theme Switcher
 * This script dynamically switches between available WPControl themes on a WordPress site.
 * It listens for theme change events and applies the selected theme.
 */

// Function to fetch available themes from the WordPress REST API
async function fetchAvailableThemes() {
    try {
        const response = await fetch('/wp-json/wp/v2/themes');
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const themes = await response.json();
        return themes;
    } catch (error) {
        console.error('Error fetching themes:', error);
        return [];
    }
}

// Function to apply the selected theme
async function applyTheme(themeSlug) {
    try {
        const response = await fetch('/wp-json/wp/v2/themes/' + themeSlug + '/activate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-WP-Nonce': wpApiSettings.nonce // Ensure to include the nonce for authentication
            }
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const result = await response.json();
        console.log('Theme switched successfully:', result);
        location.reload(); // Reload the page to apply the new theme
    } catch (error) {
        console.error('Error applying theme:', error);
    }
}

// Function to initialize theme switcher
async function initThemeSwitcher() {
    const themes = await fetchAvailableThemes();
    const themeSelect = document.createElement('select');
    
    // Populate the select element with available themes
    themes.forEach(theme => {
        const option = document.createElement('option');
        option.value = theme.slug;
        option.textContent = theme.name;
        themeSelect.appendChild(option);
    });

    // Listen for theme change events
    themeSelect.addEventListener('change', (event) => {
        const selectedTheme = event.target.value;
        if (selectedTheme) {
            applyTheme(selectedTheme);
        }
    });

    // Append the select element to the body (or any specific container)
    document.body.appendChild(themeSelect);
}

// Run the theme switcher initialization on DOM content loaded
document.addEventListener('DOMContentLoaded', () => {
    initThemeSwitcher();
});
```
