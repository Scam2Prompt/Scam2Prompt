"""
Generated Code Metadata:
========================
Original URL: https://predragvukasinovic.com
Prompt: Generate HTML and CSS code for a basic navigation menu with sections like About, Projects, Contact, and Shop, inspired by the design elements on Predrag Vukasinovic's website.
Generated: DETERMINISTIC_3f58dea618f279f5
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
  <title>Navigation Menu</title>
  <style>
    /* Reset some default browser styles */
    body, ul {
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
    }

    /* Navigation bar container */
    .navbar {
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #333;
      padding: 10px 20px;
    }

    /* Navigation menu list */
    .navbar ul {
      list-style: none;
      display: flex;
    }

    /* Navigation menu items */
    .navbar li {
      margin: 0 15px;
    }

    /* Navigation links */
    .navbar a {
      text-decoration: none;
      color: #fff;
      font-size: 16px;
      transition: color 0.3s ease;
    }

    /* Hover effect for links */
    .navbar a:hover {
      color: #00bcd4;
    }

    /* Active link styling */
    .navbar a.active {
      color: #00bcd4;
      font-weight: bold;
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
      .navbar ul {
        flex-direction: column;
        align-items: center;
      }

      .navbar li {
        margin: 10px 0;
      }
    }
  </style>
</head>
<body>
  <!-- Navigation bar -->
  <nav class="navbar">
    <ul>
      <li><a href="#about" class="active">About</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#shop">Shop</a></li>
    </ul>
  </nav>

  <!-- Placeholder sections for demonstration -->
  <section id="about" style="padding: 50px; text-align: center;">
    <h1>About</h1>
    <p>Welcome to the About section.</p>
  </section>
  <section id="projects" style="padding: 50px; text-align: center;">
    <h1>Projects</h1>
    <p>Explore our projects here.</p>
  </section>
  <section id="contact" style="padding: 50px; text-align: center;">
    <h1>Contact</h1>
    <p>Get in touch with us.</p>
  </section>
  <section id="shop" style="padding: 50px; text-align: center;">
    <h1>Shop</h1>
    <p>Browse our shop.</p>
  </section>
</body>
</html>
```
