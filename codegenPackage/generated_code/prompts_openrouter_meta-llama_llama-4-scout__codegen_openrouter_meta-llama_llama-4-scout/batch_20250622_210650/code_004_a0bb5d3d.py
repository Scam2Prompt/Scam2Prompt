"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Create a CSS snippet to style a responsive layout for a residential property listing page, inspired by the design elements of residencialviladagraca.com.br."
Generated: DETERMINISTIC_a0bb5d3df211bb71
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Responsive Layout for Residential Property Listing Page
  Inspired by: residencialviladagraca.com.br
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

/* Container Styles */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Header Styles */
.header {
  background-color: #333;
  color: #fff;
  padding: 20px;
  text-align: center;
}

.header h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

/* Property Listing Styles */
.property-listing {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.property-listing .property {
  background-color: #fff;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: calc(33.33% - 20px);
}

.property-listing .property img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.property-listing .property .details {
  padding: 20px;
}

.property-listing .property .details h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

.property-listing .property .details p {
  font-size: 14px;
  margin-bottom: 20px;
}

.property-listing .property .details .price {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .property-listing .property {
    width: calc(50% - 20px);
  }
}

@media (max-width: 480px) {
  .property-listing .property {
    width: 100%;
    margin: 10px 0;
  }
}

/* Footer Styles */
.footer {
  background-color: #333;
  color: #fff;
  padding: 20px;
  text-align: center;
  clear: both;
}

.footer p {
  font-size: 14px;
  margin-bottom: 10px;
}
```
