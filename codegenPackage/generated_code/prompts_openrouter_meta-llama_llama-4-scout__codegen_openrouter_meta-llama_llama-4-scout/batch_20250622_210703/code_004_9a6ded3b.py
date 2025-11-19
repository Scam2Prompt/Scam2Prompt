"""
Generated Code Metadata:
========================
Original URL: https://baliauthenticcoffeeandgallery.com
Prompt: "Create a JavaScript code snippet to implement a responsive navigation menu similar to the one on baliauthenticcoffeeandgallery.com, ensuring compatibility with various screen sizes."
Generated: DETERMINISTIC_9a6ded3b084034da
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// navigation.js

// Define the NavigationMenu class
class NavigationMenu {
  /**
   * Initialize the navigation menu
   * @param {HTMLElement} navElement - The navigation element
   * @param {Object} options - Options for the navigation menu
   */
  constructor(navElement, options = {}) {
    this.navElement = navElement;
    this.options = Object.assign({}, {
      breakpoint: 768, // Default breakpoint for responsive design
      toggleClass: 'nav-toggle',
      menuClass: 'nav-menu',
    }, options);

    // Initialize event listeners
    this.initEventListeners();
  }

  /**
   * Initialize event listeners for the navigation menu
   */
  initEventListeners() {
    // Add event listener for window resize
    window.addEventListener('resize', this.handleResize.bind(this));

    // Add event listener for navigation toggle
    const toggleElement = this.navElement.querySelector(`.${this.options.toggleClass}`);
    if (toggleElement) {
      toggleElement.addEventListener('click', this.handleToggle.bind(this));
    }
  }

  /**
   * Handle window resize event
   */
  handleResize() {
    // Check if the screen width is less than the breakpoint
    if (window.innerWidth < this.options.breakpoint) {
      this.convertToMobileMenu();
    } else {
      this.convertToDesktopMenu();
    }
  }

  /**
   * Handle navigation toggle event
   */
  handleToggle() {
    // Toggle the navigation menu
    this.navElement.querySelector(`.${this.options.menuClass}`).classList.toggle('active');
  }

  /**
   * Convert the navigation menu to a mobile menu
   */
  convertToMobileMenu() {
    // Get the navigation menu and toggle elements
    const menuElement = this.navElement.querySelector(`.${this.options.menuClass}`);
    const toggleElement = this.navElement.querySelector(`.${this.options.toggleClass}`);

    // Hide the menu by default
    menuElement.style.display = 'none';

    // Add a class to the nav element to style it for mobile
    this.navElement.classList.add('mobile-nav');
  }

  /**
   * Convert the navigation menu to a desktop menu
   */
  convertToDesktopMenu() {
    // Get the navigation menu and toggle elements
    const menuElement = this.navElement.querySelector(`.${this.options.menuClass}`);
    const toggleElement = this.navElement.querySelector(`.${this.options.toggleClass}`);

    // Show the menu by default
    menuElement.style.display = 'block';

    // Remove a class to the nav element to style it for desktop
    this.navElement.classList.remove('mobile-nav');
  }
}

// Initialize the navigation menu
document.addEventListener('DOMContentLoaded', () => {
  const navElement = document.querySelector('#nav');
  if (navElement) {
    new NavigationMenu(navElement);
  }
});
```

```css
/* navigation.css */

#nav {
  position: relative;
  background-color: #333;
  padding: 1em;
  text-align: center;
}

#nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

#nav li {
  margin-right: 20px;
}

#nav a {
  color: #fff;
  text-decoration: none;
}

#nav .nav-toggle {
  position: absolute;
  top: 1em;
  right: 1em;
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px;
  cursor: pointer;
}

#nav .nav-menu {
  display: block;
}

#nav.mobile-nav .nav-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #333;
  padding: 1em;
  width: 100%;
}

#nav.mobile-nav .nav-menu.active {
  display: block;
}

@media (max-width: 768px) {
  #nav ul {
    flex-direction: column;
    align-items: center;
  }

  #nav li {
    margin-right: 0;
    margin-bottom: 10px;
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
  <link rel="stylesheet" href="navigation.css">
</head>
<body>
  <nav id="nav">
    <button class="nav-toggle">Toggle Menu</button>
    <ul class="nav-menu">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <script src="navigation.js"></script>
</body>
</html>
```
