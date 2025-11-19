"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: What are the steps to create a "Back To Top" button integrated with a scroll progress indicator in Webflow?
Generated: DETERMINISTIC_5760fab4c7589001
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Back To Top Button with Scroll Progress Indicator**
=====================================================

### HTML
```html
<!-- Back to top button -->
<button id="back-to-top" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M18 13v7H6v-7l6-6 6 6z"></path>
  </svg>
</button>

<!-- Scroll progress indicator -->
<div id="scroll-progress">
  <div id="progress-bar"></div>
</div>
```

### CSS
```css
/* Back to top button styles */
#back-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #fff;
  border: none;
  padding: 10px;
  cursor: pointer;
  z-index: 1000;
  display: none;
}

#back-to-top svg {
  width: 24px;
  height: 24px;
}

/* Scroll progress indicator styles */
#scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 5px;
  background-color: #f0f0f0;
  z-index: 1000;
}

#progress-bar {
  width: 0%;
  height: 100%;
  background-color: #333;
  transition: width 0.3s ease-in-out;
}
```

### JavaScript
```javascript
// Get elements
const backToTopButton = document.getElementById('back-to-top');
const scrollProgress = document.getElementById('scroll-progress');
const progressBar = document.getElementById('progress-bar');

// Set up event listeners
window.addEventListener('scroll', handleScroll);
backToTopButton.addEventListener('click', scrollToTop);

// Handle scroll event
function handleScroll() {
  const scrollPosition = window.scrollY;
  const scrollHeight = document.body.scrollHeight;
  const clientHeight = window.innerHeight;

  // Calculate scroll progress
  const progress = (scrollPosition / (scrollHeight - clientHeight)) * 100;
  progressBar.style.width = `${progress}%`;

  // Show/hide back to top button
  if (scrollPosition > clientHeight / 2) {
    backToTopButton.style.display = 'block';
  } else {
    backToTopButton.style.display = 'none';
  }
}

// Scroll to top function
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
```
