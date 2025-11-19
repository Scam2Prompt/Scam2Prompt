"""
Generated Code Metadata:
========================
Original URL: https://larumberaradio.com
Prompt: Write a CSS style sheet for customizing the look of a radio station website, inspired by La Rumbera Radio's design.
Generated: DETERMINISTIC_c3cfd6281d56b6f7
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  CSS Stylesheet for Radio Station Website 
  Inspired by La Rumbera Radio's design
  Author: [Your Name]
  Date: [Today's Date]
*/

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: 'Arial', sans-serif;
  background-color: #1a1a1a; /* Dark background for a modern look */
  color: #ffffff; /* White text for contrast */
  line-height: 1.6;
}

/* Header Section */
header {
  background-color: #ff4500; /* Vibrant orange for energy and excitement */
  color: #ffffff;
  padding: 20px 0;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

header h1 {
  font-size: 2.5rem;
  text-transform: uppercase;
  letter-spacing: 2px;
}

header p {
  font-size: 1.2rem;
  margin-top: 10px;
}

/* Navigation Bar */
nav {
  background-color: #333333; /* Dark gray for contrast */
  padding: 10px 0;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
}

nav ul li {
  margin: 0 15px;
}

nav ul li a {
  text-decoration: none;
  color: #ffffff;
  font-size: 1rem;
  transition: color 0.3s ease;
}

nav ul li a:hover {
  color: #ff4500; /* Highlight on hover */
}

/* Main Content Section */
main {
  padding: 20px;
}

main h2 {
  font-size: 2rem;
  color: #ff4500; /* Accent color for headings */
  margin-bottom: 15px;
}

main p {
  font-size: 1rem;
  margin-bottom: 20px;
}

/* Featured Shows Section */
.featured-shows {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 30px;
}

.featured-show {
  background-color: #333333;
  color: #ffffff;
  padding: 15px;
  border-radius: 8px;
  flex: 1 1 calc(33.333% - 20px); /* Responsive grid */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.featured-show:hover {
  transform: scale(1.05); /* Subtle hover effect */
}

.featured-show h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.featured-show p {
  font-size: 0.9rem;
}

/* Footer Section */
footer {
  background-color: #333333;
  color: #ffffff;
  text-align: center;
  padding: 15px 0;
  margin-top: 30px;
}

footer p {
  font-size: 0.9rem;
}

footer a {
  color: #ff4500;
  text-decoration: none;
  transition: color 0.3s ease;
}

footer a:hover {
  color: #ffffff; /* Reverse hover effect */
}

/* Responsive Design */
@media (max-width: 768px) {
  nav ul {
    flex-direction: column;
    align-items: center;
  }

  .featured-show {
    flex: 1 1 100%; /* Full width on smaller screens */
  }
}
```
