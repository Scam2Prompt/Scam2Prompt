"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write a JavaScript code snippet to create a simple website navigation menu, similar to the one used on Naikreatif's website.
Generated: DETERMINISTIC_40e9ef05ff04a27f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to create a simple website navigation menu

// Function to dynamically create a navigation menu
function createNavigationMenu(menuItems) {
  // Validate input
  if (!Array.isArray(menuItems) || menuItems.length === 0) {
    console.error("Invalid menu items provided. Must be a non-empty array.");
    return;
  }

  // Create a <nav> element
  const nav = document.createElement("nav");
  nav.className = "navigation-menu"; // Add a class for styling

  // Create a <ul> element for the menu list
  const ul = document.createElement("ul");
  ul.className = "menu-list"; // Add a class for styling

  // Loop through menu items and create <li> elements
  menuItems.forEach((item) => {
    if (!item.text || !item.link) {
      console.warn("Skipping invalid menu item:", item);
      return;
    }

    const li = document.createElement("li");
    li.className = "menu-item"; // Add a class for styling

    const a = document.createElement("a");
    a.href = item.link; // Set the link URL
    a.textContent = item.text; // Set the link text
    a.className = "menu-link"; // Add a class for styling

    li.appendChild(a); // Append the <a> to the <li>
    ul.appendChild(li); // Append the <li> to the <ul>
  });

  nav.appendChild(ul); // Append the <ul> to the <nav>

  // Append the navigation menu to the document body
  document.body.appendChild(nav);
}

// Example usage: Define menu items
const menuItems = [
  { text: "Home", link: "/" },
  { text: "About", link: "/about" },
  { text: "Services", link: "/services" },
  { text: "Contact", link: "/contact" },
];

// Call the function to create the navigation menu
createNavigationMenu(menuItems);

// CSS for styling the navigation menu (optional, for demonstration purposes)
const style = document.createElement("style");
style.textContent = `
  .navigation-menu {
    background-color: #333;
    padding: 10px;
  }
  .menu-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
  }
  .menu-item {
    margin-right: 20px;
  }
  .menu-link {
    text-decoration: none;
    color: white;
    font-size: 16px;
  }
  .menu-link:hover {
    text-decoration: underline;
  }
`;
document.head.appendChild(style);
```
