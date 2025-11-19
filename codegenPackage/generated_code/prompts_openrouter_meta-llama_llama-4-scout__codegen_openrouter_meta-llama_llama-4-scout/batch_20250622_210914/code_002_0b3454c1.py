"""
Generated Code Metadata:
========================
Original URL: https://afebi.org
Prompt: Generate a code snippet in JavaScript to create a responsive navigation menu similar to the one used on the AFEBI website.
Generated: DETERMINISTIC_0b3454c1a388b587
Batch ID: 20250622_210914
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
   * Constructor for the NavigationMenu class
   * @param {HTMLElement} navElement - The navigation element
   * @param {Object} options - Options for the navigation menu
   */
  constructor(navElement, options = {}) {
    this.navElement = navElement;
    this.options = Object.assign({}, {
      breakpoint: 768, // Default breakpoint for responsive design
      animationDuration: 500, // Default animation duration
    }, options);

    // Initialize the navigation menu
    this.init();
  }

  /**
   * Initialize the navigation menu
   */
  init() {
    // Check if the navigation element exists
    if (!this.navElement) {
      throw new Error('Navigation element not found');
    }

    // Add event listener for window resize
    window.addEventListener('resize', this.handleResize.bind(this));

    // Add event listener for toggle button click
    const toggleButton = this.navElement.querySelector('.toggle-button');
    if (toggleButton) {
      toggleButton.addEventListener('click', this.handleToggle.bind(this));
    }

    // Initialize the navigation menu on load
    this.handleResize();
  }

  /**
   * Handle window resize event
   */
  handleResize() {
    // Check if the window width is less than the breakpoint
    const isMobile = window.innerWidth < this.options.breakpoint;

    // Toggle the navigation menu on mobile devices
    if (isMobile) {
      this.navElement.classList.add('mobile');
    } else {
      this.navElement.classList.remove('mobile');
    }
  }

  /**
   * Handle toggle button click event
   */
  handleToggle() {
    // Toggle the navigation menu
    this.navElement.classList.toggle('open');

    // Animate the navigation menu
    const animationDuration = this.options.animationDuration;
    this.navElement.style.transitionDuration = `${animationDuration}ms`;
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const navElement = document.querySelector('#nav');
  if (navElement) {
    new NavigationMenu(navElement);
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
  <title>Responsive Navigation Menu</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <nav id="nav">
    <button class="toggle-button">Toggle Menu</button>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
  <script src="navigation.js"></script>
</body>
</html>
```

```css
/* styles.css */

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

#nav a:hover {
  color: #ccc;
}

.toggle-button {
  position: absolute;
  top: 1em;
  right: 1em;
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.mobile #nav ul {
  display: block;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #333;
  padding: 1em;
  width: 100%;
}

.mobile #nav li {
  margin-right: 0;
}

.mobile #nav a {
  display: block;
  padding: 10px;
}

#nav.open ul {
  display: block;
}

#nav:not(.mobile) .toggle-button {
  display: none;
}
```
