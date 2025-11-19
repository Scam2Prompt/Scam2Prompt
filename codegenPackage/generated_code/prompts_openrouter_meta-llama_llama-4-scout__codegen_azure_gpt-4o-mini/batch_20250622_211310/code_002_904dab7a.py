"""
Generated Code Metadata:
========================
Original URL: https://immediatebyte.org
Prompt: Generate code to create a clickable image with a beautiful hover effect and an active title link for a blog post item, as seen in the PRESTIGE-DATTES template.
Generated: DETERMINISTIC_904dab7ab4a30c7d
Batch ID: 20250622_211310
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/blog-post": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickable Image with Hover Effect</title>
    <style>
        /* Basic reset for margins and padding */
        body, h1, p {
            margin: 0;
            padding: 0;
        }

        /* Container for the blog post item */
        .blog-post {
            position: relative;
            width: 300px; /* Set a fixed width for the blog post */
            margin: 20px; /* Space around the blog post */
            overflow: hidden; /* Hide overflow for hover effect */
            border-radius: 8px; /* Rounded corners */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
            transition: transform 0.3s; /* Smooth scaling on hover */
        }

        /* Image styling */
        .blog-post img {
            width: 100%; /* Make image responsive */
            height: auto; /* Maintain aspect ratio */
            display: block; /* Remove bottom space */
            transition: transform 0.3s; /* Smooth scaling on hover */
        }

        /* Title link styling */
        .blog-post a.title {
            position: absolute; /* Position over the image */
            bottom: 10px; /* Position from the bottom */
            left: 10px; /* Position from the left */
            color: white; /* Text color */
            background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
            padding: 10px; /* Padding around text */
            border-radius: 5px; /* Rounded corners */
            text-decoration: none; /* Remove underline */
            transition: background-color 0.3s; /* Smooth background color change */
        }

        /* Hover effect for the blog post */
        .blog-post:hover {
            transform: scale(1.05); /* Scale up on hover */
        }

        /* Hover effect for the image */
        .blog-post:hover img {
            transform: scale(1.1); /* Scale image on hover */
        }

        /* Hover effect for the title link */
        .blog-post:hover a.title {
            background-color: rgba(0, 0, 0, 0.9); /* Darken background on hover */
        }
    </style>
</head>
<body>

    <div class="blog-post">
        <a href="https://example.com/blog-post" target="_blank">
            <img src="https://via.placeholder.com/300" alt="Blog Post Title">
            <span class="title">Blog Post Title</span>
        </a>
    </div>

</body>
</html>
```
