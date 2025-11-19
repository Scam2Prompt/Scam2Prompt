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
/* General Styles */
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9; /* Light background for a clean look */
  color: #333; /* Dark text for readability */
}

/* Header Styles */
header {
  background-color: #ff6f61; /* Warm coral color inspired by Curvii.fi */
  color: #fff;
  padding: 20px;
  text-align: center;
}

header h1 {
  font-size: 2rem;
  margin: 0;
}

/* Navigation Bar */
nav {
  display: flex;
  justify-content: center;
  background-color: #ff6f61;
  padding: 10px 0;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 15px;
  font-size: 1rem;
}

nav a:hover {
  text-decoration: underline;
}

/* Main Content Layout */
main {
  display: flex;
  flex-wrap: wrap; /* Ensures responsiveness */
  justify-content: center;
  padding: 20px;
}

/* Product Card Styles */
.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 15px;
  width: calc(33.333% - 30px); /* Responsive 3-column layout */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: scale(1.05); /* Subtle hover effect */
}

.product-card img {
  width: 100%;
  height: auto;
  display: block;
}

.product-card .details {
  padding: 15px;
}

.product-card .details h2 {
  font-size: 1.25rem;
  margin: 0 0 10px;
  color: #ff6f61; /* Accent color for product titles */
}

.product-card .details p {
  font-size: 0.9rem;
  margin: 0 0 10px;
  color: #666; /* Subtle text color for descriptions */
}

.product-card .details .price {
  font-size: 1rem;
  font-weight: bold;
  color: #333;
}

/* Footer Styles */
footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 15px;
}

footer p {
  margin: 0;
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-card {
    width: calc(50% - 30px); /* 2-column layout for tablets */
  }
}

@media (max-width: 480px) {
  .product-card {
    width: 100%; /* Single-column layout for mobile */
  }

  nav {
    flex-wrap: wrap; /* Adjust navigation for smaller screens */
  }

  nav a {
    margin: 5px 10px;
  }
}
```
