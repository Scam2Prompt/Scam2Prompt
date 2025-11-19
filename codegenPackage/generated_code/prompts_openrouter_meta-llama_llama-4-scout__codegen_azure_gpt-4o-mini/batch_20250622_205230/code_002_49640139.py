"""
Generated Code Metadata:
========================
Original URL: https://donna-lopez-376.pages.dev
Prompt: Generate HTML and CSS code for a basic webpage that displays an image with an overlay text, similar to the promotional content on the provided URL.
Generated: DETERMINISTIC_496401391463bc21
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Overlay Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="image-container">
        <img src="your-image-url.jpg" alt="Promotional Image" class="responsive-image">
        <div class="overlay">
            <div class="text">Your Overlay Text Here</div>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset default margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Style for the image container */
.image-container {
    position: relative;
    width: 100%;
    max-width: 600px; /* Adjust as needed */
}

/* Responsive image styling */
.responsive-image {
    width: 100%;
    height: auto;
    display: block; /* Ensures no extra space below the image */
}

/* Overlay styling */
.overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black */
    display: flex;
    justify-content: center; /* Center text horizontally */
    align-items: center; /* Center text vertically */
    color: white; /* Text color */
    font-size: 24px; /* Font size */
    text-align: center; /* Center text alignment */
}

/* Responsive text styling */
.text {
    padding: 20px; /* Add some padding around the text */
}
```

Make sure to replace `your-image-url.jpg` with the actual URL of the image you want to display.
