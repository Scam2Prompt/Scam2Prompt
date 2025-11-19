"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: "Create a template for a company's about page that highlights their mission, vision, and team expertise in web design, development, and marketing."
Generated: DETERMINISTIC_1cc95f19a3b12c49
Batch ID: 20250622_210655
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
  <meta name="description" content="Learn more about our company's mission, vision, and team expertise in web design, development, and marketing.">
  <title>About Us - Company Name</title>
  <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
  <!-- Header Section -->
  <header>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html" class="active">About</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main Content Section -->
  <main>
    <!-- Mission Section -->
    <section id="mission">
      <h1>Our Mission</h1>
      <p>Our mission is to empower businesses by delivering innovative web solutions that drive growth, enhance user experiences, and create lasting value.</p>
    </section>

    <!-- Vision Section -->
    <section id="vision">
      <h1>Our Vision</h1>
      <p>We envision a world where businesses of all sizes can leverage cutting-edge technology to achieve their goals and connect with their audiences effectively.</p>
    </section>

    <!-- Team Expertise Section -->
    <section id="team-expertise">
      <h1>Our Team Expertise</h1>
      <div class="expertise">
        <article>
          <h2>Web Design</h2>
          <p>Our designers craft visually stunning and user-friendly interfaces that captivate audiences and enhance brand identity.</p>
        </article>
        <article>
          <h2>Web Development</h2>
          <p>Our developers build robust, scalable, and secure web applications tailored to meet your business needs.</p>
        </article>
        <article>
          <h2>Marketing</h2>
          <p>Our marketing experts create data-driven strategies to help you reach your target audience and achieve measurable results.</p>
        </article>
      </div>
    </section>
  </main>

  <!-- Footer Section -->
  <footer>
    <p>&copy; <span id="year"></span> Company Name. All rights reserved.</p>
  </footer>

  <!-- JavaScript -->
  <script>
    // Dynamically set the current year in the footer
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem 0;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
  margin: 0;
  padding: 0;
}

nav ul li {
  margin: 0 1rem;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}

nav ul li a.active {
  text-decoration: underline;
}

main {
  padding: 2rem;
}

section {
  margin-bottom: 2rem;
}

h1 {
  color: #444;
}

h2 {
  color: #555;
}

.expertise {
  display: flex;
  gap: 2rem;
}

.expertise article {
  flex: 1;
  background-color: #fff;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

footer {
  text-align: center;
  padding: 1rem 0;
  background-color: #333;
  color: #fff;
}
```
