"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Generate a CSS stylesheet that aligns with the design principles mentioned in the EMFresh2o portfolio, focusing on modern aesthetics and responsive design.
Generated: DETERMINISTIC_0362e61a5a40c3aa
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  EMFresh2o Portfolio CSS Stylesheet
  ======================================

  This stylesheet is designed to align with the modern aesthetics and responsive design principles of the EMFresh2o portfolio.

  Table of Contents:
  1. Global Styles
  2. Typography
  3. Color Scheme
  4. Layout and Grid
  5. Navigation
  6. Hero Section
  7. Project Showcase
  8. Footer
  9. Responsive Design
*/

/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Open Sans', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #333;
}

h1 {
  font-size: 36px;
  margin-bottom: 10px;
}

h2 {
  font-size: 28px;
  margin-bottom: 10px;
}

p {
  margin-bottom: 20px;
}

/* Color Scheme */
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --background-color: #f9f9f9;
  --text-color: #333;
}

/* Layout and Grid */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}

/* Navigation */
nav {
  background-color: #333;
  color: #fff;
  padding: 10px;
  text-align: center;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

nav li {
  display: inline-block;
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
}

nav a:hover {
  color: #ccc;
}

/* Hero Section */
.hero {
  background-image: linear-gradient(to bottom, #3498db, #2ecc71);
  background-size: 100% 300px;
  background-position: 0% 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}

.hero h1 {
  font-size: 48px;
}

/* Project Showcase */
.projects {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.project {
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.project h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

/* Footer */
footer {
  background-color: #333;
  color: #fff;
  padding: 10px;
  text-align: center;
  clear: both;
}

footer p {
  margin-bottom: 10px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    grid-template-columns: repeat(6, 1fr);
  }

  .projects {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .container {
    grid-template-columns: repeat(4, 1fr);
  }

  .projects {
    grid-template-columns: 1fr;
  }

  .hero h1 {
    font-size: 36px;
  }
}
```
