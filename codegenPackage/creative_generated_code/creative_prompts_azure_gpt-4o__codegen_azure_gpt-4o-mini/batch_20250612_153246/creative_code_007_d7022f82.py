"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Generate a CSS stylesheet to design a professional showroom display layout for a Sundance Spas retailer website, focusing on branding and product presentation.
Generated: DETERMINISTIC_d7022f82b431fefb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* 
   CSS Stylesheet for Sundance Spas Retailer Website
   Designed to create a professional showroom display layout 
   that emphasizes branding and product presentation.
*/

/* Base styles */
body {
    margin: 0;
    font-family: 'Arial', sans-serif; /* Use a clean, professional font */
    background-color: #f4f4f4; /* Light grey background for neutrality */
    color: #333; /* Dark text for readability */
}

/* Header styles */
header {
    background-color: #0056A1; /* Brand color */
    color: white; /* White text for contrast */
    padding: 20px; /* Spacing around the header */
    text-align: center; /* Center align text */
}

header h1 {
    margin: 0; /* Remove default margin */
    font-size: 2.5em; /* Larger font size for emphasis */
}

/* Navigation styles */
nav {
    margin: 15px 0;
}

nav a {
    color: white; /* White text for links */
    text-decoration: none; /* Remove underline */
    padding: 10px 15px; /* Padding for clickable area */
    transition: background-color 0.3s; /* Smooth transition for hover effect */
}

nav a:hover {
    background-color: #003d6a; /* Darker blue on hover */
}

/* Main content styles */
.main-container {
    display: flex; /* Use flexbox for layout */
    flex-wrap: wrap; /* Allow wrapping of items */
    justify-content: space-around; /* Space items evenly */
    padding: 20px; /* Padding around main content */
}

/* Product card styles */
.product-card {
    background-color: white; /* White background for product cards */
    border: 1px solid #ccc; /* Light border for separation */
    border-radius: 5px; /* Rounded corners */
    box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Subtle shadow for depth */
    margin: 15px; /* Margin around product cards */
    padding: 20px; /* Padding inside product cards */
    width: 300px; /* Fixed width for product cards */
    transition: transform 0.3s; /* Smooth transition for hover effect */
}

.product-card:hover {
    transform: scale(1.05); /* Slightly enlarge on hover */
}

/* Product image styles */
.product-card img {
    max-width: 100%; /* Responsive image */
    height: auto; /* Maintain aspect ratio */
    border-radius: 5px 5px 0 0; /* Rounded top corners */
}

/* Product title styles */
.product-card h2 {
    font-size: 1.5em; /* Larger font size for product title */
    margin: 10px 0; /* Spacing around title */
}

/* Product price styles */
.product-card p.price {
    font-size: 1.2em; /* Emphasized price */
    color: #d9534f; /* Bootstrap danger color for price */
    margin: 10px 0; /* Spacing around price */
}

/* Footer styles */
footer {
    background-color: #0056A1; /* Match header color */
    color: white; /* White text for footer */
    text-align: center; /* Center align text */
    padding: 20px; /* Spacing around footer */
    position: relative; /* Positioning */
    bottom: 0; /* Stick to the bottom */
    width: 100%; /* Full width */
}

/* Responsive styles */
@media (max-width: 768px) {
    .main-container {
        flex-direction: column; /* Stack items on smaller screens */
        align-items: center; /* Center align items */
    }

    .product-card {
        width: 90%; /* Full width on mobile */
    }
}
```
