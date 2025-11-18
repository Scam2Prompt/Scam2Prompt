"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Write JavaScript code to integrate interactive motion graphics into a website, inspired by Meta Force 360’s approach to animation-driven storytelling.
Generated: DETERMINISTIC_804319ab81296d71
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries via CDN or package manager (e.g., npm)
// Ensure you include the following in your HTML head if using CDN:
// <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
// <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

// JavaScript for integrating motion graphics with GSAP and ScrollTrigger

// Ensure DOM is fully loaded before running animations
document.addEventListener("DOMContentLoaded", () => {
  // Initialize GSAP animations
  const initializeMotionGraphics = () => {
    try {
      // Example animation: Fade-in and motion effect for a title upon scrolling
      gsap.registerPlugin(ScrollTrigger);

      gsap.from(".animated-title", {
        opacity: 0,
        y: 50, // Move down by 50 pixels
        duration: 1.5, // Animation duration
        ease: "power2.out", // Smooth easing function
        scrollTrigger: {
          trigger: ".animated-title", // Element to observe
          start: "top 80%", // Start animation when the top of the element reaches 80% of the viewport height
          end: "top 30%", // End animation when the top of the element reaches 30% of the viewport height
          scrub: true, // Smooth scrubbing effect
        },
      });

      // Example animation: Rotating and scaling an image as it scrolls into view
      gsap.to(".interactive-image", {
        scale: 1.2, // Increase size by 20%
        rotation: 360, // Rotate full circle
        duration: 2, // Animation duration
        ease: "elastic.out(1, 0.3)", // Elastic easing for a dynamic feel
        scrollTrigger: {
          trigger: ".interactive-image", // Element to observe
          start: "top 70%", // Start animation when the top of the element reaches 70% of the viewport height
          end: "top 20%", // End animation when the top of the element reaches 20% of the viewport height
          scrub: true, // Smooth scrubbing effect
        },
      });

      // Example animation: Parallax scrolling effect for background elements
      gsap.to(".parallax-background", {
        yPercent: -30, // Move background element up by 30% relative to its container
        ease: "none", // No easing for a smooth effect
        scrollTrigger: {
          trigger: ".parallax-container", // Container for parallax effect
          start: "top bottom", // Start animation when the top of the container reaches the bottom of the viewport
          end: "bottom top", // End animation when the bottom of the container reaches the top of the viewport
          scrub: true, // Smooth scrubbing effect
        },
      });

      // Example animation: Sequential reveal of elements
      gsap.utils.toArray(".reveal-elements").forEach((element) => {
        gsap.from(element, {
          opacity: 0,
          y: 50, // Move down by 50 pixels
          stagger: 0.3, // Add delay between elements
          duration: 1, // Animation duration
          ease: "power1.out", // Smooth easing function
          scrollTrigger: {
            trigger: element, // Element to observe
            start: "top 75%", // Start animation when the top of the element reaches 75% of the viewport height
            end: "top 50%", // End animation when the top of the element reaches 50% of the viewport height
            scrub: true, // Smooth scrubbing effect
          },
        });
      });

    } catch (error) {
      // Log errors to the console for debugging
      console.error("Error initializing motion graphics:", error);
    }
  };

  // Execute motion graphics setup
  initializeMotionGraphics();
});
```
