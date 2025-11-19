"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Write JavaScript code to display a responsive menu for a website like Perú Makers, including links to "Inicio," "Nosotros," "Proyectos," "Donaciones," and "Blog."
Generated: DETERMINISTIC_a621c13078855c8d
Batch ID: 20250612_153225
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
   * @param {HTMLElement} toggleElement - The toggle button element.
   */
  constructor(menuElement, toggleElement) {
    this.menuElement = menuElement;
    this.toggleElement = toggleElement;
    this.isOpen = false;

    // Add event listener to toggle button
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
}

// Create menu links
const menuLinks = [
  { text: 'Inicio', href: '#' },
  { text: 'Nosotros', href: '#' },
  { text: 'Proyectos', href: '#' },
  { text: 'Donaciones', href: '#' },
  { text: 'Blog', href: '#' },
];

// Create menu HTML
const menuHtml = `
  <nav class="menu">
    <ul>
      ${menuLinks.map(link => `<li><a href="${link.href}">${link.text}</a></li>`).join('')}
    </ul>
  </nav>
  <button class="menu-toggle" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
  </button>
`;

// Append menu HTML to body
document.body.insertAdjacentHTML('beforeend', menuHtml);

// Get menu and toggle elements
const menuElement = document.querySelector('.menu');
const toggleElement = document.querySelector('.menu-toggle');

// Create responsive menu instance
const responsiveMenu = new ResponsiveMenu(menuElement, toggleElement);

// Add CSS for menu and toggle
const style = document.createElement('style');
style.textContent = `
  .menu {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1em;
    background-color: #333;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    transform: translateX(-100%);
    transition: transform 0.3s ease-in-out;
  }

  .menu.open {
    transform: translateX(0);
  }

  .menu ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .menu li {
    margin-bottom: 1em;
  }

  .menu a {
    color: #fff;
    text-decoration: none;
  }

  .menu-toggle {
    position: fixed;
    top: 1em;
    left: 1em;
    background-color: #333;
    border: none;
    padding: 1em;
    cursor: pointer;
  }

  .menu-toggle span {
    display: block;
    width: 2em;
    height: 0.2em;
    background-color: #fff;
    margin-bottom: 0.5em;
    transition: all 0.3s ease-in-out;
  }

  .menu-toggle.open span:nth-child(1) {
    transform: rotate(45deg) translate(0.5em, 0.5em);
  }

  .menu-toggle.open span:nth-child(2) {
    opacity: 0;
  }

  .menu-toggle.open span:nth-child(3) {
    transform: rotate(-45deg) translate(0.5em, -0.5em);
  }

  @media (min-width: 768px) {
    .menu {
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      padding: 1em;
      position: static;
      width: auto;
      transform: translateX(0);
    }

    .menu-toggle {
      display: none;
    }
  }
`;
document.head.appendChild(style);
```
