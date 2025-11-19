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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Overlay Text</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="overlay-container">
        <img src="image.jpg" alt="Background Image">
        <div class="overlay-text">
            <h1>Overlay Text</h1>
            <p>This is a sample overlay text.</p>
        </div>
    </div>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #fff;
}

/* Overlay Container Styles */
.overlay-container {
    position: relative;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.overlay-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Overlay Text Styles */
.overlay-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.overlay-text h1 {
    font-size: 48px;
    margin-bottom: 16px;
}

.overlay-text p {
    font-size: 18px;
    margin-bottom: 32px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .overlay-text h1 {
        font-size: 36px;
    }
    .overlay-text p {
        font-size: 16px;
    }
}

@media (max-width: 480px) {
    .overlay-text h1 {
        font-size: 24px;
    }
    .overlay-text p {
        font-size: 14px;
    }
}
```
