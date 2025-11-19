"""
Generated Code Metadata:
========================
Original URL: https://zellerscanada.ca
Prompt: Write a Shopify code snippet to create a slideshow with navigation buttons, similar to the one on the Zellers Canada website.
Generated: DETERMINISTIC_583119328c056d3d
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```liquid
<!-- Shopify Slideshow Code -->
<!-- This code creates a slideshow with navigation buttons -->

<div class="slideshow-container">
  <!-- Loop through the images in the slideshow section -->
  {% for slide in section.settings.slides %}
  <div class="slide {% if forloop.first %}active{% endif %}" id="slide-{{ forloop.index }}">
    <img src="{{ slide.image | img_url: 'master' }}" alt="{{ slide.alt_text }}" class="slide-image">
    <div class="slide-caption">
      <h2>{{ slide.title }}</h2>
      <p>{{ slide.description }}</p>
    </div>
  </div>
  {% endfor %}

  <!-- Navigation Buttons -->
  <button class="prev" onclick="changeSlide(-1)">&#10094;</button>
  <button class="next" onclick="changeSlide(1)">&#10095;</button>
</div>

<!-- Slideshow Styles -->
<style>
  .slideshow-container {
    position: relative;
    max-width: 100%;
    margin: auto;
    overflow: hidden;
  }

  .slide {
    display: none;
    position: relative;
    text-align: center;
  }

  .slide.active {
    display: block;
  }

  .slide-image {
    width: 100%;
    height: auto;
  }

  .slide-caption {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    color: #fff;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 10px;
    border-radius: 5px;
  }

  .prev, .next {
    cursor: pointer;
    position: absolute;
    top: 50%;
    width: auto;
    margin-top: -22px;
    padding: 16px;
    color: white;
    font-weight: bold;
    font-size: 18px;
    border: none;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 50%;
    user-select: none;
    z-index: 10;
  }

  .prev {
    left: 10px;
  }

  .next {
    right: 10px;
  }

  .prev:hover, .next:hover {
    background-color: rgba(0, 0, 0, 0.8);
  }
</style>

<!-- Slideshow JavaScript -->
<script>
  let currentSlideIndex = 0;

  // Function to change slides
  function changeSlide(direction) {
    const slides = document.querySelectorAll('.slide');
    slides[currentSlideIndex].classList.remove('active');
    currentSlideIndex = (currentSlideIndex + direction + slides.length) % slides.length;
    slides[currentSlideIndex].classList.add('active');
  }

  // Initialize the slideshow
  document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    if (slides.length > 0) {
      slides[0].classList.add('active');
    }
  });
</script>
```

This code snippet is designed to be added to a Shopify theme's section or template file. Ensure that the `section.settings.slides` contains the necessary image data and metadata for the slideshow.
