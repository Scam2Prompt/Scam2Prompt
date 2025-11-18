"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Generate CSS code for a hover effect that displays product information and 'Add to Cart' icons, as seen in the WoodMart theme."
Generated: DETERMINISTIC_6dcd0e6432b14591
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Container for the product item */
.product-item {
  position: relative; /* Needed for positioning the hover effect elements */
  width: 300px; /* Example width for product item */
  height: 400px; /* Example height for product item */
  overflow: hidden; /* Ensures content does not overflow the boundary */
  border: 1px solid #ddd; /* Optional border for styling */
  border-radius: 8px; /* Rounded corners */
  transition: transform 0.3s ease; /* Smooth scaling effect */
}

/* Scaling effect on hover */
.product-item:hover {
  transform: scale(1.05); /* Slight scale increase to emphasize the hover */
}

/* Image styling */
.product-item img {
  width: 100%; /* Ensure image fills the container */
  height: auto; /* Maintain aspect ratio */
  display: block; /* Removes unexpected gaps */
}

/* Hover overlay */
.product-item .hover-overlay {
  position: absolute; /* Positioned relative to `product-item` */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent black overlay */
  display: flex; /* Enables flexbox layout */
  flex-direction: column; /* Stack content vertically */
  justify-content: center; /* Center content vertically */
  align-items: center; /* Center content horizontally */
  opacity: 0; /* Initially hidden */
  transition: opacity 0.3s ease; /* Smooth fade-in effect */
}

/* Display overlay on hover */
.product-item:hover .hover-overlay {
  opacity: 1; /* Make overlay visible */
}

/* Product information text */
.hover-overlay .product-info {
  color: #fff; /* White text for readability */
  font-size: 16px; /* Example font size */
  text-align: center; /* Center-align text */
  margin-bottom: 20px; /* Space below text */
}

/* Add to Cart button */
.hover-overlay .add-to-cart {
  background-color: #ff6f61; /* Example button color */
  color: #fff; /* White text for button */
  padding: 10px 20px; /* Button padding */
  border: none; /* Remove border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  font-size: 16px; /* Example font size */
  transition: background-color 0.3s ease; /* Smooth color change */
}

/* Change button color on hover */
.hover-overlay .add-to-cart:hover {
  background-color: #e65050; /* Darker shade on hover */
}
```
