"""
Generated Code Metadata:
========================
Original URL: https://tiffany-holz.de
Prompt: "Generate a JavaScript snippet to implement a responsive navigation menu suitable for a small personal website like tiffany-holz.de."
Generated: DETERMINISTIC_4fe18d50bf103f56
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// navigation.js

class NavigationMenu {
  /**
   * Initialize the navigation menu.
   * @param {HTMLElement} navElement - The navigation element.
   * @param {HTMLElement} toggleElement - The toggle button element.
   */
  constructor(navElement, toggleElement) {
    this.navElement = navElement;
    this.toggleElement = toggleElement;
    this.isOpen = false;

    // Add event listener to toggle button
    this.toggleElement.addEventListener('click', this.toggleMenu.bind(this));
  }

  /**
   * Toggle the navigation menu.
   */
  toggleMenu() {
    this.isOpen = !this.isOpen;
    this.navElement.classList.toggle('open', this.isOpen);
    this.toggleElement.classList.toggle('open', this.isOpen);
  }

  /**
   * Close the navigation menu.
   */
  closeMenu() {
    this.isOpen = false;
    this.navElement.classList.remove('open');
    this.toggleElement.classList.remove('open');
  }
}

// Initialize navigation menu
document.addEventListener('DOMContentLoaded', () => {
  const navElement = document.querySelector('#nav');
  const toggleElement = document.querySelector('#nav-toggle');

  if (navElement && toggleElement) {
    const navigationMenu = new NavigationMenu(navElement, toggleElement);

    // Close menu on outside click
    document.addEventListener('click', (event) => {
      if (!navElement.contains(event.target) && !toggleElement.contains(event.target)) {
        navigationMenu.closeMenu();
      }
    });

    // Close menu on resize
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        navigationMenu.closeMenu();
      }
    });
  } else {
    console.error('Navigation elements not found.');
  }
});
```

```css
/* navigation.css */

#nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  padding: 1em;
  transform: translateX(-100%);
  transition: transform 0.3s ease-in-out;
}

#nav.open {
  transform: translateX(0);
}

#nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

#nav li {
  margin-bottom: 1em;
}

#nav a {
  color: #fff;
  text-decoration: none;
}

#nav-toggle {
  position: fixed;
  top: 1em;
  right: 1em;
  background-color: #333;
  color: #fff;
  border: none;
  padding: 1em;
  cursor: pointer;
}

#nav-toggle.open {
  background-color: #555;
}

@media (min-width: 768px) {
  #nav {
    position: static;
    width: auto;
    transform: translateX(0);
    padding: 1em;
    background-color: transparent;
  }

  #nav ul {
    display: flex;
    justify-content: space-between;
  }

  #nav li {
    margin-right: 20px;
  }

  #nav a {
    color: #333;
  }

  #nav-toggle {
    display: none;
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
  <title>Tiffany Holz</title>
  <link rel="stylesheet" href="navigation.css">
</head>
<body>
  <nav id="nav">
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
  <button id="nav-toggle">Toggle Menu</button>
  <script src="navigation.js"></script>
</body>
</html>
```
