"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Provide JavaScript code for integrating a radial scroll progress indicator into a Webflow project, following the example from the Scroll Progress Indicator website.
Generated: DETERMINISTIC_25da4dcfa9e3764c
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Radial Scroll Progress Indicator for Webflow
 * This script creates a circular progress indicator that updates based on the user's scroll position.
 * 
 * Requirements:
 * - A Webflow project with a circular progress element (e.g., SVG with id="radial-progress").
 * - Proper HTML and CSS setup to style the radial progress indicator.
 * 
 * Usage:
 * Place this script in your Webflow project's custom code section, before the body tag closes.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Select the SVG circle element
  const progressCircle = document.querySelector('#radial-progress circle');
  if (!progressCircle) {
    console.error('Radial progress element not found. Ensure you have an SVG circle with id="radial-progress".');
    return;
  }

  // Get the circle's radius and circumference
  const radius = progressCircle.r.baseVal.value;
  const circumference = 2 * Math.PI * radius;

  // Set the circle's stroke-dasharray and initial stroke-dashoffset
  progressCircle.style.strokeDasharray = `${circumference} ${circumference}`;
  progressCircle.style.strokeDashoffset = circumference;

  /**
   * Update radial progress based on scroll position.
   */
  const updateProgress = () => {
    // Calculate the scroll percentage
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight;
    const clientHeight = document.documentElement.clientHeight;
    const scrollPercentage = scrollTop / (scrollHeight - clientHeight);

    // Calculate the new stroke-dashoffset
    const offset = circumference - (scrollPercentage * circumference);

    // Update the circle's stroke-dashoffset to reflect progress
    progressCircle.style.strokeDashoffset = offset;
  };

  // Listen for the scroll event to update the progress
  window.addEventListener('scroll', updateProgress);

  // Initial update to ensure progress is correct at load
  updateProgress();
});
```
