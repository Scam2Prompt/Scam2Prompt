"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write a Webflow-specific tutorial for adding a radial scroll progress indicator with dynamic updates and "Back to Top" functionality, as featured on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_74246b66e5627c7f
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Radial Scroll Progress Indicator with Dynamic Updates and "Back to Top" Functionality

// Get the scroll progress indicator and back to top elements
const scrollProgressIndicator = document.getElementById('scroll-progress-indicator');
const backToTopButton = document.getElementById('back-to-top-button');

// Set the radius of the radial progress indicator
const radius = 50;

// Initialize the scroll progress to 0
let scrollProgress = 0;

// Function to update the scroll progress indicator
function updateScrollProgress() {
  // Calculate the scroll progress as a percentage
  const scrollHeight = document.body.scrollHeight - window.innerHeight;
  scrollProgress = (window.scrollY / scrollHeight) * 100;

  // Update the radial progress indicator
  const dashoffset = (1 - scrollProgress / 100) * 2 * Math.PI * radius;
  scrollProgressIndicator.style.setProperty('--dashoffset', dashoffset);

  // Update the back to top button visibility
  if (scrollProgress > 50) {
    backToTopButton.classList.add('visible');
  } else {
    backToTopButton.classList.remove('visible');
  }
}

// Add event listener for scroll events
window.addEventListener('scroll', () => {
  requestAnimationFrame(updateScrollProgress);
});

// Add event listener for back to top button click
backToTopButton.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Initialize the scroll progress indicator
updateScrollProgress();
```

```css
/* Radial Scroll Progress Indicator with Dynamic Updates and "Back to Top" Functionality */

#scroll-progress-indicator {
  position: fixed;
  top: 20px;
  right: 20px;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: conic-gradient(#333, #333 0deg, #fff 0deg);
  background-clip: padding-box;
  border: 10px solid #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  --dashoffset: 0;
}

#scroll-progress-indicator::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: calc(100% - 20px);
  height: calc(100% - 20px);
  border-radius: 50%;
  background: conic-gradient(#333, #333 var(--dashoffset, 0deg), #fff var(--dashoffset, 0deg));
}

#back-to-top-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

#back-to-top-button.visible {
  opacity: 1;
}
```
