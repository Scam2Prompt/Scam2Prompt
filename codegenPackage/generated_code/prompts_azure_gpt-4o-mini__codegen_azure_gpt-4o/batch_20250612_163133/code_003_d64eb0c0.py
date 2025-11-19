"""
Generated Code Metadata:
========================
Original URL: https://radical-wear.cz
Prompt: Develop a CSS style guide for an online clothing store that includes options for different skin colors and layout modes, as seen on Radical Wear.
Generated: DETERMINISTIC_d64eb0c074743a5c
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
CSS Style Guide for Online Clothing Store 
Author: [Your Name]
Date: [Today's Date]
Description: This stylesheet includes options for different skin colors and layout modes.
*/

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Root Variables */
:root {
  /* Skin color options */
  --skin-light: #f5f5f5;
  --skin-medium: #d2b48c;
  --skin-dark: #8b4513;

  /* Layout modes */
  --layout-light-bg: #ffffff;
  --layout-light-text: #333333;
  --layout-dark-bg: #1a1a1a;
  --layout-dark-text: #f5f5f5;

  /* Accent colors */
  --primary-color: #ff6f61;
  --secondary-color: #4caf50;
  --tertiary-color: #2196f3;

  /* Font settings */
  --font-family: 'Arial, sans-serif';
  --base-font-size: 16px;
}

/* Base Styles */
body {
  font-family: var(--font-family);
  font-size: var(--base-font-size);
  background-color: var(--layout-light-bg);
  color: var(--layout-light-text);
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* Skin Color Options */
.skin-light {
  background-color: var(--skin-light);
}

.skin-medium {
  background-color: var(--skin-medium);
}

.skin-dark {
  background-color: var(--skin-dark);
}

/* Layout Modes */
.layout-light {
  background-color: var(--layout-light-bg);
  color: var(--layout-light-text);
}

.layout-dark {
  background-color: var(--layout-dark-bg);
  color: var(--layout-dark-text);
}

/* Header Styles */
header {
  background-color: var(--primary-color);
  color: var(--layout-light-bg);
  padding: 1rem;
  text-align: center;
}

/* Navigation Bar */
nav {
  display: flex;
  justify-content: space-around;
  background-color: var(--secondary-color);
  padding: 0.5rem;
}

nav a {
  color: var(--layout-light-bg);
  text-decoration: none;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

/* Product Card */
.product-card {
  border: 1px solid var(--layout-light-text);
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem;
  background-color: var(--layout-light-bg);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Footer Styles */
footer {
  background-color: var(--tertiary-color);
  color: var(--layout-light-bg);
  text-align: center;
  padding: 1rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  nav {
    flex-direction: column;
  }

  .product-card {
    margin: 0.5rem;
  }
}

/* Utility Classes */
.hidden {
  display: none !important;
}

.text-center {
  text-align: center;
}

.text-bold {
  font-weight: bold;
}

.bg-primary {
  background-color: var(--primary-color);
}

.bg-secondary {
  background-color: var(--secondary-color);
}

.bg-tertiary {
  background-color: var(--tertiary-color);
}

.text-light {
  color: var(--layout-light-bg);
}

.text-dark {
  color: var(--layout-dark-text);
}
```
