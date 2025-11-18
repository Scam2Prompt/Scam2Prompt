"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Write JavaScript code to create a dynamic testimonial slider for a webpage, showcasing user experiences with products like "Colágeno Hidrolizado CH+H" and "Pro Adulto," as seen on Familia Previlife.
Generated: DETERMINISTIC_6c6619ae679cf75b
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Testimonial Slider for a Webpage
 *
 * This JavaScript code creates a dynamic testimonial slider showcasing user experiences.
 * Products featured: "Colágeno Hidrolizado CH+H" and "Pro Adulto".
 * The slider automatically cycles through testimonials and provides navigation controls.
 */

// Define testimonials data
const testimonials = [
  {
    name: "Maria Garcia",
    product: "Colágeno Hidrolizado CH+H",
    feedback: "This product has greatly improved my joint health. Highly recommend it!",
    image: "images/maria.jpg"
  },
  {
    name: "John Smith",
    product: "Pro Adulto",
    feedback: "Pro Adulto is a game-changer for my daily energy and focus.",
    image: "images/john.jpg"
  },
  {
    name: "Sofia Alvarez",
    product: "Colágeno Hidrolizado CH+H",
    feedback: "My skin looks healthier and more radiant thanks to this amazing product!",
    image: "images/sofia.jpg"
  }
];

// Select DOM elements
const sliderContainer = document.querySelector(".testimonial-slider");
const testimonialName = document.querySelector(".testimonial-name");
const testimonialProduct = document.querySelector(".testimonial-product");
const testimonialFeedback = document.querySelector(".testimonial-feedback");
const testimonialImage = document.querySelector(".testimonial-image");
const prevButton = document.querySelector(".slider-prev");
const nextButton = document.querySelector(".slider-next");

// Initialize slider state
let currentIndex = 0;

/**
 * Function to update the slider content
 */
function updateSlider(index) {
  try {
    // Validate index bounds
    if (index < 0 || index >= testimonials.length) {
      throw new Error("Index out of bounds");
    }

    // Update slider content with the current testimonial
    const testimonial = testimonials[index];
    testimonialName.textContent = testimonial.name;
    testimonialProduct.textContent = testimonial.product;
    testimonialFeedback.textContent = testimonial.feedback;
    testimonialImage.src = testimonial.image;
  } catch (error) {
    console.error("Error updating slider:", error.message);
  }
}

/**
 * Function to navigate to the next testimonial
 */
function nextTestimonial() {
  currentIndex = (currentIndex + 1) % testimonials.length; // Loop back to start when reaching the end
  updateSlider(currentIndex);
}

/**
 * Function to navigate to the previous testimonial
 */
function prevTestimonial() {
  currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length; // Loop back to end when reaching the start
  updateSlider(currentIndex);
}

// Attach event listeners to navigation buttons
nextButton.addEventListener("click", nextTestimonial);
prevButton.addEventListener("click", prevTestimonial);

// Initialize slider with the first testimonial
updateSlider(currentIndex);

/**
 * Optional: Auto-slide functionality
 */
let autoSlideInterval = setInterval(nextTestimonial, 5000); // Change testimonials every 5 seconds

/**
 * Pause auto-slide on hover
 */
sliderContainer.addEventListener("mouseover", () => {
  clearInterval(autoSlideInterval);
});

/**
 * Resume auto-slide when hover ends
 */
sliderContainer.addEventListener("mouseout", () => {
  autoSlideInterval = setInterval(nextTestimonial, 5000);
});
```

### HTML Structure (for reference, not part of the request):
```html
<div class="testimonial-slider">
  <button class="slider-prev">Previous</button>
  <div class="testimonial-content">
    <img class="testimonial-image" src="" alt="User Image">
    <h3 class="testimonial-name"></h3>
    <h4 class="testimonial-product"></h4>
    <p class="testimonial-feedback"></p>
  </div>
  <button class="slider-next">Next</button>
</div>
```

### CSS (for styling, optional):
```css
.testimonial-slider {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}

.testimonial-content {
  text-align: center;
}

.testimonial-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.slider-prev,
.slider-next {
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
}
```

Above code ensures dynamic behavior, proper error handling, and easy integration into a webpage.
