"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Create a sample HTML and CSS layout for a graphic design portfolio that reflects the innovative design concepts used by Alpha Digital Solutions.
Generated: DETERMINISTIC_e3af8e1f751941a4
Batch ID: 20250612_162051
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
  <meta name="description" content="Graphic Design Portfolio for Alpha Digital Solutions">
  <title>Alpha Digital Solutions - Portfolio</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Alpha Digital Solutions</h1>
      <nav class="nav">
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#portfolio">Portfolio</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>Alpha Digital Solutions specializes in innovative graphic design concepts that push creative boundaries. Explore our diverse portfolio below.</p>
    </div>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio">
    <div class="container">
      <h2>Portfolio</h2>
      <div class="grid">
        <div class="card">
          <img src="project1.jpg" alt="Project 1">
          <h3>Project Title 1</h3>
          <p>Brief description of the project.</p>
        </div>
        <div class="card">
          <img src="project2.jpg" alt="Project 2">
          <h3>Project Title 2</h3>
          <p>Brief description of the project.</p>
        </div>
        <div class="card">
          <img src="project3.jpg" alt="Project 3">
          <h3>Project Title 3</h3>
          <p>Brief description of the project.</p>
        </div>
        <div class="card">
          <img src="project4.jpg" alt="Project 4">
          <h3>Project Title 4</h3>
          <p>Brief description of the project.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <p>Want to collaborate with us? Get in touch!</p>
      <form class="contact-form">
        <input type="text" placeholder="Your Name" required>
        <input type="email" placeholder="Your Email" required>
        <textarea placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Alpha Digital Solutions. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset basic styling */
body, h1, h2, h3, p, ul, li, img, input, textarea, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* General Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Container for consistent layout */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* Header Styling */
.header {
  background-color: #222;
  color: #fff;
  padding: 20px 0;
}

.header .logo {
  font-size: 1.8rem;
  font-weight: bold;
}

.header .nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
}

.header .nav a {
  color: #fff;
  text-decoration: none;
  transition: color 0.3s ease;
}

.header .nav a:hover {
  color: #00bcd4;
}

/* About Section Styling */
.about {
  padding: 50px 0;
  background-color: #f9f9f9;
}

.about h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

/* Portfolio Section Styling */
.portfolio {
  padding: 50px 0;
}

.portfolio h2 {
  font-size: 2rem;
  margin-bottom: 40px;
  text-align: center;
}

.portfolio .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.portfolio .card {
  border: 1px solid #ddd;
  padding: 20px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.portfolio .card img {
  max-width: 100%;
  height: auto;
  margin-bottom: 15px;
}

.portfolio .card h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.portfolio .card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

/* Contact Section Styling */
.contact {
  padding: 50px 0;
  background-color: #222;
  color: #fff;
  text-align: center;
}

.contact h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.contact-form {
  max-width: 600px;
  margin: 0 auto;
}

.contact-form input, .contact-form textarea, .contact-form button {
  width: 100%;
  margin-bottom: 10px;
  padding: 10px;
  font-size: 1rem;
}

.contact-form input, .contact-form textarea {
  border: 1px solid #ccc;
}

.contact-form button {
  background-color: #00bcd4;
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.contact-form button:hover {
  background-color: #008c9e;
}

/* Footer Section Styling */
.footer {
  background-color: #333;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}

.footer p {
  font-size: 0.9rem;
}
```
