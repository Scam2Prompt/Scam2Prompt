"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petn.org
Prompt: Create a JavaScript function that dynamically generates a navigation menu similar to the one found on the PETN website, allowing users to access different church resources.
Generated: DETERMINISTIC_3e0aa5152019e4b2
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a dynamic navigation menu for church resources.
 * This function creates a navigation bar and appends it to the specified container.
 *
 * @param {string} containerId - The ID of the HTML element where the menu will be appended.
 * @param {Array} menuItems - An array of objects representing the menu items.
 * @param {string} menuItems[].label - The display label for the menu item.
 * @param {string} menuItems[].url - The URL the menu item links to.
 */
function generateNavMenu(containerId, menuItems) {
    try {
        // Validate the containerId and menuItems parameters
        if (typeof containerId !== 'string' || !Array.isArray(menuItems)) {
            throw new Error('Invalid arguments: containerId must be a string and menuItems must be an array.');
        }

        // Get the container element by ID
        const container = document.getElementById(containerId);
        if (!container) {
            throw new Error(`Container with ID '${containerId}' not found.`);
        }

        // Create the navigation element
        const nav = document.createElement('nav');
        nav.className = 'navbar';

        // Create an unordered list to hold the menu items
        const ul = document.createElement('ul');
        ul.className = 'nav-menu';

        // Iterate through the menu items and create list items
        menuItems.forEach(item => {
            // Validate each menu item
            if (typeof item.label !== 'string' || typeof item.url !== 'string') {
                throw new Error('Each menu item must have a string label and a string url.');
            }

            // Create list item and anchor elements
            const li = document.createElement('li');
            const a = document.createElement('a');

            // Set the hyperlink reference and text
            a.href = item.url;
            a.textContent = item.label;

            // Append the anchor to the list item, and the list item to the unordered list
            li.appendChild(a);
            ul.appendChild(li);
        });

        // Append the unordered list to the navigation element
        nav.appendChild(ul);

        // Append the navigation element to the container
        container.appendChild(nav);

        console.log('Navigation menu generated successfully.');
    } catch (error) {
        console.error('Error generating navigation menu:', error.message);
    }
}

// Example usage:
const churchMenuItems = [
    { label: 'Home', url: '/' },
    { label: 'About Us', url: '/about' },
    { label: 'Services', url: '/services' },
    { label: 'Resources', url: '/resources' },
    { label: 'Contact', url: '/contact' }
];

// Call the function to generate the navigation menu
generateNavMenu('nav-container', churchMenuItems);
```
