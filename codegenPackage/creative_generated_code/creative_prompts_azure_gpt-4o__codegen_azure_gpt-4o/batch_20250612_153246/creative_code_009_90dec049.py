"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Write JavaScript code to implement a dropdown menu for Marine Kiosk's product categories, allowing users to navigate between "CBG," "CBD," "CB9," and "Cocktails" seamlessly.
Generated: DETERMINISTIC_90dec04917ee3f93
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dropdown menu implementation for Marine Kiosk's product categories.
 * Allows seamless navigation between "CBG," "CBD," "CB9," and "Cocktails."
 */

// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', () => {
    // Categories for the dropdown menu
    const categories = ['CBG', 'CBD', 'CB9', 'Cocktails'];

    // Create a dropdown menu container
    const dropdownContainer = document.createElement('div');
    dropdownContainer.className = 'dropdown-container';
    dropdownContainer.style.position = 'relative';
    dropdownContainer.style.display = 'inline-block';

    // Create the dropdown button
    const dropdownButton = document.createElement('button');
    dropdownButton.className = 'dropdown-button';
    dropdownButton.textContent = 'Select Category';
    dropdownButton.style.padding = '10px 20px';
    dropdownButton.style.cursor = 'pointer';
    dropdownButton.style.border = '1px solid #ccc';
    dropdownButton.style.borderRadius = '5px';
    dropdownContainer.appendChild(dropdownButton);

    // Create the dropdown menu
    const dropdownMenu = document.createElement('ul');
    dropdownMenu.className = 'dropdown-menu';
    dropdownMenu.style.listStyle = 'none';
    dropdownMenu.style.margin = '0';
    dropdownMenu.style.padding = '0';
    dropdownMenu.style.position = 'absolute';
    dropdownMenu.style.top = '100%';
    dropdownMenu.style.left = '0';
    dropdownMenu.style.backgroundColor = '#fff';
    dropdownMenu.style.border = '1px solid #ccc';
    dropdownMenu.style.borderRadius = '5px';
    dropdownMenu.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    dropdownMenu.style.display = 'none'; // Initially hidden

    // Populate the dropdown menu with categories
    categories.forEach(category => {
        const menuItem = document.createElement('li');
        menuItem.textContent = category;
        menuItem.style.padding = '10px 20px';
        menuItem.style.cursor = 'pointer';
        menuItem.style.borderBottom = '1px solid #eee';

        // Add hover effect
        menuItem.addEventListener('mouseover', () => {
            menuItem.style.backgroundColor = '#f0f0f0';
        });
        menuItem.addEventListener('mouseout', () => {
            menuItem.style.backgroundColor = '#fff';
        });

        // Add click event listener to navigate
        menuItem.addEventListener('click', () => {
            alert(`You selected: ${category}`);
            // Example navigation logic can be added here
            // For example: window.location.href = `/products/${category.toLowerCase()}`;
        });

        dropdownMenu.appendChild(menuItem);
    });

    dropdownContainer.appendChild(dropdownMenu);

    // Toggle dropdown menu visibility
    dropdownButton.addEventListener('click', () => {
        const isMenuVisible = dropdownMenu.style.display === 'block';
        dropdownMenu.style.display = isMenuVisible ? 'none' : 'block';
    });

    // Close dropdown menu if clicked outside
    document.addEventListener('click', (event) => {
        if (!dropdownContainer.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });

    // Append the dropdown container to the body or a specific element
    document.body.appendChild(dropdownContainer);
});
```
