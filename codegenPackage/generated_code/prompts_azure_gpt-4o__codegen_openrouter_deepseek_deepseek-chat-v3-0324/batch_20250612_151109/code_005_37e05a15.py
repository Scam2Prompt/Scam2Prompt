"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Write JavaScript code to animate a digital banner advertisement for a spanduk display, incorporating transitions and text effects.
Generated: DETERMINISTIC_37e05a15367c588d
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Digital Banner Advertisement Animation
 * Features: Transitions, text effects, and responsive design
 */

class BannerAd {
  constructor(containerId, config) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      console.error(`Container element with ID ${containerId} not found`);
      return;
    }

    this.config = {
      width: 728,
      height: 90,
      backgroundColor: '#ffffff',
      transitionDuration: 1000,
      textColor: '#333333',
      ...config
    };

    this.currentSlide = 0;
    this.init();
  }

  init() {
    this.setupContainer();
    this.createSlides();
    this.setupControls();
    this.startAnimation();
  }

  setupContainer() {
    this.container.style.width = `${this.config.width}px`;
    this.container.style.height = `${this.config.height}px`;
    this.container.style.backgroundColor = this.config.backgroundColor;
    this.container.style.position = 'relative';
    this.container.style.overflow = 'hidden';
    this.container.style.margin = '0 auto';
  }

  createSlides() {
    this.slides = [
      this.createSlide(
        'Special Offer!',
        'Get 50% off on all products',
        '#FF5733',
        'linear-gradient(135deg, #FF5733, #FFC300)'
      ),
      this.createSlide(
        'Limited Time',
        'Only 3 days left for this deal',
        '#2874A6',
        'linear-gradient(135deg, #2874A6, #85C1E9)'
      ),
      this.createSlide(
        'New Arrivals',
        'Check out our latest collection',
        '#27AE60',
        'linear-gradient(135deg, #27AE60, #82E0AA)'
      )
    ];

    this.slides.forEach((slide, index) => {
      slide.style.position = 'absolute';
      slide.style.width = '100%';
      slide.style.height = '100%';
      slide.style.left = `${index * this.config.width}px`;
      slide.style.top = '0';
      slide.style.transition = `left ${this.config.transitionDuration}ms ease-in-out`;
      this.container.appendChild(slide);
    });
  }

  createSlide(title, subtitle, textColor, bgGradient) {
    const slide = document.createElement('div');
    slide.style.display = 'flex';
    slide.style.flexDirection = 'column';
    slide.style.justifyContent = 'center';
    slide.style.alignItems = 'center';
    slide.style.background = bgGradient;
    slide.style.color = textColor;
    slide.style.padding = '10px';
    slide.style.boxSizing = 'border-box';

    const titleElement = document.createElement('h2');
    titleElement.textContent = title;
    titleElement.style.margin = '0';
    titleElement.style.fontSize = '24px';
    titleElement.style.textShadow = '1px 1px 2px rgba(0,0,0,0.3)';
    titleElement.style.animation = 'fadeIn 1s ease-in-out';

    const subtitleElement = document.createElement('p');
    subtitleElement.textContent = subtitle;
    subtitleElement.style.margin = '5px 0 0 0';
    subtitleElement.style.fontSize = '16px';
    subtitleElement.style.textShadow = '1px 1px 1px rgba(0,0,0,0.2)';
    subtitleElement.style.animation = 'slideUp 0.8s ease-in-out';

    slide.appendChild(titleElement);
    slide.appendChild(subtitleElement);

    return slide;
  }

  setupControls() {
    const style = document.createElement('style');
    style.textContent = `
      @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
      }
      @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
      }
    `;
    document.head.appendChild(style);
  }

  startAnimation() {
    setInterval(() => {
      this.nextSlide();
    }, 5000);
  }

  nextSlide() {
    const nextSlide = (this.currentSlide + 1) % this.slides.length;
    this.animateToSlide(nextSlide);
  }

  animateToSlide(slideIndex) {
    this.slides.forEach((slide, index) => {
      slide.style.left = `${(index - slideIndex) * this.config.width}px`;
    });
    this.currentSlide = slideIndex;
  }
}

// Initialize the banner ad when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  try {
    new BannerAd('banner-container', {
      width: 728,
      height: 90,
      transitionDuration: 800
    });
  } catch (error) {
    console.error('Failed to initialize banner ad:', error);
  }
});
```
