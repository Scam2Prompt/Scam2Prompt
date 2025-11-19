"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a code example in HTML/CSS to create a responsive and inviting web page showcasing home staging before-and-after photos, similar to the gallery section on Unique Home Staging & Redesign by Dee's website.
Generated: DETERMINISTIC_54874d538aa25e1c
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Staging Before-and-After</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery-container">
        <h1>Home Staging Before-and-After</h1>
        <div class="gallery">
            <div class="gallery-item">
                <div class="before-after">
                    <img src="before1.jpg" alt="Before" class="before">
                    <img src="after1.jpg" alt="After" class="after">
                </div>
                <div class="overlay">
                    <div class="before-overlay">Before</div>
                    <div class="after-overlay">After</div>
                </div>
            </div>
            <div class="gallery-item">
                <div class="before-after">
                    <img src="before2.jpg" alt="Before" class="before">
                    <img src="after2.jpg" alt="After" class="after">
                </div>
                <div class="overlay">
                    <div class="before-overlay">Before</div>
                    <div class="after-overlay">After</div>
                </div>
            </div>
            <div class="gallery-item">
                <div class="before-after">
                    <img src="before3.jpg" alt="Before" class="before">
                    <img src="after3.jpg" alt="After" class="after">
                </div>
                <div class="overlay">
                    <div class="before-overlay">Before</div>
                    <div class="after-overlay">After</div>
                </div>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.gallery-container {
    max-width: 1200px;
    margin: 40px auto;
    text-align: center;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery-item {
    position: relative;
    margin: 20px;
    width: calc(33.33% - 40px);
}

.before-after {
    position: relative;
    width: 100%;
    height: 250px;
}

.before, .after {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
}

.before {
    clip-path: polygon(0 0, 50% 0, 50% 100%, 0 100%);
}

.after {
    clip-path: polygon(50% 0, 100% 0, 100% 100%, 50% 100%);
    opacity: 0;
    transition: opacity 0.5s;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    opacity: 0;
    transition: opacity 0.5s;
}

.before-overlay, .after-overlay {
    background-color: rgba(255, 255, 255, 0.5);
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: bold;
}

.gallery-item:hover .before {
    opacity: 0;
}

.gallery-item:hover .after {
    opacity: 1;
}

.gallery-item:hover .overlay {
    opacity: 1;
}

@media (max-width: 768px) {
    .gallery-item {
        width: calc(50% - 40px);
    }
}

@media (max-width: 480px) {
    .gallery-item {
        width: 100%;
        margin: 10px 0;
    }
}
```

```javascript
// script.js

// No JavaScript required for this example
```
