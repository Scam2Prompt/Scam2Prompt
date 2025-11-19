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
  <meta name="description" content="Video Thumbnail Gallery">
  <title>Video Thumbnail Gallery</title>
  <style>
    /* General reset for consistent styling across browsers */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
      padding: 20px;
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
    }

    .thumbnail {
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .thumbnail:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

    .thumbnail img {
      width: 100%;
      height: auto;
      display: block;
    }

    .thumbnail .info {
      padding: 10px;
    }

    .thumbnail .info h2 {
      font-size: 18px;
      margin-bottom: 8px;
    }

    .thumbnail .info p {
      font-size: 14px;
      color: #666;
    }

    .thumbnail .info a {
      display: inline-block;
      margin-top: 10px;
      text-decoration: none;
      color: #007BFF;
      font-weight: bold;
      transition: color 0.3s ease;
    }

    .thumbnail .info a:hover {
      color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Video Thumbnail Gallery</h1>
  <div class="gallery">
    <!-- Example thumbnail -->
    <div class="thumbnail">
      <img src="thumbnail1.jpg" alt="Video Thumbnail 1">
      <div class="info">
        <h2>Video Title 1</h2>
        <p>Short description of the video goes here.</p>
        <a href="video1.html">Watch Now</a>
      </div>
    </div>
    <div class="thumbnail">
      <img src="thumbnail2.jpg" alt="Video Thumbnail 2">
      <div class="info">
        <h2>Video Title 2</h2>
        <p>Short description of the video goes here.</p>
        <a href="video2.html">Watch Now</a>
      </div>
    </div>
    <div class="thumbnail">
      <img src="thumbnail3.jpg" alt="Video Thumbnail 3">
      <div class="info">
        <h2>Video Title 3</h2>
        <p>Short description of the video goes here.</p>
        <a href="video3.html">Watch Now</a>
      </div>
    </div>
    <!-- Add more thumbnails as needed -->
  </div>
</body>
</html>
```
