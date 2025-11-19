"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenciainside.com
Prompt: Provide a code example for a responsive web design that reflects the modern and flexible characteristics emphasized by Agência inSIDE.
Generated: DETERMINISTIC_575dcb60495fd006
Batch ID: 20250612_161617
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.gstatic.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="A responsive web design example reflecting modern and flexible characteristics.">
  <title>Responsive Web Design - Agência inSIDE</title>
  <link rel="stylesheet" href="styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
</head>

<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Agência inSIDE</h1>
      <nav class="nav">
        <ul class="nav-list">
          <li><a href="#features" class="nav-link">Features</a></li>
          <li><a href="#about" class="nav-link">About</a></li>
          <li><a href="#contact" class="nav-link">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h2 class="hero-title">Innovative & Flexible Designs</h2>
      <p class="hero-subtext">Empowering your digital presence with modern solutions.</p>
      <a href="#about" class="cta-button">Learn More</a>
    </div>
  </section>

  <!-- Features Section -->
  <section id="features" class="features">
    <div class="container">
      <h2 class="section-title">Our Features</h2>
      <div class="features-grid">
        <div class="feature-item">
          <h3>Responsive Design</h3>
          <p>Optimized for all devices, ensuring seamless user experiences.</p>
        </div>
        <div class="feature-item">
          <h3>Modern Aesthetics</h3>
          <p>Stylish and clean designs that reflect your brand's personality.</p>
        </div>
        <div class="feature-item">
          <h3>Flexibility</h3>
          <p>Tailored solutions to meet your unique business needs.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2 class="section-title">About Us</h2>
      <p>
        At Agência inSIDE, we specialize in creating responsive and modern web designs that embody flexibility and innovation.
        Our team is passionate about delivering exceptional user experiences for businesses worldwide.
      </p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2 class="section-title">Contact Us</h2>
      <form class="contact-form">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your Name" required>

        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Your Email" required>

        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Your Message" rows="4" required></textarea>

        <button type="submit" class="submit-button">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Agência inSIDE. All Rights Reserved.</p>
    </div>
  </footer>
</body>

</html>
```

```css
/* styles.css */

/* General Style Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: 'Roboto', sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Container Class for Layout */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header Styles */
.header {
  background: #1a1a1a;
  color: #fff;
  padding: 1rem 0;
}

.header .logo {
  font-size: 1.5rem;
  font-weight: 700;
}

.nav {
  text-align: right;
}

.nav-list {
  list-style: none;
}

.nav-link {
  text-decoration: none;
  color: #fff;
  margin-left: 1rem;
  font-weight: 500;
  transition: color 0.3s;
}

.nav-link:hover {
  color: #f4a261;
}

/* Hero Section */
.hero {
  background: linear-gradient(to right, #f4a261, #e76f51);
  color: #fff;
  text-align: center;
  padding: 3rem 0;
}

.hero-title {
  font-size: 2rem;
  font-weight: 700;
}

.hero-subtext {
  margin: 1rem 0;
  font-weight: 400;
}

.cta-button {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: #264653;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background 0.3s;
}

.cta-button:hover {
  background: #2a9d8f;
}

/* Features Section */
.features {
  padding: 2rem 0;
  background: #f1f1f1;
}

.features-grid {
  display: flex;
  gap: 2rem;
}

.feature-item {
  flex: 1;
  background: #fff;
  padding: 1.5rem;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* About Section */
.about {
  padding: 2rem 0;
}

/* Contact Section */
.contact {
  padding: 2rem 0;
  background: #f4f4f4;
}

.contact-form {
  max-width: 600px;
  margin: 0 auto;
}

.contact-form label {
  display: block;
  margin-bottom: 0.5rem;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-button {
  display: inline-block;
  background: #264653;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

.submit-button:hover {
  background: #2a9d8f;
}

/* Footer Section */
.footer {
  background: #1a1a1a;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .features-grid {
    flex-direction: column;
  }

  .nav {
    text-align: center;
  }

  .nav-link {
    display: block;
    margin: 0.5rem 0;
  }
}
```
