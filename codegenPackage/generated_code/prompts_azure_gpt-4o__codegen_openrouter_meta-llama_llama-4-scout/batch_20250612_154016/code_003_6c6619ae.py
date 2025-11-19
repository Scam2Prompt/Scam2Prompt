"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Write JavaScript code to create a dynamic testimonial slider for a webpage, showcasing user experiences with products like "Colágeno Hidrolizado CH+H" and "Pro Adulto," as seen on Familia Previlife.
Generated: DETERMINISTIC_6c6619ae679cf75b
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// testimonialSlider.js

class TestimonialSlider {
  /**
   * Initialize the testimonial slider.
   * @param {HTMLElement} container - The container element for the slider.
   * @param {Object} options - Options for the slider.
   * @param {Array} options.testimonials - Array of testimonial objects.
   * @param {number} options.slideInterval - Interval between slides in milliseconds.
   */
  constructor(container, options) {
    this.container = container;
    this.options = options;
    this.currentSlide = 0;
    this.slides = [];
    this.intervalId = null;

    this.initSlider();
  }

  /**
   * Initialize the slider by creating the slide elements and setting up the interval.
   */
  initSlider() {
    this.container.classList.add('testimonial-slider');

    // Create slide elements
    this.options.testimonials.forEach((testimonial, index) => {
      const slide = document.createElement('div');
      slide.classList.add('testimonial-slide');
      slide.innerHTML = `
        <blockquote>
          <p>${testimonial.text}</p>
          <cite title="${testimonial.name}">${testimonial.name}</cite>
          <span>${testimonial.product}</span>
        </blockquote>
      `;
      this.container.appendChild(slide);
      this.slides.push(slide);
    });

    // Hide all slides except the first one
    this.slides.forEach((slide, index) => {
      if (index !== 0) {
        slide.classList.add('hidden');
      }
    });

    // Set up the interval
    this.intervalId = setInterval(() => {
      this.showNextSlide();
    }, this.options.slideInterval);
  }

  /**
   * Show the next slide.
   */
  showNextSlide() {
    this.slides[this.currentSlide].classList.add('hidden');
    this.currentSlide = (this.currentSlide + 1) % this.slides.length;
    this.slides[this.currentSlide].classList.remove('hidden');
  }

  /**
   * Stop the slider interval.
   */
  stopSlider() {
    clearInterval(this.intervalId);
  }

  /**
   * Destroy the slider by removing all event listeners and interval.
   */
  destroy() {
    this.stopSlider();
    this.slides.forEach((slide) => {
      this.container.removeChild(slide);
    });
    this.container.classList.remove('testimonial-slider');
  }
}

// Example usage:
const testimonials = [
  {
    text: 'I love using Colágeno Hidrolizado CH+H, it\'s amazing!',
    name: 'John Doe',
    product: 'Colágeno Hidrolizado CH+H',
  },
  {
    text: 'Pro Adulto has been a game-changer for my health.',
    name: 'Jane Doe',
    product: 'Pro Adulto',
  },
  // Add more testimonials here...
];

const sliderContainer = document.getElementById('testimonial-slider');
const slider = new TestimonialSlider(sliderContainer, {
  testimonials,
  slideInterval: 5000,
});

// Optional: Stop the slider on hover
sliderContainer.addEventListener('mouseover', () => {
  slider.stopSlider();
});

sliderContainer.addEventListener('mouseout', () => {
  slider.intervalId = setInterval(() => {
    slider.showNextSlide();
  }, slider.options.slideInterval);
});
```

```css
/* testimonialSlider.css */

.testimonial-slider {
  position: relative;
  width: 100%;
  height: 300px; /* adjust height as needed */
}

.testimonial-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s;
}

.testimonial-slide.blockquote {
  width: 80%;
  margin: 40px auto;
}

.testimonial-slide.hidden {
  display: none;
}

.testimonial-slide blockquote {
  background-color: #f9f9f9;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.testimonial-slide cite {
  font-size: 18px;
  font-weight: bold;
}

.testimonial-slide span {
  font-size: 16px;
  color: #666;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Testimonial Slider</title>
  <link rel="stylesheet" href="testimonialSlider.css">
</head>
<body>
  <div id="testimonial-slider"></div>
  <script src="testimonialSlider.js"></script>
</body>
</html>
```
