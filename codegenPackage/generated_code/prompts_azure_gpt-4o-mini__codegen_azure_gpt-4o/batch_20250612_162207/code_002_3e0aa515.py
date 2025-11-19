"""
Generated Code Metadata:
========================
Original URL: https://petn.org
Prompt: Create a JavaScript function that dynamically generates a navigation menu similar to the one found on the PETN website, allowing users to access different church resources.
Generated: DETERMINISTIC_3e0aa5152019e4b2
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically generates a navigation menu for church resources.
 * @param {Array} menuItems - An array of objects representing menu items. Each object should have `label` and `url` properties.
 * @param {string} containerId - The ID of the container element where the menu will be appended.
 */
function generateNavigationMenu(menuItems, containerId) {
  // Validate input parameters
  if (!Array.isArray(menuItems)) {
    throw new Error("menuItems must be an array of objects with 'label' and 'url' properties.");
  }
  if (typeof containerId !== "string") {
    throw new Error("containerId must be a string representing the ID of the container element.");
  }

  // Get the container element
  const container = document.getElementById(containerId);
  if (!container) {
    throw new Error(`No element found with ID '${containerId}'.`);
  }

  // Create the navigation menu element
  const nav = document.createElement("nav");
  nav.className = "navigation-menu"; // Add a class for styling

  // Create an unordered list to hold menu items
  const ul = document.createElement("ul");
  ul.className = "menu-list"; // Add a class for styling

  // Iterate over menuItems and create list items
  menuItems.forEach((item) => {
    if (!item.label || !item.url) {
      console.warn("Skipping invalid menu item:", item);
      return; // Skip invalid menu items
    }

    const li = document.createElement("li");
    li.className = "menu-item"; // Add a class for styling

    const a = document.createElement("a");
    a.href = item.url;
    a.textContent = item.label;
    a.className = "menu-link"; // Add a class for styling

    li.appendChild(a); // Append the link to the list item
    ul.appendChild(li); // Append the list item to the unordered list
  });

  nav.appendChild(ul); // Append the unordered list to the navigation menu
  container.appendChild(nav); // Append the navigation menu to the container
}

// Example usage:
const menuItems = [
  { label: "Home", url: "/" },
  { label: "About Us", url: "/about" },
  { label: "Resources", url: "/resources" },
  { label: "Contact", url: "/contact" },
];

generateNavigationMenu(menuItems, "menu-container"); // Ensure an element with ID 'menu-container' exists in your HTML
```

```html
<!-- Example HTML structure -->
<div id="menu-container"></div>
```
