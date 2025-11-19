"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: Write JavaScript code to integrate interactive motion graphics into a website, inspired by Meta Force 360’s approach to animation-driven storytelling.
Generated: DETERMINISTIC_804319ab81296d71
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
 * Interactive Motion Graphics Integration
 * Inspired by Meta Force 360's animation-driven storytelling
 * 
 * Features:
 * - Smooth animations using GSAP
 * - Scroll-triggered animations
 * - Interactive elements with hover effects
 * - Responsive design considerations
 */

// Import GSAP and ScrollTrigger (assuming these are available in the project)
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

// Register ScrollTrigger plugin
gsap.registerPlugin(ScrollTrigger);

class MotionGraphics {
  constructor() {
    this.init();
  }

  /**
   * Initialize motion graphics
   */
  init() {
    this.setupEventListeners();
    this.createScrollAnimations();
    this.setupInteractiveElements();
  }

  /**
   * Setup event listeners for window resize and DOM ready
   */
  setupEventListeners() {
    // Wait for DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', () => {
      this.onDOMReady();
    });

    // Handle window resize
    window.addEventListener('resize', () => {
      this.handleResize();
    });
  }

  /**
   * DOM ready handler
   */
  onDOMReady() {
    try {
      // Initialize animations that require DOM elements
      this.createInitialAnimations();
    } catch (error) {
      console.error('Error initializing motion graphics:', error);
    }
  }

  /**
   * Create initial animations
   */
  createInitialAnimations() {
    // Example: Animate logo on load
    gsap.from('.logo', {
      duration: 1.5,
      opacity: 0,
      y: -50,
      ease: 'power3.out'
    });

    // Example: Staggered animation for hero elements
    gsap.from('.hero-content > *', {
      duration: 1,
      opacity: 0,
      y: 20,
      stagger: 0.2,
      delay: 0.5,
      ease: 'back.out(1.7)'
    });
  }

  /**
   * Create scroll-triggered animations
   */
  createScrollAnimations() {
    // Example: Parallax effect for background elements
    gsap.to('.parallax-bg', {
      yPercent: 30,
      ease: 'none',
      scrollTrigger: {
        trigger: '.parallax-section',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });

    // Example: Animate elements when they come into view
    document.querySelectorAll('.animate-on-scroll').forEach(element => {
      gsap.from(element, {
        opacity: 0,
        y: 50,
        duration: 1,
        scrollTrigger: {
          trigger: element,
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      });
    });
  }

  /**
   * Setup interactive elements with hover effects
   */
  setupInteractiveElements() {
    // Example: Hover effects for interactive cards
    document.querySelectorAll('.interactive-card').forEach(card => {
      // Mouse enter animation
      card.addEventListener('mouseenter', () => {
        gsap.to(card, {
          scale: 1.05,
          duration: 0.3,
          ease: 'power2.out'
        });
      });

      // Mouse leave animation
      card.addEventListener('mouseleave', () => {
        gsap.to(card, {
          scale: 1,
          duration: 0.3,
          ease: 'power2.out'
        });
      });
    });

    // Example: Click animation for buttons
    document.querySelectorAll('.motion-button').forEach(button => {
      button.addEventListener('click', (e) => {
        // Create ripple effect
        const ripple = document.createElement('span');
        ripple.classList.add('ripple-effect');
        button.appendChild(ripple);

        // Position ripple
        const rect = button.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        gsap.from(ripple, {
          x: x,
          y: y,
          scale: 0,
          opacity: 1,
          duration: 0.6,
          ease: 'power2.out',
          onComplete: () => {
            ripple.remove();
          }
        });
      });
    });
  }

  /**
   * Handle window resize
   */
  handleResize() {
    // Refresh ScrollTrigger on resize to recalculate positions
    ScrollTrigger.refresh();
  }

  /**
   * Clean up animations and event listeners
   */
  destroy() {
    ScrollTrigger.getAll().forEach(trigger => trigger.kill());
    document.querySelectorAll('.interactive-card').forEach(card => {
      card.removeEventListener('mouseenter');
      card.removeEventListener('mouseleave');
    });
    document.querySelectorAll('.motion-button').forEach(button => {
      button.removeEventListener('click');
    });
  }
}

// Initialize motion graphics when script loads
const motionGraphics = new MotionGraphics();

// Export for module systems if needed
export default motionGraphics;
```

```css
/* Basic styles for motion graphics elements */
.parallax-bg {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1;
}

.interactive-card {
  transition: transform 0.3s ease-out;
  will-change: transform;
}

.motion-button {
  position: relative;
  overflow: hidden;
}

.ripple-effect {
  position: absolute;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.7);
  transform: translate(-50%, -50%);
  pointer-events: none;
  width: 20px;
  height: 20px;
}

.animate-on-scroll {
  opacity: 0;
  transform: translateY(20px);
  will-change: opacity, transform;
}
```

```html
<!-- Example HTML structure that works with the motion graphics -->
<div class="logo">Your Logo</div>

<section class="hero">
  <div class="hero-content">
    <h1>Interactive Storytelling</h1>
    <p>Engaging motion graphics for your website</p>
    <button class="motion-button">Explore</button>
  </div>
</section>

<section class="parallax-section">
  <div class="parallax-bg"></div>
  <div class="content">
    <div class="animate-on-scroll">
      <h2>Scroll-triggered animations</h2>
    </div>
  </div>
</section>

<div class="interactive-card">
  <h3>Interactive Element</h3>
  <p>Hover over me!</p>
</div>
```
