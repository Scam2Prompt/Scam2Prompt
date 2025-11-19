"""
Generated Code Metadata:
========================
Original URL: https://www.mintmomentco.com
Prompt: Create a CSS style sheet for a portfolio website that features sections for food and drinks, nature, and metropolitan items, inspired by the design of Mint Moment Co.
Generated: DETERMINISTIC_e13b27934382ae3c
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Portfolio Website CSS - Inspired by Mint Moment Co. */
/* Base Styles */
:root {
  --primary-color: #a8e6cf;
  --secondary-color: #dcedc1;
  --accent-color: #ffd3b6;
  --dark-color: #ffaaa5;
  --text-color: #333;
  --light-text: #f8f8f8;
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: #f9f9f9;
}

/* Header Styles */
.header {
  background-color: var(--primary-color);
  padding: 2rem 0;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header__title {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-color);
}

.header__subtitle {
  font-size: 1.2rem;
  color: var(--text-color);
  opacity: 0.8;
}

/* Navigation */
.nav {
  display: flex;
  justify-content: center;
  padding: 1rem 0;
  background-color: var(--secondary-color);
}

.nav__list {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav__link {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: var(--transition);
}

.nav__link:hover {
  background-color: var(--accent-color);
  color: var(--light-text);
}

/* Section Styles */
.section {
  padding: 4rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.section__title {
  font-size: 2rem;
  margin-bottom: 2rem;
  text-align: center;
  color: var(--text-color);
  position: relative;
}

.section__title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 3px;
  background-color: var(--dark-color);
}

/* Food & Drinks Section */
.food-drinks {
  background-color: var(--accent-color);
}

/* Nature Section */
.nature {
  background-color: var(--primary-color);
}

/* Metropolitan Section */
.metropolitan {
  background-color: var(--secondary-color);
}

/* Gallery Grid */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.gallery__item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: var(--transition);
}

.gallery__item:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.gallery__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: var(--transition);
}

.gallery__item:hover .gallery__img {
  transform: scale(1.05);
}

.gallery__caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  color: var(--light-text);
  padding: 1rem;
  transform: translateY(100%);
  transition: var(--transition);
}

.gallery__item:hover .gallery__caption {
  transform: translateY(0);
}

/* Footer */
.footer {
  background-color: var(--dark-color);
  color: var(--light-text);
  text-align: center;
  padding: 2rem 0;
  margin-top: 2rem;
}

.footer__text {
  margin-bottom: 1rem;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
}

.social-link {
  color: var(--light-text);
  font-size: 1.5rem;
  transition: var(--transition);
}

.social-link:hover {
  color: var(--accent-color);
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav__list {
    flex-direction: column;
    gap: 0.5rem;
  }

  .gallery {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}

@media (max-width: 480px) {
  .header__title {
    font-size: 2rem;
  }

  .section {
    padding: 2rem 1rem;
  }

  .gallery {
    grid-template-columns: 1fr;
  }
}
```
