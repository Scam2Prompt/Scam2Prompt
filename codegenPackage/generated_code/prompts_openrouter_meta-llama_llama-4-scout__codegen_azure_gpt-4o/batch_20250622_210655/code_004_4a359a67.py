"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: "Create a CSS style guide for a modern furniture website, ensuring responsive design for showcasing home decorations, furniture collections, and prefab home models across different devices."
Generated: DETERMINISTIC_4a359a6786be0769
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Style Guide for Modern Furniture Website */
/* Author: [Your Name] */
/* Last Updated: [Date] */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px; /* Base font size */
  scroll-behavior: smooth; /* Smooth scrolling */
}

body {
  font-family: 'Roboto', sans-serif; /* Modern, clean font */
  color: #333; /* Neutral text color */
  background-color: #f9f9f9; /* Light background for readability */
  line-height: 1.6; /* Comfortable line spacing */
}

/* Container for consistent layout */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header Styles */
header {
  background-color: #ffffff; /* Clean white background */
  border-bottom: 1px solid #ddd; /* Subtle border for separation */
  padding: 1rem 0;
}

header .logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  text-decoration: none;
}

header nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header nav ul {
  list-style: none;
  display: flex;
  gap: 1rem;
}

header nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.3s ease;
}

header nav ul li a:hover {
  color: #0078d7; /* Accent color for hover */
}

/* Hero Section */
.hero {
  background-image: url('hero-image.jpg'); /* Replace with actual image */
  background-size: cover;
  background-position: center;
  color: #ffffff;
  text-align: center;
  padding: 4rem 1rem;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
}

.hero .cta-button {
  background-color: #0078d7;
  color: #ffffff;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hero .cta-button:hover {
  background-color: #005bb5;
}

/* Responsive Grid for Furniture Collections */
.furniture-collections {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem 0;
}

.furniture-collections .collection-item {
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.furniture-collections .collection-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.furniture-collections .collection-item img {
  width: 100%;
  height: auto;
}

.furniture-collections .collection-item .details {
  padding: 1rem;
}

.furniture-collections .collection-item .details h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.furniture-collections .collection-item .details p {
  font-size: 1rem;
  color: #666;
}

/* Prefab Home Models Section */
.prefab-homes {
  padding: 2rem 0;
}

.prefab-homes h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
}

.prefab-homes .home-model {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}

.prefab-homes .home-model .model-item {
  flex: 1 1 calc(33.333% - 2rem);
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.prefab-homes .home-model .model-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.prefab-homes .home-model .model-item img {
  width: 100%;
  height: auto;
}

.prefab-homes .home-model .model-item .details {
  padding: 1rem;
}

.prefab-homes .home-model .model-item .details h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.prefab-homes .home-model .model-item .details p {
  font-size: 1rem;
  color: #666;
}

/* Footer Styles */
footer {
  background-color: #333;
  color: #ffffff;
  text-align: center;
  padding: 1rem 0;
}

footer p {
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  header nav ul {
    flex-direction: column;
    gap: 0.5rem;
  }

  .hero h1 {
    font-size: 2rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .furniture-collections {
    grid-template-columns: 1fr;
  }

  .prefab-homes .home-model .model-item {
    flex: 1 1 100%;
  }
}
```
