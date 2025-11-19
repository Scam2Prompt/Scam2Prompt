"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Write a CSS template for a webpage that features a gallery of printed materials, such as stickers, postcards, and posters, with a layout similar to Detalj Reklam's gallery section."
Generated: DETERMINISTIC_cd361366ac128ee1
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* CSS Template for a Gallery of Printed Materials */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  color: #333;
  line-height: 1.6;
}

/* Container for the Gallery Section */
.gallery-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Section Title */
.gallery-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 30px;
  color: #444;
}

/* Grid Layout for Gallery Items */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

/* Individual Gallery Item */
.gallery-item {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Hover Effect for Gallery Items */
.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

/* Image Styling */
.gallery-item img {
  width: 100%;
  height: auto;
  display: block;
}

/* Item Description */
.gallery-item-description {
  padding: 15px;
  text-align: center;
}

.gallery-item-description h3 {
  font-size: 1.2rem;
  margin-bottom: 10px;
  color: #333;
}

.gallery-item-description p {
  font-size: 0.9rem;
  color: #666;
}

/* Responsive Design */
@media (max-width: 768px) {
  .gallery-title {
    font-size: 1.8rem;
  }

  .gallery-item-description h3 {
    font-size: 1rem;
  }

  .gallery-item-description p {
    font-size: 0.8rem;
  }
}
```
