"""
Generated Code Metadata:
========================
Original URL: https://tante4dx41.com
Prompt: Write a JavaScript code snippet to implement a responsive and interactive navigation menu, like the one on TANTE4D, that adapts to different screen sizes and devices.
Generated: DETERMINISTIC_b27bd41f3dbc19fd
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Responsive and Interactive Navigation Menu

// HTML structure for the navigation menu
const navHTML = `
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="#" class="logo">TANTE4D</a>
      <button class="menu-toggle" aria-label="Toggle Menu">
        <span class="menu-icon"></span>
      </button>
    </div>
    <ul class="nav-links">
      <li><a href="#home">Home</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
`;

// Append the navigation menu to the body
document.body.insertAdjacentHTML('afterbegin', navHTML);

// CSS styles for the navigation menu
const style = document.createElement('style');
style.textContent = `
  /* Base styles */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #333;
    color: #fff;
  }

  .navbar-brand {
    display: flex;
    align-items: center;
  }

  .logo {
    font-size: 1.5rem;
    text-decoration: none;
    color: #fff;
  }

  .menu-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
  }

  .menu-icon {
    width: 25px;
    height: 3px;
    background-color: #fff;
    display: block;
    position: relative;
  }

  .menu-icon::before,
  .menu-icon::after {
    content: '';
    width: 25px;
    height: 3px;
    background-color: #fff;
    position: absolute;
    left: 0;
  }

  .menu-icon::before {
    top: -8px;
  }

  .menu-icon::after {
    top: 8px;
  }

  .nav-links {
    list-style: none;
    display: flex;
    gap: 1rem;
  }

  .nav-links a {
    text-decoration: none;
    color: #fff;
    font-size: 1rem;
  }

  /* Responsive styles */
  @media (max-width: 768px) {
    .menu-toggle {
      display: block;
    }

    .nav-links {
      display: none;
      flex-direction: column;
      background-color: #333;
      position: absolute;
      top: 100%;
      left: 0;
      width: 100%;
      padding: 1rem;
    }

    .nav-links.active {
      display: flex;
    }
  }
`;
document.head.appendChild(style);

// JavaScript for interactivity
document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  // Toggle menu visibility on button click
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  // Close menu when a link is clicked (optional for better UX)
  navLinks.addEventListener('click', (event) => {
    if (event.target.tagName === 'A') {
      navLinks.classList.remove('active');
    }
  });

  // Accessibility: Close menu on outside click
  document.addEventListener('click', (event) => {
    if (!navLinks.contains(event.target) && !menuToggle.contains(event.target)) {
      navLinks.classList.remove('active');
    }
  });
});
```
