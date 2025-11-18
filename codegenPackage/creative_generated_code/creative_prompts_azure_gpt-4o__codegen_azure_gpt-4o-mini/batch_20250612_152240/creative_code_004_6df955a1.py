"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupocapernaum.com
Prompt: Write a script to replace a default hosting confirmation page with a custom "Under Construction" page using HTML and CSS.
Generated: DETERMINISTIC_6df955a1f9b3b212
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Under Construction</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="container">
        <h1>Under Construction</h1>
        <p>We're currently working on something awesome. Please check back later!</p>
        <img src="construction-image.png" alt="Under Construction" class="construction-image">
    </div>
</body>

</html>
```

```css
/* styles.css */

/* Basic reset for default margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Set body styles */
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Full viewport height */
    background-color: #f0f0f0; /* light gray background */
    font-family: Arial, sans-serif; /* Default font */
}

/* Container for the content */
.container {
    text-align: center;
    background-color: #ffffff; /* white background for the container */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* subtle shadow */
    padding: 20px; /* Padding inside the container */
}

/* Heading styles */
h1 {
    color: #e74c3c; /* Red color for the heading */
    margin-bottom: 10px; /* Space below the heading */
}

/* Paragraph styles */
p {
    color: #333333; /* Dark gray color for the text */
    margin-bottom: 20px; /* Space below the paragraph */
}

/* Image styles */
.construction-image {
    max-width: 100%; /* Responsive image */
    height: auto; /* Maintain aspect ratio */
}
```

### Instructions for Implementation
1. Save the HTML code in a file named `index.html`.
2. Save the CSS code in a separate file named `styles.css`.
3. Ensure to replace `construction-image.png` with the actual path to your image file.
4. Host the `index.html` and `styles.css` files on your server to replace the default hosting confirmation page.
