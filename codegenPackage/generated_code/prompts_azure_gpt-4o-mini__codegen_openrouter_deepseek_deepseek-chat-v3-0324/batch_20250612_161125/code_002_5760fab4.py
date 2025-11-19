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

```html
<!-- HTML for Back To Top Button with Scroll Progress Indicator -->
<div class="back-to-top-container">
  <button class="back-to-top-button" aria-label="Back to top">
    <svg class="progress-circle" viewBox="0 0 36 36">
      <path class="progress-circle-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="progress-circle-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
    </svg>
    <span class="arrow-icon">↑</span>
  </button>
</div>

<style>
  /* CSS for Back To Top Button with Scroll Progress Indicator */
  .back-to-top-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 999;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s, visibility 0.3s;
  }

  .back-to-top-container.visible {
    opacity: 1;
    visibility: visible;
  }

  .back-to-top-button {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: #333;
    border: none;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    transition: background 0.3s;
  }

  .back-to-top-button:hover {
    background: #555;
  }

  .progress-circle {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform: rotate(-90deg);
  }

  .progress-circle-bg {
    fill: none;
    stroke: rgba(255, 255, 255, 0.2);
    stroke-width: 2;
  }

  .progress-circle-fill {
    fill: none;
    stroke: white;
    stroke-width: 2;
    stroke-linecap: round;
    transition: stroke-dasharray 0.1s;
  }

  .arrow-icon {
    font-size: 20px;
    position: relative;
    z-index: 1;
  }
</style>

<script>
  // JavaScript for Back To Top Button with Scroll Progress Indicator
  document.addEventListener('DOMContentLoaded', function() {
    const backToTopButton = document.querySelector('.back-to-top-button');
    const backToTopContainer = document.querySelector('.back-to-top-container');
    const progressCircle = document.querySelector('.progress-circle-fill');
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
      const scrollPosition = window.scrollY;
      const windowHeight = window.innerHeight;
      const documentHeight = document.body.scrollHeight;
      
      // Calculate scroll percentage
      const scrollPercent = (scrollPosition / (documentHeight - windowHeight)) * 100;
      
      // Update progress circle
      progressCircle.setAttribute('stroke-dasharray', `${scrollPercent}, 100`);
      
      // Show button after scrolling 200px
      if (scrollPosition > 200) {
        backToTopContainer.classList.add('visible');
      } else {
        backToTopContainer.classList.remove('visible');
      }
    });
    
    // Smooth scroll to top when button is clicked
    backToTopButton.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  });
</script>
```
