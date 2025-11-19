"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Create a CSS snippet to style a responsive layout for a residential property listing page, inspired by the design elements of residencialviladagraca.com.br."
Generated: DETERMINISTIC_a0bb5d3df211bb71
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Residential Property Listing Page - Responsive Layout */
/* Root styles for consistent spacing and font sizes */
:root {
  --primary-color: #2a4d69; /* Inspired by the site's color palette */
  --secondary-color: #4b86b4;
  --accent-color: #adcbe3;
  --background-color: #f4f4f4;
  --font-family: 'Arial', sans-serif;
  --max-width: 1200px;
  --spacing: 16px;
}

/* Global reset and base styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-family);
  background-color: var(--background-color);
  color: var(--primary-color);
  line-height: 1.6;
}

.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--spacing);
}

/* Header styles */
header {
  background-color: var(--primary-color);
  color: #fff;
  padding: var(--spacing);
  text-align: center;
}

header h1 {
  font-size: 2rem;
  margin-bottom: var(--spacing);
}

header nav {
  margin-top: var(--spacing);
}

header nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 var(--spacing);
}

header nav a:hover {
  text-decoration: underline;
}

/* Property listing grid */
.property-listings {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing);
  margin-top: var(--spacing);
}

.property-card {
  background-color: #fff;
  border: 1px solid var(--accent-color);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.property-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}

.property-card img {
  width: 100%;
  height: auto;
  display: block;
}

.property-card .details {
  padding: var(--spacing);
}

.property-card .details h2 {
  font-size: 1.5rem;
  margin-bottom: var(--spacing);
}

.property-card .details p {
  font-size: 1rem;
  margin-bottom: var(--spacing);
}

.property-card .details .price {
  font-weight: bold;
  color: var(--secondary-color);
}

/* Footer styles */
footer {
  background-color: var(--primary-color);
  color: #fff;
  text-align: center;
  padding: var(--spacing);
  margin-top: var(--spacing);
}

footer p {
  font-size: 0.9rem;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  header h1 {
    font-size: 1.5rem;
  }

  .property-card .details h2 {
    font-size: 1.25rem;
  }

  .property-card .details p {
    font-size: 0.9rem;
  }
}
```
