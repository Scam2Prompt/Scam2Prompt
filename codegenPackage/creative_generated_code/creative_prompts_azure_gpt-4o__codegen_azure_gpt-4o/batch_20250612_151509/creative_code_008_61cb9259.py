"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenpocketn.shop
Prompt: Generate code to create a responsive webpage layout using HTML and CSS, ensuring it adheres to SEO mobile-friendliness standards.
Generated: DETERMINISTIC_61cb9259f0682f7c
Batch ID: 20250612_151509
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
  <meta name="description" content="A responsive webpage layout adhering to SEO and mobile-friendliness standards.">
  <meta name="keywords" content="responsive design, SEO, mobile-friendly layout, webpage">
  <meta name="author" content="Your Name">
  <title>Responsive Webpage Layout</title>
  <link rel="stylesheet" href="styles.css">
  <!-- Ensure the page loads with a mobile-friendly viewport -->
</head>

<body>
  <header class="header">
    <nav class="navbar">
      <div class="logo">LOGO</div>
      <ul class="nav-menu">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <!-- Mobile hamburger menu -->
      <button class="hamburger" aria-label="Open navigation menu">
        ☰
      </button>
    </nav>
  </header>

  <main>
    <section id="home" class="hero">
      <h1>Welcome to Our Website</h1>
      <p>Your one-stop solution for responsive web designs.</p>
      <a href="#about" class="cta">Learn More</a>
    </section>

    <section id="about" class="about">
      <h2>About Us</h2>
      <p>We specialize in creating SEO-friendly and mobile-optimized webpages.</p>
    </section>

    <section id="services" class="services">
      <h2>Our Services</h2>
      <div class="service-item">Web Development</div>
      <div class="service-item">SEO Optimization</div>
      <div class="service-item">Responsive Design</div>
    </section>

    <section id="contact" class="contact">
      <h2>Contact Us</h2>
      <form action="#" method="post" class="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <button type="submit">Submit</button>
      </form>
    </section>
  </main>

  <footer class="footer">
    <p>&copy; 2023 Your Name. All rights reserved.</p>
  </footer>

  <script>
    // JavaScript to toggle the navigation menu (for mobile responsiveness)
    document.querySelector('.hamburger').addEventListener('click', () => {
      const navMenu = document.querySelector('.nav-menu');
      navMenu.classList.toggle('active');
    });
  </script>
</body>

</html>
```

```css
/* styles.css */

/* Base styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem 0;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1rem;
}

.nav-menu {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-menu a {
  color: #fff;
  text-decoration: none;
}

.hamburger {
  display: none;
  font-size: 2rem;
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
}

/* Hero section */
.hero {
  background-color: #f4f4f4;
  padding: 2rem;
  text-align: center;
}

.cta {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #333;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
}

/* About section */
.about {
  padding: 2rem;
  background-color: #fff;
}

/* Services section */
.services {
  padding: 2rem;
  background-color: #f4f4f4;
  display: flex;
  gap: 1rem;
}

.service-item {
  flex: 1;
  background-color: #fff;
  padding: 1rem;
  border: 1px solid #ddd;
}

/* Contact section */
.contact {
  padding: 2rem;
  background-color: #fff;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.contact-form input,
.contact-form textarea,
.contact-form button {
  width: 100%;
  padding: 0.5rem;
}

/* Footer */
.footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem;
}

/* Responsive styles */
@media (max-width: 768px) {
  .nav-menu {
    display: none;
    flex-direction: column;
    gap: 0.5rem;
    background-color: #333;
    padding: 1rem;
  }

  .nav-menu.active {
    display: flex;
  }

  .hamburger {
    display: block;
  }

  .services {
    flex-direction: column;
  }
}
```
