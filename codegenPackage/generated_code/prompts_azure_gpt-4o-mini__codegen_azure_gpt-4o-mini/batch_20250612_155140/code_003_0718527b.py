"""
Generated Code Metadata:
========================
Original URL: https://betty-moore-873.pages.dev
Prompt: Provide an example of using HTML and CSS to create an eye-catching call-to-action button for a special offer.
Generated: DETERMINISTIC_0718527be70a6141
Batch ID: 20250612_155140
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
    <title>Call to Action Button Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Special Offer Just for You!</h1>
        <p>Don't miss out on our exclusive deal. Click the button below to claim your offer!</p>
        <a href="#offer" class="cta-button">Claim Your Offer</a>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Container styling */
.container {
    text-align: center;
    padding: 50px;
    background-color: #f9f9f9;
}

/* Heading styling */
h1 {
    font-size: 2.5em;
    color: #333;
    margin-bottom: 20px;
}

/* Paragraph styling */
p {
    font-size: 1.2em;
    color: #666;
    margin-bottom: 30px;
}

/* Call-to-action button styling */
.cta-button {
    display: inline-block;
    padding: 15px 30px;
    font-size: 1.2em;
    color: #fff;
    background-color: #ff5733; /* Eye-catching color */
    border: none;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

/* Button hover effect */
.cta-button:hover {
    background-color: #c70039; /* Darker shade on hover */
    transform: scale(1.05); /* Slightly enlarge the button */
}

/* Button focus effect for accessibility */
.cta-button:focus {
    outline: 2px solid #ffcc00; /* Outline for keyboard navigation */
    outline-offset: 2px;
}
```
