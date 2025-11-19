"""
Generated Code Metadata:
========================
Original URL: https://phosphor.now.sh
Prompt: Generate HTML and CSS code for a simple website design inspired by Phosphor's service offerings.
Generated: DETERMINISTIC_e2989da72babf002
Batch ID: 20250622_212817
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.gstatic.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phosphor Services</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <a href="#" class="logo">Phosphor</a>
                <nav class="nav">
                    <ul class="nav-list">
                        <li class="nav-item"><a href="#services" class="nav-link">Services</a></li>
                        <li class="nav-item"><a href="#about" class="nav-link">About</a></li>
                        <li class="nav-item"><a href="#contact" class="nav-link">Contact</a></li>
                    </ul>
                </nav>
                <button class="cta-button">Get Started</button>
            </div>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container">
                <div class="hero-content">
                    <h1 class="hero-title">Illuminate Your Digital Future</h1>
                    <p class="hero-subtitle">Cutting-edge solutions to power your business growth</p>
                    <div class="hero-actions">
                        <button class="primary-button">Explore Services</button>
                        <button class="secondary-button">Learn More</button>
                    </div>
                </div>
            </div>
        </section>

        <section id="services" class="services">
            <div class="container">
                <h2 class="section-title">Our Services</h2>
                <div class="services-grid">
                    <div class="service-card">
                        <div class="service-icon">💡</div>
                        <h3 class="service-title">Digital Strategy</h3>
                        <p class="service-description">Comprehensive digital transformation roadmaps tailored to your business needs.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">🛠️</div>
                        <h3 class="service-title">Web Development</h3>
                        <p class="service-description">Custom, responsive websites built with modern technologies.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">📈</div>
                        <h3 class="service-title">Growth Marketing</h3>
                        <p class="service-description">Data-driven marketing strategies to accelerate your growth.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="about" class="about">
            <div class="container">
                <div class="about-content">
                    <div class="about-text">
                        <h2 class="section-title">About Phosphor</h2>
                        <p class="about-description">We're a team of passionate innovators dedicated to helping businesses shine in the digital landscape. Our approach combines technical excellence with creative problem-solving.</p>
                        <button class="primary-button">Meet the Team</button>
                    </div>
                    <div class="about-image">
                        <!-- Placeholder for image -->
                        <div class="image-placeholder"></div>
                    </div>
                </div>
            </div>
        </section>

        <section id="contact" class="contact">
            <div class="container">
                <h2 class="section-title">Get in Touch</h2>
                <form class="contact-form">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="primary-button">Send Message</button>
                </form>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">Phosphor</div>
                <div class="footer-links">
                    <ul class="footer-list">
                        <li><a href="#services">Services</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-social">
                    <a href="#" class="social-link">Twitter</a>
                    <a href="#" class="social-link">LinkedIn</a>
                    <a href="#" class="social-link">Instagram</a>
                </div>
            </div>
            <div class="footer-copyright">
                <p>&copy; 2023 Phosphor. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>
```

```css
/* Base Styles */
:root {
    --primary-color: #6c63ff;
    --primary-dark: #564fd8;
    --secondary-color: #f8f9fa;
    --text-color: #333;
    --text-light: #6c757d;
    --white: #ffffff;
    --black: #000000;
    --gray-light: #e9ecef;
    --border-radius: 8px;
    --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    --transition: all 0.3s ease;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    color: var(--text-color);
    line-height: 1.6;
    background-color: var(--white);
}

.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.2;
}

p {
    margin-bottom: 1rem;
}

a {
    text-decoration: none;
    color: inherit;
}

/* Buttons */
.button {
    display: inline-block;
    padding: 12px 24px;
    border-radius: var(--border-radius);
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition);
    border: none;
}

.primary-button {
    background-color: var(--primary-color);
    color: var(--white);
}

.primary-button:hover {
    background-color: var(--primary-dark);
}

.secondary-button {
    background-color: transparent;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
}

.secondary-button:hover {
    background-color: var(--primary-color);
    color: var(--white);
}

.cta-button {
    background-color: transparent;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
    padding: 8px 16px;
}

.cta-button:hover {
    background-color: var(--primary-color);
    color: var(--white);
}

/* Header */
.header {
    padding: 20px 0;
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    background-color: var(--white);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    z-index: 1000;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary-color);
}

.nav-list {
    display: flex;
    list-style: none;
    gap: 30px;
}

.nav-link {
    font-weight: 500;
    transition: var(--transition);
}

.nav-link:hover {
    color: var(--primary-color);
}

/* Hero Section */
.hero {
    padding: 180px 0 100px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    text-align: center;
}

.hero-title {
    font-size: 3rem;
    margin-bottom: 20px;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var
