"""
Generated Code Metadata:
========================
Original URL: https://stardomrecordz.com
Prompt: Write a code snippet in JavaScript to create a responsive menu similar to the one found on Stardom Recordz's website.
Generated: DETERMINISTIC_6be941290aa77f5f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// menu.js

class ResponsiveMenu {
  /**
   * Initialize the responsive menu.
   * @param {HTMLElement} menuElement - The menu element.
   * @param {HTMLElement} toggleElement - The toggle element.
   */
  constructor(menuElement, toggleElement) {
    this.menuElement = menuElement;
    this.toggleElement = toggleElement;
    this.isOpen = false;

    // Add event listener to toggle element
    this.toggleElement.addEventListener('click', this.toggleMenu.bind(this));
  }

  /**
   * Toggle the menu.
   */
  toggleMenu() {
    this.isOpen = !this.isOpen;
    this.menuElement.classList.toggle('open', this.isOpen);
    this.toggleElement.classList.toggle('open', this.isOpen);
  }

  /**
   * Close the menu.
   */
  closeMenu() {
    this.isOpen = false;
    this.menuElement.classList.remove('open');
    this.toggleElement.classList.remove('open');
  }
}

// Initialize the menu
document.addEventListener('DOMContentLoaded', () => {
  const menuElement = document.querySelector('#menu');
  const toggleElement = document.querySelector('#menu-toggle');

  if (menuElement && toggleElement) {
    const menu = new ResponsiveMenu(menuElement, toggleElement);

    // Close the menu when clicking outside
    document.addEventListener('click', (event) => {
      if (!menuElement.contains(event.target) && !toggleElement.contains(event.target)) {
        menu.closeMenu();
      }
    });
  } else {
    console.error('Menu or toggle element not found');
  }
});
```

```css
/* styles.css */

#menu {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  padding: 1em;
  transform: translateX(-100%);
  transition: transform 0.5s ease-in-out;
}

#menu.open {
  transform: translateX(0);
}

#menu ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

#menu li {
  margin-bottom: 1em;
}

#menu a {
  color: #fff;
  text-decoration: none;
}

#menu-toggle {
  position: absolute;
  top: 1em;
  right: 1em;
  background-color: #333;
  color: #fff;
  border: none;
  padding: 1em;
  cursor: pointer;
}

#menu-toggle.open {
  background-color: #555;
}

#menu-toggle::before {
  content: "\2630"; /* hamburger icon */
  font-size: 1.5em;
}

#menu-toggle.open::before {
  content: "\2715"; /* close icon */
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Menu</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <button id="menu-toggle"></button>
  <nav id="menu">
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
  <script src="menu.js"></script>
</body>
</html>
```
