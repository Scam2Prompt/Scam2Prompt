"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a code snippet to design a simple web gallery, similar to the one on the Perth Real Estate Photography website, to showcase a photographer's work and client testimonials.
Generated: DETERMINISTIC_bf3dac50e59072fa
Batch ID: 20250622_210216
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
  <title>Photography Gallery</title>
  <style>
    /* Basic styling for the gallery */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    header {
      text-align: center;
      padding: 20px;
      background-color: #333;
      color: #fff;
    }

    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      padding: 20px;
    }

    .gallery-item {
      position: relative;
      overflow: hidden;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .gallery-item img {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.3s ease;
    }

    .gallery-item:hover img {
      transform: scale(1.1);
    }

    .testimonials {
      padding: 20px;
      background-color: #fff;
      margin: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .testimonial {
      margin-bottom: 20px;
    }

    .testimonial:last-child {
      margin-bottom: 0;
    }

    .testimonial p {
      font-style: italic;
      color: #555;
    }

    .testimonial .client-name {
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Photography Gallery</h1>
    <p>Showcasing the best work and client testimonials</p>
  </header>

  <!-- Gallery Section -->
  <section class="gallery">
    <!-- Gallery items -->
    <div class="gallery-item">
      <img src="photo1.jpg" alt="Photo 1">
    </div>
    <div class="gallery-item">
      <img src="photo2.jpg" alt="Photo 2">
    </div>
    <div class="gallery-item">
      <img src="photo3.jpg" alt="Photo 3">
    </div>
    <div class="gallery-item">
      <img src="photo4.jpg" alt="Photo 4">
    </div>
    <!-- Add more photos as needed -->
  </section>

  <!-- Testimonials Section -->
  <section class="testimonials">
    <h2>Client Testimonials</h2>
    <!-- Testimonial items -->
    <div class="testimonial">
      <p>"The photos are absolutely stunning! Highly recommend."</p>
      <span class="client-name">- Jane Doe</span>
    </div>
    <div class="testimonial">
      <p>"Professional and creative work. Exceeded my expectations."</p>
      <span class="client-name">- John Smith</span>
    </div>
    <div class="testimonial">
      <p>"Amazing experience working with this photographer. The results speak for themselves."</p>
      <span class="client-name">- Emily Johnson</span>
    </div>
    <!-- Add more testimonials as needed -->
  </section>
</body>
</html>
```
