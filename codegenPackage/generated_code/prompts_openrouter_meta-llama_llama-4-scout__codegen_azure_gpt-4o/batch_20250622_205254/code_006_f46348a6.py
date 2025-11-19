"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Write a CSS code snippet to style a product card component, similar to those on Poly-Market, with a responsive design and hover effects, for a product like "Drohmo R25 polcos szekrény".
Generated: DETERMINISTIC_f46348a6c67adcc2
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Card Component Styles */

/* General container for the product card */
.product-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  max-width: 300px; /* Limit the maximum width */
  background-color: #ffffff; /* White background */
  border: 1px solid #e0e0e0; /* Light gray border */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  overflow: hidden; /* Ensure content doesn't overflow */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effects */
}

/* Hover effect for the card */
.product-card:hover {
  transform: translateY(-5px); /* Slight lift on hover */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* Enhanced shadow on hover */
}

/* Image container */
.product-card img {
  width: 100%; /* Full width of the card */
  height: auto; /* Maintain aspect ratio */
  object-fit: cover; /* Ensure the image fits nicely */
}

/* Content section */
.product-card .content {
  padding: 16px; /* Add spacing inside the card */
  text-align: center; /* Center-align text */
}

/* Product title */
.product-card .content .title {
  font-size: 1.2rem; /* Slightly larger font for title */
  font-weight: 600; /* Bold text */
  color: #333333; /* Dark gray color */
  margin-bottom: 8px; /* Space below the title */
}

/* Product description */
.product-card .content .description {
  font-size: 0.9rem; /* Smaller font for description */
  color: #666666; /* Medium gray color */
  margin-bottom: 16px; /* Space below the description */
}

/* Price section */
.product-card .content .price {
  font-size: 1rem; /* Standard font size for price */
  font-weight: 700; /* Bold text for emphasis */
  color: #007bff; /* Blue color for price */
}

/* Responsive design */
@media (max-width: 768px) {
  .product-card {
    max-width: 100%; /* Full width on smaller screens */
  }
}
```
