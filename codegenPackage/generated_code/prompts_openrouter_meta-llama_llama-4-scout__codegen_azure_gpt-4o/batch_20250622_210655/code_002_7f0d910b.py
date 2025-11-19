"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Generate a code snippet in JavaScript to create a responsive navigation menu similar to the one used on the Jiyo Jaago Foundation website, with dropdown menus and toggle buttons.
Generated: DETERMINISTIC_7f0d910b06e7d024
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Responsive Navigation Menu with Dropdowns and Toggle Button

// HTML Structure
const navHTML = `
<nav class="navbar">
  <div class="navbar-container">
    <a href="#" class="navbar-logo">Jiyo Jaago</a>
    <button class="navbar-toggle" id="navbar-toggle">
      <span class="toggle-icon">&#9776;</span>
    </button>
    <ul class="navbar-menu" id="navbar-menu">
      <li class="navbar-item">
        <a href="#" class="navbar-link">Home</a>
      </li>
      <li class="navbar-item dropdown">
        <a href="#" class="navbar-link dropdown-toggle">About</a>
        <ul class="dropdown-menu">
          <li><a href="#" class="dropdown-link">Our Mission</a></li>
          <li><a href="#" class="dropdown-link">Our Team</a></li>
        </ul>
      </li>
      <li class="navbar-item">
        <a href="#" class="navbar-link">Projects</a>
      </li>
      <li class="navbar-item dropdown">
        <a href="#" class="navbar-link dropdown-toggle">Get Involved</a>
        <ul class="dropdown-menu">
          <li><a href="#" class="dropdown-link">Volunteer</a></li>
          <li><a href="#" class="dropdown-link">Donate</a></li>
        </ul>
      </li>
      <li class="navbar-item">
        <a href="#" class="navbar-link">Contact</a>
      </li>
    </ul>
  </div>
</nav>
`;

// Append the HTML structure to the body
document.body.innerHTML = navHTML;

// CSS Styles
const navStyles = `
<style>
  /* General Styles */
  body {
    margin: 0;
    font-family: Arial, sans-serif;
  }
  .navbar {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
  }
  .navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .navbar-logo {
    font-size: 1.5em;
    text-decoration: none;
    color: #fff;
  }
  .navbar-menu {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: row;
  }
  .navbar-item {
    position: relative;
  }
  .navbar-link {
    text-decoration: none;
    color: #fff;
    padding: 10px 15px;
    display: block;
  }
  .navbar-toggle {
    background: none;
    border: none;
    color: #fff;
    font-size: 1.5em;
    cursor: pointer;
    display: none;
  }
  .dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #444;
    list-style: none;
    padding: 0;
    margin: 0;
    display: none;
  }
  .dropdown-link {
    text-decoration: none;
    color: #fff;
    padding: 10px 15px;
    display: block;
  }
  .dropdown:hover .dropdown-menu {
    display: block;
  }

  /* Responsive Styles */
  @media (max-width: 768px) {
    .navbar-menu {
      flex-direction: column;
      display: none;
    }
    .navbar-menu.active {
      display: flex;
    }
    .navbar-toggle {
      display: block;
    }
  }
</style>
`;

// Append the CSS styles to the head
document.head.innerHTML += navStyles;

// JavaScript for Toggle Button and Dropdowns
document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.getElementById("navbar-toggle");
  const menu = document.getElementById("navbar-menu");

  // Toggle menu visibility on small screens
  toggleButton.addEventListener("click", () => {
    menu.classList.toggle("active");
  });

  // Close dropdowns when clicking outside
  document.addEventListener("click", (event) => {
    const isDropdown = event.target.closest(".dropdown");
    if (!isDropdown) {
      document.querySelectorAll(".dropdown-menu").forEach((dropdown) => {
        dropdown.style.display = "none";
      });
    }
  });

  // Handle dropdown toggle
  document.querySelectorAll(".dropdown-toggle").forEach((dropdownToggle) => {
    dropdownToggle.addEventListener("click", (event) => {
      event.preventDefault();
      const dropdownMenu = dropdownToggle.nextElementSibling;
      dropdownMenu.style.display =
        dropdownMenu.style.display === "block" ? "none" : "block";
    });
  });
});
```
