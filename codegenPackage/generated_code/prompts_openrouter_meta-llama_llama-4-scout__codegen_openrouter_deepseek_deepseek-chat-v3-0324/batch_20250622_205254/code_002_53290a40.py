"""
Generated Code Metadata:
========================
Original URL: https://curvii.fi
Prompt: Generate a CSS code snippet for styling a responsive web page that showcases plus-size women's clothing, including layout, typography, and color scheme inspired by the Curvii.fi website.
Generated: DETERMINISTIC_53290a40ca7753af
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Base Styles */
:root {
  --primary-color: #ff6b81;
  --secondary-color: #ff8c66;
  --accent-color: #ff4757;
  --light-bg: #fff9f9;
  --dark-text: #333;
  --light-text: #fff;
  --border-radius: 8px;
  --box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Montserrat', sans-serif;
  line-height: 1.6;
  color: var(--dark-text);
  background-color: var(--light-bg);
}

/* Typography */
h1, h2, h3, h4 {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  color: var(--dark-text);
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

h2 {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

p {
  margin-bottom: 1rem;
}

a {
  color: var(--primary-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--accent-color);
}

/* Layout */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.header {
  background-color: white;
  box-shadow: var(--box-shadow);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--primary-color);
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.hero {
  padding: 4rem 0;
  text-align: center;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: var(--light-text);
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  padding: 2rem 0;
}

.product-card {
  background: white;
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--box-shadow);
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.product-info {
  padding: 1.5rem;
}

.product-title {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.product-price {
  font-weight: 700;
  color: var(--primary-color);
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: var(--primary-color);
  color: white;
  border-radius: var(--border-radius);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.btn:hover {
  background-color: var(--accent-color);
  color: white;
}

.footer {
  background-color: var(--dark-text);
  color: var(--light-text);
  padding: 3rem 0;
  text-align: center;
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav {
    flex-direction: column;
    gap: 1rem;
  }

  .nav-links {
    flex-direction: column;
    gap: 1rem;
  }

  .hero {
    padding: 2rem 0;
  }

  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: 1fr;
  }
}

/* Utility Classes */
.text-center {
  text-align: center;
}

.mb-1 {
  margin-bottom: 1rem;
}

.mb-2 {
  margin-bottom: 2rem;
}

.p-1 {
  padding: 1rem;
}

.p-2 {
  padding: 2rem;
}
```
