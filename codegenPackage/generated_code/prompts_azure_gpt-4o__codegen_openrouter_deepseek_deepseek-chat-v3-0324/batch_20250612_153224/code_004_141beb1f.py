"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write JavaScript code to implement a carousel showcasing project highlights, such as those featured by Naikreatif for their clients.
Generated: DETERMINISTIC_141beb1ffc836690
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Carousel component for showcasing project highlights.
 * Features:
 * - Auto-rotation with pause on hover
 * - Navigation dots and arrows
 * - Responsive design
 * - Smooth transitions
 */
class ProjectCarousel {
  /**
   * Initialize the carousel
   * @param {HTMLElement} container - The carousel container element
   * @param {Object} options - Configuration options
   */
  constructor(container, options = {}) {
    if (!container) {
      throw new Error('Carousel container element is required');
    }

    // Default options
    const defaults = {
      autoRotate: true,
      interval: 5000,
      transitionDuration: 500,
      pauseOnHover: true,
      showDots: true,
      showArrows: true
    };

    this.options = { ...defaults, ...options };
    this.container = container;
    this.slides = Array.from(container.querySelectorAll('.carousel-slide'));
    this.currentIndex = 0;
    this.intervalId = null;
    this.isTransitioning = false;

    if (this.slides.length === 0) {
      throw new Error('No slides found in carousel container');
    }

    this.init();
  }

  /**
   * Initialize carousel elements and events
   */
  init() {
    // Create carousel structure
    this.createCarouselStructure();
    
    // Set initial active slide
    this.goToSlide(this.currentIndex, false);
    
    // Start auto rotation if enabled
    if (this.options.autoRotate) {
      this.startAutoRotation();
    }

    // Add event listeners
    this.addEventListeners();
  }

  /**
   * Create necessary carousel DOM elements
   */
  createCarouselStructure() {
    // Add carousel class
    this.container.classList.add('carousel-container');

    // Create track element
    this.track = document.createElement('div');
    this.track.className = 'carousel-track';
    this.track.style.transitionDuration = `${this.options.transitionDuration}ms`;
    
    // Wrap slides in track
    this.slides.forEach(slide => {
      slide.classList.add('carousel-slide');
      this.track.appendChild(slide);
    });

    // Clear container and add track
    this.container.innerHTML = '';
    this.container.appendChild(this.track);

    // Create navigation dots if enabled
    if (this.options.showDots) {
      this.dotsContainer = document.createElement('div');
      this.dotsContainer.className = 'carousel-dots';
      
      this.slides.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.className = 'carousel-dot';
        dot.dataset.index = index;
        dot.addEventListener('click', () => this.goToSlide(index));
        this.dotsContainer.appendChild(dot);
      });
      
      this.container.appendChild(this.dotsContainer);
    }

    // Create navigation arrows if enabled
    if (this.options.showArrows) {
      this.prevButton = document.createElement('button');
      this.prevButton.className = 'carousel-arrow carousel-arrow--prev';
      this.prevButton.innerHTML = '&lsaquo;';
      this.prevButton.addEventListener('click', () => this.prevSlide());
      
      this.nextButton = document.createElement('button');
      this.nextButton.className = 'carousel-arrow carousel-arrow--next';
      this.nextButton.innerHTML = '&rsaquo;';
      this.nextButton.addEventListener('click', () => this.nextSlide());
      
      this.container.appendChild(this.prevButton);
      this.container.appendChild(this.nextButton);
    }
  }

  /**
   * Add event listeners
   */
  addEventListeners() {
    if (this.options.pauseOnHover) {
      this.container.addEventListener('mouseenter', () => this.pauseAutoRotation());
      this.container.addEventListener('mouseleave', () => this.startAutoRotation());
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (document.activeElement === this.container || this.container.contains(document.activeElement)) {
        if (e.key === 'ArrowLeft') {
          this.prevSlide();
        } else if (e.key === 'ArrowRight') {
          this.nextSlide();
        }
      }
    });
  }

  /**
   * Go to specific slide
   * @param {number} index - Slide index to go to
   * @param {boolean} animate - Whether to animate the transition
   */
  goToSlide(index, animate = true) {
    if (this.isTransitioning || index === this.currentIndex) return;
    
    // Handle wrap-around for infinite effect
    if (index < 0) {
      index = this.slides.length - 1;
    } else if (index >= this.slides.length) {
      index = 0;
    }

    this.isTransitioning = true;
    this.currentIndex = index;

    // Update track position
    this.track.style.transitionProperty = animate ? 'transform' : 'none';
    this.track.style.transform = `translateX(-${this.currentIndex * 100}%)`;

    // Update active dot
    if (this.options.showDots) {
      const dots = this.dotsContainer.querySelectorAll('.carousel-dot');
      dots.forEach(dot => dot.classList.remove('active'));
      dots[this.currentIndex].classList.add('active');
    }

    // Reset transitioning flag after animation completes
    this.track.addEventListener('transitionend', () => {
      this.isTransitioning = false;
    }, { once: true });
  }

  /**
   * Go to next slide
   */
  nextSlide() {
    this.goToSlide(this.currentIndex + 1);
  }

  /**
   * Go to previous slide
   */
  prevSlide() {
    this.goToSlide(this.currentIndex - 1);
  }

  /**
   * Start auto rotation
   */
  startAutoRotation() {
    if (!this.options.autoRotate || this.intervalId) return;
    
    this.intervalId = setInterval(() => {
      this.nextSlide();
    }, this.options.interval);
  }

  /**
   * Pause auto rotation
   */
  pauseAutoRotation() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  /**
   * Destroy carousel instance and clean up
   */
  destroy() {
    this.pauseAutoRotation();
    
    // Remove event listeners
    this.container.removeEventListener('mouseenter', this.pauseAutoRotation);
    this.container.removeEventListener('mouseleave', this.startAutoRotation);
    
    if (this.prevButton) {
      this.prevButton.removeEventListener('click', this.prevSlide);
    }
    
    if (this.nextButton) {
      this.nextButton.removeEventListener('click', this.nextSlide);
    }
    
    if (this.dotsContainer) {
      const dots = this.dotsContainer.querySelectorAll('.carousel-dot');
      dots.forEach(dot => dot.removeEventListener('click', this.goToSlide));
    }
    
    // Remove custom DOM elements
    if (this.dotsContainer) this.dotsContainer.remove();
    if (this.prevButton) this.prevButton.remove();
    if (this.nextButton) this.nextButton.remove();
    
    // Reset container to original state
    this.container.innerHTML = '';
    this.slides.forEach(slide => {
      slide.classList.remove('carousel-slide');
      this.container.appendChild(slide);
    });
    
    this.container.classList.remove('carousel-container');
  }
}

// CSS styles for the carousel (should be added to your stylesheet)
const carouselStyles = `
.carousel-container {
  position: relative;
  overflow: hidden;
  width: 100%;
}

.carousel-track {
  display: flex;
  transition: transform 0.5s ease;
  height: 100%;
}

.carousel-slide {
  min-width: 100%;
  height: 100%;
}

.carousel-dots {
  display: flex;
  justify-content: center;
  padding: 10px 0;
}

.carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #ccc;
  border: none;
  margin: 0 5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.carousel-dot.active {
  background: #333;
}

.carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 20px;
  cursor: pointer;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-arrow--prev {
  left: 15px;
}

.carousel-arrow--next {
  right: 15px;
}

.carousel-arrow:hover {
  background: rgba(0, 0, 0, 0.8);
}
`;

// Add styles to the document
const styleElement = document
