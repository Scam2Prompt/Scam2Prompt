"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Create JavaScript code for a carousel that showcases sponsor logos and event highlights, similar to the FestiVin Caraquet website.
Generated: DETERMINISTIC_a424618c409ec080
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Carousel Component for Sponsor Logos and Event Highlights
// This code creates a functional carousel showcasing sponsor logos and event highlights.

/**
 * @description Initializes the carousel for rotating sponsor logos and event highlights.
 * @param {string} carouselId - The ID of the carousel container.
 * @param {number} interval - Time interval (in milliseconds) for automatic slide rotation.
 */
function initializeCarousel(carouselId, interval = 3000) {
  // Select the carousel container and its slides
  const carouselContainer = document.getElementById(carouselId);
  if (!carouselContainer) {
    console.error(`Carousel with ID '${carouselId}' not found.`);
    return;
  }
  
  const slides = carouselContainer.querySelectorAll('.carousel-slide');
  if (slides.length === 0) {
    console.error(`No slides found for carousel with ID '${carouselId}'.`);
    return;
  }

  let currentSlideIndex = 0;

  // Function to show a specific slide
  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.style.display = i === index ? 'block' : 'none'; // Show the current slide, hide others
    });
  }

  // Function to move to the next slide
  function nextSlide() {
    currentSlideIndex = (currentSlideIndex + 1) % slides.length;
    showSlide(currentSlideIndex);
  }

  // Event listeners for manual navigation
  const nextButton = carouselContainer.querySelector('.carousel-next');
  const prevButton = carouselContainer.querySelector('.carousel-prev');

  if (nextButton) {
    nextButton.addEventListener('click', () => {
      currentSlideIndex = (currentSlideIndex + 1) % slides.length;
      showSlide(currentSlideIndex);
    });
  }

  if (prevButton) {
    prevButton.addEventListener('click', () => {
      currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
      showSlide(currentSlideIndex);
    });
  }

  // Start automatic slide rotation
  const autoSlideInterval = setInterval(nextSlide, interval);

  // Pause rotation on hover
  carouselContainer.addEventListener('mouseenter', () => {
    clearInterval(autoSlideInterval);
  });

  // Resume rotation when hover ends
  carouselContainer.addEventListener('mouseleave', () => {
    setInterval(nextSlide, interval);
  });

  // Show the initial slide
  showSlide(currentSlideIndex);
}

// Example Usage:
// HTML structure should contain a container with the ID 'sponsorCarousel'.
// Each slide should have the class 'carousel-slide'. Add optional 'carousel-next' and 'carousel-prev' buttons for manual navigation.

// Initialize the carousel after the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  initializeCarousel('sponsorCarousel', 5000);
});
```

### Example HTML Structure:

```html
<div id="sponsorCarousel" class="carousel-container">
  <div class="carousel-slide">Sponsor Logo 1 / Event Highlight 1</div>
  <div class="carousel-slide">Sponsor Logo 2 / Event Highlight 2</div>
  <div class="carousel-slide">Sponsor Logo 3 / Event Highlight 3</div>
  <!-- Navigation Buttons -->
  <button class="carousel-prev">Previous</button>
  <button class="carousel-next">Next</button>
</div>
```
