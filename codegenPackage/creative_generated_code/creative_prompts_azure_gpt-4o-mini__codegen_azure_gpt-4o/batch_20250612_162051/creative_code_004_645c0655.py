"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Suggest a CSS styling for a product page similar to the layout used on Fanzy Fashion, emphasizing categories like Doll Frocks and Stylish Earrings.
Generated: DETERMINISTIC_645c0655d7469f8a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* General Styling for the Product Page */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f8f8; /* Light background for better readability */
    color: #333; /* Text color */
}

/* Header Section */
header {
    background-color: #ff6584; /* Vibrant pink color for branding */
    padding: 20px;
    text-align: center;
    color: #fff; /* White text for contrast */
    font-size: 1.5em; /* Larger font for emphasis */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

/* Category Section */
.category-section {
    display: flex;
    justify-content: center; /* Center categories horizontally */
    gap: 30px; /* Space between categories */
    padding: 40px 20px;
    background-color: #ffffff; /* Clean white background */
    flex-wrap: wrap; /* Allow wrapping for smaller screens */
}

/* Individual Category Card */
.category-card {
    text-align: center;
    background-color: #f4f4f4; /* Light gray background */
    border: 1px solid #ddd; /* Subtle border */
    border-radius: 8px; /* Rounded corners */
    padding: 20px;
    width: 250px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Soft shadow for modern look */
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
}

.category-card:hover {
    transform: translateY(-5px); /* Slight lift on hover */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* Enhanced shadow on hover */
}

/* Category Image */
.category-card img {
    width: 100%; /* Image spans full width of card */
    border-radius: 5px; /* Rounded corners for images */
    margin-bottom: 15px; /* Space below image */
}

/* Category Title */
.category-card h3 {
    font-size: 1.2em; /* Larger font for title */
    color: #ff6584; /* Brand color */
    margin: 10px 0;
}

/* Category Description */
.category-card p {
    font-size: 1em; /* Default font size */
    color: #666; /* Subtle gray for description */
    margin: 0;
}

/* Footer Section */
footer {
    background-color: #333; /* Dark gray footer */
    color: #fff; /* White text for contrast */
    padding: 15px;
    text-align: center;
    font-size: 0.9em; /* Slightly smaller font */
}

/* Responsive Design for Smaller Screens */
@media (max-width: 768px) {
    .category-section {
        flex-direction: column; /* Stack categories vertically */
        gap: 20px; /* Adjust spacing */
        padding: 20px; /* Reduce padding */
    }

    .category-card {
        width: 100%; /* Adjust card width to full */
    }
}
```
