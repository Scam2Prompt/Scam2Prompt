"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Write a CSS template for a webpage that features a gallery of printed materials, such as stickers, postcards, and posters, with a layout similar to Detalj Reklam's gallery section."
Generated: DETERMINISTIC_cd361366ac128ee1
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* CSS Template for a Printed Materials Gallery */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif; /* Use a clean, sans-serif font */
    background-color: #f4f4f4; /* Light background for contrast */
    color: #333; /* Dark text for readability */
}

/* Container for the gallery */
.gallery-container {
    max-width: 1200px; /* Limit the width of the gallery */
    margin: 20px auto; /* Center the gallery on the page */
    padding: 20px; /* Add some padding around the gallery */
    background-color: #fff; /* White background for the gallery */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

/* Title styles */
.gallery-title {
    text-align: center; /* Center the title */
    font-size: 2.5em; /* Large title */
    margin-bottom: 20px; /* Space below the title */
    color: #2c3e50; /* Darker color for the title */
}

/* Grid layout for the gallery items */
.gallery-grid {
    display: grid; /* Use CSS Grid for layout */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* Responsive columns */
    gap: 15px; /* Space between grid items */
}

/* Individual gallery item styles */
.gallery-item {
    background-color: #ecf0f1; /* Light grey background for items */
    border-radius: 5px; /* Rounded corners for items */
    overflow: hidden; /* Hide overflow for rounded corners */
    transition: transform 0.3s; /* Smooth transition for hover effect */
}

/* Image styles */
.gallery-item img {
    width: 100%; /* Make images responsive */
    height: auto; /* Maintain aspect ratio */
}

/* Hover effect for gallery items */
.gallery-item:hover {
    transform: scale(1.05); /* Slightly enlarge on hover */
}

/* Caption styles */
.gallery-caption {
    padding: 10px; /* Space around the caption */
    text-align: center; /* Center the caption text */
    font-size: 1em; /* Standard font size for captions */
    color: #34495e; /* Darker color for captions */
}

/* Media query for smaller screens */
@media (max-width: 600px) {
    .gallery-title {
        font-size: 2em; /* Smaller title on mobile */
    }

    .gallery-caption {
        font-size: 0.9em; /* Smaller caption on mobile */
    }
}
```
