"""
Generated Code Metadata:
========================
Original URL: https://aromaterapiasalud.cl
Prompt: Generate a JavaScript code snippet to implement a product carousel or slideshow, similar to the one showcasing essential oils and diffusers on aromaterapiasalud.cl.
Generated: DETERMINISTIC_37ab9fad88a1592f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Carousel Implementation
// This code creates a simple, responsive product carousel/slideshow using JavaScript and CSS.
// Ensure you have a container with the appropriate HTML structure for this code to work.

// HTML Structure Example:
// <div id="product-carousel" class="carousel">
//   <div class="carousel-track">
//     <div class="carousel-item">Item 1</div>
//     <div class="carousel-item">Item 2</div>
//     <div class="carousel-item">Item 3</div>
//     <!-- Add more items as needed -->
//   </div>
//   <button class="carousel-button prev">❮</button>
//   <button class="carousel-button next">❯</button>
// </div>

document.addEventListener("DOMContentLoaded", () => {
  // Select carousel elements
  const carousel = document.getElementById("product-carousel");
  const track = carousel.querySelector(".carousel-track");
  const items = Array.from(track.children);
  const prevButton = carousel.querySelector(".carousel-button.prev");
  const nextButton = carousel.querySelector(".carousel-button.next");

  // Get item width dynamically
  const itemWidth = items[0].getBoundingClientRect().width;

  // Arrange items side by side
  items.forEach((item, index) => {
    item.style.left = `${itemWidth * index}px`;
  });

  // Track the current slide index
  let currentIndex = 0;

  // Function to update the carousel position
  const updateCarouselPosition = () => {
    const newPosition = -currentIndex * itemWidth;
    track.style.transform = `translateX(${newPosition}px)`;
  };

  // Event listener for the "Next" button
  nextButton.addEventListener("click", () => {
    if (currentIndex < items.length - 1) {
      currentIndex++;
      updateCarouselPosition();
    }
  });

  // Event listener for the "Previous" button
  prevButton.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarouselPosition();
    }
  });

  // Optional: Add keyboard navigation for accessibility
  document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
      if (currentIndex < items.length - 1) {
        currentIndex++;
        updateCarouselPosition();
      }
    } else if (event.key === "ArrowLeft") {
      if (currentIndex > 0) {
        currentIndex--;
        updateCarouselPosition();
      }
    }
  });

  // Optional: Add responsive behavior
  window.addEventListener("resize", () => {
    const newItemWidth = items[0].getBoundingClientRect().width;
    items.forEach((item, index) => {
      item.style.left = `${newItemWidth * index}px`;
    });
    updateCarouselPosition();
  });
});

// CSS (Add this to your stylesheet for styling)
/*
.carousel {
  position: relative;
  overflow: hidden;
  width: 100%;
}

.carousel-track {
  display: flex;
  transition: transform 0.3s ease-in-out;
}

.carousel-item {
  min-width: 100%;
  box-sizing: border-box;
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  cursor: pointer;
  padding: 10px;
  z-index: 1;
}

.carousel-button.prev {
  left: 10px;
}

.carousel-button.next {
  right: 10px;
}
*/
```
