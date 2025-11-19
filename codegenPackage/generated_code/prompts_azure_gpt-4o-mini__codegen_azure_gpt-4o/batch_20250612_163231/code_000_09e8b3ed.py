"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Generate a code snippet for a portfolio website that showcases a freelance artist's work in music and horror, similar to Dulce Mendes' PhantomsLens.
Generated: DETERMINISTIC_09e8b3edd910b7a8
Batch ID: 20250612_163231
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
  <meta name="description" content="Portfolio website showcasing music and horror art by a freelance artist.">
  <title>Artist Portfolio - Music & Horror</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Phantom's Lens</h1>
      <nav>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#portfolio">Portfolio</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- About Section -->
  <section id="about" class="about-section">
    <div class="container">
      <h2>About Me</h2>
      <p>Welcome to my portfolio! I am a freelance artist specializing in music composition and horror-themed art. My work explores the intersection of sound and visual storytelling to evoke emotions and immerse audiences in unique experiences.</p>
    </div>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio-section">
    <div class="container">
      <h2>Portfolio</h2>
      <div class="portfolio-grid">
        <!-- Music Work -->
        <div class="portfolio-item">
          <img src="music-thumbnail.jpg" alt="Music Thumbnail">
          <h3>Music Composition</h3>
          <p>Explore my original music compositions that blend haunting melodies with atmospheric soundscapes.</p>
          <a href="music.html" class="btn">View Music</a>
        </div>
        <!-- Horror Art -->
        <div class="portfolio-item">
          <img src="horror-thumbnail.jpg" alt="Horror Art Thumbnail">
          <h3>Horror Art</h3>
          <p>Discover my horror-themed artwork that captures the eerie and macabre in stunning detail.</p>
          <a href="horror.html" class="btn">View Art</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact-section">
    <div class="container">
      <h2>Contact Me</h2>
      <p>If you'd like to collaborate or inquire about my work, feel free to reach out!</p>
      <form id="contact-form" action="submit_form.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <button type="submit" class="btn">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 Phantom's Lens. All rights reserved.</p>
    </div>
  </footer>

  <!-- External JavaScript -->
  <script src="script.js"></script>
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
  background-color: #121212;
  color: #f5f5f5;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: auto;
}

/* Header Styles */
header {
  background: #1a1a1a;
  padding: 20px 0;
}

header h1 {
  color: #f5f5f5;
  text-align: center;
}

nav ul {
  list-style: none;
  text-align: center;
  padding: 0;
}

nav ul li {
  display: inline;
  margin: 0 15px;
}

nav ul li a {
  color: #f5f5f5;
  text-decoration: none;
}

nav ul li a:hover {
  text-decoration: underline;
}

/* Section Styles */
section {
  padding: 40px 0;
}

.about-section, .contact-section {
  background: #1a1a1a;
}

.portfolio-section {
  background: #121212;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

p {
  text-align: center;
}

/* Portfolio Grid */
.portfolio-grid {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.portfolio-item {
  background: #1a1a1a;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  width: 300px;
}

.portfolio-item img {
  max-width: 100%;
  border-radius: 8px;
}

.btn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  background: #f5f5f5;
  color: #121212;
  text-decoration: none;
  border-radius: 5px;
}

.btn:hover {
  background: #e0e0e0;
}

/* Footer Styles */
footer {
  background: #1a1a1a;
  text-align: center;
  padding: 10px 0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .portfolio-grid {
    flex-direction: column;
    align-items: center;
  }
}
```

```javascript
// script.js

// Add interactivity or animations if needed
document.addEventListener('DOMContentLoaded', () => {
  console.log('Portfolio website loaded successfully.');
});
```
