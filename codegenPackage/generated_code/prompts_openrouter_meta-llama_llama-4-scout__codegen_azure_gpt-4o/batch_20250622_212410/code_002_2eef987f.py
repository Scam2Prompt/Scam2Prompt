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
// Responsive Menu for Healthcare Clinic Website

// HTML structure for the menu
const menuHTML = `
  <nav id="responsive-menu" class="menu">
    <button id="menu-toggle" class="menu-toggle">☰</button>
    <ul class="menu-items">
      <li><a href="#chiropratique">Chiropratique</a></li>
      <li><a href="#osteopathie">Ostéopathie</a></li>
      <li><a href="#massotherapie">Massothérapie</a></li>
    </ul>
  </nav>
`;

// Append the menu to the body
document.body.insertAdjacentHTML('afterbegin', menuHTML);

// CSS styles for the menu
const menuStyles = `
  <style>
    .menu {
      background-color: #007BFF; /* Clinic-themed color */
      color: white;
      font-family: Arial, sans-serif;
      padding: 10px;
    }
    .menu-toggle {
      background: none;
      border: none;
      color: white;
      font-size: 24px;
      cursor: pointer;
    }
    .menu-items {
      list-style: none;
      padding: 0;
      margin: 0;
      display: none; /* Hidden by default for responsiveness */
    }
    .menu-items li {
      margin: 10px 0;
    }
    .menu-items a {
      color: white;
      text-decoration: none;
    }
    .menu-items a:hover {
      text-decoration: underline;
    }
    @media (min-width: 768px) {
      .menu-items {
        display: flex; /* Show menu items horizontally on larger screens */
        flex-direction: row;
      }
      .menu-items li {
        margin: 0 15px;
      }
      .menu-toggle {
        display: none; /* Hide toggle button on larger screens */
      }
    }
  </style>
`;

// Append the styles to the head
document.head.insertAdjacentHTML('beforeend', menuStyles);

// JavaScript for menu toggle functionality
document.getElementById('menu-toggle').addEventListener('click', () => {
  const menuItems = document.querySelector('.menu-items');
  // Toggle the visibility of the menu items
  menuItems.style.display = menuItems.style.display === 'block' ? 'none' : 'block';
});

// Error handling: Ensure menu exists before adding event listener
if (!document.getElementById('menu-toggle')) {
  console.error('Menu toggle button not found. Ensure the menu HTML is correctly loaded.');
}
```
