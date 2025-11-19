"""
Generated Code Metadata:
========================
Original URL: https://giaodien.4wellmedia.com
Prompt: "Generate code for a responsive website header using HTML, CSS, and JavaScript, inspired by 4 Well Media's designs."
Generated: DETERMINISTIC_9b588929bbe43d62
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Website Header</title>
  <style>
    /* Base styles for the header */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
      background-color: #333;
      color: #fff;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: bold;
    }

    nav {
      display: flex;
      gap: 15px;
    }

    nav a {
      text-decoration: none;
      color: #fff;
      font-size: 1rem;
      transition: color 0.3s ease;
    }

    nav a:hover {
      color: #4caf50;
    }

    .menu-toggle {
      display: none;
      font-size: 1.5rem;
      cursor: pointer;
    }

    /* Responsive styles */
    @media (max-width: 768px) {
      nav {
        display: none;
        flex-direction: column;
        background-color: #333;
        position: absolute;
        top: 60px;
        right: 20px;
        width: 200px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      }

      nav.active {
        display: flex;
      }

      .menu-toggle {
        display: block;
      }
    }
  </style>
</head>
<body>
  <header>
    <!-- Logo Section -->
    <div class="logo">4 Well Media</div>

    <!-- Navigation Menu -->
    <nav id="nav-menu">
      <a href="#home">Home</a>
      <a href="#about">About</a>
      <a href="#services">Services</a>
      <a href="#contact">Contact</a>
    </nav>

    <!-- Menu Toggle Button for Mobile -->
    <div class="menu-toggle" id="menu-toggle">&#9776;</div>
  </header>

  <script>
    // JavaScript for toggling the mobile menu
    document.addEventListener('DOMContentLoaded', () => {
      const menuToggle = document.getElementById('menu-toggle');
      const navMenu = document.getElementById('nav-menu');

      // Toggle the 'active' class on the navigation menu
      menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
      });

      // Close the menu if clicked outside
      document.addEventListener('click', (event) => {
        if (!navMenu.contains(event.target) && !menuToggle.contains(event.target)) {
          navMenu.classList.remove('active');
        }
      });
    });
  </script>
</body>
</html>
```
