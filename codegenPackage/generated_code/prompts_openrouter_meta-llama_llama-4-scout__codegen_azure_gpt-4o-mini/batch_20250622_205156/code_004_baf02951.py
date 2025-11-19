"""
Generated Code Metadata:
========================
Original URL: https://graphpool.net
Prompt: "Create a simple HTML and CSS template for a video thumbnail gallery that could be used on a site like Graphpool.net."
Generated: DETERMINISTIC_baf029511fba88e6
Batch ID: 20250622_205156
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
    <title>Video Thumbnail Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Video Thumbnail Gallery</h1>
    </header>
    <main>
        <section class="gallery">
            <article class="thumbnail">
                <a href="video1.html">
                    <img src="thumbnail1.jpg" alt="Video 1 Thumbnail">
                    <h2>Video Title 1</h2>
                </a>
            </article>
            <article class="thumbnail">
                <a href="video2.html">
                    <img src="thumbnail2.jpg" alt="Video 2 Thumbnail">
                    <h2>Video Title 2</h2>
                </a>
            </article>
            <article class="thumbnail">
                <a href="video3.html">
                    <img src="thumbnail3.jpg" alt="Video 3 Thumbnail">
                    <h2>Video Title 3</h2>
                </a>
            </article>
            <article class="thumbnail">
                <a href="video4.html">
                    <img src="thumbnail4.jpg" alt="Video 4 Thumbnail">
                    <h2>Video Title 4</h2>
                </a>
            </article>
            <!-- Add more thumbnails as needed -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Graphpool.net. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Style the header */
header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Style the main gallery section */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    padding: 20px;
}

/* Style each thumbnail */
.thumbnail {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    transition: transform 0.2s;
}

/* Add hover effect to thumbnails */
.thumbnail:hover {
    transform: scale(1.05);
}

/* Style the thumbnail image */
.thumbnail img {
    width: 100%;
    height: auto;
}

/* Style the video title */
.thumbnail h2 {
    font-size: 1.2em;
    padding: 10px;
    text-align: center;
}

/* Style the footer */
footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
