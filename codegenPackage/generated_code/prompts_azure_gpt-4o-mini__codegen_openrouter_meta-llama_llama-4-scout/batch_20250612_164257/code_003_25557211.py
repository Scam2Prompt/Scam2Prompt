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
  Poocoinswapse Shoe Catalog Style Sheet
  ======================================
  Enhances the presentation of a shoe catalog, focusing on categories like 
  "tenis de esporte" and "chuteira."
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

/* Header Styles */
.header {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

.header h1 {
  margin: 0;
}

/* Category Styles */
.category {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 2em;
}

.category h2 {
  width: 100%;
  margin-bottom: 1em;
}

/* Product Styles */
.product {
  background-color: #fff;
  margin: 1em;
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: calc(33.33% - 2em);
}

.product img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.product h3 {
  margin-top: 0;
}

.product .description {
  font-size: 0.9em;
  color: #666;
}

.product .price {
  font-weight: bold;
  color: #333;
}

/* Category Specific Styles */
.tenis-de-esporte {
  background-color: #f7f7f7;
  padding: 1em;
  border: 1px solid #ddd;
}

.chuteira {
  background-color: #f2f2f2;
  padding: 1em;
  border: 1px solid #ddd;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
  .product {
    width: calc(50% - 2em);
  }
}

@media only screen and (max-width: 480px) {
  .product {
    width: 100%;
    margin: 1em 0;
  }
}
```
