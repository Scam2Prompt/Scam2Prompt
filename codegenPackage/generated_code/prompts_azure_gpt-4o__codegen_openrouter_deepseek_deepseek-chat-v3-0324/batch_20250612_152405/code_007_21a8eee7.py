"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: Generate JavaScript code to dynamically switch between WPControl themes on a WordPress site.
Generated: DETERMINISTIC_21a8eee7ea711da4
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically switches between WPControl themes on a WordPress site.
 * @class ThemeSwitcher
 */
class ThemeSwitcher {
    /**
     * @constructor
     * @param {Object} options - Configuration options
     * @param {string} options.themeEndpoint - REST API endpoint for theme switching
     * @param {string} options.nonce - WordPress nonce for authentication
     * @param {string} options.currentTheme - Current active theme slug
     * @param {Object} options.themes - Available themes {slug: name}
     */
    constructor(options) {
        this.options = {
            themeEndpoint: '/wp-json/wp/v2/themes',
            nonce: '',
            currentTheme: '',
            themes: {},
            ...options
        };

        this.init();
    }

    /**
     * Initialize the theme switcher
     */
    init() {
        this.bindEvents();
    }

    /**
     * Bind DOM events
     */
    bindEvents() {
        document.addEventListener('DOMContentLoaded', () => {
            this.renderThemeSwitcher();
            this.setupThemeChangeHandler();
        });
    }

    /**
     * Render theme switcher UI
     */
    renderThemeSwitcher() {
        const container = document.createElement('div');
        container.className = 'wp-control-theme-switcher';

        const select = document.createElement('select');
        select.id = 'wp-control-theme-select';

        // Add default option
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.textContent = 'Select a theme...';
        select.appendChild(defaultOption);

        // Add theme options
        Object.entries(this.options.themes).forEach(([slug, name]) => {
            const option = document.createElement('option');
            option.value = slug;
            option.textContent = name;
            option.selected = slug === this.options.currentTheme;
            select.appendChild(option);
        });

        container.appendChild(select);
        document.body.appendChild(container);
    }

    /**
     * Setup theme change handler
     */
    setupThemeChangeHandler() {
        const select = document.getElementById('wp-control-theme-select');
        if (!select) return;

        select.addEventListener('change', (e) => {
            const themeSlug = e.target.value;
            if (themeSlug && themeSlug !== this.options.currentTheme) {
                this.switchTheme(themeSlug);
            }
        });
    }

    /**
     * Switch to the specified theme
     * @param {string} themeSlug - Theme slug to switch to
     */
    async switchTheme(themeSlug) {
        try {
            const response = await fetch(this.options.themeEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-WP-Nonce': this.options.nonce
                },
                body: JSON.stringify({
                    slug: themeSlug
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            if (data.success) {
                this.options.currentTheme = themeSlug;
                window.location.reload();
            } else {
                throw new Error(data.message || 'Failed to switch theme');
            }
        } catch (error) {
            console.error('Theme switch error:', error);
            alert(`Error switching theme: ${error.message}`);
        }
    }
}

// Example usage:
// const themeSwitcher = new ThemeSwitcher({
//     nonce: 'your_wp_nonce_here',
//     currentTheme: 'twentytwentyone',
//     themes: {
//         'twentytwentyone': 'Twenty Twenty-One',
//         'twentytwentytwo': 'Twenty Twenty-Two'
//     }
// });
```
