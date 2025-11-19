"""
Generated Code Metadata:
========================
Original URL: https://poocoinswapse.blogspot.com
Prompt: Develop a CSS style sheet that enhances the presentation of a shoe catalog, focusing on categories like "tenis de esporte" and "chuteira," as highlighted in the content of Poocoinswapse.
Generated: DETERMINISTIC_25557211a31519fd
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  CSS Stylesheet for Shoe Catalog 
  Enhances presentation for categories like "tenis de esporte" and "chuteira"
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
  background-color: #f9f9f9;
  color: #333;
  line-height: 1.6;
}

/* Container for the catalog */
.catalog-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Section Title Styling */
.catalog-title {
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 30px;
  color: #222;
}

/* Category Section Styling */
.category-section {
  margin-bottom: 40px;
}

/* Category Title Styling */
.category-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: #444;
  border-bottom: 2px solid #ddd;
  padding-bottom: 10px;
}

/* Shoe Item Styling */
.shoe-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  padding: 15px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.shoe-item:hover {
  transform: scale(1.02);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Shoe Image Styling */
.shoe-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 8px;
  margin-right: 20px;
}

/* Shoe Details Styling */
.shoe-details {
  flex: 1;
}

.shoe-name {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}

.shoe-description {
  font-size: 1rem;
  color: #666;
  margin-bottom: 10px;
}

.shoe-price {
  font-size: 1.1rem;
  font-weight: bold;
  color: #28a745;
}

/* Specific Styling for "Tenis de Esporte" */
.tenis-de-esporte .shoe-item {
  border: 2px solid #007bff;
}

.tenis-de-esporte .shoe-name {
  color: #007bff;
}

/* Specific Styling for "Chuteira" */
.chuteira .shoe-item {
  border: 2px solid #dc3545;
}

.chuteira .shoe-name {
  color: #dc3545;
}

/* Responsive Design */
@media (max-width: 768px) {
  .shoe-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .shoe-image {
    margin-bottom: 15px;
  }
}
```
