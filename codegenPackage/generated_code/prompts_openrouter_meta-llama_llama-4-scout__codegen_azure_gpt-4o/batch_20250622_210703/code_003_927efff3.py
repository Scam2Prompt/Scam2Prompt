"""
Generated Code Metadata:
========================
Original URL: https://medanresortcity.com
Prompt: Generate a CSS stylesheet for styling the Medan Resort City website, incorporating the colors and typography used in the current design.
Generated: DETERMINISTIC_927efff36f164b1b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Medan Resort City Website Stylesheet */
/* Author: [Your Name] */
/* Created: [Date] */
/* Description: Stylesheet for Medan Resort City website, incorporating current design colors and typography */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Root Variables for Colors and Typography */
:root {
  --primary-color: #2a9d8f; /* Main brand color */
  --secondary-color: #264653; /* Dark accent color */
  --tertiary-color: #e9c46a; /* Light accent color */
  --background-color: #f4f4f4; /* Background color */
  --text-color: #333333; /* Default text color */
  --heading-font: 'Playfair Display', serif; /* Font for headings */
  --body-font: 'Roboto', sans-serif; /* Font for body text */
}

/* Global Styles */
body {
  font-family: var(--body-font);
  font-size: 16px;
  color: var(--text-color);
  background-color: var(--background-color);
  line-height: 1.6;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--heading-font);
  color: var(--primary-color);
  margin-bottom: 0.5em;
}

a {
  color: var(--primary-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--secondary-color);
}

/* Header Styles */
header {
  background-color: var(--secondary-color);
  color: #ffffff;
  padding: 1em 0;
}

header .logo {
  font-family: var(--heading-font);
  font-size: 1.5em;
  font-weight: bold;
}

header nav {
  display: flex;
  justify-content: center;
  gap: 1em;
}

header nav a {
  color: #ffffff;
  font-weight: bold;
}

/* Hero Section */
.hero {
  background-color: var(--primary-color);
  color: #ffffff;
  text-align: center;
  padding: 2em 1em;
}

.hero h1 {
  font-size: 2.5em;
}

.hero p {
  font-size: 1.2em;
  margin-top: 0.5em;
}

/* Main Content */
main {
  padding: 2em 1em;
}

main .section {
  margin-bottom: 2em;
}

main .section h2 {
  border-bottom: 2px solid var(--tertiary-color);
  padding-bottom: 0.5em;
  margin-bottom: 1em;
}

main .section p {
  margin-bottom: 1em;
}

/* Footer Styles */
footer {
  background-color: var(--secondary-color);
  color: #ffffff;
  text-align: center;
  padding: 1em 0;
}

footer p {
  font-size: 0.9em;
}

/* Responsive Design */
@media (max-width: 768px) {
  header nav {
    flex-direction: column;
    gap: 0.5em;
  }

  .hero h1 {
    font-size: 2em;
  }

  .hero p {
    font-size: 1em;
  }
}
```
