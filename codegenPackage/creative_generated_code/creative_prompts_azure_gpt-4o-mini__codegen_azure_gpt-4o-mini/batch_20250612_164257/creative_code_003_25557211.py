"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinswapse.blogspot.com
Prompt: Develop a CSS style sheet that enhances the presentation of a shoe catalog, focusing on categories like "tenis de esporte" and "chuteira," as highlighted in the content of Poocoinswapse.
Generated: DETERMINISTIC_25557211a31519fd
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* CSS Style Sheet for Shoe Catalog Presentation */

/* General Styles */
body {
    font-family: Arial, sans-serif; /* Use a clean font for readability */
    margin: 0; /* Remove default margins */
    padding: 0; /* Remove default padding */
    background-color: #f4f4f4; /* Light grey background for a modern look */
}

/* Container for the catalog */
.catalog-container {
    max-width: 1200px; /* Limit the width of the catalog */
    margin: 20px auto; /* Center the catalog with automatic margins */
    padding: 20px; /* Add padding for better spacing */
    background-color: #ffffff; /* White background for the catalog */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

/* Title Styles */
.catalog-title {
    text-align: center; /* Center align the title */
    font-size: 2.5em; /* Large font size for the title */
    color: #333; /* Dark color for the title */
    margin-bottom: 20px; /* Space below the title */
}

/* Shoe Category Styles */
.category {
    display: flex; /* Use flexbox for layout */
    flex-wrap: wrap; /* Allow wrapping to next line */
    justify-content: space-around; /* Space items evenly */
    margin: 10px 0; /* Vertical spacing between categories */
}

/* Individual Shoe Item */
.shoe-item {
    background-color: #fff; /* White background for each shoe item */
    border: 1px solid #ddd; /* Light grey border */
    border-radius: 5px; /* Slightly rounded corners */
    width: calc(33% - 20px); /* Responsive width for three items per row */
    margin: 10px; /* Margin around each shoe item */
    padding: 15px; /* Internal padding */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow effect */
    transition: transform 0.2s; /* Smooth hover effect */
}

/* Hover effect for shoe items */
.shoe-item:hover {
    transform: scale(1.05); /* Scale up slightly on hover */
}

/* Shoe Item Image */
.shoe-item img {
    max-width: 100%; /* Make the image responsive */
    height: auto; /* Maintain aspect ratio */
    border-radius: 5px; /* Rounded corners for the image */
}

/* Shoe Item Title */
.shoe-title {
    font-size: 1.5em; /* Size of the shoe title */
    color: #007BFF; /* Bootstrap primary color for titles */
    margin: 10px 0; /* Space above and below the title */
}

/* Shoe Item Description */
.shoe-description {
    font-size: 1em; /* Standard font size for description */
    color: #666; /* Darker grey for description text */
    margin: 10px 0; /* Space around description */
}

/* Button Styles */
.button {
    display: inline-block; /* Allow margins */
    padding: 10px 15px; /* Padding for button */
    background-color: #007BFF; /* Primary button color */
    color: white; /* White text for button */
    text-decoration: none; /* Remove underline from links */
    border-radius: 5px; /* Rounded corners for buttons */
    transition: background-color 0.3s; /* Smooth transition for hover effect */
}

/* Button hover effect */
.button:hover {
    background-color: #0056b3; /* Darker shade on hover */
}

/* Media Query for Responsive Design */
@media (max-width: 800px) {
    .shoe-item {
        width: calc(50% - 20px); /* Two items per row on smaller screens */
    }
}

@media (max-width: 500px) {
    .shoe-item {
        width: 100%; /* One item per row on very small screens */
    }
}
```
