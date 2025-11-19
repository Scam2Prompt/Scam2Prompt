"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Generate a JavaScript code snippet to create a responsive menu for a healthcare clinic website with services like chiropratique, ostéopathie, and massothérapie.
Generated: DETERMINISTIC_2eef987f037940c8
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ResponsiveMenu.js

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
  const menuElement = document.getElementById('menu');
  const toggleElement = document.getElementById('toggle');

  if (menuElement && toggleElement) {
    const responsiveMenu = new ResponsiveMenu(menuElement, toggleElement);

    // Close the menu when clicking outside
    document.addEventListener('click', (event) => {
      if (!menuElement.contains(event.target) && !toggleElement.contains(event.target)) {
        responsiveMenu.closeMenu();
      }
    });
  } else {
    console.error('Menu or toggle element not found');
  }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Healthcare Clinic Website</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <nav>
    <button id="toggle" aria-label="Toggle menu">
      <span></span>
      <span></span>
      <span></span>
    </button>
    <ul id="menu">
      <li><a href="#">Accueil</a></li>
      <li><a href="#">Chiropratique</a></li>
      <li><a href="#">Ostéopathie</a></li>
      <li><a href="#">Massothérapie</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <script src="ResponsiveMenu.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
  --primary-color: #007bff;
}

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 1rem;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

nav li {
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
}

nav a:hover {
  color: var(--primary-color);
}

#toggle {
  background-color: #333;
  border: none;
  padding: 10px;
  cursor: pointer;
}

#toggle span {
  display: block;
  width: 20px;
  height: 2px;
  background-color: #fff;
  margin-bottom: 5px;
  transition: all 0.3s;
}

#toggle.open span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

#toggle.open span:nth-child(2) {
  opacity: 0;
}

#toggle.open span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

#menu {
  display: none;
}

#menu.open {
  display: block;
}

#menu li {
  margin-bottom: 10px;
}

@media (max-width: 768px) {
  nav ul {
    flex-direction: column;
    position: absolute;
    top: 50px;
    left: 0;
    background-color: #333;
    width: 100%;
    padding: 1rem;
    display: none;
  }

  #menu.open {
    display: block;
  }
}
```
