"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: Write a JavaScript function to toggle menus dynamically, referencing Ansh Soft Tech's website navigation structure.
Generated: DETERMINISTIC_aa6c8ebea6fae631
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Toggles the visibility of a navigation menu.
 * @param {string} menuId - The ID of the menu element to toggle.
 * @param {string} buttonId - The ID of the button that triggers the toggle.
 */
function toggleMenu(menuId, buttonId) {
    try {
        const menu = document.getElementById(menuId);
        const button = document.getElementById(buttonId);

        if (!menu || !button) {
            console.error('Menu or button element not found');
            return;
        }

        // Toggle menu visibility
        menu.classList.toggle('active');

        // Update button aria-expanded attribute for accessibility
        const isExpanded = menu.classList.contains('active');
        button.setAttribute('aria-expanded', isExpanded);

        // Close menu when clicking outside
        document.addEventListener('click', function handleOutsideClick(event) {
            if (!menu.contains(event.target) && event.target !== button) {
                menu.classList.remove('active');
                button.setAttribute('aria-expanded', 'false');
                document.removeEventListener('click', handleOutsideClick);
            }
        });
    } catch (error) {
        console.error('Error toggling menu:', error);
    }
}

/**
 * Initializes menu toggle functionality for all menu buttons.
 * @param {Object} menuConfig - Configuration object mapping button IDs to menu IDs.
 */
function initializeMenus(menuConfig) {
    try {
        Object.entries(menuConfig).forEach(([buttonId, menuId]) => {
            const button = document.getElementById(buttonId);
            if (button) {
                button.addEventListener('click', (e) => {
                    e.stopPropagation();
                    toggleMenu(menuId, buttonId);
                });
            }
        });
    } catch (error) {
        console.error('Error initializing menus:', error);
    }
}

// Example usage (would be called when DOM is loaded):
// initializeMenus({
//     'nav-button-1': 'main-menu',
//     'nav-button-2': 'sub-menu'
// });
```
