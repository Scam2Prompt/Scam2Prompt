"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write code to create a responsive navigation menu for an online store with categories like "Productos" and "Servicios," similar to the menu on "Mass Compras."
Generated: DETERMINISTIC_58687211fc1836e3
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Navigation Menu</title>
  <style>
    /* Base styles for the navigation bar */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #333;
      padding: 10px 20px;
      color: #fff;
    }

    .navbar .logo {
      font-size: 1.5em;
      font-weight: bold;
    }

    .menu {
      display: flex;
      list-style-type: none;
      margin: 0;
      padding: 0;
    }

    .menu li {
      margin: 0 10px;
    }

    .menu a {
      text-decoration: none;
      color: #fff;
      padding: 5px 10px;
      transition: background-color 0.3s ease;
    }

    .menu a:hover {
      background-color: #575757;
      border-radius: 5px;
    }

    /* Responsive styles */
    .menu-toggle {
      display: none;
      background-color: #333;
      color: #fff;
      border: none;
      font-size: 18px;
      padding: 10px;
      cursor: pointer;
    }

    .menu-container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .menu-container.collapsed .menu {
      display: none;
    }

    /* Media query for small screens */
    @media (max-width: 768px) {
      .menu {
        flex-direction: column;
        width: 100%;
        text-align: center;
      }

      .menu li {
        margin: 5px 0;
      }

      .menu-toggle {
        display: block;
      }
    }
  </style>
</head>
<body>
  <!-- Navigation bar -->
  <nav class="navbar">
    <div class="logo">Mass Compras</div>
    <div class="menu-container collapsed">
      <button class="menu-toggle" aria-label="Toggle Menu">☰</button>
      <ul class="menu">
        <li><a href="#productos">Productos</a></li>
        <li><a href="#servicios">Servicios</a></li>
        <li><a href="#contacto">Contacto</a></li>
        <li><a href="#acerca-de">Acerca de</a></li>
      </ul>
    </div>
  </nav>

  <script>
    // JavaScript to handle menu toggle functionality
    document.addEventListener("DOMContentLoaded", () => {
      const menuContainer = document.querySelector(".menu-container");
      const menuToggle = document.querySelector(".menu-toggle");

      // Toggle menu visibility on button click
      menuToggle.addEventListener("click", () => {
        menuContainer.classList.toggle("collapsed");
      });
    });
  </script>
</body>
</html>
```
