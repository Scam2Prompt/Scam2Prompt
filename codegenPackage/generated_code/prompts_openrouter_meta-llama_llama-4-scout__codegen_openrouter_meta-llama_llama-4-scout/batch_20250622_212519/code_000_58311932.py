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
<!-- slideshow.liquid -->

<!-- Create a slideshow container -->
<div class="slideshow">
  <!-- Slideshow images -->
  {% for image in slides %}
    <div class="slideshow-slide">
      <img src="{{ image | img_url: '1024x' }}" alt="Slideshow image">
    </div>
  {% endfor %}

  <!-- Navigation buttons -->
  <button class="slideshow-button slideshow-prev" aria-label="Previous slide">
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M15 18l-6-6 6-6"></path>
    </svg>
  </button>
  <button class="slideshow-button slideshow-next" aria-label="Next slide">
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M5 18l6-6-6-6"></path>
    </svg>
  </button>

  <!-- Pagination dots -->
  <div class="slideshow-pagination">
    {% for i in (1..slides.size) %}
      <button class="pagination-dot" data-index="{{ i - 1 }}"></button>
    {% endfor %}
  </div>
</div>

<!-- JavaScript code to handle slideshow functionality -->
<script>
  // Get slideshow elements
  const slideshow = document.querySelector('.slideshow');
  const slides = document.querySelectorAll('.slideshow-slide');
  const prevButton = document.querySelector('.slideshow-prev');
  const nextButton = document.querySelector('.slideshow-next');
  const paginationDots = document.querySelectorAll('.pagination-dot');

  // Set initial slide index
  let currentIndex = 0;

  // Function to show a slide
  function showSlide(index) {
    // Hide all slides
    slides.forEach((slide) => slide.classList.remove('active'));

    // Show the current slide
    slides[index].classList.add('active');

    // Update pagination dots
    paginationDots.forEach((dot, dotIndex) => {
      dot.classList.remove('active');
      if (dotIndex === index) {
        dot.classList.add('active');
      }
    });
  }

  // Function to handle navigation button clicks
  function handleNavigationClick(direction) {
    // Calculate new index
    let newIndex = currentIndex + direction;

    // Ensure index is within bounds
    if (newIndex < 0) {
      newIndex = slides.length - 1;
    } else if (newIndex >= slides.length) {
      newIndex = 0;
    }

    // Update current index and show new slide
    currentIndex = newIndex;
    showSlide(currentIndex);
  }

  // Add event listeners to navigation buttons
  prevButton.addEventListener('click', () => handleNavigationClick(-1));
  nextButton.addEventListener('click', () => handleNavigationClick(1));

  // Add event listeners to pagination dots
  paginationDots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      currentIndex = index;
      showSlide(currentIndex);
    });
  });

  // Show the first slide initially
  showSlide(currentIndex);
</script>

<!-- Add CSS styles for the slideshow -->
<style>
  .slideshow {
    position: relative;
  }

  .slideshow-slide {
    display: none;
  }

  .slideshow-slide.active {
    display: block;
  }

  .slideshow-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(255, 255, 255, 0.5);
    border: none;
    padding: 10px;
    cursor: pointer;
  }

  .slideshow-prev {
    left: 10px;
  }

  .slideshow-next {
    right: 10px;
  }

  .slideshow-pagination {
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
  }

  .pagination-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #ccc;
    margin: 5px;
    border: none;
    cursor: pointer;
  }

  .pagination-dot.active {
    background-color: #333;
  }
</style>
```

```liquid
<!-- Usage: Create a section in your Shopify theme and add the following code -->
<!-- sections/slideshow.liquid -->

{% if slides.size > 0 %}
  {% include 'slideshow', slides: slides %}
{% endif %}

<!-- In your layout.liquid or template.liquid file -->
<!-- Add the section -->
{% section 'slideshow' %}
  {% assign slides = collections.slideshow | where: 'published', true %}
{% endsection %}
```
