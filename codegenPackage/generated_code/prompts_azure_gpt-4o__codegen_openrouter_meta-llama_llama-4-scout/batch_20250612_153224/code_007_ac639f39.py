"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Develop a CSS style sheet for displaying product categories like "آینه حمام" and "قفسه حمام" in a grid layout, ensuring responsiveness for mobile and desktop views.
Generated: DETERMINISTIC_ac639f39fd0f8212
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Product Category Grid Styles
  ============================
  Styles for displaying product categories in a grid layout.
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
}

/* Grid Container Styles */
.category-grid {
  max-width: 1200px;
  margin: 40px auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-gap: 20px;
}

/* Grid Item Styles */
.category-grid-item {
  background-color: #f7f7f7;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.category-grid-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.category-grid-item h2 {
  font-size: 18px;
  margin-top: 10px;
}

/* Responsive Styles */
@media only screen and (max-width: 768px) {
  .category-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}

@media only screen and (max-width: 480px) {
  .category-grid {
    grid-template-columns: 1fr;
  }
  .category-grid-item {
    padding: 10px;
  }
}

/* RTL (Right-to-Left) Styles for Persian */
.category-grid-item {
  direction: rtl;
  text-align: right;
}

.category-grid-item h2 {
  font-family: 'IRANSans', sans-serif;
}
```
