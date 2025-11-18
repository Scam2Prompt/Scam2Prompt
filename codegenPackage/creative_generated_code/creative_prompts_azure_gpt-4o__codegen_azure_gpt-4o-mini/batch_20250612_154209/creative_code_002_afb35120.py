"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Generate code in JavaScript to display a dynamic menu for navigating ISIV's academic offerings, including "Recursos Humanos," "Turismo," and "Seguridad e Higiene Laboral."
Generated: DETERMINISTIC_afb35120d82d4ef6
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// DynamicMenu.js

/**
 * Class representing a dynamic menu for navigating academic offerings.
 */
class DynamicMenu {
    constructor(menuId) {
        // The ID of the menu element in the DOM
        this.menuId = menuId;
        this.menuItems = [
            { name: "Recursos Humanos", link: "#recursos-humanos" },
            { name: "Turismo", link: "#turismo" },
            { name: "Seguridad e Higiene Laboral", link: "#seguridad-higiene" }
        ];
    }

    /**
     * Initializes the menu by rendering it in the DOM.
     */
    init() {
        try {
            const menuElement = document.getElementById(this.menuId);
            if (!menuElement) {
                throw new Error(`Menu element with ID "${this.menuId}" not found.`);
            }
            this.renderMenu(menuElement);
        } catch (error) {
            console.error("Error initializing menu:", error.message);
        }
    }

    /**
     * Renders the menu items in the specified DOM element.
     * @param {HTMLElement} menuElement - The DOM element where the menu will be rendered.
     */
    renderMenu(menuElement) {
        // Clear previous menu items
        menuElement.innerHTML = '';

        // Create a list to hold the menu items
        const ul = document.createElement('ul');

        // Create and append each menu item
        this.menuItems.forEach(item => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = item.link;
            a.textContent = item.name;
            a.addEventListener('click', this.handleMenuClick.bind(this, item.name));
            li.appendChild(a);
            ul.appendChild(li);
        });

        // Append the list to the menu element
        menuElement.appendChild(ul);
    }

    /**
     * Handles the click event on a menu item.
     * @param {string} itemName - The name of the clicked menu item.
     */
    handleMenuClick(itemName) {
        // Implement any specific logic for when a menu item is clicked
        console.log(`Navigating to: ${itemName}`);
    }
}

// Usage example on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    const menu = new DynamicMenu('academic-menu');
    menu.init();
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Academic Menu</title>
    <script src="DynamicMenu.js" defer></script>
</head>
<body>
    <header>
        <h1>ISIV Academic Offerings</h1>
        <nav id="academic-menu"></nav>
    </header>
    <!-- Main content goes here -->
</body>
</html>
```
