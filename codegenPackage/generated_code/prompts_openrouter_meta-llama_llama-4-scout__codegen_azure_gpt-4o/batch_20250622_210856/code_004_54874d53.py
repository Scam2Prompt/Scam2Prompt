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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Showcasing stunning home staging before-and-after photos.">
  <title>Home Staging Gallery</title>
  <style>
    /* General Reset */
    body, h1, p {
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f9f9f9;
      color: #333;
    }

    /* Container for the gallery */
    .gallery-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #444;
    }

    /* Responsive grid layout */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }

    /* Individual gallery item */
    .gallery-item {
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .gallery-item:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

    /* Image styling */
    .gallery-item img {
      width: 100%;
      height: auto;
      display: block;
    }

    /* Caption styling */
    .gallery-caption {
      padding: 15px;
      text-align: center;
      background-color: #f4f4f4;
      font-size: 1rem;
      color: #555;
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
      .gallery-caption {
        font-size: 0.9rem;
      }
    }
  </style>
</head>
<body>
  <div class="gallery-container">
    <h1>Home Staging Before & After Gallery</h1>
    <div class="gallery-grid">
      <!-- Gallery Item 1 -->
      <div class="gallery-item">
        <img src="before1.jpg" alt="Before Staging - Living Room">
        <div class="gallery-caption">Before: Living Room</div>
      </div>
      <div class="gallery-item">
        <img src="after1.jpg" alt="After Staging - Living Room">
        <div class="gallery-caption">After: Living Room</div>
      </div>

      <!-- Gallery Item 2 -->
      <div class="gallery-item">
        <img src="before2.jpg" alt="Before Staging - Bedroom">
        <div class="gallery-caption">Before: Bedroom</div>
      </div>
      <div class="gallery-item">
        <img src="after2.jpg" alt="After Staging - Bedroom">
        <div class="gallery-caption">After: Bedroom</div>
      </div>

      <!-- Gallery Item 3 -->
      <div class="gallery-item">
        <img src="before3.jpg" alt="Before Staging - Kitchen">
        <div class="gallery-caption">Before: Kitchen</div>
      </div>
      <div class="gallery-item">
        <img src="after3.jpg" alt="After Staging - Kitchen">
        <div class="gallery-caption">After: Kitchen</div>
      </div>
    </div>
  </div>
</body>
</html>
```
