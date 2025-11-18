"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate code in JavaScript to create a gallery slider for showcasing residential and commercial property photos, inspired by the layout used on Perth Real Estate Photography's website.
Generated: DETERMINISTIC_81ce1f53e53b1c88
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Gallery Slider for showcasing property photos

// HTML Structure
// <div id="gallery-slider" class="slider">
//   <div class="slider-track">
//     <!-- Images will be dynamically injected here -->
//   </div>
//   <button id="prev-btn" class="slider-btn">Prev</button>
//   <button id="next-btn" class="slider-btn">Next</button>
// </div>

// CSS (Ensure this is included in your stylesheet)
// .slider {
//   position: relative;
//   overflow: hidden;
//   width: 100%;
//   max-width: 800px;
//   margin: auto;
// }
// .slider-track {
//   display: flex;
//   transition: transform 0.5s ease;
// }
// .slider-btn {
//   position: absolute;
//   top: 50%;
//   transform: translateY(-50%);
//   background-color: rgba(0, 0, 0, 0.5);
//   color: #fff;
//   border: none;
//   padding: 10px;
//   cursor: pointer;
// }
// #prev-btn {
//   left: 10px;
// }
// #next-btn {
//   right: 10px;
// }
// .slider img {
//   width: 100%;
//   max-width: 100%;
//   pointer-events: none;
// }

// JavaScript Code
document.addEventListener('DOMContentLoaded', () => {
  // Configuration
  const imageUrls = [
    // Replace with the actual image URLs for your gallery
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg',
  ];
  const sliderTrack = document.querySelector('.slider-track');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  let currentIndex = 0;

  // Function to initialize the slider
  const initializeSlider = () => {
    imageUrls.forEach((url) => {
      const img = document.createElement('img');
      img.src = url;
      img.alt = 'Property Image';
      sliderTrack.appendChild(img);
    });
    updateSlider();
  };

  // Function to update the slider position
  const updateSlider = () => {
    const sliderWidth = sliderTrack.parentElement.offsetWidth;
    sliderTrack.style.transform = `translateX(-${currentIndex * sliderWidth}px)`;
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex === imageUrls.length - 1;
  };

  // Event Listeners for navigation buttons
  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateSlider();
    }
  });

  nextBtn.addEventListener('click', () => {
    if (currentIndex < imageUrls.length - 1) {
      currentIndex++;
      updateSlider();
    }
  });

  // Handle window resize to recalculate slider width
  window.addEventListener('resize', updateSlider);

  // Initialize the slider
  initializeSlider();
});
```
