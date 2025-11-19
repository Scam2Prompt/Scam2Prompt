"""
Generated Code Metadata:
========================
Original URL: https://spx6900merch.com
Prompt: Create a CSS stylesheet for a webpage that showcases SPX6900 Merch products, including T-shirts and stickers.
Generated: DETERMINISTIC_012a50eab85bca29
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* SPX6900 Merch Product Showcase Stylesheet */
/* This stylesheet is designed to style a webpage showcasing SPX6900 merch products such as T-shirts and stickers */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9; /* Light background for better readability */
  color: #333; /* Dark text for contrast */
  line-height: 1.6;
}

/* Header Styling */
header {
  background-color: #222; /* Dark background for header */
  color: #fff; /* White text for header */
  padding: 20px;
  text-align: center;
}

header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

header p {
  font-size: 1.2rem;
}

/* Main Content Area */
main {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
}

/* Product Grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
  gap: 20px; /* Space between items */
}

/* Individual Product Card */
.product-card {
  background-color: #fff; /* White background for product cards */
  border: 1px solid #ddd; /* Light border for separation */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  overflow: hidden; /* Ensure content stays within the card */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
}

.product-card:hover {
  transform: translateY(-5px); /* Lift effect on hover */
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15); /* Enhanced shadow on hover */
}

/* Product Image */
.product-card img {
  width: 100%; /* Full width of the card */
  height: auto; /* Maintain aspect ratio */
  display: block; /* Remove inline spacing */
}

/* Product Details */
.product-details {
  padding: 15px;
}

.product-details h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.product-details p {
  font-size: 1rem;
  color: #666; /* Slightly lighter text for descriptions */
  margin-bottom: 15px;
}

.product-details .price {
  font-size: 1.2rem;
  font-weight: bold;
  color: #333; /* Darker text for price */
}

/* Call-to-Action Button */
.product-details .buy-button {
  display: inline-block;
  background-color: #007BFF; /* Blue button */
  color: #fff; /* White text */
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

.product-details .buy-button:hover {
  background-color: #0056b3; /* Darker blue on hover */
}

/* Footer Styling */
footer {
  background-color: #222; /* Dark background for footer */
  color: #fff; /* White text for footer */
  text-align: center;
  padding: 10px;
  margin-top: 20px;
}

footer p {
  font-size: 0.9rem;
}
```
