"""
Generated Code Metadata:
========================
Original URL: https://wooof.online
Prompt: Write a code snippet to implement a toggle menu functionality using Minimal Mistakes, a Jekyll theme.
Generated: DETERMINISTIC_896a4ff71326d041
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Toggle menu functionality for Minimal Mistakes Jekyll theme

// Get the toggle button and menu elements
const toggleButton = document.getElementById('toggle-button');
const menu = document.getElementById('menu');

// Check if elements exist
if (toggleButton && menu) {
  // Add event listener to toggle button
  toggleButton.addEventListener('click', () => {
    // Toggle the 'is-active' class on the menu
    menu.classList.toggle('is-active');
    
    // Toggle the 'is-active' class on the toggle button
    toggleButton.classList.toggle('is-active');
  });
}

// Optional: Close menu when clicking outside of it
document.addEventListener('click', (event) => {
  // Check if click was outside of menu and toggle button
  if (!menu.contains(event.target) && !toggleButton.contains(event.target)) {
    // Remove 'is-active' class from menu and toggle button
    menu.classList.remove('is-active');
    toggleButton.classList.remove('is-active');
  }
});
```

```css
/* Style the toggle button and menu */

#toggle-button {
  position: relative;
  display: block;
  width: 40px;
  height: 40px;
  background-color: transparent;
  border: none;
  cursor: pointer;
}

#toggle-button.is-active {
  background-color: #ccc;
}

#menu {
  display: none;
  position: absolute;
  top: 40px;
  left: 0;
  background-color: #f9f9f9;
  padding: 20px;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

#menu.is-active {
  display: block;
}
```

```html
<!-- HTML structure for toggle button and menu -->

<button id="toggle-button" aria-label="Toggle menu">
  <span></span>
  <span></span>
  <span></span>
</button>

<nav id="menu">
  <!-- Menu items here -->
  <ul>
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <li><a href="#">Link 3</a></li>
  </ul>
</nav>
```
