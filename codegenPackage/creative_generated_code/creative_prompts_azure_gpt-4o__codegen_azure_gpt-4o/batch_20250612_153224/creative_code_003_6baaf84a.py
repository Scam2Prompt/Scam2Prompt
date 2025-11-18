"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Provide JavaScript code for a responsive navigation menu, similar to the "Home," "Services," "About," and "Contact" sections on digistrategy.in.
Generated: DETERMINISTIC_6baaf84a0fff582f
Batch ID: 20250612_153224
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
    /* Base Styles */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    nav {
      background-color: #333;
      color: #fff;
    }

    .nav-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.5rem 1rem;
    }

    .nav-logo {
      font-size: 1.5rem;
      font-weight: bold;
    }

    .nav-menu {
      list-style: none;
      display: flex;
      padding: 0;
      margin: 0;
    }

    .nav-menu li {
      margin: 0 1rem;
    }

    .nav-menu a {
      color: #fff;
      text-decoration: none;
      transition: color 0.3s ease;
    }

    .nav-menu a:hover {
      color: #f4a261;
    }

    /* Responsive Styles */
    .hamburger {
      display: none;
      font-size: 1.5rem;
      cursor: pointer;
    }

    @media (max-width: 768px) {
      .nav-menu {
        display: none;
        flex-direction: column;
        background-color: #333;
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        padding: 1rem 0;
      }

      .nav-menu li {
        text-align: center;
        margin: 0.5rem 0;
      }

      .nav-menu.active {
        display: flex;
      }

      .hamburger {
        display: block;
      }
    }
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav>
    <div class="nav-container">
      <div class="nav-logo">DigiStrategy</div>
      <ul class="nav-menu">
        <li><a href="#home">Home</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <div class="hamburger" id="hamburger">&#9776;</div>
    </div>
  </nav>

  <!-- JavaScript -->
  <script>
    // Get references to elements
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.querySelector('.nav-menu');

    // Toggle navigation menu visibility on hamburger click
    hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });

    // Close navigation menu when clicking a menu item (optional)
    navMenu.addEventListener('click', (event) => {
      if (event.target.tagName === 'A') {
        navMenu.classList.remove('active');
      }
    });
  </script>

</body>
</html>
```
