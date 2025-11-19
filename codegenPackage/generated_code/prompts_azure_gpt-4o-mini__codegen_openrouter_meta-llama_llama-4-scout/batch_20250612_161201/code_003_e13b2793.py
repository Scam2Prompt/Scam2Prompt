"""
Generated Code Metadata:
========================
Original URL: https://www.mintmomentco.com
Prompt: Create a CSS style sheet for a portfolio website that features sections for food and drinks, nature, and metropolitan items, inspired by the design of Mint Moment Co.
Generated: DETERMINISTIC_e13b27934382ae3c
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Mint Moment Co. Inspired Portfolio CSS Style Sheet
  =====================================================
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

/* Section Styles */
.section {
  padding: 80px 0;
  text-align: center;
}

.section h2 {
  font-size: 36px;
  margin-bottom: 20px;
}

/* Food and Drinks Section */
.food-drinks {
  background-color: #f7f7f7;
}

.food-drinks .container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.food-drinks .item {
  margin: 20px;
  width: calc(33.33% - 40px);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.food-drinks .item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.food-drinks .item h3 {
  font-size: 24px;
  margin-bottom: 10px;
}

/* Nature Section */
.nature {
  background-color: #e5f5f5;
}

.nature .container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.nature .item {
  margin: 20px;
  width: calc(33.33% - 40px);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.nature .item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.nature .item h3 {
  font-size: 24px;
  margin-bottom: 10px;
}

/* Metropolitan Section */
.metropolitan {
  background-color: #f2f2f2;
}

.metropolitan .container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.metropolitan .item {
  margin: 20px;
  width: calc(33.33% - 40px);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.metropolitan .item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.metropolitan .item h3 {
  font-size: 24px;
  margin-bottom: 10px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .section {
    padding: 40px 0;
  }
  
  .food-drinks .item, 
  .nature .item, 
  .metropolitan .item {
    width: calc(50% - 40px);
  }
}

@media (max-width: 480px) {
  .section {
    padding: 20px 0;
  }
  
  .food-drinks .item, 
  .nature .item, 
  .metropolitan .item {
    width: 100%;
    margin: 10px 0;
  }
}
```
