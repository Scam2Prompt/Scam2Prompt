"""
Generated Code Metadata:
========================
Original URL: https://carvalhocr.com
Prompt: "Write a JavaScript function to create a responsive navigation menu for a portfolio site like carvalhocr."
Generated: DETERMINISTIC_77198793f67b4234
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// navigation.js

/**
 * Creates a responsive navigation menu for a portfolio site.
 * 
 * @param {Object} options - Configuration options for the navigation menu.
 * @param {String} options.menuId - The ID of the HTML element containing the menu items.
 * @param {String} options.toggleId - The ID of the HTML element to toggle the menu on smaller screens.
 * @param {String} options.activeClass - The class to add to the active menu item.
 */
function createResponsiveNav(options) {
  // Check if options are provided
  if (!options) {
    throw new Error('Options must be provided');
  }

  // Destructure options
  const { menuId, toggleId, activeClass = 'active' } = options;

  // Get menu and toggle elements
  const menu = document.getElementById(menuId);
  const toggle = document.getElementById(toggleId);

  // Check if menu and toggle elements exist
  if (!menu || !toggle) {
    throw new Error('Menu or toggle element not found');
  }

  // Add event listener to toggle button
  toggle.addEventListener('click', () => {
    // Toggle menu on smaller screens
    menu.classList.toggle('open');
  });

  // Add event listeners to menu items
  menu.addEventListener('click', (e) => {
    // Check if clicked element is a menu item
    if (e.target.tagName === 'LI' || e.target.closest('li')) {
      // Remove active class from all menu items
      menu.querySelectorAll('li').forEach((item) => item.classList.remove(activeClass));

      // Add active class to clicked menu item
      e.target.closest('li').classList.add(activeClass);
    }
  });

  // Add event listener for window resize
  window.addEventListener('resize', () => {
    // Close menu on larger screens
    if (window.innerWidth > 768) {
      menu.classList.remove('open');
    }
  });
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  createResponsiveNav({
    menuId: 'nav-menu',
    toggleId: 'nav-toggle',
  });
});
```

```css
/* styles.css */

#nav-menu {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

#nav-menu li {
  margin-right: 20px;
}

#nav-menu li a {
  text-decoration: none;
  color: #333;
}

#nav-menu li.active a {
  color: #007bff;
}

#nav-menu.open {
  display: block;
}

#nav-toggle {
  display: none;
  cursor: pointer;
}

@media (max-width: 768px) {
  #nav-menu {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #f9f9f9;
    padding: 20px;
    border: 1px solid #ddd;
  }

  #nav-menu.open {
    display: flex;
  }

  #nav-toggle {
    display: block;
  }
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Navigation Menu</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <nav>
    <button id="nav-toggle">Toggle Menu</button>
    <ul id="nav-menu">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Projects</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
  <script src="navigation.js"></script>
</body>
</html>
```
