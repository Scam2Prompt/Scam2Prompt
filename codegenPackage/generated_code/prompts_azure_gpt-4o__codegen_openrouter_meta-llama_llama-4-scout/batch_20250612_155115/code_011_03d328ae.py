"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Create a CSS stylesheet to style a product filter sidebar with categories for colors, sizes, and retailers, ensuring responsive design for mobile and desktop views.
Generated: DETERMINISTIC_03d328ae7293d2e0
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Product Filter Sidebar Stylesheet
  =================================
  Styles for product filter sidebar with categories for colors, sizes, and retailers.
  Ensures responsive design for mobile and desktop views.
*/

/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
}

/* Sidebar Container Styles */
.sidebar {
  position: relative;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Category Header Styles */
.category-header {
  font-weight: bold;
  margin-bottom: 10px;
}

/* Filter List Styles */
.filter-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.filter-list li {
  margin-bottom: 10px;
}

.filter-list li input[type="checkbox"] {
  margin-right: 10px;
}

.filter-list li label {
  cursor: pointer;
}

/* Color Filter Styles */
.color-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.color-filter .color-box {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
}

/* Size Filter Styles */
.size-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.size-filter .size-box {
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
}

/* Retailer Filter Styles */
.retailer-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.retailer-filter .retailer-box {
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
}

/* Responsive Design Styles */
@media (max-width: 768px) {
  .sidebar {
    padding: 10px;
  }
  
  .category-header {
    font-size: 18px;
  }
  
  .filter-list li {
    font-size: 14px;
  }
  
  .color-filter .color-box {
    width: 15px;
    height: 15px;
  }
  
  .size-filter .size-box {
    padding: 3px 6px;
  }
  
  .retailer-filter .retailer-box {
    padding: 3px 6px;
  }
}

@media (max-width: 480px) {
  .sidebar {
    padding: 5px;
  }
  
  .category-header {
    font-size: 16px;
  }
  
  .filter-list li {
    font-size: 12px;
  }
  
  .color-filter .color-box {
    width: 10px;
    height: 10px;
  }
  
  .size-filter .size-box {
    padding: 2px 4px;
  }
  
  .retailer-filter .retailer-box {
    padding: 2px 4px;
  }
}
```
