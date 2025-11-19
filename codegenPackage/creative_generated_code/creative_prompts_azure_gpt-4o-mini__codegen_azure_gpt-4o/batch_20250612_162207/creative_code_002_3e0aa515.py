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
 * Function to dynamically generate a navigation menu.
 * The menu items represent different church resources.
 * 
 * @param {Array} menuItems - An array of objects representing menu items. 
 * Each object should have 'label' (string) and 'link' (string) properties.
 * @param {string} containerId - The ID of the container element where the menu will be appended.
 */
function generateNavigationMenu(menuItems, containerId) {
  try {
    // Validate input parameters
    if (!Array.isArray(menuItems)) {
      throw new Error("menuItems must be an array of objects.");
    }
    if (typeof containerId !== 'string' || containerId.trim() === '') {
      throw new Error("containerId must be a non-empty string.");
    }

    // Get the container element
    const container = document.getElementById(containerId);
    if (!container) {
      throw new Error(`No element found with ID '${containerId}'.`);
    }

    // Create the navigation menu
    const nav = document.createElement('nav');
    nav.classList.add('navigation-menu'); // Add a class for styling

    const ul = document.createElement('ul');
    ul.classList.add('menu-list'); // Add a class for styling

    menuItems.forEach((item) => {
      // Validate each menu item object
      if (!item.label || !item.link || typeof item.label !== 'string' || typeof item.link !== 'string') {
        throw new Error("Each menu item must have 'label' and 'link' properties of type string.");
      }

      // Create list item and anchor elements
      const li = document.createElement('li');
      li.classList.add('menu-item'); // Add a class for styling

      const anchor = document.createElement('a');
      anchor.href = item.link;
      anchor.textContent = item.label;
      anchor.classList.add('menu-link'); // Add a class for styling

      // Append anchor to list item, and list item to the menu
      li.appendChild(anchor);
      ul.appendChild(li);
    });

    // Append the menu to the container
    nav.appendChild(ul);
    container.appendChild(nav);
  } catch (error) {
    console.error("Error generating navigation menu:", error.message);
  }
}

// Example usage:
const churchResources = [
  { label: "Home", link: "/" },
  { label: "About Us", link: "/about" },
  { label: "Ministries", link: "/ministries" },
  { label: "Events", link: "/events" },
  { label: "Contact", link: "/contact" }
];

generateNavigationMenu(churchResources, "menu-container"); // Assuming an element with ID 'menu-container' exists in your HTML
```

**Note:** Ensure you have an HTML element with the corresponding `id` (e.g., `menu-container`) in your document for the menu to render.
