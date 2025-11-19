"""
Generated Code Metadata:
========================
Original URL: https://iteamworldwide.com
Prompt: Generate JavaScript code to implement a responsive navigation menu similar to the one on the iTeam Worldwide homepage.
Generated: DETERMINISTIC_acf56d94af2097c8
Batch ID: 20250612_151024
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

    // Add event listener to window resize
    window.addEventListener('resize', this.handleResize.bind(this));

    // Initialize menu state on page load
    this.handleResize();
  }

  /**
   * Toggle the navigation menu.
   */
  toggleMenu() {
    this.isOpen = !this.isOpen;
    this.navElement.classList.toggle('open', this.isOpen);
  }

  /**
   * Handle window resize event.
   */
  handleResize() {
    const screenWidth = window.innerWidth;
    if (screenWidth > 768) {
      // Desktop screen size, reset menu state
      this.isOpen = true;
      this.navElement.classList.add('open');
    } else {
      // Mobile screen size, reset menu state
      this.isOpen = false;
      this.navElement.classList.remove('open');
    }
  }
}

// Initialize navigation menu
document.addEventListener('DOMContentLoaded', () => {
  const navElement = document.getElementById('nav');
  const toggleElement = document.getElementById('nav-toggle');

  if (navElement && toggleElement) {
    new NavigationMenu(navElement, toggleElement);
  } else {
    console.error('Navigation menu elements not found.');
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
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.3s ease-in-out;
}

#nav.open {
  transform: translateX(0);
}

#nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

#nav li {
  margin-bottom: 1em;
}

#nav a {
  color: #fff;
  text-decoration: none;
}

#nav a:hover {
  color: #ccc;
}

#nav-toggle {
  position: absolute;
  top: 1em;
  right: 1em;
  background-color: #333;
  color: #fff;
  border: none;
  padding: 1em;
  cursor: pointer;
}

#nav-toggle::before {
  content: "\2630"; /* hamburger icon */
  font-size: 1.5em;
}

@media (min-width: 768px) {
  #nav {
    position: static;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 1em 2em;
  }

  #nav ul {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 2em;
  }

  #nav li {
    margin-right: 2em;
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
  <title>iTeam Worldwide</title>
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
  <button id="nav-toggle"></button>

  <script src="navigation.js"></script>
</body>
</html>
```
