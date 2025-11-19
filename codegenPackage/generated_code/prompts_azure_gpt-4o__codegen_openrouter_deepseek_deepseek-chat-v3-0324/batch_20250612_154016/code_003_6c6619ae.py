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
/**
 * Testimonial Slider for Familia Previlife Products
 * Features:
 * - Dynamic testimonial slides
 * - Auto-rotation with pause on hover
 * - Responsive design
 * - Keyboard navigation support
 * - Accessible ARIA attributes
 */

class TestimonialSlider {
  constructor(containerId, options = {}) {
    // Default settings
    const defaults = {
      slideInterval: 5000,
      animationSpeed: 500,
      pauseOnHover: true,
      showControls: true,
      showIndicators: true
    };

    this.settings = { ...defaults, ...options };
    this.container = document.getElementById(containerId);
    this.slides = [];
    this.currentIndex = 0;
    this.timer = null;
    this.isPaused = false;

    if (!this.container) {
      console.error(`TestimonialSlider: Container with ID "${containerId}" not found.`);
      return;
    }

    this.init();
  }

  init() {
    this.cacheElements();
    this.setupEventListeners();
    this.updateAriaAttributes();
    this.startAutoRotation();
  }

  cacheElements() {
    this.slides = Array.from(this.container.querySelectorAll('.testimonial-slide'));
    this.prevBtn = this.container.querySelector('.testimonial-prev');
    this.nextBtn = this.container.querySelector('.testimonial-next');
    this.indicatorsContainer = this.container.querySelector('.testimonial-indicators');
    
    if (this.settings.showIndicators && !this.indicatorsContainer) {
      this.createIndicators();
    }
  }

  createIndicators() {
    this.indicatorsContainer = document.createElement('div');
    this.indicatorsContainer.className = 'testimonial-indicators';
    this.container.appendChild(this.indicatorsContainer);

    this.slides.forEach((slide, index) => {
      const indicator = document.createElement('button');
      indicator.className = 'testimonial-indicator';
      indicator.setAttribute('aria-label', `Go to testimonial ${index + 1}`);
      indicator.addEventListener('click', () => this.goToSlide(index));
      
      if (index === 0) {
        indicator.classList.add('active');
      }
      
      this.indicatorsContainer.appendChild(indicator);
    });
  }

  setupEventListeners() {
    if (this.settings.showControls) {
      if (this.prevBtn) {
        this.prevBtn.addEventListener('click', () => this.prevSlide());
      }
      if (this.nextBtn) {
        this.nextBtn.addEventListener('click', () => this.nextSlide());
      }
    }

    if (this.settings.pauseOnHover) {
      this.container.addEventListener('mouseenter', () => this.pauseAutoRotation());
      this.container.addEventListener('mouseleave', () => this.resumeAutoRotation());
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        this.prevSlide();
      } else if (e.key === 'ArrowRight') {
        this.nextSlide();
      }
    });
  }

  updateAriaAttributes() {
    this.slides.forEach((slide, index) => {
      slide.setAttribute('aria-hidden', index !== this.currentIndex);
      slide.setAttribute('tabindex', index === this.currentIndex ? '0' : '-1');
    });

    if (this.indicatorsContainer) {
      const indicators = this.indicatorsContainer.querySelectorAll('.testimonial-indicator');
      indicators.forEach((indicator, index) => {
        indicator.setAttribute('aria-selected', index === this.currentIndex);
      });
    }
  }

  goToSlide(index) {
    if (index < 0 || index >= this.slides.length || index === this.currentIndex) {
      return;
    }

    // Hide current slide
    this.slides[this.currentIndex].classList.remove('active');
    if (this.indicatorsContainer) {
      const indicators = this.indicatorsContainer.querySelectorAll('.testimonial-indicator');
      indicators[this.currentIndex].classList.remove('active');
    }

    // Update index and show new slide
    this.currentIndex = index;
    this.slides[this.currentIndex].classList.add('active');
    
    if (this.indicatorsContainer) {
      const indicators = this.indicatorsContainer.querySelectorAll('.testimonial-indicator');
      indicators[this.currentIndex].classList.add('active');
    }

    this.updateAriaAttributes();
    this.resetAutoRotation();
  }

  nextSlide() {
    const nextIndex = (this.currentIndex + 1) % this.slides.length;
    this.goToSlide(nextIndex);
  }

  prevSlide() {
    const prevIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
    this.goToSlide(prevIndex);
  }

  startAutoRotation() {
    if (this.slides.length <= 1) return;
    
    this.timer = setInterval(() => {
      if (!this.isPaused) {
        this.nextSlide();
      }
    }, this.settings.slideInterval);
  }

  pauseAutoRotation() {
    this.isPaused = true;
    clearInterval(this.timer);
  }

  resumeAutoRotation() {
    this.isPaused = false;
    this.resetAutoRotation();
  }

  resetAutoRotation() {
    clearInterval(this.timer);
    this.startAutoRotation();
  }

  destroy() {
    clearInterval(this.timer);
    
    if (this.prevBtn) {
      this.prevBtn.removeEventListener('click', () => this.prevSlide());
    }
    
    if (this.nextBtn) {
      this.nextBtn.removeEventListener('click', () => this.nextSlide());
    }
    
    if (this.settings.pauseOnHover) {
      this.container.removeEventListener('mouseenter', () => this.pauseAutoRotation());
      this.container.removeEventListener('mouseleave', () => this.resumeAutoRotation());
    }
    
    document.removeEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        e.preventDefault();
      }
    });
  }
}

// Example usage when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const testimonials = [
    {
      product: "Colágeno Hidrolizado CH+H",
      quote: "Desde que uso Colágeno Hidrolizado CH+H, he notado una gran mejora en mi piel y articulaciones. ¡Recomendado!",
      author: "María G.",
      rating: 5
    },
    {
      product: "Pro Adulto",
      quote: "Pro Adulto ha sido fundamental para mantener mi salud intestinal. Me siento mucho mejor desde que lo consumo regularmente.",
      author: "Carlos M.",
      rating: 4
    },
    {
      product: "Colágeno Hidrolizado CH+H",
      quote: "Excelente producto. En solo un mes de uso ya veo resultados en la elasticidad de mi piel.",
      author: "Ana L.",
      rating: 5
    }
  ];

  const sliderContainer = document.getElementById('testimonial-slider');
  
  if (sliderContainer) {
    // Create testimonial slides
    testimonials.forEach((testimonial, index) => {
      const slide = document.createElement('div');
      slide.className = `testimonial-slide ${index === 0 ? 'active' : ''}`;
      slide.innerHTML = `
        <div class="testimonial-content">
          <h3 class="testimonial-product">${testimonial.product}</h3>
          <blockquote class="testimonial-quote">"${testimonial.quote}"</blockquote>
          <div class="testimonial-author">${testimonial.author}</div>
          <div class="testimonial-rating">${'★'.repeat(testimonial.rating)}${'☆'.repeat(5 - testimonial.rating)}</div>
        </div>
      `;
      sliderContainer.appendChild(slide);
    });

    // Initialize slider
    new TestimonialSlider('testimonial-slider', {
      slideInterval: 7000,
      pauseOnHover: true
    });
  }
});
```
