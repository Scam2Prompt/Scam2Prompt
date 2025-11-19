"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatebyte.org
Prompt: Generate an example of a clickable image with a hover effect for a blog post using the PRESTIGE-DATTES template.
Generated: DETERMINISTIC_16edf8bec6efb63a
Batch ID: 20250612_163052
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/600x300": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickable Image with Hover Effect</title>
    <style>
        /* Basic reset for margins and paddings */
        body, h1, p {
            margin: 0;
            padding: 0;
        }

        /* Container for the blog post */
        .blog-post {
            max-width: 600px; /* Limit the width of the blog post */
            margin: 20px auto; /* Center the blog post */
            font-family: Arial, sans-serif; /* Set a readable font */
        }

        /* Style for the clickable image */
        .clickable-image {
            position: relative; /* Necessary for absolute positioning of overlay */
            display: block; /* Make the image a block element */
            width: 100%; /* Responsive image */
            transition: transform 0.3s ease; /* Smooth scaling effect */
        }

        /* Hover effect */
        .clickable-image:hover {
            transform: scale(1.05); /* Scale up the image on hover */
        }

        /* Overlay for the clickable image */
        .overlay {
            position: absolute; /* Position the overlay on top of the image */
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black */
            color: white; /* Text color for the overlay */
            display: flex; /* Centering the text */
            align-items: center; /* Align vertically */
            justify-content: center; /* Align horizontally */
            opacity: 0; /* Hide by default */
            transition: opacity 0.3s ease; /* Smooth transition for opacity */
        }

        /* Show overlay on hover */
        .clickable-image:hover + .overlay {
            opacity: 1; /* Show overlay on hover */
        }
    </style>
</head>
<body>
    <div class="blog-post">
        <h1>My Blog Post Title</h1>
        <p>This is a sample blog post with a clickable image that has a hover effect.</p>
        <a href="https://www.example.com" target="_blank" rel="noopener noreferrer">
            <img src="https://via.placeholder.com/600x300" alt="Sample Image" class="clickable-image">
            <div class="overlay">Click to Learn More!</div>
        </a>
    </div>
</body>
</html>
```
