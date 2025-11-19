"""
Generated Code Metadata:
========================
Original URL: https://leonardo-herrera.com
Prompt: Create a CSS style sheet for a webpage that showcases the elegance of the Leonardo Herrera fashion line, focusing on contemporary designs.
Generated: DETERMINISTIC_e930b2d653df7cfb
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Leonardo Herrera Fashion Line - CSS Stylesheet */
/* This stylesheet is designed to showcase the elegance and contemporary designs of the Leonardo Herrera fashion line */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: 'Helvetica Neue', Arial, sans-serif; /* Clean and modern font */
  font-size: 16px;
  line-height: 1.6;
  color: #333; /* Neutral text color for readability */
  background-color: #f9f9f9; /* Light background for elegance */
  overflow-x: hidden; /* Prevent horizontal scrolling */
}

/* Header Styling */
header {
  background-color: #000; /* Black for sophistication */
  color: #fff; /* White text for contrast */
  padding: 20px 40px;
  text-align: center;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
}

header h1 {
  font-size: 2.5rem;
  font-weight: bold;
  letter-spacing: 2px; /* Adds a modern touch */
  text-transform: uppercase;
}

header nav {
  margin-top: 10px;
}

header nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 15px;
  font-size: 1rem;
  transition: color 0.3s ease;
}

header nav a:hover {
  color: #f4a261; /* Accent color for hover effect */
}

/* Hero Section */
.hero {
  background-image: url('hero-image.jpg'); /* Replace with actual image URL */
  background-size: cover;
  background-position: center;
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  text-align: center;
}

.hero h2 {
  font-size: 3rem;
  font-weight: 300;
  margin-bottom: 20px;
}

.hero p {
  font-size: 1.2rem;
  max-width: 600px;
  margin: 0 auto;
}

/* Main Content */
main {
  padding: 40px 20px;
}

main h3 {
  font-size: 2rem;
  margin-bottom: 20px;
  color: #444;
}

main .collection {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

main .collection-item {
  flex: 1 1 calc(33.333% - 20px); /* Responsive grid layout */
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

main .collection-item:hover {
  transform: translateY(-5px); /* Subtle hover effect */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

main .collection-item img {
  width: 100%;
  height: auto;
  display: block;
}

main .collection-item .details {
  padding: 15px;
}

main .collection-item .details h4 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

main .collection-item .details p {
  font-size: 1rem;
  color: #666;
}

/* Footer Styling */
footer {
  background-color: #000;
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-top: 40px;
}

footer p {
  font-size: 0.9rem;
}

footer a {
  color: #f4a261;
  text-decoration: none;
  transition: color 0.3s ease;
}

footer a:hover {
  color: #fff;
}

/* Responsive Design */
@media (max-width: 768px) {
  main .collection-item {
    flex: 1 1 calc(50% - 20px); /* Adjust grid for smaller screens */
  }
}

@media (max-width: 480px) {
  main .collection-item {
    flex: 1 1 100%; /* Single column layout for very small screens */
  }

  header h1 {
    font-size: 2rem;
  }

  .hero h2 {
    font-size: 2.5rem;
  }
}
```
