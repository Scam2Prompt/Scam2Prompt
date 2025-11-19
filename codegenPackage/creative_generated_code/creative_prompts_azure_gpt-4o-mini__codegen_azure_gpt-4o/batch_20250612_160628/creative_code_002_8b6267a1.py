"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveandevan.com
Prompt: Create a CSS stylesheet to style a product grid similar to the one found on the Evan Mens website for showcasing men's clothing.
Generated: DETERMINISTIC_8b6267a1b8916475
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* -----------------------------------------------------------------------------
   Product Grid Stylesheet
   Author: [Your Name]
   Description: Styles for a product grid showcasing men's clothing
   Last Updated: [Date]
----------------------------------------------------------------------------- */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styles */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  color: #333;
}

/* Container for the Product Grid */
.product-grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px; /* Space between grid items */
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto; /* Center the container */
  background-color: #ffffff;
}

/* Individual Product Card */
.product-card {
  background-color: #ffffff;
  border: 1px solid #ddd; /* Light gray border */
  border-radius: 8px; /* Rounded corners */
  overflow: hidden; /* Ensure content fits within card bounds */
  transition: box-shadow 0.3s ease; /* Smooth hover effect */
}

/* Hover Effect for Product Card */
.product-card:hover {
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Slight shadow on hover */
}

/* Image Container */
.product-card img {
  width: 100%;
  height: auto;
  display: block; /* Ensure the image fits the container */
}

/* Product Details Section */
.product-details {
  padding: 15px;
  text-align: center; /* Center align text */
}

/* Product Title */
.product-details .product-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #222; /* Darker text for better readability */
  text-transform: capitalize; /* Ensure uniform styling */
}

/* Product Price */
.product-details .product-price {
  font-size: 16px;
  color: #27ae60; /* Green color for price */
  margin-bottom: 10px;
}

/* Add to Cart Button */
.product-details .add-to-cart-btn {
  display: inline-block;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: bold;
  color: #ffffff;
  background-color: #333; /* Dark background */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none; /* Remove link underline */
  transition: background-color 0.3s ease;
}

/* Button Hover Effect */
.product-details .add-to-cart-btn:hover {
  background-color: #555; /* Slightly lighter on hover */
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-grid-container {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Adjust for smaller screens */
  }
}

@media (max-width: 480px) {
  .product-details .product-title {
    font-size: 16px; /* Reduce font size for small devices */
  }

  .product-details .product-price {
    font-size: 14px;
  }

  .product-details .add-to-cart-btn {
    font-size: 12px; /* Smaller button text on small screens */
    padding: 8px 15px;
  }
}
```
