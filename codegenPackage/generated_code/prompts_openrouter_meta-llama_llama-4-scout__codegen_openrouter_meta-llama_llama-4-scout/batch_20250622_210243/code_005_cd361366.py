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
/* 
  Gallery CSS Template
  =====================
  A responsive gallery template for showcasing printed materials.
*/

/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Gallery Container */
.gallery {
  max-width: 1200px;
  margin: 40px auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

/* Gallery Item */
.gallery-item {
  margin: 20px;
  width: calc(33.33% - 40px);
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.2s ease-in-out;
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Gallery Image */
.gallery-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

/* Gallery Content */
.gallery-content {
  padding: 20px;
}

.gallery-content h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

.gallery-content p {
  font-size: 14px;
  color: #666;
}

/* Responsive Layout */
@media (max-width: 768px) {
  .gallery-item {
    width: calc(50% - 40px);
  }
}

@media (max-width: 480px) {
  .gallery-item {
    width: 100%;
    margin: 10px 0;
  }
}
```
