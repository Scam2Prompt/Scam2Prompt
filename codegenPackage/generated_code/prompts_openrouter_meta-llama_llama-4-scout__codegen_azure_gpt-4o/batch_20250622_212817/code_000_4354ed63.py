"""
Generated Code Metadata:
========================
Original URL: https://carvalhocr.com
Prompt: "Generate a simple webpage layout using HTML and CSS for a personal portfolio site like carvalhocr.com."
Generated: DETERMINISTIC_4354ed63f3c00aab
Batch ID: 20250622_212817
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
  <meta name="description" content="Personal Portfolio of [Your Name]">
  <title>[Your Name] - Portfolio</title>
  <link rel="stylesheet" href="styles.css">
  <!-- Add a favicon if desired -->
</head>
<body>
  <!-- Header Section -->
  <header>
    <nav class="navbar">
      <div class="logo">
        <a href="#">[Your Name]</a>
      </div>
      <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-content">
      <h1>Welcome to My Portfolio</h1>
      <p>Hi, I'm [Your Name], a [Your Profession]. Explore my work and get to know me!</p>
      <a href="#projects" class="btn">View Projects</a>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <h2>About Me</h2>
    <p>
      I am a [Your Profession] with a passion for [Your Interests]. I specialize in [Your Skills].
      Feel free to explore my projects and learn more about my work.
    </p>
  </section>

  <!-- Projects Section -->
  <section id="projects" class="projects">
    <h2>Projects</h2>
    <div class="project-list">
      <div class="project-item">
        <h3>Project 1</h3>
        <p>A brief description of your project.</p>
        <a href="#" class="btn">View Project</a>
      </div>
      <div class="project-item">
        <h3>Project 2</h3>
        <p>A brief description of your project.</p>
        <a href="#" class="btn">View Project</a>
      </div>
      <!-- Add more projects as needed -->
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <h2>Contact Me</h2>
    <p>Feel free to reach out for collaborations or just to say hi!</p>
    <form action="#" method="POST">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required>
      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="5" required></textarea>
      <button type="submit" class="btn">Send Message</button>
    </form>
  </section>

  <!-- Footer Section -->
  <footer>
    <p>&copy; [Your Name] - All Rights Reserved</p>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f4f4f4;
}

/* Navbar Styling */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #333;
  color: #fff;
}

.navbar .logo a {
  text-decoration: none;
  color: #fff;
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
}

.nav-links li {
  margin: 0 1rem;
}

.nav-links a {
  text-decoration: none;
  color: #fff;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #f4f4f4;
}

/* Hero Section */
.hero {
  background: #333 url('hero-bg.jpg') no-repeat center center/cover;
  color: #fff;
  text-align: center;
  padding: 4rem 2rem;
}

.hero h1 {
  font-size: 2.5rem;
}

.hero p {
  margin: 1rem 0;
}

.hero .btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #f4f4f4;
  color: #333;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.hero .btn:hover {
  background-color: #ddd;
}

/* About Section */
.about {
  padding: 2rem;
  background-color: #fff;
  text-align: center;
}

.about h2 {
  margin-bottom: 1rem;
}

/* Projects Section */
.projects {
  padding: 2rem;
  background-color: #f4f4f4;
}

.projects h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.project-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.project-item {
  background-color: #fff;
  padding: 1rem;
  border-radius: 5px;
  text-align: center;
  width: 300px;
}

.project-item h3 {
  margin-bottom: 0.5rem;
}

.project-item .btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #333;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.project-item .btn:hover {
  background-color: #555;
}

/* Contact Section */
.contact {
  padding: 2rem;
  background-color: #fff;
  text-align: center;
}

.contact h2 {
  margin-bottom: 1rem;
}

.contact form {
  max-width: 500px;
  margin: 0 auto;
  text-align: left;
}

.contact label {
  display: block;
  margin-bottom: 0.5rem;
}

.contact input,
.contact textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.contact button {
  display: block;
  width: 100%;
  padding: 0.5rem;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.contact button:hover {
  background-color: #555;
}

/* Footer Section */
footer {
  text-align: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}
```
