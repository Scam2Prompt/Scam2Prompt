"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Create a CSS stylesheet to design a product page layout for items like "Mount Plates" and "Ring Stickers," ensuring it matches the aesthetic of the Volport website.
Generated: DETERMINISTIC_fcadc6c1cf29319c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Volport Product Page Stylesheet */

/* Reset default margin and padding for all elements */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body styles */
body {
  font-family: 'Arial', sans-serif; /* Use a clean, professional font */
  background-color: #ffffff; /* Set a white background for the page */
  color: #333333; /* Use dark gray for text for readability */
  line-height: 1.6; /* Improve text readability */
}

/* Container for the product page */
.container {
  width: 90%;
  max-width: 1200px; /* Restrict container width for large screens */
  margin: 0 auto; /* Center the container horizontally */
  padding: 20px; /* Add spacing inside the container */
}

/* Product header styles */
.product-header {
  text-align: center;
  margin-bottom: 40px; /* Add space below the header */
}

.product-header h1 {
  font-size: 2.5rem; /* Large, prominent title */
  color: #1a1a1a; /* Dark color for contrast */
}

.product-header p {
  font-size: 1.2rem; /* Subtitle font size */
  color: #555555; /* Subtle gray for less emphasis */
}

/* Product grid layout */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid layout */
  gap: 20px; /* Space between grid items */
}

/* Individual product card */
.product-card {
  background-color: #f9f9f9; /* Light gray background for product cards */
  border: 1px solid #dddddd; /* Thin border for structure */
  border-radius: 10px; /* Rounded corners */
  overflow: hidden; /* Ensure content stays inside borders */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effects */
}

/* Hover effect for product card */
.product-card:hover {
  transform: scale(1.05); /* Scale up slightly */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Add shadow for depth */
}

/* Product image styles */
.product-card img {
  width: 100%; /* Full width of the card */
  height: auto; /* Maintain aspect ratio */
  border-bottom: 1px solid #dddddd; /* Separator between image and details */
}

/* Product details section */
.product-details {
  padding: 15px; /* Add spacing inside the details section */
}

.product-details h2 {
  font-size: 1.5rem; /* Product title size */
  color: #1a1a1a; /* Dark color for titles */
  margin-bottom: 10px; /* Space below title */
}

.product-details p {
  font-size: 1rem; /* Regular paragraph size */
  color: #666666; /* Subtle gray for text */
}

.product-details .price {
  font-size: 1.2rem; /* Highlight price size */
  font-weight: bold; /* Emphasize price */
  color: #008cba; /* Use brand color for price */
  margin-top: 10px; /* Space above price */
}

/* CTA button styles */
.cta-button {
  display: inline-block;
  padding: 10px 20px; /* Button size */
  background-color: #008cba; /* Volport brand color */
  color: #ffffff; /* White text for contrast */
  font-size: 1rem;
  font-weight: bold;
  text-align: center;
  text-decoration: none; /* Remove underline */
  border-radius: 5px; /* Rounded corners */
  transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth hover effects */
  margin-top: 15px; /* Space above the button */
}

/* Hover effect for CTA button */
.cta-button:hover {
  background-color: #005f8d; /* Darker shade on hover */
  transform: translateY(-2px); /* Slight upward movement */
}

/* Footer styles */
.footer {
  text-align: center;
  margin-top: 50px; /* Space above footer */
  padding: 20px;
  background-color: #f2f2f2; /* Light gray background */
  color: #333333; /* Dark gray text */
}

.footer p {
  font-size: 0.9rem; /* Smaller text size */
}
```
