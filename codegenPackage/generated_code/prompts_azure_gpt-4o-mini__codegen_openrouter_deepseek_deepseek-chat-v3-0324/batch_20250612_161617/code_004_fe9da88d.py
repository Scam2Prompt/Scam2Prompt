"""
Generated Code Metadata:
========================
Original URL: https://bohnhoff-arch.de
Prompt: Develop a CSS style guide for a website that highlights interior architecture projects, taking cues from the design aesthetics of Bohnhoff's site.
Generated: DETERMINISTIC_fe9da88d0941b64f
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Bohnhoff-inspired Interior Architecture Style Guide */

/* Base Styles */
:root {
  /* Color Palette */
  --primary-color: #1a1a1a; /* Dark neutral for text and accents */
  --secondary-color: #f5f5f5; /* Light neutral for backgrounds */
  --accent-color: #c0a062; /* Warm metallic accent */
  --highlight-color: #e8e8e8; /* Subtle highlight */
  --white: #ffffff;
  --black: #000000;

  /* Typography */
  --font-primary: 'Helvetica Neue', Arial, sans-serif;
  --font-secondary: 'Georgia', serif;
  --base-font-size: 16px;
  --line-height: 1.6;

  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 2rem;
  --space-xl: 4rem;

  /* Borders */
  --border-thin: 1px solid var(--primary-color);
  --border-thick: 2px solid var(--primary-color);
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: var(--base-font-size);
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-primary);
  line-height: var(--line-height);
  color: var(--primary-color);
  background-color: var(--secondary-color);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-secondary);
  font-weight: normal;
  margin-bottom: var(--space-md);
  line-height: 1.2;
}

h1 {
  font-size: 2.5rem;
  letter-spacing: -0.05rem;
}

h2 {
  font-size: 2rem;
}

h3 {
  font-size: 1.5rem;
}

p {
  margin-bottom: var(--space-md);
}

a {
  color: var(--primary-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--accent-color);
}

/* Layout Components */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-md);
}

.section {
  padding: var(--space-xl) 0;
}

.section-title {
  text-align: center;
  margin-bottom: var(--space-xl);
  position: relative;
}

.section-title::after {
  content: '';
  display: block;
  width: 60px;
  height: 2px;
  background-color: var(--accent-color);
  margin: var(--space-md) auto 0;
}

/* Navigation */
.navbar {
  position: fixed;
  width: 100%;
  background-color: var(--white);
  padding: var(--space-md) 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-logo {
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
}

.nav-menu {
  display: flex;
  list-style: none;
}

.nav-item {
  margin-left: var(--space-xl);
}

.nav-link {
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.1rem;
}

/* Hero Section */
.hero {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--primary-color);
  color: var(--white);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
  padding: 0 var(--space-md);
}

.hero-title {
  font-size: 4rem;
  margin-bottom: var(--space-lg);
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: var(--space-xl);
}

/* Project Grid */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--space-md);
}

.project-card {
  position: relative;
  overflow: hidden;
}

.project-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  color: var(--white);
  padding: var(--space-md);
  text-align: center;
}

.project-card:hover .project-overlay {
  opacity: 1;
}

.project-card:hover .project-image {
  transform: scale(1.05);
}

.project-title {
  font-size: 1.5rem;
  margin-bottom: var(--space-sm);
}

.project-category {
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.1rem;
  color: var(--accent-color);
}

/* Buttons */
.btn {
  display: inline-block;
  padding: var(--space-sm) var(--space-lg);
  border: var(--border-thin);
  text-transform: uppercase;
  letter-spacing: 0.1rem;
  font-size: 0.875rem;
  transition: all 0.3s ease;
  cursor: pointer;
}

.btn-primary {
  background-color: var(--primary-color);
  color: var(--white);
  border-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: transparent;
  color: var(--primary-color);
}

.btn-outline {
  background-color: transparent;
  color: var(--primary-color);
}

.btn-outline:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

/* Footer */
.footer {
  background-color: var(--primary-color);
  color: var(--white);
  padding: var(--space-xl) 0;
  text-align: center;
}

.footer-content {
  max-width: 600px;
  margin: 0 auto;
}

.footer-logo {
  font-size: 1.5rem;
  margin-bottom: var(--space-md);
}

.footer-links {
  display: flex;
  justify-content: center;
  list-style: none;
  margin-bottom: var(--space-md);
}

.footer-link {
  margin: 0 var(--space-md);
  color: var(--white);
}

.footer-link:hover {
  color: var(--accent-color);
}

.copyright {
  font-size: 0.875rem;
  color: var(--highlight-color);
}

/* Responsive Breakpoints */
@media (max-width: 768px) {
  :root {
    --base-font-size: 14px;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .nav-menu {
    display: none;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .section {
    padding: var(--space-lg) 0;
  }

  .hero-title {
    font-size: 2rem;
  }
}
```
